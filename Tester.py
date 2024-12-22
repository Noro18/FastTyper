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
# conn = create_connection()

class TypingGame(QMainWindow):
    def __init__(self):

        super(TypingGame, self).__init__()
        self.sounde = [ "sounds/sound2.wav",  "sounds/sound4wav.wav"]
        self.words_typed = 0
        self.words_typed_wrond = 0
        # self.
        self.char_typed = 0
        self.wrong_char = 0

        self.totalChar = 0
        self.words = [
    "the", "and", "for", "you", "not",
    "with", "but", "that", "are", "can",
    "was", "have", "all", "one", "out",
    "use", "get", "how", "why", "if",
    "him", "she", "say", "we", "see",
    "let", "new", "now", "who", "try",
    "good", "no", "yes", "big", "run",
    "play", "make", "love", "keep", "work",
    "take", "go", "want", "help", "feel",
    "find", "know", "think", "look", "come",
    "give", "tell", "need", "back", "show",
    "long", "fast", "life", "small", "time",
    "when", "where", "thing", "same", "change",
    "call", "right", "short", "wait", "next",
    "watch", "house", "friend", "talk", "leave",
    "smile", "school", "walk", "begin", "close",
    "clear", "again", "first", "second", "third",
    "under", "before", "after", "always", "simple",
    "happy", "better", "answer", "enjoy", "follow",
    "inside", "moment", "listen", "minute", "person"
]
        self.setFocus()
        self.ui = Ui_MainWindow()  # Initialize the UI
        self.ui.setupUi(self)  # Setup the UI in this main window

      
        self.duration = int(self.ui.lan_combo_2.currentText())
        print(self.duration)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        # Connecting buttons and input fields
        # self.start_game()

        self.isStarting = False     
        self.ui.input_box.textChanged.connect(self.start_game)  # Connect to start game

        self.ui.input_box.textChanged.connect(self.check_input)
        self.ui.input_box.textChanged.connect(self.playsoundss)

        self.ui.lan_combo.currentTextChanged.connect(self.change_language)
        self.ui.lan_combo_2.currentTextChanged.connect(self.change_duration)
        self.ui.lan_combo_3.currentTextChanged.connect(self.change_language)
        
        # self.ui.display_box.setText("HAHAHA")

        self.ui.input_box.installEventFilter(self)
        self.ui.lan_combo.installEventFilter(self)
        self.ui.lan_combo_2.installEventFilter(self)
        self.ui.lan_combo_3.installEventFilter(self)
    
    def playsoundss(self):
        self.sound = random.choice(self.sounde)
        self.sound1 = random.choice(self.sounde)
        print(self.sound)
        QSound.play(self.sound)
        # QSound.play(self.sound1)
        # threading.Thread(target=playsound, args=(self.sounde,), daemon=True).start()
        # if len(self.ui.input_box.text()) > 1:
        #     threading.Thread(target=playsound, args=("sound1newflp.mp3",), daemon=True).start()
    # def keyPressEvent(self, event):
    #     self.keyPressEvent(event)
    #     self.sounde.play()
     
    # def keyPressEvent(self, event):
    #     super().keyPressEvent(event)
    #     threading.Thread(target=playsound, args=("untitled.mp3",), daemon=True).start()

    
    def change_language(self):

        # Indonesia
        if(self.ui.lan_combo.currentText().strip()=="Indonesian" and self.ui.lan_combo_3.currentText().strip()=="Easy"): 
            self.words = indo_easy
        elif(self.ui.lan_combo.currentText().strip()=="Indonesian" and self.ui.lan_combo_3.currentText().strip()=="Medium"):
            self.words = indo_medium
        elif(self.ui.lan_combo.currentText().strip()=="Indonesian" and self.ui.lan_combo_3.currentText().strip()=="Hard"):
            self.words = indo_hard


        # English
        elif(self.ui.lan_combo.currentText().strip()=="English" and self.ui.lan_combo_3.currentText().strip()=="Easy"):
            self.words = english_easy 
        elif(self.ui.lan_combo.currentText().strip()=="English" and self.ui.lan_combo_3.currentText().strip()=="Medium"):
            self.words = english_medium 
        elif(self.ui.lan_combo.currentText().strip()=="English" and self.ui.lan_combo_3.currentText().strip()=="Hard"):
            self.words = english_hard       

        # Tetun

        elif(self.ui.lan_combo.currentText().strip()=="Tetun" and self.ui.lan_combo_3.currentText().strip()=="Easy"):
            self.words = tetun_easy
        elif(self.ui.lan_combo.currentText().strip()=="Tetun" and self.ui.lan_combo_3.currentText().strip()=="Medium"):
            self.words = tetun_medium
        elif(self.ui.lan_combo.currentText().strip()=="Tetun" and self.ui.lan_combo_3.currentText().strip()=="Hard"):
            self.words = tetun_hard


    def change_duration(self):
        self.duration = int(self.ui.lan_combo_2.currentText())
    
    def start_game(self):
        """Start the game by displaying a random word."""
        
        # self.ui.display_box.setStyleSheet(
        #     "color: blue;\n"
        #     "border: 4px solid black;\n"
        #     "border-radius: 28px;\n"
        #     "background-color: rgba(34, 61, 97, 1);\n"
        #     "margin-bottom: 40px; padding: 5px;\n"
        #     "font-family: 'Roboto Mono';\n"
        #     "font-size : 50px;\n"
        #     "height: 60px;\n")


        if not self.isStarting and self.ui.input_box.text().strip():
            self.ui.input_box.setDisabled(False)  # Disable the input field
            self.isStarting = True
            self.ui.input_box.clear()  # Clear the input field
            self.ui.input_box.setFocus()  # Set focus to the input field
            self.time_left = self.duration  # Reset the timer
            self.ui.time.setText(f"{self.time_left}")  # Display remaining time
            self.timer.start(1000)

            # Show a random word
            self.show_new_word()
            self.words_typed = 0
            self.words_typed_wrong = 0
            self.char_typed = 0
            self.wrong_char = 0
            self.words_typed = 0
            self.totalChar = 0

            # self.show_words() # use this function for a pre set text 

   

    def show_words(self):
        
        self.ui.display_box.setText(generate_words(self.words))

        
    def show_new_word(self):
        """Display a new random word."""
        word = random.choice(self.words)  # Select a random word
        self.ui.display_box.setText(word)  # Display the word

    def check_input(self, text):
        """Check if the input matches the displayed word."""

        print("char typed: ", self.char_typed)
        print("words typed: ", self.words_typed)
        print("wrong char: ", self.wrong_char)
        char_list= []
        char_list.append("tatt")
        print("char list=", char_list)
        print(type(text))
        char_list += str(text)
        

        displayed_word = self.ui.display_box.text()  # Get the displayed word
        typedtext = text
        print(typedtext)

        # if len(self.ui.display_box.text().strip()) == "" :
        #     self.ui.display_box.setStyleSheet(
        #     "color: blue;\n"
        #     "border: 4px solid black;\n"
        #     "border-radius: 28px;\n"
        #     "background-color: rgba(34, 61, 97, 1);\n"
        #     "margin-bottom: 40px; padding: 5px;\n"
        #     "font-family: 'Roboto Mono';\n"
        #     "font-size : 50px;\n"
        #     "height: 60px;\n")

        if text not in displayed_word:
            
            self.wrong_char += 1
            if text == " ":
                self.wrong_char -= 1
                
        if typedtext not in displayed_word:
            
            self.ui.display_box.setStyleSheet('color: rgba(255, 74, 74, 1);\n'"border: 4px solid black;\n"
            "border-radius: 28px;\n"
           "background-color: rgba(34, 61, 97, 1);\n"
            "margin-bottom: 40px; padding: 5px;\n"
            "font-family: 'Roboto Mono';\n"
            "font-size : 50px")
            
                

        if text in displayed_word:
            
            # print("char ryped: ", self.char_typed, "\n", "total char: ", self.totalChar)
            self.ui.display_box.setStyleSheet('color: rgba(60, 229, 97, 1);\n'"border: 4px solid black;\n"
            "border-radius: 28px;\n"
            "background-color: rgba(34, 61, 97, 1);\n"
            "margin-bottom: 40px; padding: 5px;\n"
            "font-family: 'Roboto Mono';\n"
            "font-size : 50px\n"
            )
        
            # if typedtext and typedtext[-1] != ' ':
                # self.char_typed += 1 
        if typedtext and typedtext[-1] == ' ':
            # self.char_typed += len(displayed_word)
            if typedtext[:-1] == displayed_word:
                self.char_typed += len(text)-1
                self.words_typed += 1
                self.ui.input_box.clear()  # Clear the input field
                self.show_new_word()  # Display the next word'
                self.ui.display_box.setStyleSheet('color: white;\n'"border: 4px solid black;\n"
            "border-radius: 28px;\n"
            "background-color: rgba(34, 61, 97, 1);\n"
            "margin-bottom: 40px; padding: 5px;\n"
            "font-family: 'Roboto Mono';\n"
            "font-size : 50px;\n"
            "height: 50px;\n")

        # if len(text) == 0 or len(self.ui.display_box.text())== 0 :
        #     self.ui.display_box.setStyleSheet('color: white;\n'"border: 4px solid black;\n"
        #     "border-radius: 28px;\n"
        #     "background-color: rgba(34, 61, 97, 1);\n"
        #     "margin-bottom: 40px; padding: 5px;\n"
        #     "font-family: 'Roboto Mono';\n"
        #     "font-size : 50px;\n"
        #     "height: 60px;\n")

            

    # def eventFilter(self, source, event):
    #     if source == self.ui.input_box and event.type() == event.KeyPress:
    #         if event.key() == Qt.Key_Tab:
    #             self.reset_app()
    #             return True  # Indicate the event has been handled
    #     return super().eventFilter(source, event)
    
    # def reset_app(self):
    #     # self.ui.input_box.setText("this function run perfectly")

    # def on_tab_pressed(self):
    #     print("this works")
    #     self.start_game()
    #     return super().eventFilter(source, event)

   

    # def eventFilter(self, source, event):
    #     if event.type() == event.KeyPress:
    #         if event.key() == Qt.Key_Tab:
    #             print("Helllow")
    #             self.start_game()
    #     return True
            
    #     return super().eventFilter(source, event)
            
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Tab:
    #         print("Hhh")
    #         self.reset_app()
            
        


    # def reset_app(self):
        
    #     self.isStarting = False
    #     self.duration = 30
    #     self.ui.input_box.clear()
    #     self.start_game()

    

    def update_timer(self):
        """Update the timer every second and stop the game when time is up."""
        self.time_left -= 1  # Decrease the remaining time by 1 second
        self.ui.time.setText(f"{self.time_left}")  # Update the timer display
        # print(self.time_left)
        # self.wpm = self.char_typed

        if self.time_left == 0:
            self.isStarting = False
            self.ui.input_box.setDisabled(True)
            time.sleep(3)
            self.wpm = int(self.char_typed/(5*(self.duration/60)))
            self.true_wrong_char = self.wrong_char-self.words_typed

            if self.char_typed == 0:
                self.accuracy = 0
            else:
                self.accuracy = int(((self.char_typed-self.true_wrong_char)/self.char_typed)*100)

            self.ui.wpm_acc.setText(f"{self.wpm}/{self.accuracy}%")
            self.timer.stop()  # Stop the timer
            self.ui.display_box.setText("Press Any Key to Continue")  # Display 'Game Over'
            self.ui.input_box.setDisabled(False)  # Disable the input field
            # def eventFilter(self, source, event):
            #     if event.type() == event.KeyPress and event.key() == Qt.Key_Tab:
            #         if source in (self.ui.lan_combo_2, self.ui.input_box):
            #             self.reset_app()
            #             return True
            #     return super().eventFilter(source, event)
    
            # def on_tab_pressed(self):
            #     print("this works")
            #     self.start_game()


            
            

if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = TypingGame()
    window.show()
    app.exec()

