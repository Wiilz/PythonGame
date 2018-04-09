﻿import sys
from PyQt4 import QtCore, QtGui, uic
import random

form_class = uic.loadUiType("hangman.ui")

#查找字母
def find_letters(letter, a_string):
    locations = []
    start = 0
    while a_string.find(letter, start, len(a_string)) != -1 :
        location = a_string.find(letter, start, len(a_string))
        locations.append(location)
        start = location + 1
    return locations

#玩家猜对字母时，用字母替换横线
def replace_letters(string, locations, letter):
    new_string = ''
    for i in range(0, len(string)):
        if i in locations:
            new_string = new_string + letter
        else:
            new_string = new_string + string[i]
    return new_string

#程序开始时用横线替换字母
def dashes(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    new_string = ''
    for i in word:
        if i in letters:
            new_string += "-"
        else:
            new_string += i
    return new_string

class MyWidget(QtGui.QMainWindow, form_class):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_guess.clicked.connect(self.btn_guess_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)
        self.pieces = [self.head, self.body, self.leftarm, self.leftleg, self.rightarm, self.rightleg]
        self.gallows = [self.line1, self.line2, self.line3, self.line4]
        self.pieces_shown = 0
        self.currentword = ""
        f = open("words.txt",'r')  #得到词汇表
        self.lines = f.readlines()
        f.close()
        self.new_game()

    def new_game(self):
        self.guesses.setText("")
        #从词汇表中随机选择一个单词
        self.currentword = random.choice(self.lines)
        self.currentword = self.currentword.strip()
        for i in self.pieces:
            i.setFrameShadow(QtGui.QFrame.Plain)
            i.setHidden(True)
        for i in self.gallows:
            i.setFrameShadow(QtGui.QFrame.Plain)
        self.word.setText(dashes(self.currentword))
        self.pieces_shown = 0  #调用函数，用横线替换字母

    def btn_guess_clicked(self):
        guess = str(self.guessBox.text())
        if str(self.guesses.text()) != "":
            self.guesses.setText(str(self.guesses.text())+", " + guess)
        else:
            self.guesses.setText(guess)
        if len(guess) == 1:
            if guess in self.currentword:
                locations = find_letters(guess, self.currentword)
                self.word.setText(replace_letters(str(self.word.text()), locations,guess))
                if str(self.word.text()) == self.currentword:
                    self.win()
                else:
                    self.wrong()
            else:
                if guess == self.currentword:
                    self.win()
                else:
                    self.wrong()
            self.guessBox.setText("")

        def win(self):
            QtGui.QMessageBox.information(self,"Hangman","You win!")
            self.new_game()

        def wrong(self):
            self.pieces_shown += 1
            for i in range(self.pieces_shown):
                self.pieces[i].setHidden(False)
            if self.pieces_shown == len(self.pieces):
                message = "You lose. The word was " + self.currentword
                QtGui.QMessageBox.warning(self,"Hangman",message)
                self.new_game()
                
        def menuExit_selected(self):
            self.close()
app = QtGui.QApplication(sys.argv)
myapp = MyWidget(None)
myapp.show()
app.exec_()
