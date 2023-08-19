from typing import Optional, Any, overload

from PyQt5.QtCore import (Qt,
                          QObject,
                          QPropertyAnimation,
                          QParallelAnimationGroup,
                          QSequentialAnimationGroup,
                          QRect
                          )
from PyQt5.QtGui import QCursor, QIcon, QPixmap
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QGraphicsOpacityEffect, QGraphicsEffect

from OptComponent import ReDialog, RePushButton, ReTextEdit
from Source import CursorType


class ShadowEffects(QGraphicsDropShadowEffect):
    def __init__(self,
                 offset: tuple = (0., 0.),
                 radius: float = 10.,
                 color=Qt.gray,
                 object_name: Optional[str] = None,
                 ):
        super().__init__()
        self.setOffset(*offset)
        self.setBlurRadius(radius)

        self.setColor(color)

        if object_name is not None:
            self.setObjectName(object_name)


class OpacityEffects(QGraphicsOpacityEffect):
    def __init__(self,
                 opacity: float = 1.,
                 object_name: Optional[str] = None):
        super().__init__()
        self.setOpacity(opacity)

        if object_name is not None:
            self.setObjectName(object_name)


class ReAnimation(QPropertyAnimation):
    def __init__(self,
                 _type: str,
                 target: QObject,
                 start: Any,
                 end: Any,
                 duration: int = 1000,
                 loop: int = 1,
                 object_name: Optional[str] = None):
        super().__init__()

        self.setPropertyName(_type.encode())
        self.setTargetObject(target)
        self.setStartValue(start)
        self.setEndValue(end)
        self.setDuration(duration)
        self.setLoopCount(loop)

        if object_name is not None:
            self.setObjectName(object_name)


class ReSeqAnimationGroup(QSequentialAnimationGroup):
    def setAnimations(self,
                      animations: list[ReAnimation]
                      ) -> None:
        for animation in animations:
            self.addAnimation(animation)
        self.start()


class ReParAnimationGroup(QParallelAnimationGroup):
    def setAnimations(self,
                      animations: list[ReAnimation]
                      ) -> None:
        for animation in animations:
            self.addAnimation(animation)
        self.start()


class SingleButtonMessageBox(ReDialog):
    @overload
    def setWidgets(self,
                   title: Optional[str] = None,
                   modal: bool = False,
                   icon: Optional[QIcon] = None,
                   flags=Qt.FramelessWindowHint,
                   effects: Optional[QGraphicsEffect] = None,
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
        ...

    @overload
    def setWidgets(self,
                   title: Optional[str] = None,
                   modal: bool = False,
                   icon: Optional[QIcon] = None,
                   flags=Qt.FramelessWindowHint,
                   effects: Optional[QGraphicsEffect] = None,
                   rect: Optional[list] = None,
                   parent: Optional[QObject] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None,
                   button_args: Optional[dict] = None,
                   textedit_args: Optional[dict] = None,
                   animation: Optional[ReAnimation] = None
                   ) -> None:
        ...

    def setWidgets(self,
                   title: Optional[str] = None,
                   modal: bool = False,
                   icon: Optional[QIcon] = None,
                   flags=Qt.FramelessWindowHint,
                   effects: Optional[QGraphicsEffect] = None,
                   rect: Optional[list] = None,
                   parent: Optional[QObject] = None,
                   object_name: Optional[str] = None,
                   maxHeight: int | float | None = None,
                   minHeight: int | float | None = None,
                   maxWidth: int | float | None = None,
                   minWidth: int | float | None = None,
                   cursor: Optional[QCursor] = None,
                   qss: Optional[str] = None,
                   button_args: Optional[dict] = None,
                   textedit_args: Optional[dict] = None,
                   animation: Optional[ReAnimation] = None
                   ) -> None:

        super().setWidgets()

        if button_args is not None and textedit_args is not None:
            ReTextEdit(self).setWidgets(**textedit_args)
            RePushButton(self).setWidgets(**button_args)

        if animation is not None:
            animation.setParent(self)
            animation.start()
def singleButtonMessageBox(parent : QObject, title : str, content : str, show : bool = False) -> None:
    _msgbox = SingleButtonMessageBox()
    _msgbox.setWidgets(
        flags=Qt.CustomizeWindowHint | Qt.Window,
        parent=parent,
        button_args=dict(
            rect=[140, 250, 100, 40],
            function=_msgbox.close,
            object_name='singleButton',
            text='确定',
            qss='''
                color : white;
                border-radius : 5px;
                border : 5px solid white;
                background-color : tan;
                font-size : 22px;
                font-weight:bold;
                font-family : Arial;
            ''',
            cursor=QCursor(QPixmap(CursorType.Link))
        ),
        textedit_args=dict(
            wrap_mode=None,
            rect=[25, 30, 350, 210],
            qss="""
                background-color : tan;
                color : white;
                border-radius : 15px;
                border : 5px solid white;
                qproperty-alignment:AlignCenter;
                font-size : 18px;
                font-weight :bold;
                font-family : Arial;
                """,
            text="{}!\n{}".format(title, content),
            cursor=QCursor(QPixmap(CursorType.Text))
        ),
        animation=ReAnimation(
            _type='geometry',
            target=_msgbox,
            start=QRect(760, 0, 400, 300),
            end=QRect(760, 300, 400, 300),
            duration=300,
        )
    )
    _msgbox.setStyleSheet('background-color : lightskyblue;'
                          'border-radius : 20px;')
    _msgbox.setModal(True)
    if show : _msgbox.show()