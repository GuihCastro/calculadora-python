import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet
from main_window import MainWindow
from variables import ICON_PATH
from styles import qss

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml', style=qss)
    window = MainWindow()

    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation'
        )

    window.show()
    app.exec()
