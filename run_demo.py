#!/usr/bin/env python3
"""
Demo script for AI Voice Assistant
Demonstrates key features without requiring microphone input
"""

import time
import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_header():
    """Print demo header"""
    print(f"{Fore.MAGENTA}{'='*60}")
    print(f"{Fore.MAGENTA}🤖 AI Voice Assistant - Interactive Demo")
    print(f"{Fore.MAGENTA}Created by Dhruvil Upadhyay")
    print(f"{Fore.MAGENTA}{'='*60}")
    print()

def print_section(title):
    """Print section header"""
    print(f"\n{Fore.CYAN}{'─'*50}")
    print(f"{Fore.CYAN}📋 {title}")
    print(f"{Fore.CYAN}{'─'*50}")

def simulate_conversation(user_input, assistant_response):
    """Simulate a conversation exchange"""
    print(f"{Fore.GREEN}👤 You: {user_input}")
    time.sleep(0.5)
    print(f"{Fore.BLUE}🤖 ARIA: {assistant_response}")
    time.sleep(1)

def demo_basic_commands():
    """Demonstrate basic commands"""
    print_section("Basic Commands Demo")
    
    commands = [
        ("Hey ARIA", "Yes, I'm listening!"),
        ("What time is it?", "The current time is 2:30 PM"),
        ("What's the date today?", "Today is Monday, December 09, 2024"),
        ("Tell me a joke", "Why don't scientists trust atoms? Because they make up everything!"),
        ("Help", "Here are some things you can ask me: Ask for time, date, tell jokes, calculations..."),
        ("Goodbye", "Goodbye! It was nice talking with you.")
    ]
    
    for user_input, response in commands:
        simulate_conversation(user_input, response)

def demo_calculations():
    """Demonstrate calculation features"""
    print_section("Math Calculations Demo")
    
    calculations = [
        ("Calculate 15 plus 7", "15 plus 7 equals 22"),
        ("Calculate 25 minus 8", "25 minus 8 equals 17"),
        ("Calculate 6 times 9", "6 times 9 equals 54"),
        ("Calculate 144 divided by 12", "144 divided by 12 equals 12.00")
    ]
    
    for calc_input, calc_response in calculations:
        simulate_conversation(calc_input, calc_response)

def demo_conversations():
    """Demonstrate conversation capabilities"""
    print_section("AI Conversation Demo")
    
    conversations = [
        ("How are you?", "I'm doing well, thank you for asking! How are you?"),
        ("What can you do?", "I can tell time, date, tell jokes, do simple calculations, and have conversations with you!"),
        ("What's your favorite color?", "I don't see colors, but I imagine blue would be nice - like the sky!"),
        ("Do you like music?", "I can't play music directly, but I'd love to chat about your favorite songs!")
    ]
    
    for conv_input, conv_response in conversations:
        simulate_conversation(conv_input, conv_response)

def demo_voice_control():
    """Demonstrate voice control features"""
    print_section("Voice Control Demo")
    
    controls = [
        ("Volume up", "Volume increased to 80%"),
        ("Volume down", "Volume decreased to 70%"),
        ("Volume up", "Volume increased to 80%")
    ]
    
    for control_input, control_response in controls:
        simulate_conversation(control_input, control_response)

def show_features():
    """Show key features"""
    print_section("Key Features")
    
    features = [
        "🎤 Speech Recognition with Wake Word Detection",
        "🗣️  Natural Text-to-Speech with Voice Customization",
        "🧠 AI-Powered Conversations and Responses",
        "🔢 Voice-Controlled Mathematical Calculations",
        "⏰ Time, Date, and Information Queries",
        "😄 Entertainment with Random Jokes",
        "🔧 Configurable Settings and Preferences",
        "💾 Conversation History and Logging",
        "🎛️  Voice-Activated Volume Control",
        "🌐 Multi-language Support Capability"
    ]
    
    for feature in features:
        print(f"{Fore.YELLOW}  ✓ {feature}")
        time.sleep(0.3)

