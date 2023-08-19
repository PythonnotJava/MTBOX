from os import PathLike
from typing import Optional, Callable, Iterable

from PyQt5.QtWidgets import (QGroupBox,
                             QLayout,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QTextEdit,
                             QSplitter,
                             QWidget,
                             QApplication,
                             QComboBox,
                             QDialog,
                             QTreeView,
                             QRadioButton,
                             QGraphicsEffect
                             )
from PyQt5.QtGui import QCursor, QIcon, QStandardItemModel
from PyQt5.QtCore import Qt, QRect, QObject
from PyQt5.QtWebEngineWidgets import QWebEngineView


class BaseWidget(QWidget):
    def _baseArgs(self,
                  parent : Optional[QObject] = None,
                  rect : Optional[list] = None,
                  object_name: Optional[str] = None,
                  maxHeight: int | float | None = None,
                  minHeight: int | float | None = None,
                  maxWidth: int | float | None = None,
                  minWidth: int | float | None = None,
                  cursor: Optional[QCursor] = None,
                  qss: Optional[str] = None,
                  ):
        if parent is not None:
            self.setParent(parent)

        if rect is not None:
            self.setGeometry(QRect(*rect))

        if object_name is not None:
            self.setObjectName(object_name)

        if minHeight is not None:
            self.setMinimumHeight(minHeight)

        if maxHeight is not None:
            self.setMaximumHeight(maxHeight)

        if minWidth is not None:
            self.setMinimumWidth(minWidth)

        if maxWidth is not None:
            self.setMinimumWidth(maxWidth)

        if cursor is not None:
            self.setCursor(cursor)

        if qss is not None:
            self.setStyleSheet(qss)

class ReDialog(QDialog, BaseWidget):
    def setWidgets(self,
                   title: Optional[str] = None,
                   modal: bool = False,
                   icon: Optional[QIcon] = None,
                   flags=Qt.FramelessWindowHint,
                   effects: Optional[QGraphicsEffect] = None,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ) -> None:

        self.setWindowFlags(flags)
        self.setModal(modal)

        if effects is not None:
            self.setGraphicsEffect(effects)

        if title is not None:
            self.setWindowTitle(title)

        if icon is not None:
            self.setWindowIcon(icon)

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )
class ReGroupBox(QGroupBox, BaseWidget):
    def setWidgets(self,
                   title: Optional[str] = None,
                   layout: Optional[QLayout] = None,
                   rect: Optional[list] = None,
                   parent: Optional[QObject] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ) -> None:
        if title is not None:
            self.setTitle(title)

        if layout is not None:
            self.setLayout(layout)

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )

class RePushButton(QPushButton, BaseWidget):
    def setWidgets(self,
                   text: Optional[str] = None,
                   function: Callable = lambda: ...,
                   icon: Optional[QIcon] = None,
                   icon_fixed: bool = False,
                   toolTips: Optional[str] = None,
                   shortcuts: Optional[str] = None,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ) -> None:

        if text is not None:
            self.setText(text)

        if function is not None:
            self.clicked.connect(function)

        if toolTips is not None:
            self.setToolTip(toolTips)

        if shortcuts is not None:
            self.setShortcut(shortcuts)

        if icon is not None:
            self.setIcon(icon)
            if icon_fixed:
                self.setIconSize(self.size())

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )

class ReLabel(QLabel, BaseWidget):
    def setWidgets(self,
                   text: Optional[str] = None,
                   toolTips: Optional[str] = None,
                   wrap: bool = True,
                   link_enable: bool = True,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ) -> None:

        self.setWordWrap(wrap)
        self.setOpenExternalLinks(link_enable)

        if text is not None:
            self.setText(text)

        if toolTips is not None:
            self.setToolTip(toolTips)

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )

class ReLineEdit(QLineEdit, BaseWidget):
    def setWidgets(self,
                   text: Optional[str] = None,
                   menu_policy=Qt.NoContextMenu,
                   enable: bool = True,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ) -> None:

        self.setContextMenuPolicy(menu_policy)
        self.setEnabled(enable)

        if text is not None:
            self.setText(text)

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )

