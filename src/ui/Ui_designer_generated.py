# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\tmp\python\pyqt_framework\src\ui\designer_generated.ui'
#
# Created: Sat Aug 03 09:14:53 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(606, 527)
        self.gridLayout = QtGui.QGridLayout(Settings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(Settings)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.tblLoginSet = QtGui.QTableWidget(Settings)
        self.tblLoginSet.setObjectName(_fromUtf8("tblLoginSet"))
        self.tblLoginSet.setColumnCount(2)
        self.tblLoginSet.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblLoginSet.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblLoginSet.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tblLoginSet)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Settings)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.tblPcsSet = QtGui.QTableWidget(Settings)
        self.tblPcsSet.setObjectName(_fromUtf8("tblPcsSet"))
        self.tblPcsSet.setColumnCount(3)
        self.tblPcsSet.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblPcsSet.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblPcsSet.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblPcsSet.setHorizontalHeaderItem(2, item)
        self.tblPcsSet.horizontalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tblPcsSet)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAddPcsApp = QtGui.QPushButton(Settings)
        self.btnAddPcsApp.setObjectName(_fromUtf8("btnAddPcsApp"))
        self.horizontalLayout.addWidget(self.btnAddPcsApp)
        self.btnDelPcsApp = QtGui.QPushButton(Settings)
        self.btnDelPcsApp.setObjectName(_fromUtf8("btnDelPcsApp"))
        self.horizontalLayout.addWidget(self.btnDelPcsApp)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 7)
        self.verticalLayout_3.setStretch(2, 1)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Settings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "current user settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Settings", "my login:", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblLoginSet.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("Settings", "user name", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblLoginSet.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("Settings", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Settings", "my pcs netdisk info:", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblPcsSet.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("Settings", "app name", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblPcsSet.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("Settings", "app screct", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblPcsSet.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("Settings", "access token", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddPcsApp.setText(QtGui.QApplication.translate("Settings", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelPcsApp.setText(QtGui.QApplication.translate("Settings", "delete", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Settings = QtGui.QDialog()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())

