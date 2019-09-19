from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QLabel


class initUI(QWidget):
    def __init__(self):
        super(initUI, self).__init__()
    def on_button_clicked(self):
        alert = QMessageBox()
        alert.setText("Hello World!")
        alert.exec_()


#create application to show
app=QApplication([])

#create new widget
window=initUI()

#create buttons
Btn_Top=QPushButton('Top')
Btn_Bottom=QPushButton('Bottom')
Btn_OK = QPushButton('OK')

#connect single to button
Btn_OK.clicked.connect(window.on_button_clicked)

# Style
app.setStyle('Fusion')

#palette
palette=QPalette()
palette.setColor(QPalette.ButtonText,Qt.red)
app.setPalette(palette)

#Style Sheet
app.setStyleSheet('margin:10ex')

# set Layout for windows
layout=QVBoxLayout()
layout.addWidget(Btn_Bottom)
layout.addWidget(Btn_Top)
layout.addWidget(Btn_OK)

window.setLayout(layout)

# Label
label = QLabel('Heklow Lsaf')

window.show()

app.exec_()

