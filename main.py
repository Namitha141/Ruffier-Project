from PyQt5.QtCore import Qt
from PyQt5.QtWidgets  import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit

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

screen2 = QVBoxLayout()
name = QLabel("Enter your full name:")
screen2btn = QLineEdit(Full name)
years = QLabel("Full years:")
agebtn = QLineEdit("0")
instr = QLabel("Lie on your back.... ect")
start1 = QPushButton("Start the first test")
test1 = QLineEdit("0")
instr2 = QLabel("perform 30 squats in 45 seconds..... ect")
start2 = QPushButton("Start doing squats")
instr3 = QLabel("Lie on your back.... ect")
start3 = QPushButton("Start the final test")
test2 = QLineEdit("0")
test3 = QLineEdit("0")
screen2.addWidget(name)
screen2.addWidget(screen2btn)
screen2.addWidget(years)
screen2.addWidget(agebtn)
screen2.addWidget(instr)
screen2.addWidget(start1)
screen2.addWidget(test1)
screen2.addWidget(instr2)
screen2.addWidget(start2)
screen2.addWidget(instr3)
screen2.addWidget(start3)
screen2.addWidget(test2)
screen2.addWidget(test3)










main_win.show()
app.exec_()