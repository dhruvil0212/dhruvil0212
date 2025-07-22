#!/usr/bin/env python3
"""
Configuration Manager for AI Voice Assistant
Handles settings, preferences, and customization options
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
from colorama import Fore, Style


class ConfigManager:
    """Manages configuration settings for the voice assistant"""
    
    def __init__(self, config_dir: str = "data"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.default_config = self._get_default_config()
        self.config = self.load_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration settings"""
        return {
            "assistant": {
                "name": "ARIA",
                "personality": "friendly",
                "response_style": "conversational"
            },
            "speech": {
                "recognition_timeout": 5,
                "phrase_timeout": 10,
                "language": "en-US",
                "wake_word": "hey aria"
            },
            "voice": {
                "rate": 200,
                "volume": 0.9,
                "voice_gender": "auto"
            },
            "features": {
                "save_conversations": True,
                "max_conversation_history": 100,
                "enable_jokes": True,
                "enable_calculations": True,
                "enable_weather": False
            },
            "audio": {
                "input_device": "default",
                "output_device": "default",
                "noise_reduction": True
            },
            "advanced": {
                "debug_mode": False,
                "log_level": "INFO",
                "auto_save": True
            }
        }
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                
                # Merge with defaults to ensure all keys exist
                config = self.default_config.copy()
                self._deep_update(config, loaded_config)
                return config
                
            except (json.JSONDecodeError, IOError) as e:
                print(f"{Fore.YELLOW}⚠️  Error loading config: {e}")
                print(f"{Fore.YELLOW}Using default configuration...")
                return self.default_config.copy()
        else:
            return self.default_config.copy()
    
    def save_config(self) -> bool:
        """Save current configuration to file"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            return True
        except IOError as e:
            print(f"{Fore.RED}❌ Error saving config: {e}")
            return False
    
    def get(self, key_path: str, default: Any = None) -> Any:
        """Get configuration value using dot notation (e.g., 'voice.rate')"""
        keys = key_path.split('.')
        value = self.config
        
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key_path: str, value: Any) -> bool:
        """Set configuration value using dot notation"""
        keys = key_path.split('.')
        config = self.config
        
        try:
            # Navigate to the parent of the target key
            for key in keys[:-1]:
                if key not in config:
                    config[key] = {}
                config = config[key]
            
            # Set the value
            config[keys[-1]] = value
            
            if self.get('advanced.auto_save', True):
                return self.save_config()
            return True
            
        except (KeyError, TypeError) as e:
            print(f"{Fore.RED}❌ Error setting config: {e}")
            return False
    
    def reset_to_defaults(self) -> bool:
        """Reset configuration to default values"""
        self.config = self.default_config.copy()
        return self.save_config()
    
    def _deep_update(self, base_dict: Dict, update_dict: Dict) -> None:
        """Recursively update base_dict with values from update_dict"""
        for key, value in update_dict.items():
            if key in base_dict and isinstance(base_dict[key], dict) and isinstance(value, dict):
                self._deep_update(base_dict[key], value)
            else:
                base_dict[key] = value
    
    def display_config(self) -> None:
        """Display current configuration in a readable format"""
        print(f"\n{Fore.CYAN}🔧 Current Configuration:")
        print(f"{Fore.CYAN}{'='*50}")
        self._print_config_section(self.config, "")
    
    def _print_config_section(self, config: Dict, prefix: str) -> None:
        """Recursively print configuration sections"""
        for key, value in config.items():
            if isinstance(value, dict):
                print(f"{Fore.YELLOW}{prefix}{key}:")
                self._print_config_section(value, prefix + "  ")
            else:
                print(f"{Fore.WHITE}{prefix}{key}: {Fore.GREEN}{value}")
    
    def interactive_setup(self) -> None:
        """Interactive configuration setup"""
        print(f"\n{Fore.MAGENTA}🔧 Interactive Configuration Setup")
        print(f"{Fore.MAGENTA}{'='*40}")
        
        try:
            # Assistant settings
            print(f"\n{Fore.CYAN}Assistant Settings:")
            name = input(f"Assistant name [{self.get('assistant.name')}]: ").strip()
            if name:
                self.set('assistant.name', name)
            
            # Voice settings
            print(f"\n{Fore.CYAN}Voice Settings:")
            try:
                rate = input(f"Speaking rate (150-300) [{self.get('voice.rate')}]: ").strip()
                if rate:
                    rate_val = int(rate)
                    if 150 <= rate_val <= 300:
                        self.set('voice.rate', rate_val)
                    else:
                        print(f"{Fore.YELLOW}⚠️  Rate should be between 150-300")
            except ValueError:
                print(f"{Fore.YELLOW}⚠️  Invalid rate value")
            
            try:
                volume = input(f"Volume (0.1-1.0) [{self.get('voice.volume')}]: ").strip()
                if volume:
                    vol_val = float(volume)
                    if 0.1 <= vol_val <= 1.0:
                        self.set('voice.volume', vol_val)
                    else:
                        print(f"{Fore.YELLOW}⚠️  Volume should be between 0.1-1.0")
            except ValueError:
                print(f"{Fore.YELLOW}⚠️  Invalid volume value")
            
            # Wake word
            print(f"\n{Fore.CYAN}Speech Recognition:")
            wake_word = input(f"Wake word [{self.get('speech.wake_word')}]: ").strip()
            if wake_word:
                self.set('speech.wake_word', wake_word.lower())
            
            # Features
            print(f"\n{Fore.CYAN}Features:")
            save_conv = input(f"Save conversations? (y/n) [{('y' if self.get('features.save_conversations') else 'n')}]: ").strip().lower()
            if save_conv in ['y', 'yes', 'n', 'no']:
                self.set('features.save_conversations', save_conv in ['y', 'yes'])
            
            print(f"\n{Fore.GREEN}✅ Configuration updated successfully!")
            
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}⏹️  Configuration setup cancelled")
        except Exception as e:
            print(f"\n{Fore.RED}❌ Error during setup: {e}")


def main():
    """Configuration manager CLI"""
    import sys
    
    config_manager = ConfigManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "setup":
            config_manager.interactive_setup()
        elif command == "show":
            config_manager.display_config()
        elif command == "reset":
            if config_manager.reset_to_defaults():
                print(f"{Fore.GREEN}✅ Configuration reset to defaults")
            else:
                print(f"{Fore.RED}❌ Failed to reset configuration")
        elif command == "get" and len(sys.argv) > 2:
            key = sys.argv[2]
            value = config_manager.get(key)
            print(f"{key}: {value}")
        elif command == "set" and len(sys.argv) > 3:
            key = sys.argv[2]
            value = sys.argv[3]
            # Try to convert to appropriate type
            try:
                if value.lower() in ['true', 'false']:
                    value = value.lower() == 'true'
                elif value.replace('.', '').isdigit():
                    value = float(value) if '.' in value else int(value)
            except:
                pass
            
            if config_manager.set(key, value):
                print(f"{Fore.GREEN}✅ Set {key} = {value}")
            else:
                print(f"{Fore.RED}❌ Failed to set {key}")
        else:
            print(f"""
{Fore.CYAN}AI Voice Assistant - Configuration Manager

Usage:
  python config_manager.py setup    - Interactive configuration setup
  python config_manager.py show     - Display current configuration
  python config_manager.py reset    - Reset to default configuration
  python config_manager.py get <key> - Get configuration value
  python config_manager.py set <key> <value> - Set configuration value

Examples:
  python config_manager.py get voice.rate
  python config_manager.py set assistant.name "My Assistant"
            """)
    else:
        config_manager.interactive_setup()


if __name__ == "__main__":
    main()
