import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

imagePath = r"/media/pi/ESD-USB3/New GUI/newGUI_files/"

def initStaticGUI_Heating(self):
        print("Static GUI Initializing...")
        
        lbl_background = QLabel(self)
        lbl_background.setPixmap(QPixmap(imagePath + "background.png").scaled(810, 490, transformMode = Qt.SmoothTransformation))
        lbl_background.move(-1,0)
        lbl_background.adjustSize() 
        
        window_bk = QLabel(self)
        window_bk.setPixmap(QPixmap(imagePath + "window_bk.png").scaled(372, 363, transformMode = Qt.SmoothTransformation))
        window_bk.move(17,101)
        window_bk.adjustSize()
        
        window_hlt = QLabel(self)
        window_hlt.setPixmap(QPixmap(imagePath + "window_hlt.png").scaled(372, 363, transformMode = Qt.SmoothTransformation))
        window_hlt.move(406,101)
        window_hlt.adjustSize() 
        
        
def initStaticGUI_Mashing(self):
        lbl_background = QLabel(self)
        lbl_background.setPixmap(QPixmap(imagePath + "background.png").scaled(800, 480, transformMode = Qt.SmoothTransformation))
        lbl_background.move(0,0)
        lbl_background.adjustSize()        
        
        window_mlt = QLabel(self)
        window_mlt.setPixmap(QPixmap(imagePath + "window_mlt.png").scaled(372, 363, transformMode = Qt.SmoothTransformation))
        window_mlt.move(17,101)
        window_mlt.adjustSize()
        
        window_hlt = QLabel(self)
        window_hlt.setPixmap(QPixmap(imagePath + "window_hlt.png").scaled(372, 363, transformMode = Qt.SmoothTransformation))
        window_hlt.move(406,101)
        window_hlt.adjustSize()
        
def initStaticGUI_Boiling(self):
        lbl_background = QLabel(self)
        lbl_background.setPixmap(QPixmap(imagePath + "background.png").scaled(800, 480, transformMode = Qt.SmoothTransformation))
        lbl_background.move(0,0)
        lbl_background.adjustSize()
        
        window_bk = QLabel(self)
        window_bk.setPixmap(QPixmap(imagePath + "window_bk.png").scaled(372, 363, transformMode = Qt.SmoothTransformation))
        window_bk.move(17,101)
        window_bk.adjustSize()
        
        window_bk_temp = QLabel(self)
        window_bk_temp.setPixmap(QPixmap(imagePath + "bk_temp.png").scaled(372, 174, transformMode = Qt.SmoothTransformation))
        window_bk_temp.move(406,101)
        window_bk_temp.adjustSize()
        
        window_bk_timer = QLabel(self)
        window_bk_timer.setPixmap(QPixmap(imagePath + "bk_timer.png").scaled(372, 174, transformMode = Qt.SmoothTransformation))
        window_bk_timer.move(406,292)
        window_bk_timer.adjustSize()
        
