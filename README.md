# Speak2Switch
Speak2Switch is a Python program that allows you to change the keyboard input language using voice commands. It uses the SpeechRecognition library to recognize voice commands and the PyAutoGUI library to simulate keyboard shortcuts to change the language.

Speak2Switch - это программа на языке Python, которая позволяет менять язык ввода на клавиатуре с помощью голосовых команд. Она использует библиотеку SpeechRecognition для распознавания голосовых команд и библиотеку PyAutoGUI для имитации комбинаций клавиш для изменения языка.

## Installation
Install the required libraries by running the following command in your terminal:
```
pip install SpeechRecognition pyautogui PyQt5
```

## Usage
To use Speak2Switch, simply run the main.py or GUI.py

## How it works
Speak2Switch uses the SpeechRecognition library to recognize voice commands.
The available commands for changing the language are:

"English" - change the language to English
"Russian" - change the language to Russian
"change" - switch language

If Speak2Switch doesn't recognize your voice command, it will print an error message to the console.

Speak2Switch uses the PyAutoGUI library to simulate keyboard shortcuts to change the language. The available keyboard shortcuts are:

Ctrl + 1 - change the language to English
Ctrl + 2 - change the language to Russian
Shift + Alt - switch the language
If Speak2Switch doesn't recognize the command you spoke, it will print an error message to the console.
