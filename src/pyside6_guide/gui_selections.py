from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QSpinBox,
    QComboBox)

from PySide6.QtCore import Qt
import sys

class BlankMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main GUI")
        self.setFixedSize(600, 400)

        # central widget
        central = QWidget(self)
        self.setCentralWidget(central)

        # simple layout and label
        layout = QVBoxLayout(central)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addStretch()
        layout.addStretch()

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
        
        # date inputs area
        inputs_layout = QHBoxLayout()
        # year input
        year_layout = QVBoxLayout()
        year_layout.addWidget(QLabel("Year:"))
        self.year_input = QSpinBox()
        self.year_input.setRange(2000, 2100)
        self.year_input.setValue(2026) # Default
        year_layout.addWidget(self.year_input)
        inputs_layout.addLayout(year_layout)

        # month input
        month_layout = QVBoxLayout()
        month_layout.addWidget(QLabel("Month:"))
        self.month_input = QComboBox()
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        self.month_input.addItems(months)
        month_layout.addWidget(self.month_input)
        inputs_layout.addLayout(month_layout)

        # day input
        day_layout = QVBoxLayout()
        day_layout.addWidget(QLabel("Day:"))
        self.day_input = QSpinBox()
        self.day_input.setRange(1, 31) 
        self.day_input.setValue(1)
        day_layout.addWidget(self.day_input)
        inputs_layout.addLayout(day_layout)

        main_layout.addLayout(inputs_layout)

        # pushes buttons to bottom
        main_layout.addStretch()
        
        # Button layout
        button_layout = QHBoxLayout()
        
        # push buttons to the right
        button_layout.addStretch()
        
        # Create buttons
        self.cancel_button = QPushButton("Cancel")
        self.select_button = QPushButton("Select")
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.select_button)
        
        # Add button layout to main layout
        main_layout.addLayout(button_layout)

        self.cancel_button.clicked.connect(self.close)
        self.select_button.clicked.connect(self.open_main_gui)
        
        self.show()

    def open_main_gui(self):
        # retrieve selected date
        year = self.year_input.value()
        month = self.month_input.currentIndex() + 1
        day = self.day_input.value()
        self.selected_date = (year, month, day)

        # open blank main gui
        self.main_window = BlankMainWindow()
        self.main_window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
