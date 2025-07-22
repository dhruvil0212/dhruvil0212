#!/usr/bin/env python3
"""
AI Voice Assistant
A comprehensive voice assistant with speech recognition, text-to-speech, and AI capabilities.
Created by Dhruvil Upadhyay
"""

import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

try:
    import speech_recognition as sr
    import pyttsx3
    from colorama import init, Fore, Style
except ImportError as e:
    print(f"Missing dependencies. Please install requirements: {e}")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)

# Initialize colorama for colored output
init(autoreset=True)

class VoiceAssistant:
    """Main AI Voice Assistant class"""
    
    def __init__(self):
        self.setup_logging()
        self.setup_directories()
        self.load_config()
        self.setup_components()
        self.running = False
        self.listening = False
        
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('assistant.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def setup_directories(self):
        """Create necessary directories"""
        self.data_dir = Path("data")
        self.data_dir.mkdir(exist_ok=True)
        
        self.config_file = self.data_dir / "config.json"
        self.conversation_history = self.data_dir / "conversations.json"
        
    def load_config(self):
        """Load or create configuration"""
        default_config = {
            "assistant_name": "ARIA",
            "voice_rate": 200,
            "voice_volume": 0.9,
            "recognition_timeout": 5,
            "phrase_timeout": 10,
            "wake_word": "hey aria",
            "language": "en-US"
        }
        
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = default_config
            self.save_config()
            
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
            
    def setup_components(self):
        """Initialize speech recognition and TTS components"""
        try:
            # Speech Recognition
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            
            # Adjust for ambient noise
            print(f"{Fore.YELLOW}🎤 Calibrating microphone for ambient noise...")
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print(f"{Fore.GREEN}✓ Microphone calibrated")
            
            # Text-to-Speech
            self.tts_engine = pyttsx3.init()
            self.setup_tts()
            
            # Load conversation history
            self.load_conversation_history()
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error setting up components: {e}")
            print("Make sure you have a microphone connected and working.")
            
    def setup_tts(self):
        """Configure text-to-speech engine"""
        try:
            voices = self.tts_engine.getProperty('voices')
            
            # Try to find a female voice
            for voice in voices:
                if 'female' in voice.name.lower() or 'woman' in voice.name.lower():
                    self.tts_engine.setProperty('voice', voice.id)
                    break
            else:
                # Use first available voice
                if voices:
                    self.tts_engine.setProperty('voice', voices[0].id)
                    
            self.tts_engine.setProperty('rate', self.config['voice_rate'])
            self.tts_engine.setProperty('volume', self.config['voice_volume'])
        except Exception as e:
            self.logger.error(f"TTS setup error: {e}")
        
    def load_conversation_history(self):
        """Load conversation history"""
        if self.conversation_history.exists():
            try:
                with open(self.conversation_history, 'r') as f:
                    self.conversations = json.load(f)
            except:
                self.conversations = []
        else:
            self.conversations = []
            
    def save_conversation(self, user_input: str, assistant_response: str):
        """Save conversation to history"""
        conversation = {
            "timestamp": datetime.now().isoformat(),
            "user": user_input,
            "assistant": assistant_response
        }
        self.conversations.append(conversation)
        
        # Keep only last 100 conversations
        if len(self.conversations) > 100:
            self.conversations = self.conversations[-100:]
            
        try:
            with open(self.conversation_history, 'w') as f:
                json.dump(self.conversations, f, indent=2)
        except Exception as e:
            self.logger.error(f"Error saving conversation: {e}")
            
    def speak(self, text: str):
        """Convert text to speech"""
        print(f"{Fore.CYAN}🗣️  {self.config['assistant_name']}: {text}")
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            self.logger.error(f"TTS error: {e}")
        
    def listen(self) -> Optional[str]:
        """Listen for speech input"""
        try:
            print(f"{Fore.YELLOW}🎧 Listening...")
            with self.microphone as source:
                # Listen for audio with timeout
                audio = self.recognizer.listen(
                    source, 
                    timeout=self.config['recognition_timeout'],
                    phrase_time_limit=self.config['phrase_timeout']
                )
                
            print(f"{Fore.BLUE}🔄 Processing speech...")
            
            # Recognize speech using Google's service
            text = self.recognizer.recognize_google(audio, language=self.config['language'])
            print(f"{Fore.GREEN}👤 You: {text}")
            return text.lower()
            
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            print(f"{Fore.RED}❌ Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"{Fore.RED}❌ Speech recognition error: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Listen error: {e}")
            return None
            
    def process_command(self, command: str) -> str:
        """Process voice command and generate response"""
        command = command.lower().strip()
        
        # Built-in commands
        if any(word in command for word in ['time', 'what time']):
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"
            
        elif any(word in command for word in ['date', 'what date', 'today']):
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {current_date}"
            
        elif any(word in command for word in ['weather']):
            return "I don't have access to weather data right now, but you can check your local weather app or website."
            
        elif any(word in command for word in ['hello', 'hi', 'hey']):
            return f"Hello! I'm {self.config['assistant_name']}, your AI voice assistant. How can I help you today?"
            
        elif any(word in command for word in ['goodbye', 'bye', 'exit', 'quit']):
            return "Goodbye! It was nice talking with you."
            
        elif any(word in command for word in ['name', 'who are you']):
            return f"I'm {self.config['assistant_name']}, your AI voice assistant created by Dhruvil Upadhyay."
            
        elif any(word in command for word in ['joke', 'tell me a joke']):
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? He was outstanding in his field!",
                "Why don't eggs tell jokes? They'd crack each other up!",
                "What do you call a fake noodle? An impasta!",
                "Why did the math book look so sad? Because it had too many problems!",
                "What's orange and sounds like a parrot? A carrot!"
            ]
            import random
            return random.choice(jokes)
            
        elif 'calculate' in command or 'plus' in command or 'minus' in command or 'times' in command or 'divided' in command:
            return self.handle_calculation(command)
            
        elif any(word in command for word in ['volume up', 'louder']):
            current_volume = self.config['voice_volume']
            new_volume = min(1.0, current_volume + 0.1)
            self.config['voice_volume'] = new_volume
            self.tts_engine.setProperty('volume', new_volume)
            self.save_config()
            return f"Volume increased to {int(new_volume * 100)}%"
            
        elif any(word in command for word in ['volume down', 'quieter']):
            current_volume = self.config['voice_volume']
            new_volume = max(0.1, current_volume - 0.1)
            self.config['voice_volume'] = new_volume
            self.tts_engine.setProperty('volume', new_volume)
            self.save_config()
            return f"Volume decreased to {int(new_volume * 100)}%"
            
        elif any(word in command for word in ['help', 'commands']):
            return self.get_help_message()
            
        else:
            # Fallback response
            return self.generate_ai_response(command)
            
    def handle_calculation(self, command: str) -> str:
        """Handle simple math calculations"""
        try:
            import re
            
            # Extract numbers and operators
            numbers = re.findall(r'\d+\.?\d*', command)
            
            if 'plus' in command or '+' in command:
                if len(numbers) >= 2:
                    result = float(numbers[0]) + float(numbers[1])
                    return f"{numbers[0]} plus {numbers[1]} equals {result}"
                    
            elif 'minus' in command or '-' in command:
                if len(numbers) >= 2:
                    result = float(numbers[0]) - float(numbers[1])
                    return f"{numbers[0]} minus {numbers[1]} equals {result}"
                    
            elif 'times' in command or 'multiply' in command or '*' in command:
                if len(numbers) >= 2:
                    result = float(numbers[0]) * float(numbers[1])
                    return f"{numbers[0]} times {numbers[1]} equals {result}"
                    
            elif 'divided by' in command or '/' in command:
                if len(numbers) >= 2:
                    if float(numbers[1]) != 0:
                        result = float(numbers[0]) / float(numbers[1])
                        return f"{numbers[0]} divided by {numbers[1]} equals {result:.2f}"
                    else:
                        return "I can't divide by zero!"
                        
        except Exception as e:
            self.logger.error(f"Calculation error: {e}")
            
        return "I couldn't understand that calculation. Try saying something like 'calculate 5 plus 3'"
        
    def generate_ai_response(self, user_input: str) -> str:
        """Generate AI response using simple pattern matching"""
        # Simple AI responses based on keywords
        responses = {
            'how are you': "I'm doing well, thank you for asking! How are you?",
            'what can you do': "I can tell time, date, tell jokes, do simple calculations, and have conversations with you!",
            'favorite color': "I don't see colors, but I imagine blue would be nice - like the sky!",
            'music': "I can't play music directly, but I'd love to chat about your favorite songs!",
            'hobby': "I enjoy learning new things and helping people with their questions!",
            'food': "I don't eat, but I find it fascinating how food brings people together!",
            'book': "I love stories and information! What's your favorite book?",
            'movie': "Movies are amazing ways to tell stories! What genre do you enjoy?",
            'sport': "Sports are great for staying active! Do you have a favorite team?",
            'travel': "Travel sounds wonderful! Where would you like to visit?",
            'thanks': "You're very welcome! I'm happy to help.",
            'thank you': "You're very welcome! Is there anything else I can help you with?"
        }
        
        for keyword, response in responses.items():
            if keyword in user_input.lower():
                return response
                
        # Default responses
        default_responses = [
            "That's interesting! Tell me more about it.",
            "I see! What do you think about that?",
            "That sounds fascinating! Can you elaborate?",
            "Hmm, I'm still learning about that topic. What's your experience with it?",
            "That's a great point! I'd love to hear more of your thoughts.",
            "Interesting! I'd love to learn more about that from you."
        ]
        
        import random
        return random.choice(default_responses)
        
    def get_help_message(self) -> str:
        """Get help message with available commands"""
        return """Here are some things you can ask me:
        
        • Ask for the time or date
        • Tell me a joke
        • Simple calculations like 'calculate 5 plus 3'
        • Control my volume with 'volume up' or 'volume down'
        • Ask about the weather
        • Have a conversation with me
        • Say 'goodbye' to exit
        
        Just speak naturally and I'll do my best to help!"""
        
    def continuous_listen(self):
        """Continuously listen for wake word"""
        print(f"{Fore.GREEN}🤖 {self.config['assistant_name']} is ready!")
        print(f"{Fore.CYAN}💡 Say '{self.config['wake_word']}' to start a conversation")
        print(f"{Fore.CYAN}💡 Or press Ctrl+C to exit")
        
        while self.running:
            try:
                if not self.listening:
                    # Listen for wake word
                    command = self.listen()
                    if command and self.config['wake_word'] in command:
                        self.speak(f"Yes, I'm listening!")
                        self.handle_conversation()
                else:
                    time.sleep(0.1)
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.logger.error(f"Error in continuous listen: {e}")
                time.sleep(1)
                
    def handle_conversation(self):
        """Handle a conversation session"""
        self.listening = True
        
        try:
            while self.listening:
                command = self.listen()
                
                if command:
                    # Check for exit commands
                    if any(word in command for word in ['goodbye', 'bye', 'stop', 'exit']):
                        response = "Goodbye! Say the wake word to talk again."
                        self.speak(response)
                        self.save_conversation(command, response)
                        self.listening = False
                        break
                        
                    # Process command
                    response = self.process_command(command)
                    self.speak(response)
                    self.save_conversation(command, response)
                    
                    # Continue listening for follow-up
                    print(f"{Fore.YELLOW}🎧 Listening for follow-up...")
                    
        except Exception as e:
            self.logger.error(f"Error in conversation: {e}")
        finally:
            self.listening = False
            
    def run(self):
        """Start the voice assistant"""
        self.running = True
        
        try:
            # Welcome message
            welcome_msg = f"Hello! I'm {self.config['assistant_name']}, your AI voice assistant!"
            self.speak(welcome_msg)
            
            # Start continuous listening
            self.continuous_listen()
            
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}👋 Shutting down...")
        except Exception as e:
            self.logger.error(f"Error running assistant: {e}")
        finally:
            self.running = False
            self.speak("Goodbye!")

def main():
    """Main function"""
    print(f"{Fore.MAGENTA}🤖 AI Voice Assistant")
    print(f"{Fore.MAGENTA}Created by Dhruvil Upadhyay")
    print(f"{Fore.MAGENTA}{'='*50}")
    
    try:
        assistant = VoiceAssistant()
        assistant.run()
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to start assistant: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
