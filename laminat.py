import sys
import math
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QRadioButton, QButtonGroup
)


class LaminateCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор ламината")
        self.setGeometry(300, 200, 420, 420)

        main_layout = QVBoxLayout()

        self.room_length = QLineEdit()
        self.room_width = QLineEdit()
        self.room_length.setPlaceholderText("Длина комнаты (см)")
        self.room_width.setPlaceholderText("Ширина комнаты (см)")

        self.board_length = QLineEdit()
        self.board_width = QLineEdit()
        self.board_length.setPlaceholderText("Длина доски (мм)")
        self.board_width.setPlaceholderText("Ширина доски (мм)")

        self.boards_per_pack = QLineEdit()
        self.boards_per_pack.setPlaceholderText("Досок в упаковке")

        dir_layout = QHBoxLayout()
        dir_layout.addWidget(QLabel("Направление укладки:"))

        self.rb_len = QRadioButton("Вдоль длины")
        self.rb_wid = QRadioButton("Вдоль ширины")
        self.rb_len.setChecked(True)

        self.dir_group = QButtonGroup()
        self.dir_group.addButton(self.rb_len)
        self.dir_group.addButton(self.rb_wid)

        dir_layout.addWidget(self.rb_len)
        dir_layout.addWidget(self.rb_wid)

        method_layout = QHBoxLayout()
        method_layout.addWidget(QLabel("Способ укладки:"))

        self.rb_no_cut = QRadioButton("Без отрезков")
        self.rb_with_cut = QRadioButton("С отрезками")
        self.rb_no_cut.setChecked(True)

        self.method_group = QButtonGroup()
        self.method_group.addButton(self.rb_no_cut)
        self.method_group.addButton(self.rb_with_cut)

        method_layout.addWidget(self.rb_no_cut)
        method_layout.addWidget(self.rb_with_cut)

        self.min_cut = QLineEdit()
        self.min_cut.setPlaceholderText("Мин. длина обрезка (мм)")
        self.min_cut.setEnabled(False)

        self.rb_with_cut.toggled.connect(
            lambda checked: self.min_cut.setEnabled(checked)
        )

        self.button = QPushButton("Рассчитать")
        self.button.clicked.connect(self.calculate)

        self.result = QLabel("Результат:")

        main_layout.addWidget(QLabel("Размеры комнаты:"))
        main_layout.addWidget(self.room_length)
        main_layout.addWidget(self.room_width)

        main_layout.addWidget(QLabel("Размеры доски:"))
        main_layout.addWidget(self.board_length)
        main_layout.addWidget(self.board_width)

        main_layout.addWidget(self.boards_per_pack)
        main_layout.addLayout(dir_layout)
        main_layout.addLayout(method_layout)
        main_layout.addWidget(self.min_cut)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.result)

        self.setLayout(main_layout)

    def calculate(self):
        try:
            room_l = float(self.room_length.text()) / 100
            room_w = float(self.room_width.text()) / 100

            board_l = float(self.board_length.text()) / 1000
            board_w = float(self.board_width.text()) / 1000

            boards_in_pack = int(self.boards_per_pack.text())

            room_area = room_l * room_w
            board_area = board_l * board_w

            base_boards = room_area / board_area
            if self.rb_with_cut.isChecked():
                min_cut = float(self.min_cut.text())
                waste_coeff = 1.05 if min_cut <= board_l * 1000 / 2 else 1.08
            else:
                waste_coeff = 1.10

            boards_needed = math.ceil(base_boards * waste_coeff)
            packs_needed = math.ceil(boards_needed / boards_in_pack)

            self.result.setText(
                f"Площадь комнаты: {room_area:.2f} м²\n"
                f"Досок с учётом отходов: {boards_needed}\n"
                f"Упаковок: {packs_needed}"
            )

        except ValueError:
            self.result.setText("Проверьте ввод данных")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LaminateCalculator()
    window.show()
    sys.exit(app.exec_())
