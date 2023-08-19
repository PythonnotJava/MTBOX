# 1.0.8版本  

## 我在新版本都做了些什么？
- 类型优化，对部分变量/参数进行了静态类型声明
- 对一些基础类进行了封装，采用声明式，尽可能让结构分明可寻
- 对一些变量进行了重命名，更清晰表达"是什么"
- 增/删了部分函数功能（下面会提到）

## 新增函数
- setCard(self, **kwargs)：允许用户自定义设置里面的卡片内容（因为考虑到以后可能会被用作个人软件、文档等的说明、前述等部分），kwarg是ReLabel里面的参数

## 主要命名改动

###  全局
- total_lay -> _globalLay

### 左区
- left_lay -> _leftLay
- left_line_lay -> _runAndSet
- homepageLine -> _statusLay
- left_listBox -> listBox

### 中区
- mid_spliter -> midSplitter

### 右区
- right_lay -> _rightLay
- homepageLay -> _homepageLay
- right_tutorial_group -> remakerGroup
- right_editor -> codesViewer
- right_tutorial -> remarker
- group_lay -> _groupLay
- title_show -> codeTitle
- right_temp_widget_hp -> _showHomePage
- right_temp_widget_org -> _showCodes

注 : 1.0.8版本比较匆匆忙忙，暂时对部分内容做出了调整，但总体功能可以说是基本没变，奈何最近时间仓促，剩下的还需留到日后开发；另外，1.0.8版本只作为预览版本，暂不支持建立等功能
> 日后可能会出现的功能
> - 命令行生成PDF
> - 调用pyinstaller更快捷的打包命令行
> - 对listBox的全面优化
> - 初始化载入性能优化
> - “我不能做的更多，但我一定沿着初心去走……” ——2023.8，19
