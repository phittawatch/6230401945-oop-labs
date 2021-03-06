import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *


class Caltrack(QWidget):
    def __init__(self):
        self.a = 1
        self.b = 1
        super().__init__()
        self.initUI()

    def initUI(self):
        name = QLabel('Name ')
        age = QLabel('Age ')
        weight = QLabel('Weight ')
        height = QLabel('Height ')
        gender = QLabel('Gender ')
        ex_fq = QLabel('Exercise frequency ')
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        name.setFont(QFont("Arial", 8))
        name.setStyleSheet("color : yellow")
        age.setFont(QFont("Arial", 8))
        age.setStyleSheet("color : yellow")
        weight.setFont(QFont("Arial", 8))
        weight.setStyleSheet("color : yellow")
        height.setFont(QFont("Arial", 8))
        height.setStyleSheet("color : yellow")
        gender.setFont(QFont("Arial", 8))
        gender.setStyleSheet("color : yellow")
        ex_fq.setFont(QFont("Arial", 8))
        ex_fq.setStyleSheet("color : yellow")
        ok_button.setFont(QFont("Arial", 8))
        ok_button.setStyleSheet("background-color : yellow")
        ok_button.clicked.connect(lambda:self.calculate())
        cancel_button.setFont(QFont("Arial", 8))
        cancel_button.setStyleSheet("background-color : yellow")


        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.weightEdit = QLineEdit()
        self.heightEdit = QLineEdit()


        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1, 1, 2)

        grid.addWidget(age, 2, 0)
        grid.addWidget(self.ageEdit, 2, 1, 1, 2)

        grid.addWidget(weight, 3, 0)
        grid.addWidget(self.weightEdit, 3, 1, 1, 2)

        grid.addWidget(height, 4, 0)
        grid.addWidget(self.heightEdit, 4, 1, 1, 2)

        hbox = QHBoxLayout()
        self.radio_male = QRadioButton("Male")
        self.radio_male.setFont(QFont("Arial", 8))
        self.radio_male.setStyleSheet("color : yellow")
        self.radio_male.setChecked(True)
        self.radio_male.toggled.connect(lambda:self.isClicked(self.radio_male))
        self.radio_female = QRadioButton("Female")
        self.radio_female.setFont(QFont("Arial", 8))
        self.radio_female.setStyleSheet("color : yellow")
        self.radio_female.toggled.connect(lambda:self.isClicked(self.radio_female))
        hbox.addStretch()
        grid.addWidget(gender, 5, 0)
        grid.addWidget(self.radio_male, 5, 1, 1, 2)
        grid.addWidget(self.radio_female, 5, 2, 1, 2)

        grid.addWidget(ok_button, 9, 1)
        grid.addWidget(cancel_button, 9, 2)

        grid.addWidget(ex_fq, 6, 0)
        self.label = QLabel()
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(200, 150, 150, 30)
        ex_fq_list = ["-", "Never", "Seldom", "Sometimes", "Often", "Sportsman"]
        self.combo_box.setEditable(True)
        self.combo_box.addItems(ex_fq_list)
        self.combo_box.activated.connect(lambda:self.Find())
        grid.addWidget(self.combo_box, 6, 1, 1, 2)


        background = QtGui.QImage('background.png')
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(background))

        self.setPalette(palette)
        self.setLayout(grid)
        self.setWindowTitle('CALTRACK DEMO VERSION')
        self.setWindowIcon(QIcon("app-icon.png"))
        self.resize(300, 400)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def calculate(self):
        try:
            if self.a == 1:
                bmr = 66 + (13.7 * float(self.weightEdit.text())) + (5 * float(self.heightEdit.text())) - (6.8 * int(self.ageEdit.text()))
                print(f"[{self.nameEdit.text()}'s BMR is : {bmr:.2f}]")
                if self.content == "Seldom":
                    tdee = bmr * 1.05
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                elif self.content == "Occasionally":
                    tdee = bmr * 1.15
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                elif self.content == "Never":
                    tdee = bmr * 1.15
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                elif self.content == "Sometimes":
                    tdee = bmr * 1.20
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                elif self.content == "Often":
                    tdee = bmr * 1.25
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                elif self.content == "Sportsman":
                    tdee = bmr * 1.45
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

            elif self.b == 1:
                bmr = 65.5 + (9.6 * float(self.weightEdit.text())) + (5 * float(self.heightEdit.text())) - (4.7 * int(self.ageEdit.text()))
                print(f"[{self.nameEdit.text()}'s BMR is : {bmr:.2f}]")
                if self.content == "Seldom":
                    tdee = bmr * 1.05
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                elif self.content == "Occasionally":
                    tdee = bmr * 1.15
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                elif self.content == "Never":
                    tdee = bmr * 1.15
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                elif self.content == "Sometimes":
                    tdee = bmr * 1.20
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                elif self.content == "Often":
                    tdee = bmr * 1.25
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                elif self.content == "Sportsman":
                    tdee = bmr * 1.45
                    reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                 f"{self.nameEdit.text()}'s total daily energy is : {tdee:.2f}",
                                                 QMessageBox.Ok)

                else:
                    pass
        except Exception:
            reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                         f"Value Error please try again......",
                                         QMessageBox.Ok)

    def isClicked(self, b):
        if b.text() == "Male":
            if b.isChecked() == True:
                self.a = 1
            else:
                self.a = 0

        if b.text() == "Female":
            if b.isChecked() == True:
                self.b = 1
            else:
                self.b = 0

    def Find(self):
        self.content = self.combo_box.currentText()
        self.label.setText(self.content)

def mains():
    app = QApplication(sys.argv)
    ex = Caltrack()
    app.exec_()


if __name__ == '__main__':
    mains()
