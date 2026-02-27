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
    QTableWidgetItem,
    QCheckBox,
    QHeaderView)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase, QFont
import sys

class BlankMainWindow(QMainWindow):
    def __init__(self, selected_date):
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

        # date display
        top_layout = QHBoxLayout()
        top_layout.addStretch()
        year, month, day = selected_date
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        date_text = f"{months[month - 1]} {day}, {year}"
        date_label = QLabel(date_text)
        top_layout.addWidget(date_label)
        main_layout.addLayout(top_layout)

        # task table
        self.task_table = QTableWidget()
        self.task_table.setColumnCount(4)
        self.task_table.horizontalHeader().setVisible(False) # might end up using this for labels
        self.task_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.task_table.resizeRowsToContents()
        main_layout.addWidget(self.task_table)

        main_layout.addStretch()

        button_layout = QHBoxLayout()

        # create buttons
        self.add_button = QPushButton("Add+")
        
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
        
        self.add_button.clicked.connect(self.add_task)
        
        button_layout.addWidget(self.add_button)

        main_layout.addLayout(button_layout)

    def add_task(self):
        # adds row to table
        row = self.task_table.rowCount()
        self.task_table.insertRow(row)

        # checkbox
        checkbox = QCheckBox()
        self.task_table.setCellWidget(row, 0, checkbox)

        # task name
        name_item = QTableWidgetItem("Name: ")
        name_item.setFlags(name_item.flags() | Qt.ItemIsEditable)
        self.task_table.setItem(row, 1, name_item)

        # time dropdown
        time_combo = QComboBox()
        times = ["12:00 AM", "12:30 AM", "1:00 AM", "1:30 AM", "2:00 AM", "2:30 AM",
                 "3:00 AM", "3:30 AM", "4:00 AM", "4:30 AM", "5:00 AM", "5:30 AM",
                 "6:00 AM", "6:30 AM", "7:00 AM", "7:30 AM", "8:00 AM", "8:30 AM",
                 "9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
                 "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM",
                 "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM",
                 "6:00 PM", "6:30 PM", "7:00 PM", "7:30 PM", "8:00 PM", "8:30 PM",
                 "9:00 PM", "9:30 PM", "10:00 PM", "10:30 PM", "11:00 PM", "11:30 PM"]
        time_combo.addItems(times)
        self.task_table.setCellWidget(row, 2, time_combo)

        # remove button
        remove_btn = QPushButton("X")
        remove_btn.setFixedWidth(30)
        remove_btn.clicked.connect(lambda: self.remove_task(row))
        self.task_table.setCellWidget(row, 3, remove_btn)

        # resize rows
        self.task_table.resizeRowsToContents()

    def remove_task(self, row):
        # remove row
        self.task_table.removeRow(row)

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
        self.year_input.setRange(2000, 2100) # range of years
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
        self.day_input.setRange(1, 31) # ranges of days
        self.day_input.setValue(1) # default
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
        self.main_window = BlankMainWindow(self.selected_date)
        self.main_window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # font
    QFontDatabase.addApplicationFont("Knewave")
    font = QFont("Knewave")
    app.setFont(font)
    
    window = MainWindow()
    sys.exit(app.exec())
