from PySide6.QtWidgets import (
     QApplication,
     QWidget,
     )

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Date Selector")
        self.setFixedSize(400, 200) # set dimensions
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
