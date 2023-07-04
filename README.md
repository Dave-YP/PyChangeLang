# PyChangeLang
PyChangeLang is a Python program that allows you to change the language of your operating system using voice commands. It uses the SpeechRecognition library to recognize voice commands and the PyAutoGUI library to simulate keyboard shortcuts to change the language.

## Installation
Install the required libraries by running the following command in your terminal:
```
pip install SpeechRecognition pyautogui PyQt5
```

## Usage
To use PyChangeLang, simply run the main.py or GUI.py

How it works
PyChangeLang uses the SpeechRecognition library to recognize voice commands. When you speak a command, PyChangeLang will recognize it and will change the language of your operating system based on the command.

The available commands for changing the language are:

"English" - change the language to English
"Russian" - change the language to Russian
"change" - switch the 

If PyChangeLang doesn't recognize your voice command, it will print an error message to the console.

PyChangeLang uses the PyAutoGUI library to simulate keyboard shortcuts to change the language. The available keyboard shortcuts are:

Ctrl + 1 - change the language to English
Ctrl + 2 - change the language to Russian
Shift + Alt - switch the language
If PyChangeLang doesn't recognize the command you spoke, it will print an error message to the console.