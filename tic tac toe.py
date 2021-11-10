# Filename: main_window.py

__version__ = '0.1'
__author__ = 'Ron Brilhante'

"""Main Window-Style application."""

import sys
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QCheckBox, QDesktopWidget, QLabel, QMainWindow, QWidget
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Tic Tac Toe')
        self.setFixedWidth(375)
        self.setFixedHeight(400)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createTitle()
        self._createGrid()
        self._createNames()
        # center app/ widget
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def _createTitle(self):
        """Create the display."""
        # Create the display widget
        self.display = QLabel('Welcome to Tic Tac Toe')
        self.display.setStyleSheet('QLabel {color: #0000ee; font-size: 20px;}')
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignCenter)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createGrid(self):
        """Create the ."""
        self.grid = {}
        grid_Layout = QGridLayout()
        # Button | position on the QGridLayout
        self.grid = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                     '4': (1, 0), '5': (1, 1), '6': (1, 2),
                     '7': (2, 0), '8': (2, 1), '9': (2, 2)
                     }
        # Create the squares and add them to the grid layout
        for square_txt, pos in self.grid.items():
            icon = QPixmap('blank.png')
            self.grid[square_txt] = QPushButton(QIcon(icon), "")
            self.grid[square_txt].setFixedSize(80, 80)
            self.grid[square_txt].setIconSize(QSize(70, 70))
            grid_Layout.addWidget(self.grid[square_txt], pos[0], pos[1])
        # Add grid_Layout to the general layout
        self.generalLayout.addLayout(grid_Layout)
        self.grid['1'].clicked.connect(self.player_o_turn)
        self.grid['1'] = QPushButton(QIcon(QPixmap('x_icon.png')), "")

    def _createNames(self):
        """Create the player plaque."""
        # Create the display widget
        self.display = QLineEdit('Player X Turn')
        self.display.setReadOnly(True)
        # Set some display's properties
        self.display.setFixedHeight(30)
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setStyleSheet(
            'QLineEdit {background: #11cc00; color: white;}')
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

        self.display2 = QLineEdit('Player O Turn')
        self.display2.setReadOnly(True)
        # Set some display's properties
        self.display2.setFixedHeight(30)
        self.display2.setAlignment(Qt.AlignCenter)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display2)

    def player_o_turn(self):
        self.display2.setStyleSheet(
            'QLineEdit {background: #11cc00; color: white;}')
        self.display.setStyleSheet(
            'QLineEdit {background: white; color: black;}')
        self.grid['1']

    def player_x_turn(self):
        pass

    def is_winner(self):
        pass


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
