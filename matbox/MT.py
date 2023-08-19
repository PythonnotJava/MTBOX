import sys
from typing import Generator, Callable
from os import system

from PyQt5.QtWidgets import QVBoxLayout, QApplication, QStackedWidget, QHBoxLayout
from PyQt5.QtGui import QIcon, QCursor, QPixmap, QKeyEvent, QCloseEvent
from PyQt5.QtCore import Qt, QObject
from qt_material import apply_stylesheet

from Util import _load_yaml, _dump_new_cfg
from TreeItems import BaseTree
from CodeViewer import ViewSeletedItemCodes
from Setting import ReSetDiag
from HomePage import HomePage
from Source import CFG, LOGO, CursorType, README_SVG, TUTORIAL_H5
from OptComponent import *


# ------------------------------------------------------------------------------
# MatBox V1.0.8 -- Since 2023.8.17
# From version 1.0.8, my main but core work is to optimize coders.
# I try to improve code readability and usage as much as possible
# Also, starting from this release,
# I'm going to focus on making this module an out-of-the-box file
# layout container, not just a tutorial software
# ------------------------------------------------------------------------------

class CoreUI(ReWidget):

    def __init__(self, statement: bool = True):
        super(CoreUI, self).__init__()

        # widgets
        # left frame and lay
        self.listBox = BaseTree(statement)
        self.runCode = RePushButton()
        self.setting = RePushButton()

        self._leftLay = QVBoxLayout()
        self._runAndSet = QHBoxLayout()
        self._set = ReSetDiag()

        # staring with v 1.0.7, add a homepage
        self.homepageButton = RePushButton()
        self.homepage = HomePage()
        self.homepageState = ReLabel()

        self._statusLay = QHBoxLayout()
        self._homepageLay = QVBoxLayout()

        # right frame and lay
        self.codesViewer = ViewSeletedItemCodes(statement)
        self.remakerGroup = ReGroupBox()
        self.remarker = ReTextEdit()
        self._rightLay = QVBoxLayout()
        self._groupLay = QVBoxLayout()
        self.codeTitle = ReLineEdit()
        self._showHomePage = ReWidget()
        self._showCodes = ReWidget()

        # mid splitter
        self.midSplitter = ReSplitter()

        # main layout
        self._globalLay = QVBoxLayout()

        # config_datas
        self._config_datas = _load_yaml(CFG)

        # parameters for global using
        self._statement = statement

        self.__setUI()
        self.__send_receive_signal()

    def __setUI(self):
        ReAppication.setWidgets(
            attribute=Qt.AA_EnableHighDpiScaling,
            display_name="Version 1.0",
            icon=QIcon(LOGO)
        )

        self.setWidgets(
            title="MatBox",
            minWidth=self._config_datas['Main']['sizes'][0],
            minHeight=self._config_datas['Main']['sizes'][1],
            cursor=QCursor(QPixmap(CursorType.Working))
        )

        self.homepageButton.setWidgets(
            text="访问主页中",
            icon=QIcon(LOGO),
            cursor=QCursor(QPixmap(CursorType.Link)),
            function=self.__setCurRigthWidget
        )

        self.homepageState.setWidgets(
            text="当前状态",
            qss=self._config_datas['HomePage-Label']['style'],
            cursor=QCursor(QPixmap(CursorType.Working))
        )

        self.remakerGroup.setWidgets(
            layout=self._groupLay,
            title="参数详解        Help : ① Ctrl+C=复制  ② Ctrl+V=粘贴 ③ Ctrl+X=剪切 ④ Ctrl+A=全选",
            maxHeight=self._config_datas['QGroupBox']['max-height'],
            qss=self._config_datas['QGroupBox']['style'],
            cursor=QCursor(QPixmap(CursorType.Text))
        )

        self.runCode.setWidgets(
            text="Run the Code",
            cursor=QCursor(QPixmap(CursorType.Link)),
            function=self._runCode
        )

        self.setting.setWidgets(
            text="Settings",
            cursor=QCursor(QPixmap(CursorType.Link)),
            function=self._settings,
            shortcuts="Ctrl+S",
        )

        self.codeTitle.setWidgets(
            text="Code Example",
            enable=False,
            qss=self._config_datas['Title']['style'],
            cursor=QCursor(QPixmap(CursorType.Working))
        )

        self.midSplitter.setWidgets(
            widgets=[ReWidget(), QStackedWidget()],
            sizes=self._config_datas['QSplitter']['sizes']
        )

        # starting with v 1.0.7 , right_face changed as a stackWidget
        # type(self.midSplitter.widget(1)) == QStackedWidget
        self.midSplitter.widget(0).setLayout(self._leftLay)
        self.midSplitter.widget(1).addWidget(self._showHomePage)
        self.midSplitter.widget(1).addWidget(self._showCodes)
        self.midSplitter.handle(1).setMinimumWidth(10)
        self.midSplitter.handle(1).setCursor(QCursor(QPixmap(CursorType.Move)))

        # set layouts
        self._runAndSet.addWidget(self.runCode, alignment=Qt.Alignment())
        self._runAndSet.addWidget(self.setting, alignment=Qt.Alignment())

        self._statusLay.addWidget(self.homepageState, alignment=Qt.Alignment())
        self._statusLay.addWidget(self.homepageButton, alignment=Qt.Alignment())
        self._showHomePage.setLayout(self._homepageLay)
        self._homepageLay.addWidget(self.homepage, alignment=Qt.Alignment())

        self._leftLay.addLayout(self._statusLay)
        self._leftLay.addWidget(self.listBox, alignment=Qt.Alignment())
        self._leftLay.addLayout(self._runAndSet)

        self._rightLay.addWidget(self.codeTitle, alignment=Qt.Alignment())
        self._rightLay.addWidget(self.codesViewer, alignment=Qt.Alignment())
        self._rightLay.addWidget(self.remakerGroup, alignment=Qt.Alignment())
        self._groupLay.addWidget(self.remarker, alignment=Qt.Alignment())
        self._showCodes.setLayout(self._rightLay)

        self._globalLay.addWidget(self.midSplitter, alignment=Qt.Alignment())
        self.setLayout(self._globalLay)

        # theme
        apply_stylesheet(self, self._config_datas['Theme']['name'])
        apply_stylesheet(self._set, self._config_datas['Theme']['name'])

    # Triggered when the interface is actively changed and the left interface is clicked
    def __setCurRigthWidget(self):
        getIndex: QStackedWidget = self.midSplitter.widget(1)
        if getIndex.currentIndex() == 0:
            getIndex.setCurrentIndex(1)
            self.homepageButton.setText('使用功能中')
        else:
            getIndex.setCurrentIndex(0)
            self.homepageButton.setText('访问主页中')

    # run code function -- which is connected with the button runCode
    def _runCode(self):
        # When clicking on the run-button, jump immediately
        self.midSplitter.widget(1).setCurrentIndex(1)
        self.homepageButton.setText("使用功能中")
        try:
            exec(self.codesViewer.toPlainText(), globals())
            print("SUC")
        except Exception as e:
            print(self.codesViewer.toPlainText(), '\n % s' % str(e))
            singleButtonMessageBox(self, 'Error', str(e), True)

    # refresh settings
    def _settings(self):
        self._set.curTheme.connect(self._renewTheme)
        self._set.show()

    # refresh settings--change the theme
    def _renewTheme(self, name: str):
        apply_stylesheet(self, name)
        apply_stylesheet(self._set, name)
        self._config_datas['Theme']['name'] = name

    # close event
    def closeEvent(self, a0: QCloseEvent):
        # When you close the main Ui firstly, the setting UI must also be closed
        _dump_new_cfg(CFG, self._config_datas)

    # signal 、 functions 、shortcuts
    def __send_receive_signal(self):
        self.listBox.selected_item.connect(self._setMtml)

    def _setMtml(self, itemName: str):
        _func: Generator = self.codesViewer.setMtml(itemName)
        self.codesViewer.setStyleSheet(_func.__next__())
        self.remarker.setStyleSheet(_func.__next__())
        # Now, I'm not going to consider this list of dictionaries
        self.remarker.setText(_func.__next__().__str__())
        # When clicking on the ribbon, jump immediately
        self.homepageButton.setText("使用功能")
        self.midSplitter.widget(1).setCurrentIndex(1)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_F5:
            system(README_SVG)
        elif event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier) and event.key() == Qt.Key_Z:
            system(TUTORIAL_H5)
        else:
            super().keyPressEvent(event)

    # Allow users to customize card content
    def setCard(self, **kwargs) -> None:
        self._set.card.setWidgets(**kwargs)

    # Allow users to operate some core controls.
    # This function is still under study and is currently in the idea stage
    @staticmethod
    def resetWidget(widget : QObject, func : Callable, **kwargs):
        func(widget, **kwargs)

# an example for beginners who use it for the first time
def example(statement=True):
    app = QApplication(sys.argv)
    ui = CoreUI(statement)
    ui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    example()