class ReTextEdit(QTextEdit, BaseWidget):
    def setWidgets(self,
                   text: Optional[str] = None,
                   wrap_mode=QTextEdit.NoWrap,
                   menu_policy=Qt.NoContextMenu,
                   enable: bool = True,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ):

        self.setEnabled(enable)
        if menu_policy is not None:
            self.setContextMenuPolicy(menu_policy)

        if wrap_mode is not None:
            self.setLineWrapMode(wrap_mode)

        if text is not None:
            self.setText(text)

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )

class ReSplitter(QSplitter, BaseWidget):

    def setWidgets(self,
                   widgets: Optional[list[QWidget]] = None,
                   sizes: Optional[Iterable] = None,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ):

        if sizes is not None:
            self.setSizes(sizes)

        if widgets is not None:
            for widget in widgets:
                self.addWidget(widget)

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )

class ReWidget(BaseWidget):
    def setWidgets(self,
                   title: Optional[str] = None,
                   icon: Optional[QIcon] = None,
                   flags=Qt.Window,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ) -> None:

        self.setWindowFlags(flags)

        if title is not None:
            self.setWindowTitle(title)

        if icon is not None:
            self.setWindowIcon(icon)

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )

class ReAppication(QApplication):
    @classmethod
    def setWidgets(cls,
                   attribute=Qt.AA_EnableHighDpiScaling,
                   display_name: Optional[str] = None,
                   icon: Optional[QIcon] = None,
                   ):
        cls.setAttribute(attribute)

        if display_name is not None:
            cls.setApplicationDisplayName(display_name)
        cls.setWindowIcon(icon)

class ReComboBox(QComboBox, BaseWidget):
    def wheelEvent(self, _): ...

    def setWidgets(self,
                   items: Iterable,
                   current_index: int = 0,
                   currentTextChanged_function: Optional[Callable] = None,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ) -> None:

        self.addItems(items)
        self.setCurrentIndex(current_index)

        if currentTextChanged_function is not None:
            self.currentTextChanged.connect(currentTextChanged_function)

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )

class ReWebEngineView(QWebEngineView, BaseWidget):
    def setWidgets(self,
                   html_file: PathLike | str,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ):

        self.setHtml(open(html_file, 'r', encoding='U8').read())

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )
class ReTreeView(QTreeView, BaseWidget):
    def setWidgets(self,
                   model: QStandardItemModel,
                   horizontal_labels: Optional[Iterable] = None,
                   hide_labels: bool = False,
                   expands_double_click: bool = True,
                   function: Optional[Callable] = None,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ) -> None:

        self.setModel(model)
        self.setExpandsOnDoubleClick(expands_double_click)

        if horizontal_labels is not None:
            model.setHorizontalHeaderLabels(horizontal_labels)
            self.setHeaderHidden(hide_labels)

        if function is not None:
            self.clicked.connect(function)

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )

class ToggleButton(QRadioButton, BaseWidget):
    def setWidgets(self,
                   text: Optional[str] = None,
                   toggle_function: Callable = lambda: ...,
                   checked : bool = True,
                   icon: Optional[QIcon] = None,
                   icon_fixed: bool = False,
                   toolTips: Optional[str] = None,
                   shortcuts: Optional[str] = None,
                   parent: Optional[QObject] = None,
                   rect: Optional[list] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None
                   ) -> None:

        self.setChecked(checked)

        if text is not None:
            self.setText(text)

        if toggle_function is not None:
            self.toggled.connect(toggle_function)

        if toolTips is not None:
            self.setToolTip(toolTips)

        if shortcuts is not None:
            self.setShortcut(shortcuts)

        if icon is not None:
            self.setIcon(icon)
            if icon_fixed:
                self.setIconSize(self.size())

        self._baseArgs(
            rect=rect,
            object_name=object_name,
            qss=qss,
            cursor=cursor,
            minWidth=minWidth,
            minHeight=minHeight,
            maxHeight=maxHeight,
            maxWidth=maxWidth,
            parent=parent
        )

