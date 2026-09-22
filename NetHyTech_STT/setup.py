from setuptools import setup, find_packages

setup(
    name="NetHyTech_STT",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "edge-tts",
        "pydantic"
    ],
    entry_points={
        "console_scripts": [
            "jarvis=NetHyTech_STT.Alter:start",
        ],
    },
)