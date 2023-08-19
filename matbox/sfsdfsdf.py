from MT import *
import sys

if __name__ == '__main__':
    app = ReAppication(sys.argv)
    ui = CoreUI(False)
    ui.setCard(text="""
    QApplication 是 PyQt 库中用于管理GUI应用程序的主要类。它是一个应用程序对象，负责管理和协调GUI应用程序的各种操作和事件，包括窗口管理、事件循环、资源管理等。在使用PyQt编写图形用户界面（GUI）应用程序时，通常会在应用程序的入口处创建一个QApplication对象。

以下是QApplication的一些主要功能：

事件循环（Event Loop）管理： QApplication会创建一个事件循环，该循环等待用户输入和系统事件，并将它们分发到适当的GUI组件中。这使得应用程序能够响应用户的操作。

窗口管理： QApplication管理应用程序的主窗口和其他窗口。它可以处理窗口的创建、显示、隐藏、最小化、关闭等操作。

资源管理： 在应用程序中可能需要加载和管理各种资源，如图像、样式表、国际化翻译等。QApplication提供了一些方法用于管理这些资源。

应用程序配置： QApplication可以设置一些全局的应用程序级配置，如应用程序名称、图标、样式等。

全局事件处理： 通过QApplication，你可以设置全局的事件处理函数，以便在整个应用程序中处理特定类型的事件，如键盘事件、鼠标事件等。

线程支持： QApplication可以协调多个线程中的GUI操作，确保线程安全。

在大多数情况下，一个PyQt应用程序的入口点会像这样创建一个QApplication对象：""")
    ui.show()
    sys.exit(app.exec())