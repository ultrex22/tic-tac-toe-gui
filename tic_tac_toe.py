""" Simple Tic Tac Toe GUI game using PyQt5.
    I built this with some online code snippits and the GUI otherwise by hand , not using Designer.
"""

import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QLabel, QMainWindow, QMessageBox, QWidget
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout

__version__ = '1.0'
__author__ = 'Ron Brilhante'


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle(' ')
        self.setFixedWidth(350)
        self.setFixedHeight(400)
        self.general_layout = QVBoxLayout()
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.general_layout)
        self.create_title()
        self.create_grid()
        self.create_names()
        self.connect()
        self.turns = 0
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
        self.setStyleSheet('background-color: rgb(170, 170, 255);')

    def create_title(self):
        """Create the title display."""
        # Create the display widget
        self.title = QLabel('Welcome to Tic Tac Toe!')
        self.title.setStyleSheet('QLabel {color: #333333; font-size: 20px;}')
        # Set some title's properties
        self.title.setFixedHeight(35)
        self.title.setAlignment(Qt.AlignCenter)
        # Add the display to the general layout
        self.general_layout.addWidget(self.title)

    def create_grid(self):
        """Create the grid"""
        grid_layout = QGridLayout()
        # Button number | position on the QGridLayout
        self.grid = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                     '4': (1, 0), '5': (1, 1), '6': (1, 2),
                     '7': (2, 0), '8': (2, 1), '9': (2, 2)
                     }
        # Create the squares and add them to the grid layout
        for square_num, pos in self.grid.items():
            self.grid[square_num] = QPushButton(square_num)
            self.grid[square_num].setFixedSize(80, 80)
            self.grid[square_num].setIconSize(QSize(70, 70))
            grid_layout.addWidget(self.grid[square_num], pos[0], pos[1])
            # change text to bg color to hide it, aadd border to center icon
            self.grid[square_num].setStyleSheet(
                'QPushButton {padding-left: 12px; color: #d6d6fc};')
        # Add grid_layout to the general layout
        self.general_layout.addLayout(grid_layout)

    def connect(self):
        """ 
        Setup off all the button click events.
        """
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

    def create_names(self):
        """Create the player plaques."""
        # Create the names widget
        self.player_x = QLineEdit('Player X Turn')
        self.player_x.setReadOnly(True)
        # Set some display's properties
        self.player_x.setFixedHeight(30)
        self.player_x.setAlignment(Qt.AlignCenter)
        self.player_x.setStyleSheet(
            'QLineEdit {background: ; color: white;}')
        # Add the display to the general layout
        self.general_layout.addWidget(self.player_x)

        self.player_o = QLineEdit('Player O Turn')
        self.player_o.setReadOnly(True)
        # Set some display's properties
        self.player_o.setFixedHeight(30)
        self.player_o.setAlignment(Qt.AlignCenter)
        # Add the display to the general layout
        self.general_layout.addWidget(self.player_o)

        self.player_x.setStyleSheet(
            'QLineEdit {background: #00aaff; color: white;}')
        self.player_o.setStyleSheet(
            'QLineEdit {background: white; color: black;}')

    def update_grid(self, grid_item):
        """updates the game board with X or O and icon, also updates background color for player turn
        Args:
            grid_item (QPushbutton Object): Takes the curredct box clicked on and places icon.
        """
        if self.grid_squares_filled[grid_item.text()] == 'F':
            self.turns += 1
            self.grid_squares_filled[grid_item.text()] = self.current_player
            if self.current_player == 'x':
                self.player_o.setStyleSheet(
                    'QLineEdit {background: #00aaff; color: white;}')
                self.player_x.setStyleSheet(
                    'QLineEdit {background: white; color: black;}')
                grid_item.setIcon(QIcon(QPixmap('icons/x_icon.png')))
                self.check_for_winner()
                self.current_player = 'o'
            elif self.current_player == 'o':
                self.player_x.setStyleSheet(
                    'QLineEdit {background:#00aaff ; color: white;}')
                self.player_o.setStyleSheet(
                    'QLineEdit {background: white; color: black;}')
                grid_item.setIcon(QIcon(QPixmap('icons/o_icon.png')))
                self.check_for_winner()
                self.current_player = 'x'
        else:
            pass

    def check_for_winner(self):
        """
        Checks the board for a winner and if no winner then its a Tie.
        """
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
            self.play_again()

        elif self.turns == 9:
            print('TIE !!')
            self.title.setText('TIE !!!')
            self.play_again()

    def play_again(self):
        """Creates and displays the message box to show winner and ask if user wants to play again.
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText(
            f'{self.current_player.upper()}  Wins!\nDo you want to play again?')
        msg_box.setWindowTitle("WINNER!")
        msg_box.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msg_box.buttonClicked.connect(self.decide)
        msg_box.exec()

    def decide(self, i):
        """If the user wants to play again, reset the board to initial state. Otherwise game app closes.

        Args:
            i (QMessagebox object): This is the response object from asking if the user wants to play again.
        """
        choice = i.text()
        if choice == '&Yes':
            # reset board
            self.turns = 0
            self.current_player = 'x'
            self.grid_squares_filled = {
                '1': 'F', '2': 'F', '3': 'F',
                '4': 'F', '5': 'F', '6': 'F',
                '7': 'F', '8': 'F', '9': 'F', }
            self.title.setText('Welcome to Tic Tac Toe')
            self.title.setStyleSheet(
                'QLabel {color: #0000ee; font-size: 20px;}')
            self.player_x.setStyleSheet(
                'QLineEdit {background: ; color: white;}')
            self.player_o.setStyleSheet(
                'QLineEdit {background: white; color: black;}')
            for square_num in self.grid:
                self.grid[square_num].setIcon(QIcon(QPixmap('')))
        if choice == '&No':
            # exit game
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
