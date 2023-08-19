import sys
from os import PathLike
from pathlib import Path
from typing import Union

from PyQt5.QtCore import Qt, pyqtSignal, pyqtBoundSignal, QModelIndex
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from Util import MTFileTool
from OptComponent import ReTreeView

_path = Path(__file__).parent

class BaseTree(ReTreeView):
    # current selected item
    # Send a signal to the right column via the selected node
    # According to the name passed by the signal,
    # the corresponding file will be found, and then parsed
    selected_item: pyqtBoundSignal = pyqtSignal(str)

    def __init__(self, statement: bool = True):
        super(BaseTree, self).__init__()

        # the total model
        self.model = QStandardItemModel()
        self.rootNode : QStandardItem = self.model.invisibleRootItem()

        # the statement that defines whether U want to master tree-items by yourself
        self._statement = statement

        self.setUI()

    # base Ui setting
    def setUI(self):
        self.setWidgets(
            model=self.model,
            hide_labels=True,
            horizontal_labels=['', ''],
            function=self.item_clicked
        )
        if self._statement: self._baseItems()

    # Reserved method, when you import the default_example file (that is, it already exists)
    # you don't need to pass in the file path
    @staticmethod
    def addItem(new_item_name: str, basement: QStandardItem):
        modelItem = QStandardItem(new_item_name)
        modelItem.setFlags(modelItem.flags() & ~Qt.ItemIsEditable)
        basement.appendRow(modelItem)

    # add a new Item in the beginning of th root
    @staticmethod
    def addItem2(new_item_name: str, basement: QStandardItem, file: Union[PathLike or str], **kwargs):
        modelItem = QStandardItem(new_item_name)
        modelItem.setFlags(modelItem.flags() & ~Qt.ItemIsEditable)
        basement.appendRow(modelItem)
        # get file-cotent from file-path
        path = _path / '../' / "Source" / 'default_example' / '{}.mtml'.format(new_item_name)
        _file = open(path, 'w', encoding='U8')
        # now, I still input any file as a Python stream
        _mtml_text = MTFileTool.write(open(file, 'r', encoding='U8').read(), **kwargs)
        _file.write(_mtml_text)
        _file.close()

    # add a new Root as a basement.
    # the new root's basement is the model
    def addRoot(self, new_root_name: str):
        _newRoot = QStandardItem(new_root_name)
        _newRoot.setFlags(_newRoot.flags() & ~Qt.ItemIsEnabled)
        self.rootNode.appendRow(_newRoot)
        self.expand(self.model.indexFromItem(_newRoot))

    # add a tree , the tree is based on a root and many items
    # length of new_item_names must be equal to the length of listFilePaths and the length of kwargs.
    # kwargs are a combination of dictionaries for each different style
    def addTree(self,
                new_root_name: str,
                new_item_names: list[str],
                listFilePaths : list[str or PathLike],
                kwargs : list[dict]
                ):
        if new_item_names.__len__() == new_item_names.__len__() and len(new_item_names) == kwargs.__len__():
            _newRoot = QStandardItem(new_root_name)
            _newRoot.setFlags(_newRoot.flags() & ~Qt.ItemIsEnabled)
            def _addTree():
                for eachItemName in new_item_names:
                    modelItem = QStandardItem(eachItemName)
                    modelItem.setFlags(modelItem.flags() & ~Qt.ItemIsEditable)
                    # as the method adItem does
                    path = _path / '../' / "Source" / 'default_example' / '{}.mtml'.format(eachItemName)
                    _file = open(path, 'w', encoding='U8')
                    _index = new_item_names.index(eachItemName)
                    _mtml_text = MTFileTool.write(open(listFilePaths[_index], 'r', encoding='U8').read(), **kwargs[_index])
                    _file.write(_mtml_text)
                    _file.close()
                    yield modelItem

            _newRoot.appendRows(list(_addTree()))
            self.rootNode.appendRow(_newRoot)
            self.expand(self.model.indexFromItem(_newRoot))
        else:
            raise "The length must be the same."

    # get root by name quickly
    # This idea stems from JavaScript's tag object acquisition
    # The current version does not support the same name detection
    # root, named xx by default, exists
    def getRootByName(self, rootName: str) -> QStandardItem:
        for i in range(self.rootNode.rowCount()):
            if self.rootNode.child(i).text() == rootName:
                return self.rootNode.child(i)

    # when child item is clicked, send the signal
    def item_clicked(self, index: QModelIndex):
        # get the clicked item
        item = self.model.itemFromIndex(index)
        if not item.parent(): return
        child_item = item.parent().child(index.row())
        child_item_name = child_item.text()
        # send seleceted item-name
        self.selected_item.emit(child_item_name)

    # base items
    # In the current version (starting from 1.0.7),
    # the existence of this column depends on the user declaring True in the initialization
    # starting from version 1.0.7
    # New features, in order to allow users to customize the extension
    # You can choose the interface to use the default default_example by setting the status,
    # so that users can still expand based on the original project;
    # or it is completely empty project, which is dominated by the user
    # The statement is defined by __init__
    def _baseItems(self):
        # items which based on the model
        # such as plot、scatter、pie etc
        root_basement = QStandardItem("Basic Plots")
        # such as subgraphs or axises in a figure etc
        root_canvas = QStandardItem("Canvas")
        # such as font、color etc
        root_details = QStandardItem("Detail Description")

        # basement
        _basement = [QStandardItem("line chart"), QStandardItem('scatter plot'),
                     QStandardItem('bar chart'), QStandardItem('histogram'),
                     QStandardItem('pie chart'), QStandardItem('box plot'),
                     QStandardItem('heatmap'), QStandardItem('polar plot')]
        root_basement.appendRows(_basement)
        root_basement.setFlags(root_basement.flags() & ~Qt.ItemIsEnabled)

        # canvas
        _canvas = [QStandardItem("multi-subplots"), QStandardItem("axes design")]
        root_canvas.appendRows(_canvas)
        root_canvas.setFlags(root_canvas.flags() & ~Qt.ItemIsEnabled)

        # details
        _details = [QStandardItem("color settings"), QStandardItem("font settings"),
                    QStandardItem("lines settings"), QStandardItem("labels settings"),
                    QStandardItem("points settings"), QStandardItem('titles settings')]
        root_details.appendRows(_details)
        root_details.setFlags(root_details.flags() & ~Qt.ItemIsEnabled)

        for item in _canvas + _details + _basement:
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        """True means that you choose the default default_example, rather than being dominated by yourself"""
        self.rootNode.appendRows([root_basement, root_canvas, root_details])
        self.expand(self.model.indexFromItem(root_basement))
        self.expand(self.model.indexFromItem(root_details))
        self.expand(self.model.indexFromItem(root_canvas))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = BaseTree()
    ui.addItem("f1", ui.getRootByName('Basic Plots'))
    ui.addItem('f2', ui.getRootByName('Basic Plots'))
    ui.show()
    sys.exit(app.exec())
