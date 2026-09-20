import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt 

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        # design layout of the clock here
        self.setWindowTitle("Digital clock")
        self.setGeometry(600, 400, 400, 600)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 150px;
            font-family: Arial;
            color: #b348bd;
        """)
        self.setStyleSheet("background-color: black;")
        

        self.timer.timeout.connect(self.update_time)

        self.timer.start(1000)

        self.update_time

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP") # AP displays the am or pm
        self.time_label.setText(current_time)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
