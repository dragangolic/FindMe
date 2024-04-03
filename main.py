from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QBoxLayout, QPushButton, QHBoxLayout, QTreeView, QLineEdit, QMainWindow, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel


class FindMeApp(QMainWindow):
    def __init__(self):
        super(FindMeApp, self).__init__()
        self.setWindowTitle("FindMe")
        self.resize(950, 750)

        main_window = QWidget()

        self.home_button = QPushButton("Home")
        self.settings_button = QPushButton("Settings")
        self.vcard_button = QPushButton("vCard")
        self.find_me = QPushButton("Find Me")
        self.hide_me = QPushButton("Hide Me")

        self.figure = QLabel("Photo")
        self.text = QLabel("Some text")

        # Design
        self.master_layout = QVBoxLayout()

        self.row1 = QHBoxLayout()
        self.col = QVBoxLayout
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()

        self.row1.addWidget(self.home_button)
        self.row1.addWidget(self.settings_button)
        self.row1.addWidget(self.vcard_button)

        picture_box = QLabel("Picture will appear here")
        self.row2.addWidget(picture_box, 35)
        self.row2.addWidget(self.text, 65
                            )

        self.row3.addWidget(self.find_me)
        self.row3.addWidget(self.hide_me)

        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)
        self.master_layout.addLayout(self.row3)

        main_window.setLayout(self.master_layout)
        self.setCentralWidget(main_window)


if __name__ == "__main__":
    app = QApplication([])
    my_app = FindMeApp()
    my_app.show()
    app.exec_()