def show_technical_specs():
    """Show technical specifications"""
    print_section("Technical Specifications")
    
    specs = {
        "Language": "Python 3.7+",
        "Speech Recognition": "Google Speech API",
        "Text-to-Speech": "pyttsx3 Engine",
        "Audio Processing": "PyAudio, SoundDevice",
        "Configuration": "JSON-based Settings",
        "Logging": "Comprehensive Error Handling",
        "Testing": "Unit Tests with pytest",
        "Platform": "Cross-platform (Linux, macOS, Windows)"
    }
    
    for spec, detail in specs.items():
        print(f"{Fore.WHITE}  {spec}: {Fore.GREEN}{detail}")
        time.sleep(0.2)

def show_installation():
    """Show installation steps"""
    print_section("Quick Installation")
    
    steps = [
        "1. Clone the repository",
        "2. Run ./install.sh (automated setup)",
        "3. Or manually: pip install -r requirements.txt",
        "4. Start with: python3 voice_assistant.py",
        "5. Say 'Hey ARIA' to begin!"
    ]
    
    for step in steps:
        print(f"{Fore.CYAN}  {step}")
        time.sleep(0.5)

def interactive_demo():
    """Run interactive demo mode"""
    print_section("Interactive Demo Mode")
    print(f"{Fore.YELLOW}💡 This simulates how the voice assistant responds to commands")
    print(f"{Fore.YELLOW}💡 In the real version, you would speak these commands")
    print()
    
    try:
        while True:
            user_input = input(f"{Fore.GREEN}👤 Enter command (or 'quit' to exit): {Fore.WHITE}").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print(f"{Fore.BLUE}🤖 ARIA: Goodbye! Thanks for trying the demo!")
                break
            
            # Simple response generation for demo
            if 'time' in user_input.lower():
                response = "The current time is 2:30 PM"
            elif 'date' in user_input.lower():
                response = "Today is Monday, December 09, 2024"
            elif 'joke' in user_input.lower():
                response = "Why did the programmer quit his job? Because he didn't get arrays!"
            elif 'calculate' in user_input.lower() or 'plus' in user_input.lower():
                response = "I'd perform that calculation for you!"
            elif 'hello' in user_input.lower() or 'hi' in user_input.lower():
                response = "Hello! I'm ARIA, your AI voice assistant. How can I help you?"
            elif 'help' in user_input.lower():
                response = "I can help with time, date, calculations, jokes, and conversations!"
            else:
                response = "That's interesting! In the full version, I'd have a more detailed response."
            
            print(f"{Fore.BLUE}🤖 ARIA: {response}")
            print()
            
    except KeyboardInterrupt:
        print(f"\n{Fore.BLUE}🤖 ARIA: Demo interrupted. Goodbye!")

def main():
    """Main demo function"""
    print_header()
    
    # Check if running in interactive mode
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'interactive':
        interactive_demo()
        return
    
    print(f"{Fore.YELLOW}🎬 Starting Automated Demo...")
    time.sleep(1)
    
    # Run all demo sections
    show_features()
    demo_basic_commands()
    demo_calculations()
    demo_conversations()
    demo_voice_control()
    show_technical_specs()
    show_installation()
    
    print_section("Demo Complete!")
    print(f"{Fore.GREEN}✅ Demo completed successfully!")
    print(f"{Fore.CYAN}🚀 Ready to try the real voice assistant?")
    print(f"{Fore.YELLOW}   Run: python3 voice_assistant.py")
    print()
    print(f"{Fore.CYAN}🎮 Want to try interactive demo?")
    print(f"{Fore.YELLOW}   Run: python3 run_demo.py interactive")
    print()
    print(f"{Fore.MAGENTA}Made with ❤️  by Dhruvil Upadhyay")

if __name__ == "__main__":
    main()
