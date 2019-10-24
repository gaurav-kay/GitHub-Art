from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QMainWindow, QGroupBox, QGridLayout
import datetime

import button_stylesheets
from app import draw


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GitHub Art')
        self.move(200, 200)
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

        self.dates_list = list()
        self.start_day = datetime.date.today() - datetime.timedelta(days=365)
        day_value = int(self.start_day.strftime('%w'))

        if day_value != 0:
            self.start_day -= datetime.timedelta(days=day_value)

        self.main_layout.addWidget(self.create_grid_layout())

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.get_list_dates)
        self.main_layout.addWidget(submit_button)

        save_button = QPushButton('Save Art')
        save_button.clicked.connect(self.save_art)
        self.main_layout.addWidget(save_button)

        self.show()

    def save_art(self):
        with open(f'./saved_art/{str(datetime.datetime.now()).split(".")[0]}.txt', 'w', encoding='utf-8') as f:
            for date in self.dates_list:
                f.write(date)

    def create_grid_layout(self):
        group_box = QGroupBox("Draw desired graphics here")
        layout = QGridLayout()

        day_count = 0

        for column in range(52):
            for row in range(7):
                date_button = QPushButton(
                    f"{(self.start_day + datetime.timedelta(days=day_count)).strftime('%Y-%m-%d %H:%M:%S')} +0530"
                )

                date_button.setMinimumSize(15, 15)
                date_button.setMaximumSize(15, 15)
                date_button.setCheckable(True)
                date_button.setStyleSheet(button_stylesheets.UNCHECKED_BUTTON_STYLESHEET)
                date_button.clicked.connect(self.add_to_list)
                layout.addWidget(date_button, row, column)
                day_count += 1

        layout.setSpacing(3)
        group_box.setLayout(layout)
        return group_box

    def add_to_list(self):
        self.dates_list.append(self.sender().text())

        # print(self.sender().palette().button().color().name())  # holy fuck https://stackoverflow.com/a/43779167/9664283
        if self.sender().palette().button().color().name().lower() == button_stylesheets.UNCHECKED_BUTTON_COLOR.lower():
            self.sender().setStyleSheet(button_stylesheets.CHECKED_LEVEL_1_BUTTON_STYLESHEET)
        elif self.sender().palette().button().color().name().lower() == button_stylesheets.CHECKED_LEVEL_1_BUTTON_COLOR.lower():
            self.sender().setStyleSheet(button_stylesheets.CHECKED_LEVEL_2_BUTTON_STYLESHEET)
        elif self.sender().palette().button().color().name().lower() == button_stylesheets.CHECKED_LEVEL_2_BUTTON_COLOR.lower():
            self.sender().setStyleSheet(button_stylesheets.CHECKED_LEVEL_3_BUTTON_STYLESHEET)
        elif self.sender().palette().button().color().name().lower() == button_stylesheets.CHECKED_LEVEL_3_BUTTON_COLOR.lower():
            self.sender().setStyleSheet(button_stylesheets.CHECKED_LEVEL_4_BUTTON_STYLESHEET)
        elif self.sender().palette().button().color().name().lower() == button_stylesheets.CHECKED_LEVEL_4_BUTTON_COLOR.lower():
            self.sender().setStyleSheet(button_stylesheets.UNCHECKED_BUTTON_STYLESHEET)

            while self.sender().text() in self.dates_list:
                self.dates_list.remove(self.sender().text())

    # def get_button_text(self):
    #     if self.sender().isChecked():
    #         self.sender().setStyleSheet(button_stylesheets.CHECKED_BUTTON_STYLESHEET)
    #         self.dates_list.append(self.sender().text())
    #     else:
    #         self.sender().setStyleSheet(button_stylesheets.UNCHECKED_BUTTON_STYLESHEET)
    #         self.dates_list.remove(self.sender().text())
    #
    #     print(self.sender().text())

    def get_list_dates(self):
        draw(self.dates_list)


if __name__ == '__main__':
    app = QApplication([])
    gui = GUI()
    gui.setFixedSize(gui.size())
    app.exec_()
