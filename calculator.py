# import module name
import sys # sys is a built-in module in python
# from top-level module.submodul import  element1,element2,........
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt6.QtCore import Qt # PyQt6 is a 3rd party library

# 1.  class defination 
class CalculatorApp(QWidget):
    #1.1 prpperty
    #1.2   construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self):  #always put first argument as self, self is internal object
        super().__init__() # classobject.memer

        # classobject.memer
        self.setWindowTitle("My Calculator")
        self.setup_ui()
    #1. function defination is a one time process
    def setup_ui(self):
        # Create the display
        self.display = QLineEdit(self)
        self.display.setFixedHeight(40)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)

        # Create the buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create a grid layout for buttons
        grid_layout = QGridLayout()

        row_val = 1
        col_val = 0

        for button in buttons:
            btn = QPushButton(button, self)
            btn.clicked.connect(lambda state, button=button: self.on_button_click(button) if button != '=' else self.calculate())
            grid_layout.addWidget(btn, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Create the clear button
        clear_button = QPushButton('C', self)
        clear_button.clicked.connect(self.clear_entry)
        grid_layout.addWidget(clear_button, row_val, col_val)

        # Create the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)

    def on_button_click(self, value):
        current_text = self.display.text()
        new_text = current_text + value
        self.display.setText(new_text)

    def clear_entry(self):
        self.display.clear()

    def calculate(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText("Error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec())

