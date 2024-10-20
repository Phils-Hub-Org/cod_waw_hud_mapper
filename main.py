from PySide6.QtWidgets import QApplication
from Core.main_window import MainWindow
from Core.hud_mapper import HudMapper

class Entry:

    @classmethod
    def init(cls):
        
        # Initialize main window
        cls.mainWindow = MainWindow()

        # Initialize hud mapper
        cls.hudMapper = HudMapper(cls.mainWindow)

        # Show main window
        cls.mainWindow.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    entry = Entry()
    entry.init()
    sys.exit(app.exec())