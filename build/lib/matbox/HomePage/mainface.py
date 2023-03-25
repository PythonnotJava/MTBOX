import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from pathlib import Path

_path = Path(__file__).parent

class ComingHome(QWidget):
    def __init__(self):
        super(ComingHome, self).__init__()

        self.webview = QWebEngineView()
        self.webview.settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.lay = QVBoxLayout(self)

        self.setUI()


    def setUI(self):

        path = _path / "../" / "Source" / "h5" / "main.html"

        self.webview.setHtml(open(path, 'r', encoding='U8').read())

        self.lay.addWidget(self.webview)
        self.setLayout(self.lay)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ComingHome()
    ui.show()
    sys.exit(app.exec())
