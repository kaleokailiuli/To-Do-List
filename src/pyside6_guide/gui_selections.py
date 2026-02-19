from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton)

from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Date Selector")
        self.setFixedSize(400, 200)
        
        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # push buttons to bottom
        main_layout.addStretch()
        
        # Button layout
        button_layout = QHBoxLayout()
        
        # push buttons right
        button_layout.addStretch()
        
        # Create buttons
        self.cancel_button = QPushButton("Cancel")
        self.select_button = QPushButton("Select")
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.select_button)
        
        # Add button layout to main layout
        main_layout.addLayout(button_layout)

        self.cancel_button.clicked.connect(self.close)
        self.select_button.clicked.connect(self.close) # Closes window for now will open main GUI at some point
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
