import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtGui import QPixmap, QCursor

from Source import MAIN_PAGE, CursorType
from OptComponent import ReWebEngineView, ReWidget

class HomePage(ReWidget):
    def __init__(self, *args, **kwargs):
        super(HomePage, self).__init__(*args, **kwargs)

        self.webview = ReWebEngineView()
        self.webview.settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.lay = QVBoxLayout(self)

        self.setUI()

    def setUI(self):
        self.webview.setWidgets(
            html_file=MAIN_PAGE,
            cursor=QCursor(QPixmap(CursorType.Working))
        )
        self.lay.addWidget(self.webview, alignment=Qt.Alignment())
        self.setLayout(self.lay)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = HomePage()
    ui.show()
    sys.exit(app.exec())
