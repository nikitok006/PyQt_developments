import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTabWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QFormLayout
)


class PercentCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор процентов")
        self.setGeometry(300, 200, 400, 250)

        self.tabs = QTabWidget()
        self.init_tabs()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def init_tabs(self):
        self.tabs.addTab(self.percent_of_number_tab(), "Процент от числа")
        self.tabs.addTab(self.percent_x_of_y_tab(), "% X от Y")
        self.tabs.addTab(self.add_percent_tab(), "Прибавить %")
        self.tabs.addTab(self.subtract_percent_tab(), "Вычесть %")

    def percent_of_number_tab(self):
        tab = QWidget()
        layout = QFormLayout()

        self.p1 = QLineEdit()
        self.n1 = QLineEdit()
        self.r1 = QLabel("Результат:")

        btn = QPushButton("Рассчитать")
        btn.clicked.connect(self.calc_percent_of_number)

        layout.addRow("Процент (%):", self.p1)
        layout.addRow("Число:", self.n1)
        layout.addRow(btn)
        layout.addRow(self.r1)

        tab.setLayout(layout)
        return tab

    def calc_percent_of_number(self):
        try:
            percent = float(self.p1.text())
            number = float(self.n1.text())
            result = number * percent / 100
            self.r1.setText(f"Результат: {result}")
        except ValueError:
            self.r1.setText("Ошибка ввода")

    def percent_x_of_y_tab(self):
        tab = QWidget()
        layout = QFormLayout()

        self.x2 = QLineEdit()
        self.y2 = QLineEdit()
        self.r2 = QLabel("Результат:")

        btn = QPushButton("Рассчитать")
        btn.clicked.connect(self.calc_x_of_y)

        layout.addRow("Число X:", self.x2)
        layout.addRow("Число Y:", self.y2)
        layout.addRow(btn)
        layout.addRow(self.r2)

        tab.setLayout(layout)
        return tab

    def calc_x_of_y(self):
        try:
            x = float(self.x2.text())
            y = float(self.y2.text())
            result = (x / y) * 100
            self.r2.setText(f"Результат: {result:.2f} %")
        except ValueError:
            self.r2.setText("Ошибка ввода")

    def add_percent_tab(self):
        tab = QWidget()
        layout = QFormLayout()

        self.p3 = QLineEdit()
        self.n3 = QLineEdit()
        self.r3 = QLabel("Результат:")

        btn = QPushButton("Рассчитать")
        btn.clicked.connect(self.calc_add_percent)

        layout.addRow("Процент (%):", self.p3)
        layout.addRow("Число:", self.n3)
        layout.addRow(btn)
        layout.addRow(self.r3)

        tab.setLayout(layout)
        return tab

    def calc_add_percent(self):
        try:
            percent = float(self.p3.text())
            number = float(self.n3.text())
            result = number + number * percent / 100
            self.r3.setText(f"Результат: {result}")
        except ValueError:
            self.r3.setText("Ошибка ввода")

    def subtract_percent_tab(self):
        tab = QWidget()
        layout = QFormLayout()

        self.n4 = QLineEdit()
        self.p4 = QLineEdit()
        self.r4 = QLabel("Результат:")

        btn = QPushButton("Рассчитать")
        btn.clicked.connect(self.calc_subtract_percent)

        layout.addRow("Число:", self.n4)
        layout.addRow("Процент (%):", self.p4)
        layout.addRow(btn)
        layout.addRow(self.r4)

        tab.setLayout(layout)
        return tab

    def calc_subtract_percent(self):
        try:
            number = float(self.n4.text())
            percent = float(self.p4.text())
            result = number - number * percent / 100
            self.r4.setText(f"Результат: {result}")
        except ValueError:
            self.r4.setText("Ошибка ввода")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PercentCalculator()
    window.show()
    sys.exit(app.exec_())
