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
        self.setGeometry(300, 200, 400, 350)

        main_layout = QVBoxLayout()

        # ---- Room size ----
        self.room_length = QLineEdit()
        self.room_width = QLineEdit()
        self.room_length.setPlaceholderText("Длина комнаты (см)")
        self.room_width.setPlaceholderText("Ширина комнаты (см)")

        # ---- Board size ----
        self.board_length = QLineEdit()
        self.board_width = QLineEdit()
        self.board_length.setPlaceholderText("Длина доски (мм)")
        self.board_width.setPlaceholderText("Ширина доски (мм)")

        # ---- Boards per pack ----
        self.boards_per_pack = QLineEdit()
        self.boards_per_pack.setPlaceholderText("Досок в упаковке")

        # ---- Direction ----
        direction_layout = QHBoxLayout()
        direction_layout.addWidget(QLabel("Направление укладки:"))

        self.rb_len = QRadioButton("Вдоль длины")
        self.rb_wid = QRadioButton("Вдоль ширины")
        self.rb_len.setChecked(True)

        self.dir_group = QButtonGroup()
        self.dir_group.addButton(self.rb_len, 1)
        self.dir_group.addButton(self.rb_wid, 2)

        direction_layout.addWidget(self.rb_len)
        direction_layout.addWidget(self.rb_wid)

        # ---- Button & result ----
        self.button = QPushButton("Рассчитать")
        self.button.clicked.connect(self.calculate)

        self.result = QLabel("Результат:")

        # ---- Layout assembling ----
        main_layout.addWidget(QLabel("Размеры комнаты:"))
        main_layout.addWidget(self.room_length)
        main_layout.addWidget(self.room_width)

        main_layout.addWidget(QLabel("Размеры доски:"))
        main_layout.addWidget(self.board_length)
        main_layout.addWidget(self.board_width)

        main_layout.addWidget(self.boards_per_pack)
        main_layout.addLayout(direction_layout)
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

            boards_needed = math.ceil(room_area / board_area)
            packs_needed = math.ceil(boards_needed / boards_in_pack)

            self.result.setText(
                f"Площадь комнаты: {room_area:.2f} м²\n"
                f"Необходимо досок: {boards_needed}\n"
                f"Необходимо упаковок: {packs_needed}"
            )

        except ValueError:
            self.result.setText("Проверьте корректность ввода данных")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LaminateCalculator()
    window.show()
    sys.exit(app.exec_())
