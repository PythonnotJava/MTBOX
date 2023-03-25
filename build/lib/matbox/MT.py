import sys
from collections.abc import Generator
from pathlib import Path
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLabel,
                             QGroupBox,
                             QTextEdit,
                             QLineEdit,
                             QSplitter,
                             QApplication,
                             QStackedWidget,
                             QMessageBox,
                             QSplitterHandle
                             )
from PyQt5.QtGui import QIcon, QCursor, QPixmap, QKeyEvent, QCloseEvent
from os import system
from PyQt5.QtCore import Qt
from qt_material import apply_stylesheet
from matbox.Setting._load_or_dump_config import _load_yaml, _dump_new_cfg
from matbox.TreeItems.basetree import BaseTree
from matbox.CodeViewer.CodeViewer import ViewSeletedItemCodes
from matbox.Setting.Settings import ReSetDiag
from matbox.HomePage.mainface import ComingHome

__author__ = "PythonnotJava"
__version__ = "1.0.7"

_path = Path(__file__).parent

class MatTutorial(QWidget):

    def __init__(self, statement: bool = True):
        super(MatTutorial, self).__init__()

        # widgets
        # left frame and lay
        self.left_listBox = BaseTree(statement)
        self.runCode = QPushButton("Run the Code")
        self.setting = QPushButton("Settings")
        self.left_lay = QVBoxLayout()
        self.left_line_lay = QHBoxLayout()
        self._set = ReSetDiag()

        # staring with v 1.0.7, add a homepage
        self.homepage = ComingHome()
        self.homepageState = QLabel("当前状态")
        self.homepageButton = QPushButton("访问主页")
        self.homepageLine = QHBoxLayout()
        self.homepageLay = QVBoxLayout()

        # right frame and lay
        self.right_editor = ViewSeletedItemCodes(statement)
        self.right_tutorial_group = QGroupBox()
        self.right_tutorial = QTextEdit()
        self.right_lay = QVBoxLayout()
        self.group_lay = QVBoxLayout()
        self.title_show = QLineEdit("Code Example")
        self.right_temp_widget_hp = QWidget()
        self.right_temp_widget_org = QWidget()

        # mid splitter
        self.mid_spliter = QSplitter()

        # main layout
        self.total_lay = QVBoxLayout()

        # config_datas
        path = _path / "Source" / "cfg" / "config.yaml"
        self._config_datas = _load_yaml(path)

        # parameters for global using
        self._statement = statement

        self.setUI()
        self.load_optimization()
        self.send_receive_signal()

    def setUI(self):
        # initialize window
        self.setMinimumSize(*self._config_datas['Main']['sizes'])
        self.setWindowTitle("Matplotlib-Tutorial")
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setApplicationDisplayName("Version 1.0")
        QApplication.setWindowIcon(QIcon(str(_path / 'Source' / 'img' / 'logo.ico')))

        # homepage
        self.homepageLine.addWidget(self.homepageState)
        self.homepageLine.addWidget(self.homepageButton)
        self.right_temp_widget_hp.setLayout(self.homepageLay)
        self.homepageLay.addWidget(self.homepage)

        # set layouts
        self.left_lay.addLayout(self.homepageLine)
        self.left_lay.addWidget(self.left_listBox)
        self.left_line_lay.addWidget(self.runCode)
        self.left_line_lay.addWidget(self.setting)
        self.left_lay.addLayout(self.left_line_lay)

        self.right_tutorial_group.setLayout(self.group_lay)
        self.right_lay.addWidget(self.title_show)
        self.right_lay.addWidget(self.right_editor)
        self.right_lay.addWidget(self.right_tutorial_group)
        self.group_lay.addWidget(self.right_tutorial)
        self.right_temp_widget_org.setLayout(self.right_lay)

        # set control properties
        self.title_show.setContextMenuPolicy(Qt.NoContextMenu)
        self.title_show.setEnabled(False)

        self.right_tutorial_group.setTitle(
            "参数详解        Help : ① Ctrl+C=复制  ② Ctrl+V=粘贴 ③ Ctrl+X=剪切 ④ Ctrl+A=全选")
        # The temporary setting parameter detailed interface is fixed
        self.right_tutorial.setLineWrapMode(QTextEdit.NoWrap)

        self.mid_spliter.addWidget(QWidget())
        self.mid_spliter.addWidget(QStackedWidget())
        # starting with v 1.0.7 , right_face changed as a stackWidget
        # type(self.mid_spliter.widget(1)) == QStackedWidget
        self.mid_spliter.widget(0).setLayout(self.left_lay)
        self.mid_spliter.widget(1).addWidget(self.right_temp_widget_hp)
        self.mid_spliter.widget(1).addWidget(self.right_temp_widget_org)

        self.mid_spliter.setSizes(self._config_datas['QSplitter']['sizes'])
        self.total_lay.addWidget(self.mid_spliter)
        self.setLayout(self.total_lay)

        # theme
        apply_stylesheet(self, self._config_datas['Theme']['name'])
        apply_stylesheet(self._set, self._config_datas['Theme']['name'])

    # Triggered when the interface is actively changed and the left interface is clicked
    def setCurRigthWidget(self):
        get_index : QStackedWidget = self.mid_spliter.widget(1)
        if get_index.currentIndex() == 0:
            get_index.setCurrentIndex(1)
            self.homepageButton.setText('使用功能')
        else:
            get_index.setCurrentIndex(0)
            self.homepageButton.setText('访问主页')

    # UI beautification
    def load_optimization(self):
        self.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'working.cur'))))
        handle: QSplitterHandle = self.mid_spliter.handle(1)
        handle.setMinimumWidth(10)
        handle.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'move.cur'))))
        self.runCode.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'link.cur'))))
        self.setting.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'link.cur'))))
        self.right_editor.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'text.cur'))))
        self.homepageButton.setIcon(QIcon(str(_path / 'Source' / 'img' / 'logo.ico')))
        self.right_tutorial_group.setMaximumHeight(self._config_datas['QGroupBox']['max-height'])
        self.homepageButton.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'link.cur'))))
        # default settinds, but you can change it in mtml-file now!
        self.title_show.setStyleSheet(self._config_datas['Title']['style'])
        self.right_tutorial_group.setStyleSheet(self._config_datas['QGroupBox']['style'])
        self.right_editor.setStyleSheet(self._config_datas['Editor']['style'])
        self.homepageState.setStyleSheet(self._config_datas['HomePage-Label']['style'])

    # run code function -- which is connected with the button runCode
    def _runCode(self):
        # When clicking on the run-button, jump immediately
        self.mid_spliter.widget(1).setCurrentIndex(1)
        self.homepageButton.setText("使用功能")
        try:
            exec(self.right_editor.toPlainText(), globals())
            print("SUC")
        except Exception as e:
            print(self.right_editor.toPlainText())
            QMessageBox.warning(self, 'Error', e.__str__(), QMessageBox.Ok)

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
        if self.close(): self._set.close()
        _dump_new_cfg(_path / "Source" / "cfg" / "config.yaml", self._config_datas)

    # signal 、 functions 、shortcuts
    def send_receive_signal(self):
        self.left_listBox.selected_item.connect(self._setMtml)
        self.runCode.clicked.connect(self._runCode)
        self.setting.clicked.connect(self._settings)
        self.homepageButton.clicked.connect(self.setCurRigthWidget)
        self.setting.setShortcut("Ctrl+S")

    def _setMtml(self, itemName : str):
        _func : Generator = self.right_editor.setMtml(itemName)
        self.right_editor.setStyleSheet(_func.__next__())
        self.right_tutorial.setStyleSheet(_func.__next__())
        # Now, I'm not going to consider this list of dictionaries
        self.right_tutorial.setText(_func.__next__().__str__())
        # When clicking on the ribbon, jump immediately
        self.homepageButton.setText("使用功能")
        self.mid_spliter.widget(1).setCurrentIndex(1)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_F5:
            system(str(_path / 'Source' / 'h5' / 'readme.svg'))
        elif event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier) and event.key() == Qt.Key_Z:
            system(str(_path / 'Source' / 'h5' / 'tutorial.html'))
        else :
            super().keyPressEvent(event)

# an example for beginners who use it for the first time
def main(statement=True):
    app = QApplication(sys.argv)
    ui = MatTutorial(statement)
    ui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
