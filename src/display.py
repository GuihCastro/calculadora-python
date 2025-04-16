from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget
from utils import isDigitOrDot, isEmpty, isOperator
from variables import BIG, SMALL, TXT_MARGIN, WIN_WIDTH


class Display(QLineEdit):
    eq_requested = Signal()
    clr_requested = Signal()
    bs_requested = Signal()
    op_requested = Signal(str)
    input_requested = Signal(str)
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = (TXT_MARGIN for _ in range(4))
        self.setStyleSheet(f'font-size: {BIG}px;')
        self.setMinimumHeight(BIG * 2)
        self.setMinimumWidth(WIN_WIDTH - 10)
        self.setTextMargins(*margins)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        KEYS = Qt.Key
        key = event.key()
        char = event.text().strip()
        
        if key == KEYS.Key_Enter or key == KEYS.Key_Return or char == '=':
            self.eq_requested.emit()
            return event.ignore()
        
        if key == KEYS.Key_Backspace or key == KEYS.Key_Delete:
            self.bs_requested.emit()
            return event.ignore()
        
        if key == KEYS.Key_Escape or char.lower() == 'c':
            self.clr_requested.emit()
            return event.ignore()
        
        if isEmpty(char):
            return event.ignore()
        
        if isDigitOrDot(char):
            self.input_requested.emit(char)
            return event.ignore()
        
        if isOperator(char):
            self.op_requested.emit(char)
            return event.ignore()
        
        # return super().keyPressEvent(event)


class Info(QLabel):
    def __init__(self, text: str = '', parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()
        
    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
