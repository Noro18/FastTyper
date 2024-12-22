import random
import time
import keyboard
from playsound import playsound
import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, Qt
from Ui import Ui_MainWindow
from PyQt5.QtMultimedia import QSound 
import recources_rc
# from conn import create_connection
# from TestFiles.generate_random import generate_words
from words import *

class TypingGame(QMainWindow):
    def __init__(self):
        
        super(TypingGame, self).__init__()
        self.sound_file = QSound("untitled.mp3")
        self.input_box = QtWidgets.QLineEdit(self)
        self.input_box.textChanged.connect(self.play)
    
    def play(self):
        QSound.play("TW.wav")

            

if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = TypingGame()
    window.show()
    app.exec()