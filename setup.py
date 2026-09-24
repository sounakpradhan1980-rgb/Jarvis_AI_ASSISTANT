from setuptools import setup, find_packages

setup(
    name="NetHighTech_TTS",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "edge-tts",
        "pydantic",
        "faster-whisper",
        "pyaudio"
    ],
    entry_points={
        "console_scripts": [
            "jarvis=NetHighTech_TTS.app:start",
        ],
    },
)
