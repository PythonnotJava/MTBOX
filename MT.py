import sys
from pathlib import Path
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QSplitter,
                             QGroupBox,
                             QHBoxLayout,
                             QLineEdit,
                             QVBoxLayout,
                             QTextEdit,
                             QSplitterHandle,
                             QMessageBox
                             )
from PyQt5.QtGui import QCursor, QPixmap, QCloseEvent, QIcon
from PyQt5.QtCore import Qt
from qt_material import apply_stylesheet
from matbox.Setting._load_or_dump_config import _load_yaml, _dump_new_cfg
from matbox.TreeItems.basetree import BaseTree
from matbox.CodeViewer.CodeViewer import ViewSeletedItemCodes
from matbox.Setting.Settings import ReSetDiag

__author__ = "PythonnotJava"

_path = Path(__file__).parent

class MatTutorial(QWidget):
    def __init__(self):
        super(MatTutorial, self).__init__()

        # wdigets
        # left frame and lay
        self.left_listBox = BaseTree()
        self.runCode = QPushButton("Run the Code")
        self.setting = QPushButton("Settings")
        self.left_lay = QVBoxLayout()
        self.left_line_lay = QHBoxLayout()
        self._set = ReSetDiag()

        # right frame and lay
        self.right_editor = ViewSeletedItemCodes()
        self.right_tutorial_group = QGroupBox()
        self.right_tutorial = QTextEdit()
        self.right_lay = QVBoxLayout()
        self.group_lay = QVBoxLayout()
        self.title_show = QLineEdit("Code Example")

        # mid splitter
        self.mid_spliter = QSplitter()

        # main layout
        self.total_lay = QVBoxLayout()

        # config_datas
        path = _path / "Source" / "cfg" / "config.yaml"
        self._config_datas = _load_yaml(path)

        self.setUI()
        self.load_optimization()

    def setUI(self):
        # initialize window
        self.setMinimumSize(*self._config_datas['Main']['sizes'])
        self.setWindowTitle("Matplotlib-Tutorial")
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setApplicationDisplayName("Version 1.0")
        QApplication.setWindowIcon(QIcon(str(_path / 'Source' / 'img' / 'logo.ico')))

        # set layouts
        self.left_lay.addWidget(self.left_listBox)
        self.left_line_lay.addWidget(self.runCode)
        self.left_line_lay.addWidget(self.setting)
        self.left_lay.addLayout(self.left_line_lay)

        self.right_lay.addWidget(self.title_show)
        self.right_lay.addWidget(self.right_editor)
        self.right_lay.addWidget(self.right_tutorial_group)
        self.group_lay.addWidget(self.right_tutorial)
        self.right_tutorial_group.setLayout(self.group_lay)
        self.mid_spliter.addWidget(QWidget())
        self.mid_spliter.addWidget(QWidget())
        self.mid_spliter.widget(0).setLayout(self.left_lay)
        self.mid_spliter.widget(1).setLayout(self.right_lay)
        self.total_lay.addWidget(self.mid_spliter)
        self.setLayout(self.total_lay)

        # set control properties
        self.title_show.setContextMenuPolicy(Qt.NoContextMenu)
        self.title_show.setEnabled(False)
        self.mid_spliter.setSizes(self._config_datas['QSplitter']['sizes'])
        self.right_tutorial_group.setTitle("参数详解        Help : ① Ctrl+C=复制  ② Ctrl+V=粘贴 ③ Ctrl+X=剪切 ④ Ctrl+A=全选")
        self.right_tutorial_group.setMaximumHeight(self._config_datas['QGroupBox']['max-height'])

        # signal and functions
        self.left_listBox.selected_item.connect(self.right_editor.setCodes)
        self.runCode.clicked.connect(self._runCode)
        self.setting.clicked.connect(self._settings)

        # theme
        apply_stylesheet(self, self._config_datas['Theme']['name'])
        apply_stylesheet(self._set, self._config_datas['Theme']['name'])
        self.title_show.setStyleSheet("qproperty-alignment: AlignHCenter; font-size : 16px;")
        self.right_tutorial_group.setStyleSheet("""
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding: 0 3px;
            qproperty-titleAlign: center;
        }
        """)
        self.right_editor.setStyleSheet("""font-size : {}px;font-family : {}""".format(
            self._config_datas['QFont']['size'], self._config_datas['QFont']['family']
        ))
        # The temporary setting parameter detailed interface is fixed
        self.right_tutorial.setLineWrapMode(QTextEdit.NoWrap)
        path = _path / "Source" / "tutorial" / "Matplotlib_Getting_Started_Tutorial_Ch.py"
        self.right_tutorial.setText(open(path, 'r', encoding='U8').read())

    # UI beautification
    def load_optimization(self):
        self.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'working.cur'))))
        handle: QSplitterHandle = self.mid_spliter.handle(1)
        handle.setMinimumWidth(10)
        handle.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'move.cur'))))
        self.runCode.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'link.cur'))))
        self.setting.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'link.cur'))))
        self.right_editor.setCursor(QCursor(QPixmap(str(_path / 'Source' / 'mouseCursor' / 'text.cur'))))

    # run code function -- which is connected with the button runCode
    def _runCode(self):
        try: exec(self.right_editor.toPlainText())
        except Exception as e: QMessageBox.warning(self, 'Error', e.__str__(), QMessageBox.Ok)

    # refresh settings
    def _settings(self):
        self._set.curTheme.connect(self._renewTheme)
        self._set.show()

    # refresh settings--change the theme
    def _renewTheme(self, name : str):
        apply_stylesheet(self, name)
        apply_stylesheet(self._set, name)
        self._config_datas['Theme']['name'] = name

    # close event
    def closeEvent(self, a0 : QCloseEvent):
        # When you close the main Ui firstly, the setting UI must also be closed
        if self.close(): self._set.close()
        _dump_new_cfg(_path / "Source" / "cfg" / "config.yaml", self._config_datas)

def main():
    app = QApplication(sys.argv)
    # app.setAttribute(Qt.AA_EnableHighDpiScaling)
    # app.setApplicationDisplayName("Version 1.0")
    # app.setWindowIcon(QIcon('source/img/logo.ico'))
    ui = MatTutorial()
    ui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
   main()

