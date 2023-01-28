from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_foldername())
        self.additem_pushButton.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.deleteitem_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.delete_foldername())
        self.deleteitem_pushButton_2.setGeometry(QtCore.QRect(130, 50, 101, 31))
        self.deleteitem_pushButton_2.setObjectName("deleteitem_pushButton_2")
        self.clearall_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear_all())
        self.clearall_pushButton_3.setGeometry(QtCore.QRect(250, 50, 101, 31))
        self.clearall_pushButton_3.setObjectName("clearall_pushButton_3")
        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(10, 10, 341, 31))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 90, 341, 291))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #add item
    def add_foldername(self):
        #Grab item from input
        item = self.additem_lineEdit.text()

        #add to list
        self.mylist_listWidget.addItem(item)

        #Clearing Input Field
        self.additem_lineEdit.setText("")

    #delete item
    def delete_foldername(self):
        #Grab Current Row 
        clicked = self.mylist_listWidget.currentRow()

        #Delete Selected Row
        self.mylist_listWidget.takeItem(clicked)

    #clear all
    def clear_all(self):
        self.mylist_listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TODO List"))
        self.additem_pushButton.setText(_translate("MainWindow", "Add Item"))
        self.deleteitem_pushButton_2.setText(_translate("MainWindow", "Delete Item"))
        self.clearall_pushButton_3.setText(_translate("MainWindow", "Clear All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())