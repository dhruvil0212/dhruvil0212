#!/bin/bash

# AI Voice Assistant Installation Script
# Created by Dhruvil Upadhyay

set -e

echo "🤖 AI Voice Assistant Installation Script"
echo "========================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check if Python 3 is installed
check_python() {
    echo -e "${BLUE}🐍 Checking Python installation...${NC}"
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        echo -e "${GREEN}✅ Python 3 found: ${PYTHON_VERSION}${NC}"
    else
        echo -e "${RED}❌ Python 3 not found. Please install Python 3.7+${NC}"
        exit 1
    fi
}

# Check if pip is installed
check_pip() {
    echo -e "${BLUE}📦 Checking pip installation...${NC}"
    
    if command -v pip3 &> /dev/null; then
        echo -e "${GREEN}✅ pip3 found${NC}"
    elif command -v pip &> /dev/null; then
        echo -e "${GREEN}✅ pip found${NC}"
    else
        echo -e "${RED}❌ pip not found. Installing pip...${NC}"
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        python3 get-pip.py
        rm get-pip.py
    fi
}

# Install system dependencies
install_system_deps() {
    echo -e "${BLUE}🔧 Installing system dependencies...${NC}"
    
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        if command -v apt-get &> /dev/null; then
            echo -e "${YELLOW}📱 Installing dependencies for Ubuntu/Debian...${NC}"
            sudo apt-get update
            sudo apt-get install -y \
                python3-dev \
                python3-pip \
                portaudio19-dev \
                alsa-utils \
                espeak \
                espeak-data \
                libespeak1 \
                libespeak-dev \
                ffmpeg
        elif command -v dnf &> /dev/null; then
            echo -e "${YELLOW}📱 Installing dependencies for Fedora...${NC}"
            sudo dnf install -y \
                python3-devel \
                python3-pip \
                portaudio-devel \
                alsa-utils \
                espeak \
                espeak-devel \
                ffmpeg
        elif command -v pacman &> /dev/null; then
            echo -e "${YELLOW}📱 Installing dependencies for Arch Linux...${NC}"
            sudo pacman -S --noconfirm \
                python \
                python-pip \
                portaudio \
                alsa-utils \
                espeak \
                espeak-ng \
                ffmpeg
        else
            echo -e "${YELLOW}⚠️  Unknown Linux distribution. Please install portaudio and espeak manually.${NC}"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        echo -e "${YELLOW}🍎 Installing dependencies for macOS...${NC}"
        if command -v brew &> /dev/null; then
            brew install portaudio espeak ffmpeg
        else
            echo -e "${RED}❌ Homebrew not found. Please install Homebrew first: https://brew.sh${NC}"
            exit 1
        fi
    else
        echo -e "${YELLOW}⚠️  Unknown operating system. Please install portaudio and espeak manually.${NC}"
    fi
}

# Create virtual environment
create_venv() {
    echo -e "${BLUE}🏠 Creating virtual environment...${NC}"
    
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        echo -e "${GREEN}✅ Virtual environment created${NC}"
    else
        echo -e "${YELLOW}📁 Virtual environment already exists${NC}"
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    echo -e "${GREEN}✅ Virtual environment activated${NC}"
}

# Install Python dependencies
install_python_deps() {
    echo -e "${BLUE}📚 Installing Python dependencies...${NC}"
    
    # Upgrade pip first
    pip install --upgrade pip
    
    # Install dependencies
    pip install -r requirements.txt
    
    echo -e "${GREEN}✅ Python dependencies installed${NC}"
}

# Set up configuration
setup_config() {
    echo -e "${BLUE}⚙️  Setting up configuration...${NC}"
    
    # Create data directory
    mkdir -p data
    
    # Run configuration setup
    python3 config_manager.py setup
    
    echo -e "${GREEN}✅ Configuration completed${NC}"
}

# Test installation
test_installation() {
    echo -e "${BLUE}🧪 Testing installation...${NC}"
    
    python3 -c "
import speech_recognition as sr
import pyttsx3
import colorama
print('✅ All core modules imported successfully')
"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Installation test passed${NC}"
    else
        echo -e "${RED}❌ Installation test failed${NC}"
        exit 1
    fi
}

# Main installation function
main() {
    echo -e "${MAGENTA}Starting installation...${NC}"
    echo ""
    
    check_python
    check_pip
    install_system_deps
    create_venv
    install_python_deps
    test_installation
    
    echo ""
    echo -e "${GREEN}🎉 Installation completed successfully!${NC}"
    echo ""
    echo -e "${CYAN}To run the AI Voice Assistant:${NC}"
    echo -e "${YELLOW}  source venv/bin/activate${NC}"
    echo -e "${YELLOW}  python3 voice_assistant.py${NC}"
    echo ""
    echo -e "${CYAN}To configure settings:${NC}"
    echo -e "${YELLOW}  python3 config_manager.py setup${NC}"
    echo ""
    echo -e "${CYAN}Enjoy your AI Voice Assistant! 🤖${NC}"
}

# Handle script interruption
trap 'echo -e "\n${YELLOW}⏹️  Installation interrupted${NC}"; exit 1' INT

# Run main function
main "$@"
