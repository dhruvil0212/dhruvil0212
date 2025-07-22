#!/usr/bin/env python3
"""
Test suite for AI Voice Assistant
"""

import unittest
import sys
import os
import json
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add current directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from voice_assistant import VoiceAssistant
    from config_manager import ConfigManager
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure all dependencies are installed.")
    sys.exit(1)


class TestConfigManager(unittest.TestCase):
    """Test cases for ConfigManager"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_config_dir = Path("test_data")
        self.test_config_dir.mkdir(exist_ok=True)
        self.config_manager = ConfigManager(str(self.test_config_dir))
    
    def tearDown(self):
        """Clean up test environment"""
        import shutil
        if self.test_config_dir.exists():
            shutil.rmtree(self.test_config_dir)
    
    def test_default_config_creation(self):
        """Test default configuration creation"""
        self.assertIsInstance(self.config_manager.config, dict)
        self.assertIn('assistant', self.config_manager.config)
        self.assertIn('voice', self.config_manager.config)
        self.assertIn('speech', self.config_manager.config)
    
    def test_config_get_set(self):
        """Test configuration get and set operations"""
        # Test setting and getting values
        self.config_manager.set('assistant.name', 'TestBot')
        self.assertEqual(self.config_manager.get('assistant.name'), 'TestBot')
        
        # Test nested setting
        self.config_manager.set('voice.rate', 250)
        self.assertEqual(self.config_manager.get('voice.rate'), 250)
        
        # Test default value
        self.assertEqual(self.config_manager.get('nonexistent.key', 'default'), 'default')
    
    def test_config_save_load(self):
        """Test configuration save and load"""
        # Modify config
        self.config_manager.set('assistant.name', 'SavedBot')
        
        # Save config
        self.assertTrue(self.config_manager.save_config())
        
        # Create new config manager and verify loaded config
        new_config_manager = ConfigManager(str(self.test_config_dir))
        self.assertEqual(new_config_manager.get('assistant.name'), 'SavedBot')


class TestVoiceAssistant(unittest.TestCase):
    """Test cases for VoiceAssistant"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_data_dir = Path("test_data")
        self.test_data_dir.mkdir(exist_ok=True)
        
        # Mock the audio components to avoid hardware dependencies
        with patch('speech_recognition.Recognizer'), \
             patch('speech_recognition.Microphone'), \
             patch('pyttsx3.init'):
            self.assistant = VoiceAssistant()
            self.assistant.data_dir = self.test_data_dir
            self.assistant.config_file = self.test_data_dir / "config.json"
            self.assistant.conversation_history = self.test_data_dir / "conversations.json"
    
    def tearDown(self):
        """Clean up test environment"""
        import shutil
        if self.test_data_dir.exists():
            shutil.rmtree(self.test_data_dir)
    
    def test_command_processing(self):
        """Test command processing functionality"""
        # Test time command
        response = self.assistant.process_command("what time is it")
        self.assertIn("time", response.lower())
        
        # Test date command
        response = self.assistant.process_command("what is the date")
        self.assertIn("today", response.lower())
        
        # Test joke command
        response = self.assistant.process_command("tell me a joke")
        self.assertTrue(len(response) > 10)  # Should return a joke
        
        # Test greeting
        response = self.assistant.process_command("hello")
        self.assertIn("hello", response.lower())
    
    def test_calculation_handling(self):
        """Test calculation functionality"""
        # Test addition
        response = self.assistant.handle_calculation("calculate 5 plus 3")
        self.assertIn("8", response)
        
        # Test subtraction
        response = self.assistant.handle_calculation("calculate 10 minus 4")
        self.assertIn("6", response)
        
        # Test multiplication
        response = self.assistant.handle_calculation("calculate 6 times 7")
        self.assertIn("42", response)
        
        # Test division
        response = self.assistant.handle_calculation("calculate 15 divided by 3")
        self.assertIn("5", response)
        
        # Test division by zero
        response = self.assistant.handle_calculation("calculate 5 divided by 0")
        self.assertIn("can't divide by zero", response.lower())
    
    def test_conversation_saving(self):
        """Test conversation history saving"""
        # Save a conversation
        self.assistant.save_conversation("test input", "test response")
        
        # Check if file was created and contains the conversation
        self.assertTrue(self.assistant.conversation_history.exists())
        
        with open(self.assistant.conversation_history, 'r') as f:
            conversations = json.load(f)
        
        self.assertEqual(len(conversations), 1)
        self.assertEqual(conversations[0]['user'], "test input")
        self.assertEqual(conversations[0]['assistant'], "test response")
    
    def test_ai_response_generation(self):
        """Test AI response generation"""
        # Test keyword matching
        response = self.assistant.generate_ai_response("how are you")
        self.assertIn("well", response.lower())
        
        # Test default response for unknown input
        response = self.assistant.generate_ai_response("random unknown input")
        self.assertTrue(len(response) > 0)
    
    def test_help_message(self):
        """Test help message generation"""
        help_msg = self.assistant.get_help_message()
        self.assertIn("time", help_msg.lower())
        self.assertIn("joke", help_msg.lower())
        self.assertIn("calculate", help_msg.lower())


class TestSystemIntegration(unittest.TestCase):
    """Integration tests for the complete system"""
    
    def test_module_imports(self):
        """Test that all required modules can be imported"""
        try:
            import speech_recognition
            import pyttsx3
            import colorama
            import json
            import pathlib
        except ImportError as e:
            self.fail(f"Failed to import required module: {e}")
    
    def test_file_structure(self):
        """Test that all required files exist"""
        required_files = [
            'voice_assistant.py',
            'config_manager.py',
            'requirements.txt',
            'setup.py',
            'install.sh'
        ]
        
        for filename in required_files:
            self.assertTrue(Path(filename).exists(), f"Required file {filename} not found")


def run_performance_test():
    """Run a simple performance test"""
    print("\n🚀 Running Performance Tests...")
    
    import time
    
    # Test config manager performance
    start_time = time.time()
    config_manager = ConfigManager("test_perf_data")
    
    # Perform 100 get/set operations
    for i in range(100):
        config_manager.set(f'test.key{i}', f'value{i}')
        config_manager.get(f'test.key{i}')
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"✅ Config operations (200 ops): {duration:.3f}s")
    
    # Cleanup
    import shutil
    test_dir = Path("test_perf_data")
    if test_dir.exists():
        shutil.rmtree(test_dir)
    
    if duration < 1.0:
        print("✅ Performance test passed!")
    else:
        print("⚠️  Performance test shows slow operations")


def main():
    """Main test runner"""
    print("🧪 AI Voice Assistant - Test Suite")
    print("=" * 50)
    
    # Run unit tests
    print("\n📋 Running Unit Tests...")
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run performance tests
    run_performance_test()
    
    print("\n✅ All tests completed!")
    print("\n💡 To run specific tests:")
    print("  python3 test_assistant.py TestConfigManager")
    print("  python3 test_assistant.py TestVoiceAssistant")
    print("  python3 test_assistant.py TestSystemIntegration")


if __name__ == "__main__":
    main()
