import speech_recognition as sr
import pyautogui
import threading
import time


pyautogui.FAILSAFE = False


def change_language(language):
    if language == 'English':
        pyautogui.hotkey('ctrl', '1')
    elif language == 'Russian':
        pyautogui.hotkey('ctrl', '2')
    elif language == 'change':
        pyautogui.hotkey('shift', 'alt')


def listen_and_recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while not stop_listening.is_set():
            print('Waiting for command')
            try:
                audio = r.record(source, duration=2)
                text = r.recognize_google(audio, language='en-EN')
                print('You said: ', text)
                if text == 'exit':
                    stop_listening.set()
                else:
                    change_language(text)
            except sr.UnknownValueError:
                print('Could not understand speech')
            except sr.RequestError as e:
                print('Speech recognition service error; {0}'.format(e))


stop_listening = threading.Event()
listen_thread = threading.Thread(target=listen_and_recognize)
listen_thread.start()

try:
    while listen_thread.is_alive():
        time.sleep(1)
except KeyboardInterrupt:
    stop_listening.set()
    listen_thread.join()
