```text
                         __ __ _ _ _ _ _ _ _______ _ _ _
                        | \/ | | | | | | | | |(_)| | |__ __| | | (_) | |
                        | \ / | __ _ | |_ _ __ | | ___ | |_ | | _ | |__ | | _ _ | |_ ___ _ __ _ __ _ | |
                        | |\/| | / _` || __|| '_ \ | | / _ \ | __|| || || '_ \ | || | | || __|/ _ \ | '__|| | / _` || |
                        | | | || (_| || |_ | |_) || || (_) || |_ | || || |_) | | || |_| || |_| (_) || | | || (_| || |
                        |_| |_| \__,_| \__|| .__/ |_| \___/ \__||_||_||_.__/ |_| \__,_| \__|\ ___/ |_| |_| \__,_||_|
                                            | |
                                            |_|
```

# About matplotlib_tutorial
## Introduction
### As you can see, matplotlib_tutorial (hereinafter referred to as MT) is a toolbox dedicated to teaching you to quickly get started [Matplotlib] (https://matplotlib.org/), and it is now in the initial testing stage of 1.0, as A tool that took nearly a day to develop, even if I have done a lot of testing and careful consideration, I cannot guarantee that MT is a perfect toolbox, but at least it will bring you a more convenient and efficient introductory tutorial

## current orientation
### Fortunately, from the beginning of development, I thought about it. MT is not only a toolbox, but also can be customized. You can call its functions and expand it. The current MT built-in tutorial is not very comprehensive. , however, you only need to add the new knowledge you have learned (even if these may be completed in future updates) according to the following process
* Take a look before expanding
![exa1](https://user-images.githubusercontent.com/88701385/226183612-cdfa1106-5095-43c3-acd8-428b2d09bf39.png)

   * This is after the expansion, the process I did is
     1. Call the addItem method of the left tree directory to add a "New Item" behind the root_details branch
     2. Add the file New Item.md with the same name in the src/tutorial folder, because the program will automatically detect such files with the same name to display the tutorial. As for the display of detailed parameters, it will be mentioned later. It is worth noting that you The md file with the same name needs to be defined according to the following tutorial
```python
# Here you must write code examples, and must declare that this is a python (requires lowercase python) code block
from matplotlib.pyplot import plot
def func() : ...
className: ...
```

* After doing this, here is the code sample and the redefined interface
```python
# Exammple show U that expand new items by yourself
import sys
import MT

if __name__ == '__main__':
     app = MT.QApplication(sys.argv)
     ui = MT.MatTutorial()
     ui.left_listBox.addItem("New Item", ui.left_listBox.root_details)
     ui. show()
     sys. exit(app. exec())
```

![exa2](https://user-images.githubusercontent.com/88701385/226183606-07742827-ec03-49da-a78f-d5f31ba092a6.png)

## uncomfortable
### Maybe you have already felt it - a tool developed in one day (not even enough to be called a tool), there are many annoying places
* There is no function to directly expand the root branch tutorial node
* Requires tedious writing of own tutorial
* Did not provide relevant instructions for each tutorial in the parameter details area, but just used a full function tutorial to perfunctory the past
* No more comprehensive bug fixes (especially for users) or throwing errors (especially for callers)
* There is no comprehensive function for multiple languages (currently only Chinese is supported, and the English function cannot be triggered)
* The tutorial area and the parameter details area do not have a drag split effect similar to the left and right partitions
*etc

## future development
### Through the above bugs and so on, in the near future, I am very likely to improve through the following ideas
* Provide additional methods to create root branches in BaseTree
* Modify the grammar of the added tutorial file, or change the type of the read-in file (in fact, I considered html files at the beginning, and used the request+re module to obtain the code tag content, although html is more legible to ordinary users , but because I am not very good at writing H5 and the H5 file size is large, I gave up)
* Define the file related to the parameter details, and use the signal to replace the display of the parameter details when changing the tutorial
* Multilingual function, multinational interface, just like my readme file is divided into Chinese and English versions
* Try optimizing the right column with a split column. Can customize height display
* Bug detection and processing functions
* More and more comprehensive matplotlib_tutorial tutorial
