# Anecdote before development:
## When I started to write the 1.0.7 version, it was in a public class called employment guidance. At that time, I was having a headache when it was more convenient to build and change functions from 1.0.6, and my Around, especially behind, there are rows of female students sitting. I know that even though I am well aware of the shallowness of my current technology, I must show my hand in front of a bunch of female students who have nothing to do with computer majors and probably do not understand code. . So, I wrote down the first improvement about the code, related readme documents, and then the second, third... When I returned to the dormitory on the night road, I felt that the efficiency was very high at that time, and it was difficult to For the whole job, I just played it arbitrarily, so I have version 1.0.7

# Ok, no kidding, let's get to the point

# Bilibili demo address: https://www.bilibili.com/video/BV12v4y1G7iD/?spm_id_from=333.999.0.0&vd_source=9ab64e93362442ee5ac84c1c2078f8e7

# YouTube demo address: https://youtu.be/hOW51iAL2eg

# PyPi link: https://pypi.org/project/matbox/1.0.7/

# quick install
```
pip install matbox==1.0.7
```

# MatBox version 1.0.7

## Starting from MatBox (hereinafter referred to as MT) 1.0.7, users can choose whether to use the default or custom interface. Even if it is the default, users can still customize it, and provide a friendly method for building
### Text: The user only needs to pass in a python file path (only Python is currently supported), and the user can quickly write
### qss : Users can customize the qss style of their own code area and comment area, so that different interfaces present different effects

## default example
```python
from MT import main
main()
```
![Screenshot 2023-03-25 232252](https://user-images.githubusercontent.com/88701385/227726415-56912def-88ae-4d3c-bbca-d3624310f8a2.png)



## Custom version
```python
from MT import *

if __name__ == '__main__':
     app = QApplication(sys. argv)
     ui = MatTutorial(False)

     kargs = {"editor_style": "font-size: 72px;color: red;",
              'lines': [{'parameter': 'Parameter A','function': "Function A"}], 'details_style': "font-size : 72px;color : red;"}
     # All the following files contain only Python code
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


     ui. show()
     sys. exit(app. exec())

```
![Screenshot 2023-03-25 190019](https://user-images.githubusercontent.com/88701385/227726435-de5c385d-3736-4c6b-8ff7-8de696a986b4.png)


#### Remarks: The font is large because of the custom qss

# Inheritance relationship and the core method of the class

## MatTutorial (core class, inherits QWidget)

### The core controls of MT, the starting point for users to create instances, the core controls and methods are listed below, and the following categories are the same

### left_listBox : BaseTree instance,

### _set: ReSeDiag instance

### homepage : ComingHome instance

### right_editor : ViewSeletedItemCodes instance

### right_tutorial: QTextEdit instance

### right_temp_widget_hp : The stack area displayed on the main interface, index is 0

### right_temp_widget_org : The stack area displayed in the functional area, index is 1

### mid_spliter : QSplitter instance, the right widget is set as a stack area, storing right_temp_widget_hp and right_temp_widget_org

### _config_datas : The data of the configuration file, which is a dictionary

### setCurRigthWidget This method sets the switch between the homepage and the ribbon

### load_optimization is used to store UI beautification functions

### _runCode , the function of running the code block code, maybe the code block is not necessarily code, in the current version (1.0.7), only python is supported by default

### _settings calls out the setting column

### _renewTheme updates the theme in real time and writes configuration data

### CloseEvent rewrites the closing function, the core is to write new configuration when closing

### send_receive_signal here integrates button click function, signal connection function, button shortcut key

### _setMtml When the user clicks on a branch, the signals sent by setMTMl from BaeTree will be fully invoked here, namely qss, qss, tutorial_codes. Of course, when clicking on a branch, it is reasonable to switch from the homepage immediately

### keyPressEvent Other button events, some are presented on the home page

## BaseTree (inherited from QTreeView)

### BaseTree implements the tree branch on the left, and it is also the class mainly provided to the user to call the interface

### addItem2(new_item_name: str, basement: QStandardItem, file : Union[PathLike or str], **kwargs), this is an extension of the function of the same name in version 1.0.6, which supports the scheme that the user selects the added file and automatically parses it , instead of requiring the user to pass in a file according to the format, the parameters of the function are: the name of the new node, the root node based on the new node, the file path, and the dictionary parameters allow you to customize the different display effects of each interface , the same below

### addItem(new_item_name: str, basement: QStandardItem), reserved for 1.0.66, adding a new node named xx to the root node, but the premise is that it is located in the Source/tutorial folder and must be able to find the same name mtml file for xx

### addRoot( new_root_name: str), this method is used to create a new root node

### addTree(self, new_root_name: str, new_item_names: list[str], listFilePaths: list[str or PathLike], kwargs: list[dict]), this method is used to create a new branch, the branch includes the root node, The name list of child nodes under the root node, the file path of the same length as the list of child nodes

### getRootByName(rootName : str), this is a function inspired by Javascript, when you create or already exist a root node named xx, you can use this function to extract and manipulate it

### configModel(labels: Iterable[str], hide=True), set the label of the tree. If hide is set to True, there will be no label. Otherwise, the label name will be set. So far, BaseTree only supports the root node+ The way child nodes are constructed, so the label must be 2

### item_clicked(index: QModelIndex), is the core function that links most of the controls under MT. I don't want users to operate it. Its core function is to send the node name to the signal when the user clicks on the child node

## ComingHome(QWidget

### Since version 1.0.7, MT has provided the main interface, and ComingHome is essentially a webpage embedded in the UI interface

## ViewSeletedItemCodes (inherited from Qutepart)

### setMtml(self, itemName: str)

#### Through the name of the MTML file passed in, set the code block data and the file format of the current file of the code block, and return the data of the code block qss, comment area qss, and comment area

### ViewSeletedItemCodes is the code block implementation area

## ReSetDiag (inherited from QDialog)

### ReSetDiag is the implementation of the setting interface, currently only supports changing the theme, and the multi-language is not yet open

### ThemeChanged() function is to connect the signal when the user changes the theme

# About the layout of the matbox. U need pay attention to the total_lay, which is the global layout.
<img alt="" src="https://github.com/PythonnotJava/MTBOX/blob/matbox1.0.7/Layout-Show-Img/layout.png?raw=true"/>
