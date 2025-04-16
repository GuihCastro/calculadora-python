from PySide6.QtWidgets import QGridLayout, QMainWindow, QMessageBox, QVBoxLayout, QWidget
from buttons import Button, GridLayout
from display import Display, Info
from styles import qss


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurações da janela
        self.setWindowTitle('Calculadora')
        self.central_widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.v_layout)
        
        # Widgets
        self.info = Info()
        self.display = Display()
        self.display.setPlaceholderText('')

        self.addWidgetToLayout(self.info)
        self.addWidgetToLayout(self.display)
        
        # Grid de botões
        self.grid_layout = GridLayout(self.display, self.info, self)
        self.grid_layout.setSpacing(10)
        self.v_layout.addLayout(self.grid_layout)
        self.grid_layout.mntGrid()

        # Depois de tudo
        self.setStyleSheet(qss)
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToLayout(self, widget: QWidget) -> None:
        self.v_layout.addWidget(widget)
        # self.adjustSize()
        
    def makeMsgBox(self, title: str, text: str) -> QMessageBox:
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        return msg_box
