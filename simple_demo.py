#!/usr/bin/env python3
"""
Simple Demo for AI Voice Assistant (No Dependencies)
Demonstrates key features without requiring additional packages
"""

import time
import sys

def print_header():
    """Print demo header"""
    print("=" * 60)
    print("🤖 AI Voice Assistant - Interactive Demo")
    print("Created by Dhruvil Upadhyay")
    print("=" * 60)
    print()

def print_section(title):
    """Print section header"""
    print(f"\n{'-'*50}")
    print(f"�� {title}")
    print(f"{'-'*50}")

def simulate_conversation(user_input, assistant_response):
    """Simulate a conversation exchange"""
    print(f"👤 You: {user_input}")
    time.sleep(0.5)
    print(f"🤖 ARIA: {assistant_response}")
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
        print(f"  ✓ {feature}")
        time.sleep(0.3)

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
        print(f"  {step}")
        time.sleep(0.5)

def interactive_demo():
    """Run interactive demo mode"""
    print_section("Interactive Demo Mode")
    print("💡 This simulates how the voice assistant responds to commands")
    print("💡 In the real version, you would speak these commands")
    print()
    
    try:
        while True:
            user_input = input("👤 Enter command (or 'quit' to exit): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("🤖 ARIA: Goodbye! Thanks for trying the demo!")
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
            
            print(f"🤖 ARIA: {response}")
            print()
            
    except KeyboardInterrupt:
        print("\n🤖 ARIA: Demo interrupted. Goodbye!")

def main():
    """Main demo function"""
    print_header()
    
    # Check if running in interactive mode
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'interactive':
        interactive_demo()
        return
    
    print("🎬 Starting Automated Demo...")
    time.sleep(1)
    
    # Run demo sections
    show_features()
    demo_basic_commands()
    demo_calculations()
    show_installation()
    
    print_section("Demo Complete!")
    print("✅ Demo completed successfully!")
    print("🚀 Ready to try the real voice assistant?")
    print("   Run: python3 voice_assistant.py")
    print()
    print("🎮 Want to try interactive demo?")
    print("   Run: python3 simple_demo.py interactive")
    print()
    print("Made with ❤️  by Dhruvil Upadhyay")

if __name__ == "__main__":
    main()
