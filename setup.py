#!/usr/bin/env python3
"""
Setup script for AI Voice Assistant
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-voice-assistant",
    version="1.0.0",
    author="Dhruvil Upadhyay",
    author_email="dhruvilu2@gmail.com",
    description="A comprehensive AI Voice Assistant with speech recognition and text-to-speech",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dhruvil0212/ai-voice-assistant",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=[
        "SpeechRecognition>=3.10.0",
        "pyttsx3>=2.90",
        "pyaudio>=0.2.11",
        "colorama>=0.4.6",
        "sounddevice>=0.4.6",
        "numpy>=1.24.3",
    ],
    extras_require={
        "dev": ["pytest>=7.0.0", "black", "flake8"],
        "ai": ["openai>=0.28.0", "requests>=2.31.0"],
    },
    entry_points={
        "console_scripts": [
            "voice-assistant=voice_assistant:main",
        ],
    },
)
