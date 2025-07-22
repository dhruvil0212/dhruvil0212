# 🤖 AI Voice Assistant

<div align="center">

![AI Voice Assistant](https://img.shields.io/badge/AI-Voice%20Assistant-blue?style=for-the-badge&logo=python)
![Python](https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**A comprehensive AI-powered voice assistant with speech recognition, text-to-speech, and intelligent conversation capabilities.**

*Created by [Dhruvil Upadhyay](https://github.com/dhruvil0212)*

</div>

---

## 🌟 Features

### 🎤 **Speech Recognition**
- **Wake Word Detection**: Activate with "Hey ARIA"
- **Continuous Listening**: Always ready to help
- **Multi-language Support**: English (US) with expandable language options
- **Noise Adaptation**: Automatic ambient noise calibration

### 🗣️ **Text-to-Speech**
- **Natural Voice**: High-quality speech synthesis
- **Voice Customization**: Adjustable rate, volume, and voice selection
- **Gender Preference**: Auto-selects female voice when available
- **Real-time Response**: Instant audio feedback

### 🧠 **AI Capabilities**
- **Smart Conversations**: Context-aware responses
- **Built-in Commands**: Time, date, weather, calculations
- **Joke Generator**: Entertainment with random jokes
- **Math Calculator**: Voice-controlled arithmetic operations
- **Help System**: Interactive command guidance

### ⚙️ **Advanced Features**
- **Configuration Management**: Customizable settings
- **Conversation History**: Persistent chat logging
- **Volume Control**: Voice-activated audio adjustment
- **Modular Design**: Easy feature extension
- **Error Handling**: Robust error recovery

---

## 🚀 Quick Start

### 1. **Automated Installation**
```bash
# Clone the repository
git clone https://github.com/dhruvil0212/ai-voice-assistant.git
cd ai-voice-assistant

# Run the installation script
./install.sh
```

### 2. **Manual Installation**
```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3-dev python3-pip portaudio19-dev espeak

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. **Run the Assistant**
```bash
# Activate virtual environment
source venv/bin/activate

# Start the voice assistant
python3 voice_assistant.py
```

---

## 📖 Usage Guide

### **Basic Commands**
- **"Hey ARIA"** - Wake up the assistant
- **"What time is it?"** - Get current time
- **"What's the date today?"** - Get current date
- **"Tell me a joke"** - Hear a random joke
- **"Calculate 5 plus 3"** - Perform math operations
- **"Volume up"** / **"Volume down"** - Adjust voice volume
- **"Help"** - Show available commands
- **"Goodbye"** - End conversation

### **Math Operations**
```text
"Calculate 10 plus 5"     → 15
"Calculate 20 minus 8"    → 12
"Calculate 6 times 7"     → 42
"Calculate 15 divided by 3" → 5
```

### **Conversation Examples**
```text
You: "Hey ARIA"
ARIA: "Yes, I'm listening!"

You: "How are you?"
ARIA: "I'm doing well, thank you for asking! How are you?"

You: "What can you do?"
ARIA: "I can tell time, date, tell jokes, do simple calculations, and have conversations with you!"
```

---

## ⚙️ Configuration

### **Interactive Setup**
```bash
python3 config_manager.py setup
```

### **Manual Configuration**
```bash
# View current settings
python3 config_manager.py show

# Change assistant name
python3 config_manager.py set assistant.name "MyBot"

# Adjust voice settings
python3 config_manager.py set voice.rate 180
python3 config_manager.py set voice.volume 0.8

# Change wake word
python3 config_manager.py set speech.wake_word "hello assistant"
```

### **Configuration Options**
- **Assistant Name**: Customize your assistant's name
- **Voice Settings**: Rate (150-300), Volume (0.1-1.0)
- **Speech Recognition**: Timeout, language, wake word
- **Features**: Enable/disable jokes, calculations, history
- **Audio**: Input/output device selection

---

## 🏗️ Architecture

```
ai-voice-assistant/
├── voice_assistant.py      # Main application
├── config_manager.py       # Configuration handler
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup
├── install.sh             # Installation script
├── test_assistant.py      # Test suite
├── data/                  # Configuration & data
│   ├── config.json        # Settings file
│   └── conversations.json # Chat history
└── venv/                  # Virtual environment
```

### **Core Components**
- **VoiceAssistant**: Main application class
- **ConfigManager**: Settings management
- **Speech Recognition**: Google Speech API integration
- **Text-to-Speech**: pyttsx3 engine
- **Command Processor**: Natural language understanding

---

## 🔧 Development

### **Running Tests**
```bash
# Run all tests
python3 test_assistant.py

# Run specific test categories
python3 test_assistant.py TestVoiceAssistant
python3 test_assistant.py TestConfigManager
```

### **Adding New Features**
1. **Command Handler**: Add to `process_command()` method
2. **AI Responses**: Extend `generate_ai_response()` method
3. **Configuration**: Add settings to `default_config`
4. **Tests**: Create test cases in `test_assistant.py`

### **Example: Adding Weather Command**
```python
elif 'weather' in command:
    return self.get_weather_info()

def get_weather_info(self):
    # Implement weather API integration
    return "Today's weather is sunny with 25°C"
```

---

## 📋 Requirements

### **System Requirements**
- **Python**: 3.7 or higher
- **Operating System**: Linux, macOS, Windows
- **Microphone**: For voice input
- **Speakers/Headphones**: For audio output
- **Internet**: For speech recognition (Google API)

### **Python Dependencies**
```text
SpeechRecognition==3.10.0   # Speech-to-text
pyttsx3==2.90              # Text-to-speech
pyaudio==0.2.11            # Audio interface
colorama==0.4.6            # Colored output
sounddevice==0.4.6         # Audio device management
numpy==1.24.3              # Numerical operations
```

---

## �� Troubleshooting

### **Common Issues**

#### **Microphone Not Working**
```bash
# Test microphone
arecord -l
pactl list sources short

# Fix permissions (Linux)
sudo usermod -a -G audio $USER
```

#### **Speech Recognition Errors**
```text
Error: "Speech recognition error"
Solution: Check internet connection for Google API
```

#### **Audio Output Issues**
```bash
# Test speakers
speaker-test -t wav -c 2

# Install audio drivers (Ubuntu)
sudo apt-get install alsa-utils pulseaudio
```

#### **Import Errors**
```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Check Python path
python3 -c "import sys; print(sys.path)"
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### **Development Setup**
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/ai-voice-assistant.git
cd ai-voice-assistant

# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Run tests
python3 test_assistant.py
```

### **Contribution Guidelines**
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### **Code Standards**
- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include unit tests for new features
- Maintain backwards compatibility

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```text
MIT License

Copyright (c) 2024 Dhruvil Upadhyay

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👤 Author

**Dhruvil Upadhyay**
- 🌐 **Portfolio**: [dhruvil0212.github.io](https://dhruvil0212.github.io)
- 📧 **Email**: dhruvilu2@gmail.com
- �� **GitHub**: [@dhruvil0212](https://github.com/dhruvil0212)
- 🐦 **Twitter**: [@offcialdhruvil](https://twitter.com/offcialdhruvil)
- 💼 **LinkedIn**: [dhruvil-upadhyay](https://www.linkedin.com/in/dhruvil-upadhyay-)

---

## 🙏 Acknowledgments

- **Google Speech Recognition API** for speech-to-text capabilities
- **pyttsx3** for text-to-speech functionality
- **Python Speech Recognition Library** for audio processing
- **Open Source Community** for inspiration and support

---

## 🔮 Future Enhancements

### **Planned Features**
- [ ] **Integration with ChatGPT/OpenAI** for advanced AI responses
- [ ] **Weather API Integration** for real-time weather information
- [ ] **Smart Home Control** for IoT device management
- [ ] **Multi-language Support** for international users
- [ ] **Voice Training** for personalized wake word detection
- [ ] **Plugin System** for easy feature extensions
- [ ] **GUI Interface** for visual interaction
- [ ] **Mobile App** for remote control
- [ ] **Cloud Sync** for settings and conversation history
- [ ] **Voice Commands** for system control

### **Technical Improvements**
- [ ] **Offline Speech Recognition** using Vosk or similar
- [ ] **Neural Text-to-Speech** for more natural voices
- [ ] **Continuous Learning** from user interactions
- [ ] **Context Awareness** for better conversation flow
- [ ] **Performance Optimization** for faster responses

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

**🐛 Found a bug? [Report it here](https://github.com/dhruvil0212/ai-voice-assistant/issues)**

**💡 Have a feature request? [Let us know!](https://github.com/dhruvil0212/ai-voice-assistant/discussions)**

---

*Made with ❤️ by Dhruvil Upadhyay*

</div>
