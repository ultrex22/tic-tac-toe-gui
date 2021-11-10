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
        self.current_player = 'x'
        self.grid_squares_filled = {
            '1': 'F', '2': 'F', '3': 'F',
            '4': 'F', '5': 'F', '6': 'F',
            '7': 'F', '8': 'F', '9': 'F', }
        # center app/ widget
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def _createTitle(self):
        """Create the display."""
        # Create the display widget
        self.title = QLabel('Welcome to Tic Tac Toe')
        self.title.setStyleSheet('QLabel {color: #0000ee; font-size: 20px;}')
        # Set some title's properties
        self.title.setFixedHeight(35)
        self.title.setAlignment(Qt.AlignCenter)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.title)

    def _createGrid(self):
        """Create the grid"""
        grid_Layout = QGridLayout()
        # Button number | position on the QGridLayout
        self.grid = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                     '4': (1, 0), '5': (1, 1), '6': (1, 2),
                     '7': (2, 0), '8': (2, 1), '9': (2, 2)
                     }
        # Create the squares and add them to the grid layout
        for square_num, pos in self.grid.items():
            icon = QPixmap('blank.png')
            self.grid[square_num] = QPushButton(QIcon(icon), square_num)
            self.grid[square_num].setFixedSize(80, 80)
            self.grid[square_num].setIconSize(QSize(70, 70))
            grid_Layout.addWidget(self.grid[square_num], pos[0], pos[1])
        # Add grid_Layout to the general layout
        self.generalLayout.addLayout(grid_Layout)
        self.grid['1'].clicked.connect(
            lambda: self.update_grid(self.grid['1']))
        self.grid['2'].clicked.connect(
            lambda: self.update_grid(self.grid['2']))
        self.grid['3'].clicked.connect(
            lambda: self.update_grid(self.grid['3']))
        self.grid['4'].clicked.connect(
            lambda: self.update_grid(self.grid['4']))
        self.grid['5'].clicked.connect(
            lambda: self.update_grid(self.grid['5']))
        self.grid['6'].clicked.connect(
            lambda: self.update_grid(self.grid['6']))
        self.grid['7'].clicked.connect(
            lambda: self.update_grid(self.grid['7']))
        self.grid['8'].clicked.connect(
            lambda: self.update_grid(self.grid['8']))
        self.grid['9'].clicked.connect(
            lambda: self.update_grid(self.grid['9']))

    def _createNames(self):
        """Create the player plaques."""
        # Create the names widget
        self.player_x = QLineEdit('Player X Turn')
        self.player_x.setReadOnly(True)
        # Set some display's properties
        self.player_x.setFixedHeight(30)
        self.player_x.setAlignment(Qt.AlignCenter)
        self.player_x.setStyleSheet(
            'QLineEdit {background: #11cc00; color: white;}')
        # Add the display to the general layout
        self.generalLayout.addWidget(self.player_x)

        self.player_o = QLineEdit('Player O Turn')
        self.player_o.setReadOnly(True)
        # Set some display's properties
        self.player_o.setFixedHeight(30)
        self.player_o.setAlignment(Qt.AlignCenter)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.player_o)

    def update_grid(self, grid_item):
        print(self.grid_squares_filled[grid_item.text()])
        if self.grid_squares_filled[grid_item.text()] == 'F':
            self.grid_squares_filled[grid_item.text()] = self.current_player
            self.check_for_winner()
            if self.current_player == 'x':
                self.player_o.setStyleSheet(
                    'QLineEdit {background: #11cc00; color: white;}')
                self.player_x.setStyleSheet(
                    'QLineEdit {background: white; color: black;}')
                grid_item.setIcon(QIcon(QPixmap('x_icon.png')))
                self.current_player = 'o'
            elif self.current_player == 'o':
                self.player_x.setStyleSheet(
                    'QLineEdit {background: #11cc00; color: white;}')
                self.player_o.setStyleSheet(
                    'QLineEdit {background: white; color: black;}')
                grid_item.setIcon(QIcon(QPixmap('o_icon.png')))
                self.current_player = 'x'
        else:
            pass

    def check_for_winner(self):
        print('checking for winner or tie...')
        if (self.grid_squares_filled['1'] == self.grid_squares_filled['2'] == self.grid_squares_filled['3'] and self.grid_squares_filled['1'] != 'F' or
            self.grid_squares_filled['4'] == self.grid_squares_filled['5'] == self.grid_squares_filled['6'] and self.grid_squares_filled['4'] != 'F' or
            self.grid_squares_filled['7'] == self.grid_squares_filled['8'] == self.grid_squares_filled['9'] and self.grid_squares_filled['7'] != 'F' or
            self.grid_squares_filled['7'] == self.grid_squares_filled['4'] == self.grid_squares_filled['1'] and self.grid_squares_filled['7'] != 'F' or
            self.grid_squares_filled['8'] == self.grid_squares_filled['5'] == self.grid_squares_filled['2'] and self.grid_squares_filled['8'] != 'F' or
            self.grid_squares_filled['9'] == self.grid_squares_filled['6'] == self.grid_squares_filled['3'] and self.grid_squares_filled['9'] != 'F' or
            self.grid_squares_filled['7'] == self.grid_squares_filled['5'] == self.grid_squares_filled['3'] and self.grid_squares_filled['7'] != 'F' or
                self.grid_squares_filled['9'] == self.grid_squares_filled['5'] == self.grid_squares_filled['1'] and self.grid_squares_filled['9'] != 'F'):
            print(f'You win {self.current_player.upper()}!')
            self.title.setText(f'You win {self.current_player.upper()}!')
        elif len(self.grid_squares_filled) == 12:
            self.title.setText('TIE !!!')


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
