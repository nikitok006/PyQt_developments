import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QRadioButton, QButtonGroup, QGridLayout
)


class MatrixCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор матриц")
        self.setGeometry(200, 100, 600, 500)

        main_layout = QVBoxLayout()

        # ---- Size selection ----
        size_layout = QHBoxLayout()
        self.rows_input = QLineEdit()
        self.cols_input = QLineEdit()
        self.rows_input.setPlaceholderText("Строки")
        self.cols_input.setPlaceholderText("Столбцы")

        size_layout.addWidget(QLabel("Размер матрицы:"))
        size_layout.addWidget(self.rows_input)
        size_layout.addWidget(self.cols_input)

        # ---- Operation ----
        op_layout = QHBoxLayout()
        op_layout.addWidget(QLabel("Операция:"))

        self.rb_add = QRadioButton("Сложение")
        self.rb_sub = QRadioButton("Вычитание")
        self.rb_add.setChecked(True)

        self.op_group = QButtonGroup()
        self.op_group.addButton(self.rb_add)
        self.op_group.addButton(self.rb_sub)

        op_layout.addWidget(self.rb_add)
        op_layout.addWidget(self.rb_sub)

        # ---- Buttons ----
        self.create_btn = QPushButton("Создать матрицы")
        self.create_btn.clicked.connect(self.create_matrices)

        self.calc_btn = QPushButton("Рассчитать")
        self.calc_btn.clicked.connect(self.calculate)
        self.calc_btn.setEnabled(False)

        # ---- Layouts for matrices ----
        self.matrix_layout = QHBoxLayout()
        self.matrix_a_layout = QGridLayout()
        self.matrix_b_layout = QGridLayout()
        self.matrix_r_layout = QGridLayout()

        self.matrix_layout.addLayout(self.matrix_a_layout)
        self.matrix_layout.addLayout(self.matrix_b_layout)
        self.matrix_layout.addLayout(self.matrix_r_layout)

        # ---- Add to main layout ----
        main_layout.addLayout(size_layout)
        main_layout.addLayout(op_layout)
        main_layout.addWidget(self.create_btn)
        main_layout.addLayout(self.matrix_layout)
        main_layout.addWidget(self.calc_btn)

        self.setLayout(main_layout)

        self.a_inputs = []
        self.b_inputs = []
        self.r_labels = []

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def create_matrices(self):
        try:
            rows = int(self.rows_input.text())
            cols = int(self.cols_input.text())

            if rows <= 0 or cols <= 0:
                return

            self.clear_layout(self.matrix_a_layout)
            self.clear_layout(self.matrix_b_layout)
            self.clear_layout(self.matrix_r_layout)

            self.a_inputs = []
            self.b_inputs = []
            self.r_labels = []

            for i in range(rows):
                row_a = []
                row_b = []
                row_r = []

                for j in range(cols):
                    a = QLineEdit()
                    b = QLineEdit()
                    r = QLabel("0")

                    a.setFixedWidth(50)
                    b.setFixedWidth(50)
                    r.setFixedWidth(50)

                    self.matrix_a_layout.addWidget(a, i, j)
                    self.matrix_b_layout.addWidget(b, i, j)
                    self.matrix_r_layout.addWidget(r, i, j)

                    row_a.append(a)
                    row_b.append(b)
                    row_r.append(r)

                self.a_inputs.append(row_a)
                self.b_inputs.append(row_b)
                self.r_labels.append(row_r)

            self.calc_btn.setEnabled(True)

        except ValueError:
            pass

    def calculate(self):
        try:
            rows = len(self.a_inputs)
            cols = len(self.a_inputs[0])

            for i in range(rows):
                for j in range(cols):
                    a = float(self.a_inputs[i][j].text())
                    b = float(self.b_inputs[i][j].text())

                    result = a + b if self.rb_add.isChecked() else a - b
                    self.r_labels[i][j].setText(str(result))

        except ValueError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatrixCalculator()
    window.show()
    sys.exit(app.exec_())
