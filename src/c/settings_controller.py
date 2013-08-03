# -*- coding: utf-8 -*-

"""
Module implementing Settings.
"""
import os
import sys
#print sys.getdefaultencoding()
from ctypes import *

from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot, Qt, QPoint, QTime, QTimer, QTextCodec
from PyQt4.QtCore import QTextDecoder, QByteArray, QString
from PyQt4.QtGui import QApplication, QMainWindow, QTableWidgetItem, QKeyEvent, QTextCursor

from ui.Ui_designer_generated import Ui_Settings
from m.mydatawrapper import MyDataWrapper
class Settings(QDialog, Ui_Settings):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(Settings,self).__init__(parent)
        self.setupUi(self)      
        self.initUi()
        self.initData()
        
    def initUi(self):
        #QTimer.singleShot(0,self.searchWords,QtCore.SLOT(self.searchWords.setFocus()))
        self.tblPcsSet.setRowCount(self.maxRowCount);
        pass
        
    def initData(self):
        self.data = MyDataWrapper("hello world!")
        self.curRow = 0
        self.maxRowCount = 10
        pass
        
    @pyqtSlot()
    def on_btnAddPcsApp_clicked(self):
        newItem = QTableWidgetItem( self.data.interface_doSomeThing())
        self.tblPcsSet.setItem(self.curRow, 0, newItem);
        self.curRow += 1
    pass
    
if __name__ == '__main__': 
    reload(sys)
    sys.setdefaultencoding('utf-8') 
    app = QApplication(sys.argv)
    main_window = Settings()
    #main_window.showMaximized()
    main_window.show()
    sys.exit(app.exec_())
