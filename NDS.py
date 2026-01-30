import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QRadioButton, QButtonGroup
)


class VATCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор НДС")
        self.setGeometry(300, 200, 380, 300)

        main_layout = QVBoxLayout()

        # ---- Input fields ----
        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Сумма")

        self.vat_rate = QLineEdit()
        self.vat_rate.setPlaceholderText("Ставка НДС (%)")

        # ---- Operation selection ----
        op_layout = QHBoxLayout()
        op_layout.addWidget(QLabel("Операция:"))

        self.rb_add = QRadioButton("Начислить НДС")
        self.rb_extract = QRadioButton("Выделить НДС")
        self.rb_add.setChecked(True)

        self.op_group = QButtonGroup()
        self.op_group.addButton(self.rb_add)
        self.op_group.addButton(self.rb_extract)

        op_layout.addWidget(self.rb_add)
        op_layout.addWidget(self.rb_extract)

        # ---- Button & result ----
        self.button = QPushButton("Рассчитать")
        self.button.clicked.connect(self.calculate)

        self.result = QLabel("Результат:")

        # ---- Layout assembling ----
        main_layout.addWidget(QLabel("Введите данные:"))
        main_layout.addWidget(self.amount)
        main_layout.addWidget(self.vat_rate)
        main_layout.addLayout(op_layout)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.result)

        self.setLayout(main_layout)

    def calculate(self):
        try:
            amount = float(self.amount.text())
            rate = float(self.vat_rate.text())

            if self.rb_add.isChecked():
                vat = amount * rate / 100
                total = amount + vat
                self.result.setText(
                    f"НДС: {vat:.2f}\n"
                    f"Сумма с НДС: {total:.2f}"
                )
            else:
                vat = amount * rate / (100 + rate)
                base = amount - vat
                self.result.setText(
                    f"НДС: {vat:.2f}\n"
                    f"Сумма без НДС: {base:.2f}"
                )

        except ValueError:
            self.result.setText("Введите корректные числовые значения")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VATCalculator()
    window.show()
    sys.exit(app.exec_())
