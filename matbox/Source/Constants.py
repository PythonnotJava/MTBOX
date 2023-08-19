from pathlib import Path

_path = Path(__file__).parent

class CursorType:
    Busy = str(_path / "mouseCursor" / "busy.cur")
    Help = str(_path / "mouseCursor" / "help.cur")
    Move = str(_path / "mouseCursor" / "move.cur")
    Link = str(_path / "mouseCursor" / "link.cur")
    Text = str(_path / "mouseCursor" / "text.cur")
    Table = str(_path / "mouseCursor" / "table.cur")
    Working = str(_path / "mouseCursor" / "working.cur")
    Normal = str(_path / "mouseCursor" / "normal.cur")
    Vertical = str(_path / "mouseCursor" / "vertical.cur")
    Precision = str(_path / "mouseCursor" / "precision.cur")
    Alternate = str(_path / "mouseCursor" / "alternate.cur")
    Diagonal1 = str(_path / "mouseCursor" / "diagonal1.cur")
    Diagonal2 = str(_path / "mouseCursor" / "diagonal2.cur")
    Horizontal = str(_path / "mouseCursor" / "horizontal.cur")
    Unavailable = str(_path / "mouseCursor" / "unavailable.cur")
    Handwriting = str(_path / "mouseCursor" / "handwriting.cur")


# logo
LOGO = (_path / "img" / "logo.ico").__str__()

# main-page.html
MAIN_PAGE = (_path / "h5" / "main.html").__str__()

# doc
README_SVG = (_path / "h5" / "readme.svg").__str__()
TUTORIAL_H5 = (_path / "h5" / "default_example.html").__str__()

# cfg-file
CFG = (_path / "cfg" / "config.yaml").__str__()

# MTML-example-PATH
MTML_EXAMPLE_PATH = _path / "default_example"

# music
class MusicType:
    Error = str(_path / "music" / "error.mp3")

