import sys
from pathlib import Path
from PyQt5.QtGui import QWheelEvent
from PyQt5.QtCore import Qt, pyqtSignal, pyqtBoundSignal
from qt_material import list_themes
from PyQt5.QtWidgets import QLabel, QApplication, QVBoxLayout, QDialog, QHBoxLayout, QComboBox, QRadioButton

_path = Path(__file__).parent

if __name__ == '__main__':
    from _load_or_dump_config import _load_yaml
else:
    from ._load_or_dump_config import _load_yaml

class ReSetDiag(QDialog):

    # theme signal
    curTheme : pyqtBoundSignal = pyqtSignal(str)
    curLang : pyqtBoundSignal = pyqtSignal(str)

    def __init__(self):
        super(ReSetDiag, self).__init__()
        self.setMinimumHeight(400)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Settings")

        # main layout
        self.main_lay = QVBoxLayout()

        # widgets and layouts
        self.card = QLabel()

        self.themeLabel = QLabel("设置主题")
        self.themeComboBox = QComboBox()
        self.theme_lay = QHBoxLayout()

        self.languageLabel = QLabel("语言设置")
        self.languageCh = QRadioButton("中文")
        self.languageEn = QRadioButton("English")
        self.language_lay = QHBoxLayout()

        self.setUI()

    def setUI(self):
        self.theme_lay.addWidget(self.themeLabel)
        self.theme_lay.addWidget(self.themeComboBox)

        self.language_lay.addWidget(self.languageLabel)
        self.language_lay.addWidget(self.languageCh)
        self.language_lay.addWidget(self.languageEn)

        self.main_lay.addWidget(self.card)
        self.main_lay.addLayout(self.theme_lay)
        self.main_lay.addLayout(self.language_lay)
        self.setLayout(self.main_lay)

        # basic attributes
        self.themeComboBox.addItems(list_themes())
        _text = """
        <pre>                    
        Here is MatBox V 1.0.7.
        Thank you for your trust in Matplotlib Tutorial
        (hereinafter referred to as MT).
        MT is a tool developed based on Python and designed 
        to teach you to use matplotlib to draw pictures.
        You can visit my open source address
        <a href="https://github.com/PythonnotJava">https://github.com/PythonnotJava</a>
        or <a href="https://gitee.com/PythonnotJava">https://gitee.com/PythonnotJava</a> to find it
        </pre>
        """
        self.card.setText(_text)
        self.card.setOpenExternalLinks(True)
        def _wheelEvent(a0: QWheelEvent) -> None: ...
        self.themeComboBox.wheelEvent = _wheelEvent
        self.themeComboBox.currentTextChanged.connect(self.themeChanged)
        self.setMaximumWidth(400)
        path = _path / "../" / "Source" / "cfg" / "config.yaml"
        if _load_yaml(path)['Lang'] == 'ch' : self.languageCh.setChecked(True)
        elif _load_yaml(path)['Lang'] == 'en' : self.languageEn.setChecked(True)
        else : pass

    # theme signal linked
    def themeChanged(self): self.curTheme.emit(self.themeComboBox.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ReSetDiag()
    ui.show()
    sys.exit(app.exec())
