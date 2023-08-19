import sys

from qt_material import list_themes
from PyQt5.QtCore import Qt, pyqtSignal, pyqtBoundSignal
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import (QApplication,
                             QVBoxLayout,
                             QHBoxLayout)

from Util import _load_yaml
from Source import CFG, CursorType
from OptComponent import ReLabel, ReComboBox, ReDialog, ToggleButton

class ReSetDiag(ReDialog):

    # theme signal
    curTheme : pyqtBoundSignal = pyqtSignal(str)
    curLang : pyqtBoundSignal = pyqtSignal(str)

    def __init__(self):
        super(ReSetDiag, self).__init__()

        # main layout
        self.main_lay = QVBoxLayout()

        # widgets and layouts
        self.card = ReLabel()

        self.themeLabel = ReLabel()
        self.themeComboBox = ReComboBox()
        self.theme_lay = QHBoxLayout()

        self.languageLabel = ReLabel()
        self.languageCh = ToggleButton()
        self.languageEn = ToggleButton()
        self.language_lay = QHBoxLayout()

        self.setUI()

    def setUI(self):
        # setLay
        self.theme_lay.addWidget(self.themeLabel, alignment=Qt.Alignment())
        self.theme_lay.addWidget(self.themeComboBox, alignment=Qt.Alignment())

        self.language_lay.addWidget(self.languageLabel, alignment=Qt.Alignment())
        self.language_lay.addWidget(self.languageCh, alignment=Qt.Alignment())
        self.language_lay.addWidget(self.languageEn, alignment=Qt.Alignment())

        self.main_lay.addWidget(self.card, alignment=Qt.Alignment())
        self.main_lay.addLayout(self.theme_lay)
        self.main_lay.addLayout(self.language_lay)
        self.setLayout(self.main_lay)

        self.setWidgets(
            modal=True,
            cursor=QCursor(QPixmap(CursorType.Busy)),
            flags=self.windowFlags() & ~Qt.WindowContextHelpButtonHint,
            title="Settings",
            minHeight=400,
            minWidth=400,
        )

        self.themeComboBox.setWidgets(
            items=list_themes(),
            currentTextChanged_function=self.themeChanged,
            cursor=QCursor(QPixmap(CursorType.Link))
        )

        self.languageCh.setWidgets(
            text='中文',
            cursor=QCursor(QPixmap(CursorType.Link))
        )

        self.languageEn.setWidgets(
            text='English',
            cursor=QCursor(QPixmap(CursorType.Link))
        )

        self.languageLabel.setWidgets(
            text='语言设置',
        )

        self.themeLabel.setWidgets(
            text='设置主题',
        )

        self.card.setWidgets(
            text="""
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
                """,
            link_enable=True
        )

        if _load_yaml(CFG)['Lang'] == 'ch' : self.languageCh.setChecked(True)
        elif _load_yaml(CFG)['Lang'] == 'en' : self.languageEn.setChecked(True)
        else : pass

    # theme signal linked
    def themeChanged(self): self.curTheme.emit(self.themeComboBox.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ReSetDiag()
    ui.show()
    sys.exit(app.exec())
