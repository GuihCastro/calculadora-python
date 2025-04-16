from PySide6.QtWidgets import QGridLayout, QMessageBox, QPushButton, QWidget
from PySide6.QtCore import Slot
from typing import TYPE_CHECKING
from utils import isEmpty, isDigitOrDot, isOperator, isValidNumber
if TYPE_CHECKING:
    from display import Display, Info
    from main_window import MainWindow


class GridLayout(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._window = window
        self._display = display
        self._info = info
        self._grid_mask = [
            ['C', '◀', '^', '÷'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-',  '0', '.', '=']
        ]

    def mntGrid(self):
        for i, row in enumerate(self._grid_mask):
            for j, col in enumerate(row):
                btn = Button(col, self._display, self._info, self._window)

                if isEmpty(col):
                    continue

                if not isDigitOrDot(col):
                    btn.setProperty('cssClass', 'specialButton')

                self.addWidget(btn, i, j)


class Button(QPushButton):

    def __init__(self, txt: str, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._configStyle()
        self.setText(txt)
        self._window = window
        self._display = display
        self._info = info
        self._equation = ''
        self.clicked.connect(self._insertToDisplay)
        if txt == '=':
            self._display.eq_requested.connect(self._click)
        if txt == '◀':
            self._display.bs_requested.connect(self._click)
        if txt == 'C':
            self._display.clr_requested.connect(self._click)
        if isDigitOrDot(txt) and txt:
            self._display.input_requested.connect(self._input)
        if isOperator(txt):
            self._display.op_requested.connect(self._operation)
        if txt == '+/-':
            self.clicked.connect(self._invertNumber)

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self._info.setText(self.equation)

    def _configStyle(self):
        self.setMinimumSize(80, 80)

    @Slot(bool)
    def _insertToDisplay(self):
        if self.property('cssClass') == 'specialButton':
            self._handleSpecialButton()
            return

        if len(self._info.text()) != 0 and not isOperator(self._info.text()[-1]):
            self.equation = ''

        new_display_text = self._display.text() + self.text()
        if not isValidNumber(new_display_text):
            self._display.setFocus()
            return

        self._display.insert(self.text())
        self._display.setFocus()

    def _handleSpecialButton(self):
        if isOperator(self.text()):
            operator = self.text()

            if self.text() == '÷':
                operator = '/'
            if self.text().lower() == 'x':
                operator = '*'
            if self.text() == '^':
                operator = '**'

            if isValidNumber(self._info.text()):
                self.equation = f'{self._info.text()} {operator}'
                self._display.setFocus()
                return

            if not isEmpty(self._info.text()) and isOperator(self._info.text()[-1]):
                self.equation = self._info.text()[:-1] + operator
                self._display.setFocus()
                return

            if isValidNumber(self._display.text()):
                self.equation = f'{self._info.text()} {self._display.text()} {operator}'
                self._display.clear()
                self._display.setFocus()
                return

        if self.text().lower() == 'c':
            self.equation = ''
            self._display.clear()
            self._display.setFocus()

        if self.text() == '◀':
            self._display.backspace()
            self._display.setFocus()

        if self.text() == '=':
            if isValidNumber(self._display.text()):
                self.equation = f'{self._info.text()} {self._display.text()}'
                try:
                    result = str(eval(self.equation))
                    if len(result) > 20:
                        result = f'~ {result[:20]}...'
                        self._showWarning(
                            'O número excedeu o limite de caracteres!')
                        self._display.clear()
                    self.equation = result
                    self._display.clear()
                except ZeroDivisionError:
                    self._showError('Impossível dividir por 0!')
                    self.equation = ''
                    self._display.clear()
                except OverflowError:
                    self._showError('Número muito grande!')
                    self.equation = ''
                    self._display.clear()
                self._display.setFocus()

    # dialogs
    def _makeDialog(self, title: str, msg: str) -> QMessageBox:
        dialog = self._window.makeMsgBox(title, msg)
        return dialog

    def _showError(self, msg: str) -> None:
        msg_box = self._makeDialog('Erro', msg)
        msg_box.setIcon(msg_box.Icon.Critical)
        msg_box.exec()
        self._display.setFocus()

    def _showWarning(self, msg: str) -> None:
        msg_box = self._make('Aviso', msg)
        msg_box.setIcon(msg_box.Icon.Warning)
        msg_box.exec()
        self._display.setFocus()

    @Slot()
    def _invertNumber(self):
        display = self._display.text()
        if not isValidNumber(display):
            self._display.setFocus()
            return
        inverted_number = -float(display)
        if inverted_number.is_integer():
            inverted_number = int(inverted_number)
        self._display.setText(str(inverted_number))
        self._display.setFocus()

    # keyboard
    @Slot()
    def _click(self):
        self.click()
        self._display.setFocus()

    @Slot()
    def _input(self, *args):
        if args[0] == self.text():
            self.click()
        if args[0] == ',' and self.text() == '.':
            self.click()
        self._display.setFocus()

    @Slot()
    def _operation(self, *args):
        if args[0] == self.text():
            self.click()
        if args[0] == '/' and self.text() == '÷':
            self.click()
        if args[0] == '*' and self.text() == 'x':
            self.click()
        self._display.setFocus()
