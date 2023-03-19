import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QTextOption
from qutepart import Qutepart

class ViewSeletedItemCodes(Qutepart):
    def __init__(self):
        super(ViewSeletedItemCodes, self).__init__()

        self.setUI()

    # basement
    def setUI(self):
        self.detectSyntax(sourceFilePath=".py")
        self.setWordWrapMode(QTextOption.NoWrap)
        self.setPlainText(self.getCodes('line chart'))

    # open codes example file and return related code
    # you can see the related codes file in the dir--src/tutorial.
    # Each file starts with the image name and ends with md
    @staticmethod
    def getCodes(itemName : str):
        if __name__ == '__main__' : path = '../src/tutorial/{}.md'.format(itemName)
        else: path = 'src/tutorial/{}.md'.format(itemName)
        # path = os.path.abspath(path)
        print(path)
        _f = open(path, 'r', encoding='U8')
        _codes = _f.read()[len("```python") : len(_f.read())-len('```')]
        _f.close()
        return _codes

    # set current codes by signal from TreeView
    def setCodes(self, itemName : str) : self.setPlainText(self.getCodes(itemName))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ViewSeletedItemCodes()
    ui.show()
    sys.exit(app.exec())