from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QSpinBox,
    QComboBox,
    QTableWidget,
    QTableWidgetItem)

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

        # main layout
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # task table
        self.task_table = QTableWidget()
        self.task_table.setColumnCount(3)
        self.task_table.horizontalHeader().setVisible(False) # might end up using this for labels
        main_layout.addWidget(self.task_table)

        main_layout.addStretch()

        button_layout = QHBoxLayout()

        # create buttons
        self.add_button = QPushButton("Add+")
        self.remove_button = QPushButton("Remove-")
        self.edit_button = QPushButton("Edit")
        
        # Button styling
        button_style = """
            background-color: #FFFFFF;
            color: black;
            border: 1px solid #CCCCCC;
            padding: 10px;
            font-size: 14px;
            border-radius: 5px;
        """
        self.add_button.setStyleSheet(button_style)
        self.remove_button.setStyleSheet(button_style)
        self.edit_button.setStyleSheet(button_style)
        
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.remove_button)
        button_layout.addWidget(self.edit_button)

        main_layout.addLayout(button_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Date Selector")
        self.setFixedSize(400, 200)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
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
        button_layout = QHBoxLayout()
        
        # push buttons to the right
        button_layout.addStretch()
        
        # Create buttons
        self.cancel_button = QPushButton("Cancel")
        self.select_button = QPushButton("Select")
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.select_button)
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

        # open main gui
        self.main_window = BlankMainWindow()
        self.main_window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
