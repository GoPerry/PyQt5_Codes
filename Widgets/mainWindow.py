import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QHBoxLayout, QLineEdit, QWidget, \
    QMessageBox


class OtherWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        layout = QHBoxLayout()
        lineEdit = QLineEdit()
        lineEdit.setText("Just to fill up the dialog")
        layout.addWidget(lineEdit)

        self.widget = QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)
        self.setWindowTitle("Win2")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5"
        self.top = 500
        self.left= 400
        self.width= 500
        self.height = 550
        #call init window fun
        self.UIcomponets()
        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        buttonReply = QMessageBox.question(self,"Linux Testing","Do you want to start the testing?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('YES ,Start Testing')
        else:
            print('No，Stop Testing')
        self.show()

    def UIcomponets(self):
        button = QPushButton("Click me",self)
        button.setGeometry(QRect(100,100,111,28))
        button.setText("Click Me")
        button.sizeHint()
        # button.toolTip("Hellow")
        button.setIcon(QtGui.QIcon("home.png"))
        button.setIconSize(QtCore.QSize(40,40))
        # 设置按下button 的signal 处理方法
        button.clicked.connect(self.slotUserNew)

    def slotUserNew(self):
        self.userDiaglog = OtherWindow()
        self.userDiaglog.show()

if __name__ == "__main__":
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

