from PyQt5.QtCore import Qt
from PyQt5.QtWidgets  import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()

main_win.resize(800, 600)
main_win.setWindowTitle("Ruffier Cardiac Health Test")
screen1 = QVBoxLayout()
instructions = QLabel("Welcome to the ruffier test!\nGet ready to test your cardiac fitness.\n\nPress the button below to begin!")
screen1btn = QPushButton("Begin Test")
screen1.addWidget(instructions)
screen1.addWidget(screen1btn)
main_win.setLayout(screen1)

main_win.show()
app.exec_()