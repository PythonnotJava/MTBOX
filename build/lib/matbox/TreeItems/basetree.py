import sys
from PyQt5.QtCore import Qt, pyqtSignal, pyqtBoundSignal, QModelIndex
from PyQt5.QtWidgets import QApplication, QTreeView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from typing import Iterable

class BaseTree(QTreeView):

    # current selected item
    selected_item : pyqtBoundSignal = pyqtSignal(str)

    def __init__(self):
        super(BaseTree, self).__init__()

        # the total model
        self.model = QStandardItemModel()
        self.rootNode = self.model.invisibleRootItem()

        # items which based on the model
        # such as plot、scatter、pie etc
        self.root_basement = QStandardItem("Basic Plots")
        # such as subgraphs or axises in a figure etc
        self.root_canvas = QStandardItem("Canvas")
        # such as font、color etc
        self.root_details = QStandardItem("Detail Description")

        self.setUI()
        self.baseItems()
        self.configModel(['', ''])

    # base Ui setting
    def setUI(self):
        self.setModel(self.model)
        self.rootNode.appendRows([self.root_basement, self.root_canvas, self.root_details])
        self.setExpandsOnDoubleClick(True)
        self.expand(self.model.indexFromItem(self.root_basement))
        self.expand(self.model.indexFromItem(self.root_details))
        self.expand(self.model.indexFromItem(self.root_canvas))
        self.clicked.connect(self.item_clicked)

    # add a new Item in the beginning of th root
    def addItem(self, rootName : str, basement : QStandardItem):
        modelItem = QStandardItem(rootName)
        modelItem.setFlags(modelItem.flags() & ~Qt.ItemIsEditable)
        basement.appendRow([modelItem])

    # base items
    def baseItems(self):
        # basement
        _basement = [QStandardItem("line chart"), QStandardItem('scatter plot'),
            QStandardItem('bar chart'), QStandardItem('histogram'),
            QStandardItem('pie chart'), QStandardItem('box plot'),
            QStandardItem('heatmap'), QStandardItem('polar plot')]
        self.root_basement.appendRows(_basement)
        self.root_basement.setFlags(self.root_basement.flags() & ~Qt.ItemIsEnabled)

        # canvas
        _canvas = [QStandardItem("multi-subplots"), QStandardItem("axes design")]
        self.root_canvas.appendRows(_canvas)
        self.root_canvas.setFlags(self.root_canvas.flags() & ~Qt.ItemIsEnabled)

        # details
        _details = [QStandardItem("color settings"), QStandardItem("font settings"),
                    QStandardItem("lines settings"), QStandardItem("labels settings"),
                    QStandardItem("points settings"), QStandardItem('titles settings')]
        self.root_details.appendRows(_details)
        self.root_details.setFlags(self.root_details.flags() & ~Qt.ItemIsEnabled)

        for item in _canvas + _details + _basement:
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    # set basic model
    def configModel(self, labels : Iterable[str], hide=True):
        self.model.setHorizontalHeaderLabels(labels)
        self.setHeaderHidden(hide)

    # when child item is clicked, send the signal
    def item_clicked(self, index: QModelIndex):
        # get the clicked item
        item = self.model.itemFromIndex(index)
        if not item.parent(): return
        child_item = item.parent().child(index.row())
        child_item_name = child_item.text()
        # send
        self.selected_item.emit(child_item_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = BaseTree()
    ui.configModel(['t1', 't2'])
    ui.addItem("f1", ui.root_canvas)
    ui.addItem('f2', ui.root_canvas)
    ui.show()
    sys.exit(app.exec())