```text
      __  __         _           _         _    _  _  _       _______      _                _         _ 
     |  \/  |       | |         | |       | |  | |(_)| |     |__   __|    | |              (_)       | |
     | \  / |  __ _ | |_  _ __  | |  ___  | |_ | | _ | |__      | | _   _ | |_  ___   _ __  _   __ _ | |
     | |\/| | / _` || __|| '_ \ | | / _ \ | __|| || || '_ \     | || | | || __|/ _ \ | '__|| | / _` || |
     | |  | || (_| || |_ | |_) || || (_) || |_ | || || |_) |    | || |_| || |_| (_) || |   | || (_| || |
     |_|  |_| \__,_| \__|| .__/ |_| \___/  \__||_||_||_.__/     |_| \__,_| \__|\___/ |_|   |_| \__,_||_|
                         | |                                                                            
                         |_|                                                                            
```
# 使用前引导
## pypi下载链接 : https://pypi.org/manage/project/matbox/release/1.0.6/
```text
## 安装命令
pip install matbox==1.0.6
```
## 基于开发的库
```text
PyQt5
qutepart
pyyaml
qt_material
numpy
matplotlib
```


# 关于matplotlib_tutorial
## 简介
### 正如你所见，matplotlib_tutorial（下面简称MT）是一款致力于教会你快速入门[Matplotlib](https://matplotlib.org/)的工具箱，现在正处于1.0的初测阶段，作为一个用了将近一天开发的工具，即使我做了大量的测试以及深思熟虑，我也并不能保证MT是一个很完美的工具箱，但是，至少它会给你带来更方便、更效率的入门教程

## 当前导向
### 幸运的是，从开发当初，我就想好了，MT不仅是作为一款工具箱，更可以被自定义，你可以调用它的功能并拓展它，当前MT内置教程并不是很全面，但是，你只需要把学到的（即使这些在未来的更新中可能会补全）新知识按照下面流程就可以额外添加
* 先看一下拓展之前

![exa1](https://user-images.githubusercontent.com/88701385/226288689-ca14401e-48ad-4d9c-be50-1b5cc0f66fce.png)
  * 这是拓展之后，我所做的流程是
    1. 调用左侧树目录的addItem方法添加了一个"New Item"的在root_details分支后面
    2. 在src/tutorial文件夹添加同名文件New Item.md，因为程序会自动检测这类同名文件用来展示教程，至于详情参数展示的问题，将会在后面提及，值得注意的是，你需要按照下面教程定义同名的md文件
```python
# 这里面你必须写入代码示例，且必须声明这是一个python（需要小写python）的代码块
from matplotlib.pyplot import plot
def func() : ...
class Name : ...
```

* 做完这些之后，下面是代码示例以及重新定义的界面
```python
# Exammple show U that expand new items by yourself
import sys
import MT

if __name__ == '__main__':
    app = MT.QApplication(sys.argv)
    ui = MT.MatTutorial()
    ui.left_listBox.addItem("New Item", ui.left_listBox.root_details)
    ui.show()
    sys.exit(app.exec())
```
![exa2](https://user-images.githubusercontent.com/88701385/226288710-d92edbbb-1c75-44f0-9ab7-e04fde9562c3.png)


## 不舒适
### 或许你已经感觉到了——一个一天开发的工具（甚至不足以叫做工具吧），有很多让人感到厌烦的地方
* 没有直接拓展根分支教程结点的功能函数
* 需要繁琐的写入自己的教程
* 没有在参数详情区提供每个教程的相关说明，而只是用一个全部函数教程敷衍过去
* 没有更全面的bug解决措施（尤其对于用户）或者抛出错误（尤其对于调用者）
* 没有多国语言的完善功能（目前仅支持中文，且英文功能无法触发）
* 教程区以参数详情区没有类似左右分区的拖动分割效果
* etc

## 未来发展
### 通过上述的bug等等等问题，在不久，我极其可能通过以下思路改善
* 提供额外创建根分支的方法在BaseTree中
* 修改被添加的教程文件的语法，或者更换读入文件的类型（其实一开始我有考虑html文件，并使用request+re模块获取code标签内容，虽然html对普通用户的易读性更好了，但是囿于我并不是很擅长写H5以及H5文件体积较大的原因放弃了）
* 定义参数详情有关的文件，并在更换教程时使用信号更换参数详情的显示
* 多语言功能，界面的多国化，正如我的readme文件分为中英文两个版本
* 尝试使用分割栏优化右侧栏目。可以自定义高度展示
* bug检测以及处理功能
* 更多更全面的matplotlib_tutorial教程

