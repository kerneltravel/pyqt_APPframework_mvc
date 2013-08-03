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

from settings_controller import Settings

if __name__ == '__main__': 
    reload(sys)
    sys.setdefaultencoding('utf-8') 
    app = QApplication(sys.argv)
    main_window = Settings()
    #main_window.showMaximized()
    main_window.show()
    sys.exit(app.exec_())
