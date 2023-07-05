import speech_recognition as sr
import pyautogui
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys

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
                text = r.recognize_google(audio, language='en')
                print('You said: ', text)
                if text == 'exit':
                    stop_listening.set()
                    QApplication.quit()
                else:
                    change_language(text)
            except sr.UnknownValueError:
                print('Could not understand speech')
            except sr.RequestError as e:
                print('Speech recognition service error; {0}'.format(e))


class PyChangeMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyChangeLang')
        self.setLayout(QVBoxLayout())

        self.startButton = QPushButton(
            'Start Listening',
            clicked=self.start_listening
        )
        self.layout().addWidget(self.startButton)

        self.pauseButton = QPushButton(
            'Stop Listening',
            clicked=self.stop_listening
        )
        self.layout().addWidget(self.pauseButton)

        self.exitButton = QPushButton('Exit', clicked=self.exit_app)
        self.layout().addWidget(self.exitButton)

    def start_listening(self):
        global stop_listening
        stop_listening.clear()
        if not listen_thread.is_alive():
            listen_thread.start()

    def stop_listening(self):
        global stop_listening
        stop_listening.set()

    def exit_app(self):
        global stop_listening
        stop_listening.set()
        QApplication.quit()


stop_listening = threading.Event()
listen_thread = threading.Thread(target=listen_and_recognize)

app = QApplication(sys.argv)

demo = PyChangeMenu()
demo.show()

sys.exit(app.exec_())
