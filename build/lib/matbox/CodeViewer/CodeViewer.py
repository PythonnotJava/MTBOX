import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QTextOption
from qutepart import Qutepart

if __name__ == '__main__':
    from grammar_tool import MTFileTool
else:
    from .grammar_tool import MTFileTool

class ViewSeletedItemCodes(Qutepart):

    def __init__(self, statement : bool = True, text_format : str = ".py"):
        super(ViewSeletedItemCodes, self).__init__()
        self._statement = statement
        self._text_format = text_format

        self.setUI()

    # basement
    def setUI(self):
        self.detectSyntax(language=self._text_format)
        self.setWordWrapMode(QTextOption.NoWrap)

    # open codes example file and return related code
    # you can see the related codes file in the dir--src/tutorial.
    # Each file starts with the example name and ends with md(version 1.0.6 supports)
    # Starting from version 1.0.7, I have made a tag file with the suffix mtml for this purpose,
    #  which can be flexibly defined as follows:
    #  {
    #  code block [editor_style],
    #  code block qss setting [editor_content] ,
    #  file type declaration in code area [code_format],
    #  parameter area (or you say remarks area can also be) [lines]
    #  and related qss settings [details_style]
    #  }
    # as I am showing U, you can operate it as a dict obj
    # this function has already written the corresponding function and returns the fixed function as above.
    def setMtml(self, itemName : str):
        def _setMtml():
            _path = Path(__file__).parent
            path = (_path / ".." / "Source" / "tutorial" / '{}.mtml'.format(itemName)).__str__()
            return MTFileTool().read(path)
        # change current editor codes
        self.setPlainText(_setMtml()['editor_content'])
        # change current editor code_format
        self.detectSyntax(language=_setMtml()['code_format'])
        # return a generator containing [qss_e, qss_t, text_t]
        yield from [_setMtml()['editor_style'], _setMtml()['details_style'], _setMtml()['lines']]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ViewSeletedItemCodes()
    ui.show()
    sys.exit(app.exec())