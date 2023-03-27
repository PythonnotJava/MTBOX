# 开发前的逸事:
## 开始着手写1.0.7版本的时候，是在一节叫做就业指导的公共课上，当时的我正头疼于从1.0.6何处更方便的构建并更改何种功能时，而我的周围，尤其是背后，坐着成排的女同学，我知道，即使我深知我当前技术的浅显，但在一堆与计算机专业无关并很大可能不了解代码的女同学面前，我必须露一手。于是，我随手写下了关于代码的第一个改善、相关的readme文档，然后第二个、第三个……当我在夜路回到宿舍时，我感觉到当时效率很高，难能整活，我就任意发挥了，于是就有了1.0.7版本

# 好了，不开玩笑了，请让我们进入主题吧

# 哔哩哔哩演示地址 ： https://www.bilibili.com/video/BV12v4y1G7iD/?spm_id_from=333.999.0.0&vd_source=9ab64e93362442ee5ac84c1c2078f8e7

# YouTube演示地址 ： https://youtu.be/hOW51iAL2eg


# PyPi 链接 : https://pypi.org/project/matbox/1.0.7/

# 快速安装
```
pip install matbox==1.0.7
```

# MatBox 1.0.7 版本

## MatBox（以下简称MT）1.0.7开始，支持用户选择界面是否使用默认还是自定义。即使是默认，用户仍然可以自定义，并且提供了友善的方法用于构建
### 文本 ： 用户只需传入一个python文件路径（囿于当前仍只支持Python），即可以快速写入
### qss ：用户可以定制自己的代码区以及注释区的qss样式，这样，不同界面呈现不同效果

## 默认示例
```python
from MT import main
main()
```
![屏幕截图 2023-03-25 232252](https://user-images.githubusercontent.com/88701385/227726669-8cf66a25-22c5-4e17-a5ba-5866bda290f6.png)



## 自定义版
```python
from MT import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatTutorial(False)

    kargs = {"editor_style": "font-size : 72px;color : red;",
             'lines': [{'parameter': '参数A','function': "功能A"}], 'details_style': "font-size : 72px;color : red;"}
    # 以下所有文件里面只含有Python代码
    ui.left_listBox.addRoot("Root1")
    root1 = ui.left_listBox.getRootByName('Root1')
    ui.left_listBox.addItem("Three D Show", root1)
    ui.left_listBox.addItem2("MyExample", root1, 'demo.py')
    ui.left_listBox.addItem2('3D', root1, 'eeeee.py')
    ui.left_listBox.addItem2('EasyExample', root1, 'ea.txt', **kargs)
    ui.left_listBox.addTree("Root2",
                            ['t1', 't2', 't3'],
                            ('1.txt', '2.txt', '3.txt'),
                            [kargs, kargs, kargs])


    ui.show()
    sys.exit(app.exec())

```
![屏幕截图 2023-03-25 190019](https://user-images.githubusercontent.com/88701385/227726435-de5c385d-3736-4c6b-8ff7-8de696a986b4.png)


#### 备注 ： 字体大是因为自定义的qss

# 继承关系与类的核心方法

## MatTutorial(核心类，继承了QWidget)

### MT的核心控件，用户创建实例的起始点，下面列举核心控件以及方法，下面几个大类同此

### left_listBox ： BaseTree实例，

### _set：ReSeDiag实例

### homepage ： ComingHome实例

### right_editor ： ViewSeletedItemCodes实例

### right_tutorial ： QTextEdit实例

### right_temp_widget_hp ：主界面显示的栈区，index为0

### right_temp_widget_org ：功能区显示的栈区，index为1

### mid_spliter ： QSplitter实例，右侧widget设置为了栈区，存放right_temp_widget_hp和right_temp_widget_org

### _config_datas : 配置文件的数据，是个字典

### setCurRigthWidget该方法设置主页与功能区的来回切换

### load_optimization用于存放UI美化的功能

### _runCode ，运行代码块代码的功能，可能代码块不一定是代码，在当前版本（1.0.7），默认只支持python

### _settings呼出设置栏目

### _renewTheme实时更新主题并写入配置数据

### closeEvent重写的关闭功能，核心在于关闭时写入新配置

### send_receive_signal这里集成了按钮点击功能、信号连接功能、按钮快捷键

### _setMtml当用户点击分支，来自BaeTree的setMTMl发送的信号会在这里完全调用，分别是qss、qss、tutorial_codes，当然了，点击分支时，会从主页立即切换也是合情合理的

### keyPressEvent另一些按钮事件，部分在主页呈现

## BaseTree（继承了QTreeView）

### BaseTree实现了左侧树状分支，也是主要提供给用户调用接口的类

### addItem2(new_item_name: str, basement: QStandardItem, file : Union[PathLike or str]， **kwargs)， 这是对1.0.6版本同名函数拓展，支持了用户选中添加的文件并自动解析的方案，而不是需要用户按照格式传入一个文件，函数的参数依次是 ： 新结点名字、新结点基于的根结点、文件路径，同时字典参数可以使你自定义每个界面不同的展示效果，下同

### addItem(new_item_name: str,  basement: QStandardItem)，对1.0.66的保留，添加一个名为xx的新结点到根结点，但是前提是位于Source/tutorial文件夹里面，必须能够找到同名为xx的mtml文件

### addRoot( new_root_name: str)，该方法用于创建一个新的根结点

### addTree(self, new_root_name: str, new_item_names: list[str],listFilePaths:list[str or PathLike],kwargs:list[dict]),该方法用于创建一个新分支，分支包括根结点、该根结点下面的子结点名字列表、子结点列表同长度的文件路径

### getRootByName(rootName : str),这是一个源于Javascript灵感的函数，当你创建或者已经存在一个名为xx的根结点，你就可以使用此函数提取并操作它

### configModel(labels: Iterable[str], hide=True)，设置树的标签，如果设置hide为True，就不存在标签，否则，将会设置标签名字，至此，BaseTree仅支持根结点+子结点的构建方式，所以标签必须是2个

### item_clicked( index: QModelIndex)，是链接大部分MT下控件的核心函数，我不希望用户去操作它，它的核心作用是在用户点击子结点时候，发送结点名字到信号

## ComingHome(QWidget

### 自1.0.7版本开始，MT提供了主界面，ComingHome实质是一个嵌入UI界面的网页

## ViewSeletedItemCodes(继承了Qutepart)

### setMtml(self, itemName : str)

#### 通过传入的MTML文件名字，设置代码块数据和代码块当前文件的文件格式，返回代码块qss、注释区qss、注释区的数据

### ViewSeletedItemCodes是代码块实现区域

## ReSetDiag(继承了QDialog)

### ReSetDiag是设置界面的实现，目前仅支持更换主题，多国语言暂未开放

### themeChanged()函数是在用户改变了主题时连接信号

# 关于当前matbox的整体布局，注意，total_lay是全局布局

<img alt="" src="https://github.com/PythonnotJava/MTBOX/blob/matbox1.0.7/Layout-Show-Img/layout.png?raw=true"/>
