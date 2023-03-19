print(
    '--------------------------------------------matplotlib.pyplot API 入门学习--------------------------------------------')
MyNote = """
    *a:
        >>>默认参数都是我随便设置的
    *b:
        >>>部分参数是可以缩写的
plt.figure(figsize=(9, 9), dpi=1000)->创建画布
    figsize-> 画布大小
    dpi-> 像素密度
plt.plot(x, y, linestyle='-', color='green', linewidth=3, label='cos(x)', fillstyle='full', markersize=20)-> 折线图
    linestyle-> 图像类型(缩写是ls)
    color-> 图像颜色(缩写是c，当然了，颜色也可以缩写; example: c='r'->c='red', 参数也可以是0到1浮点数形式的字符串，越大颜色越深, c='1'->c='black')
    linewidth-> 图像线粗(缩写是lw)
    label-> 图像标题(需要plt.legend()来进行显示)
    fillstyle-> 点的填充方式，有left/right/full/bottom/top/none可选
    markersize-> 点的大小
    *a:
        >>>plot函数可以在同一个画布上创建多个图线，比如：plot(x1, y1, 'r--',…… x2, y2, 'g--', ……)表示了两个图线的不同参数配置，返回值为两个图线实例
plt.scatter(x, y, color='red', label='scatter image', s=5)-> 散点图
    s-> 点的大小
plt.xlim(a, b)->限制x坐标范围
plt.ylim(a, b)->限制y坐标范围
    a-> 最小值
    b-> 最大值
plt.xlabel('X Point', color='r')-> x轴标签
plt.ylabel('Y Point', color='y')-> y轴标签
plt.grid(color='red', lw=3, ls=':', alpha=0.5, axis='y')->网格化画布
    alpha->透明度
    axis-> 网格线选取（这里是只显示y轴，默认是全部）
plt.axhline(y=0, lw=5, ls='--', c='r')-> 绘制平行于x轴的水平参考线
plt.axvline(x=0, lw=5, ls='--', c='y')-> 绘制平行于y轴的水平参考线
plt.axvspan(xmin=-7, xmax=7, fc='r', alpha=0.5)-> 绘制垂直于x轴的参考区域
    xmin->可以认为是起点
    xmax->可以认为是终点
    fc(全称是facecolor)->区域颜色
    alpha->透明度
plt.axhspan用法同上
plt.annotate(
    text='It is the point by two funcs: (0, 0)',
    xy=(0, 0),
    xytext=(2.5, -1),
    fontsize=64,
    color='b',
    arrowprops=dict(arrowstyle='->',connectionstyle='arc3',color='b'
    ))-> 箭头注释
    text->注释内容
    xy->指向坐标
    xytext->起点坐标
    fontsize-> 字体大小
    color-> 颜色
    arrowprops-> 箭头的属性
plt.text(x, y, s='y=f(x)', fontdict=dict(weight='bold', size=64), c='r')-> 无指向文本
    x-> 文本x坐标
    y-> 文本y坐标
    s-> 文本内容
plt.title(label='Using so fluently!!!', fontdict=dict(weight='bold', size=64, loc='left'))->标题(一个画布外面可以使用多个标题)
    loc-> 标题位置
plt.legend(line=[line1, line2, ……], name=['name1', 'name2', ……], loc=1, bbox_to_anchor=(0.91, 0, 0.3, 1), title='This is the name of box.',
 shadow=True, mode='expand', fancybox=True, nloc=3, fontsize=48, borderaxespad=0.3， frameon=True, framealpha=1.0)-> 图列
    *a:
        >>>这里的line和name只是随便起的参数名字（并不存在）
    line-> 根据实例匹配对应的图线
    name-> 实例匹配对应的图线的新命名
    loc-> 位置，这里的1相当于'upper right'
    bbox_to_anchor-> 盒子的定位坐标在画布占位的百分比(左边，右边，顶边，底边)
    title-> 盒子的标题
    shadow-> 盒子边框阴影效果
    nloc-> 图例的列的数量，一般为1
    fancybox-> 是否将图例框的边角设为圆形
    fontsize-> 字体大小
    borderaxespad-> 轴与图例边框之间的距离
    frameon-> 是否显示边框
    framealpha-> 边框透明度（0~1）
    mode-> 盒子边框形状（这里的expand是让盒子直接拓展到画布两侧）

plt.bar(x, height, width=0.5, align='center', color=colors, tick_label=list('ABCDEFGH'), hatch='\\o', label='随机模拟', bottom=0)-> 柱状图(纵向柱状图)
    x-> 默认底部变量名称
    height-> 变量数值
    width-> 柱的粗细
    align-> 底部变量名称的位置，默认居中，当然也可以edge->左边缘开始
    color-> 柱的颜色(也可以是列表)
    tick_label-> 替换底部变量名称
    hatch-> 驻的风格
    label-> 图像标题(需要plt.legend()来进行显示)
    bottom-> 基线

plt.bar(x, height, width=0.5, align='center', yerr=std_, color=colors,
error_kw=dict(elinewidth=2, ecolor='yellow', capsize=3), tick_label=['园区{}'.format(s) for s in range(1, 6)])-> 误差棒柱状图
    error_kw-> 误差棒的属性组成的字典
    yerr-> 每一组对应的误差数据组成的列表

plt.barh(y, width, height=0.5, align='center', color='0.5', tick_label=list('ABCDEFGH'), hatch='\\\o')-> 条形图(横向柱状图)
    y-> 默认底部变量名称
    width-> 变量数值
    height-> 柱的粗细
    align-> 底部变量名称的位置，默认居中，当然也可以edge->左边缘开始
    color-> 柱的颜色(也可以是列表)
    tick_label-> 替换底部变量名称
    hatch-> 驻的风格

plt.barh(y, width, height=bar_width, align='center', color=colors, xerr=std_err, tick_label=['误差{}'.format(s) for s in range(5)])-> 误差棒条形图(原理类似误差棒柱状图)
plt.hist(x, bins=bin_, align='mid',histtype='bar', color='r', rwidth=0.5)-> 直方图
    x-> 统计的变量
    bins-> 统计的变量所在区间
    align-> 变量位置
    history-> 直方图类型
    color-> 直方图颜色
    rwidth-> 直方图柱子的粗细
堆积图-> 两个bar
plt.bar(x, y, align='center', color='blue', tick_label=list('ARCADE'), label='数据1', width=0.5, hatch='\\')
plt.bar(x, y1, align='center', color='pink', bottom=y, label='数据2', width=0.5, hatch='\\')
    第二个bar堆积在第一个bar上， 原理是bottom参数，使得新的 bar坐落在于上一个bar的值
堆积条形图-> 两个barh
plt.barh(y=x, width=y, height=0.7, color='blue', tick_label=list('ABCDE'), label='数据1', hatch='\\')
plt.barh(y=x, width=y, height=0.7, color='green', left=y, label='数据2', hatch='\\')
    原理同上，只不过用left来代替bottom参数
并列堆积图-> 两个bar
plt.bar(x, y, width=0.3, tick_label=list('ABCDE'), color='r', align='center', label='数据A', hatch='\\')
plt.bar(x+width, y1, width=0.3, color='b', align='center', label='数据A', hatch='\\')
    x-> 数组形式，这样可以进行计算，而列表不能
    x+width-> 这样会并一起，否则会有空隙
并列条形图-> 两个barh
plt.barh(y, width=y, height=0.3, align='center', color='red', tick_label=list('ABCDE'), label='数据1', hatch='\\')
plt.barh(y=x+height, width=y1, height=0.3, align='center', color='y',  label='数据2', hatch='\\o')
    原理与上类似

plt.pie(x, explode=explode, labels=labels, autopct='%3.8f%%', startangle=45, shadow=True, colors=colors,
 radius=2, pctdistance=0.5, labeldistance=0.7)-> 饼状图
    x-> 变量的量
    explode-> 分块之间的间隙，在被赋予值之后，就是分裂式饼图
    labels-> 变量名字
    colors-> 变量分配的饼对应的颜色
    autopct-> 变量占比精确位数
    startangle-> 第一个变量开始分配饼时相当于x轴的角度(逆时针为正)
    shadow-> 是否有重影效果
    radius-> 半径
    pctdistance-> 占比相对于原点的距离
    labeldistance-> 变量名字相当于原点的距离
多个plt.pie(x, autopct='%3.2f%%', radius=0.7, 
    pctdistance=0.75, colors=outer_c, textprops=dict(color='w'),
    wedgeprops=dict(width=0.3, edgecolor='w'), shadow=True, explode=expe)-> 内嵌环形饼图(这里不推荐shadow和exeplode这两个参数，因为效果图不好看了)
    textprops-> 占比文本配置
    wedgeprops-> 分块的饼图配置，这里的width表示每块（扇形）的完整性
plt.polar(theta, r, color='yellow', lw=2, marker='o', mfc='red', ms=22, ls='--)-> 极线图（极坐标）
    theta-> 点的角度和对应个数
    r-> 点到极点的距离
    color-> 点的连线颜色
    lw-> 连线的线宽
    marker-> 点的样式
    mfc-> 点的颜色
    ms-> 点的半径
    ls-> 连线风格(linestyle)
plt.scatter(x, y, s=numpy.power(10*a+20*b, 2), c=numpy.random.rand(100), cmap=mpl.cm.RdYlBu, marker='o')-> 气泡图（散点图）
    x-> x轴的值
    y-> y轴的值
    s-> 散点大小
    c-> 散点标记的颜色
    cmap-> 将浮点数映射成颜色的颜色映射表
    marker-> 点的样式
plt.stem(x, y, linefmt='--', markerfmt='*', basefmt='-.', bottom=0.)-> 棉棒图：表现出一堆变量相当于一个共同标准的离散形式
    x-> 棉棒在x轴的位置
    y-> 棉棒长度
    linefmt-> 棉棒样式
    markerfmt-> 棉棒点的样式
    basefmt-> 共同标准的所在基线的样式
    bottom-> 共同标准的所在基线
plt.boxplot(x, whis=whis, sym='o', widths=width, labels=labels, patch_artist=True, notch=True, vert=False, showfliers=False， meanprops=dict(color='r'))-> 箱线图
    x-> 每组数据组成的列表（数组）
    whis-> 四分位间距的倍数，用来确定相须包含数据的范围大小
    sym-> 离群值的样式
    widths-> 箱体的宽度
    labels-> 每组数据的名字
    notch-> 设置为True时，会使得箱体呈现V型凹陷
    patch_artist-> 每组数据箱体颜色(设置为True时，可以把此函数视为一个对象bplot，并使用如下*a配色)
    vert-> 设置为False时，显示的是水平方向的箱线图
    showfliers-> False时,不显示离群值
    showmeans-> 是否以点的形式显示均值
    meanprops-> 均值点的配置
    *a:
        >>>for patch, color in zip(bplot['boxes'], colors):
        >>>     patch.set_facecolor(color)

plt.errorbar(x, y, fmt='ro--', yerr=0.2, xerr=0.02, ecolor='y', elinewidth=4, ms=5, mfc='c', mec='r', capthick=1, capsize=2)-> 误差棒图
    fmt-> 样式，我这里默认值意思是蓝色o形点用虚线连接
    yerr-> y轴误差
    xerr-> x轴误差
    ecolor-> 误差棒颜色
    elinewidth-> 误差棒粗细
    ms-> 数据点大小
    mfc-> 数据点颜色
    mec-> 数据点边缘颜色
    capthick-> 误差棒边界横杠厚度
    capsize-> 误差棒边界横杠大小

plt.yticks(list(a1),list('ABCDE'), rotation=-90)-> y轴变量名字定位以及变量名字，变量名字相当于tick_label参数的作用,rotation是标题的旋转角度
plt.xticks(list(a2),list('ABCDE'), rotation=-90)-> x轴变量名字定位以及变量名字，变量名字相当于tick_label参数的作用，rotation是标题的旋转角度
    list(a1)-> 轴变量名字定位(即原来的轴上值的列表)
    list('ABCDE')-> 替换原来的轴上值为xxx
plt.stackplot(x, y, y1, ……, labels=['func(x)', 'func(a)', 'func(t)'], colors=['red', 'green', 'gray'])-> 堆积折线图
    labels-> 标签
    colors-> 每个折线的颜色
plt.broken_barh(xranges=[(30, 100), (180, 50), (260, 70)], yrange=(20, 8), facecolor=['red', 'red', 'gray'])-> 间断条形图
    xranges-> 由每个部分组成的列表， 比如： [(2, 50), (30, 10)]表示有两个部分， 第一个从2开始，延长50距离
    yrange-> 宽度， 比如： (20, 8)表示从20开始，宽8
    facecolor(或者 fc 或者 facecolors)-> 可以是单个颜色，也可以是颜色序列，表示每部分的颜色
plt.step(x, y, color='y', where='mid', lw=5, ls='--')-> 阶梯图
    where-> 点根据参数的选取，决定图像
plt.hist(x=[scoresT, scoresT1], bins, color=['y', 'b'], rwidth=1, histtype='bar', hatch='\\o', stacked=True)-> 堆积（并列）直方图
    x-> 堆积数据列表
    bins-> 分类区间
    colors-> 每个部分的颜色
    stacked-> 是否堆积： True表示堆积图，False表示并列图
    histtype->直方图类型，当值为stepfilled时，是阶梯型直方图
plt.table(cellText=[['班级{}'.format(ti) for ti in range(1, 6)], stu],
          cellLoc='center',
          colWidths=[0.3] * 5,
          colLabels=labels,
          colColours=colors,
          rowLabels=['班级', '学生人数'],
          rowLoc='left',
          loc='bottom')-> 表格
    cellText-> 由每一行标签对应的的值组成的列表的列表
    cellLoc-> 列标签的文字在单元格中的位置
    colWidth-> 单元格宽度
    colLabel-> 列标签
    colColour-> 列标签单元格颜色
    rowLabel-> 行标签组成的列表
    rowLoc-> 行标签文字在单元格的位置
    loc-> 表格整体的定位

plt.subplot(nrows, ncols, index, polar=True)-> 子区函数（相当于在一个画布上分出多个子画布）
    *a: 
        >>>subplot参数：nrows, ncols, index只是代号，输入时还需用数字代替,写成nrows=5这样的形式会报错
    nrows-> 分出画布的行数
    ncols-> 分出画布的列数
    index-> ,从上往下，左数第index个子画布（index索引从一开始）
    polar-> 把该子画布当成极坐标图
    *b:
        >>>子区函数也可以写成plt.subplot(RCN, ……)形式，其中RCN是三个整数，分别代表分出画布的行数、分出画布的列数、左数第index个子画布（index索引从一开始）
    *c:
        >>>你可以直接对子区函数的画布进行操作，比如： plt.plot(……)；可以将子区函数返回一个对象实例，你也可以对该对象实例进行操作，比如：object_.plot(……)
    *d:
        >>>当然，fig=plt.figure(……)返回一个fig实例，对这个实例使用add_subplot(……)/add_axes(……)等等等方法，同样也可以进行子画布创建
    *e:
        >>>在fig实例的参数polar设置为True，会将画布变成极坐标，此时fig实例·下使用add_subplot创建子画布，子画布可以使用bar函数创建极区图

plt.suptitle(t='all titles', size=32, color='red')-> 针对subplot图像的共同标题
    t-> 标题名字
plt.margins(x=0.5, y=0.5)-> 设置数据范围的空白区域(x和y表示额外扩张倍数)
多个plt.subplot2grid将画布分为多个大小不同的子画布(subplot也提供了支持，但是这里不细讲)
例子：
    plt.subplot2grid((3, 4), (0, 0), colspan=1)
    plt.subplot2grid((3, 4), (0, 1), colspan=2)
    plt.subplot2grid((3, 4), (1, 0), colspan=3)
    plt.subplot2grid((3, 4), (2, 0), colspan=2)
    plt.subplot2grid((3, 4), (2, 2), colspan=1)
    plt.subplot2grid((3, 4), (0, 3), rowspan=3)
plt.subplot2grid(shape=(3, 4), loc=(0, 0), rowspan=2, colspan=3)
    shape-> 画布形状（可以看作画布由x*y个一样的子画布）
    loc-> 当前想要划分的起点
    rowspan-> 从起点横坐标开始，划分rowspan长度
    colspan-> 从起点纵坐标开始，划分colspan长度

plt.subplots(nrows=1, ncols=2, figsize=(8, 4), sharey='all', sharex='all')-> 同时创建画布，同时将画布分成nrows*cols个子画布
    nrows-> 分出画布的行数
    ncols-> 分出画布的列数
    figsize-> 画布大小
    sharex-> 子画布共享x轴刻度标准的模式
    sharey-> 子画布共享y轴刻度标准的模式
    *a:
        >>>subplots函数返回两个值，第一个是原画布fig，第二个是被平分的子画布实例组成的数组ax，ax[1][2](或者a[1, 2])表示第二行左数第三个子画布
    *b:
        >>>针对画布实例fig, 可以使用fig.subplots_adjust(wspace=0, hspace=0)-> 设置子画布之间的空白区域大小
        >>>    hspace-> 纵向空白大小，设置0的时候，无空白
        >>>    wsapce-> 横向空白大小，设置0的时候，无空白
    *c:
        >>>想要使得一个子画布和另一个子画布具有相同的某一坐标轴刻度，可以使用subplot获得此画布，在参数选择时使用sharex或者sharey，将值设定为另一个子画布的实例就可以了，比如：
        ax2 = plt.subplot(345, sharex=ax1)

plt.tick_params(axis='both', width=5, colors='y', length=12, labelsize=16, labelbottom=True,
                labeltop=True, labelleft=True, labelright=True, left=True, right=True, bottom=True, top=True)-> 坐标轴刻度的相关操作
    axis-> 选取操作的坐标轴
    width-> 刻度线宽
    colors-> 刻度线和刻度数字颜色
    length-> 刻度线长
    labelsize-> 刻度数字大小
    labelbottom/labeltop/labelleft/;abelright-> 是否显示底部/上方/左侧/右侧的刻度数字
    left/right/top/bottom-> 是否显示左侧/右侧/上方/底部的刻度
plt.subplots_adjust(wspace=0, hspace=0)-> 设置不同子画布之间的空白区域大小
    hspace-> 纵向空白大小，设置0的时候，无空白
    wsapce-> 横向空白大小，设置0的时候，无空白
plt.axes(arg=[0.5, 0., 0.3, 0.3], frameon=True, facecolor='w', aspect='equal')-> 坐标轴操作
    arg-> 坐标轴所在画布的[left, bottom, width, height]
    frameon-> 设置为True则显示坐标轴外框，反之
    facecolor-> 坐标轴背景颜色
    aspect-> 控制轴的纵横比。该参数可能使图像失真，即像素不是方形的
plt.axis([xmin. xmax, ymin, ymax)-> 重新定位坐标轴坐标范围
plt.setp(obj, visible=True)-> 设置
    obj-> 设置的对象(可以是子画布，可以是子画布的标签，可以是子画布的标题，普通画布线宽等等等)
    visible-> 刻度的显示或者隐藏
plt.gca()-> 获取当前画布(它返回的是一个Axes实例)
    *a:
        >>>Axes实例可以使用object.spines['direction'].set_color('color')
        >>>    direction-> 指定轴，有left/top/bottom/right四个值可以选择
        >>>    color-> 指定轴的颜色，设置为none时候，该方向坐标轴隐藏
    *b:
        >>>Axes实例可以使用object.spines['direction'].set_position(('data', 0))改变坐标轴位置
plt.pcolor([x, y], edgecolors='k', linewidths=5)-> 有助于创建带有非规则矩形网格的pseudo-color图(二维图)
    [x, y]-> 二维数组
plt.colorbar(mappable=cs)-> 颜色标尺
    mappable-> 标注对象
plt.contour(*args, cmap=mpl.cm.hot)-> 等高线
    可变参数arg-> 
    cmap-> 使用颜色映射表

plt.clabel(CS, fmt='%3.2f', colors='r', fontsize=16)-> 等值线标注
    CS-> 要标注的线条轮廓的对象，即plt.contour(*args, cmap=mpl.cm.hot)返回的实例
    fmt-> 标准数据精确值
plt.imshow(X, cmap=mpl.cm.hot)-> 展示图片
    X-> 构成图片的BGR数组
    cmap-> 使用颜色映射表,这里成为了图片显示的颜色
plt.savefig(road)-> 保存图片
    road(这里只是代号)-> 存储的路径加图片名字.格式（支持的格式请通过查看print(help(plt.savefig))）
部分函数支持的统一关键字参数：
    line(line只是代号，下同)-> 我们熟知的lw/ls/color/marker…………
    font-> 我们熟知的lfamily/size/color/weight…………
如果不希望在函数里面指定某些属性的值，比如字体大小，背景颜色，又或者统一线粗细/颜色等等等，你可以通过以下方案：
    plt.rcParams[key] = value
    mpl.rcParams[key] = value
    mpl.rc(……)
颜色的三种模式：
    Hex模式-> #RRGGBB字符串
    HTML/CSS模式-> 颜色英文名（部分可以缩写）
    Decimal模式-> (R,G,B)元组，元组的每个值都属于0~1范围
子画布实例支持的方法：
    plot/scatter/polar等等绘图函数
    set_title-> 子画布标题
    set_xlabel/set_ylabel-> 子画布坐标轴标签
    set_ylim/set_xlim-> 子画布坐标轴限定范围
    tick_params-> 相当于plt.tick_params的用法
    set_x(y)ticks(被代替的x(y)轴刻度值组成的序列)+set_x(y)ticklabels(由代替的x(Y)轴刻度值的标签组成的序列)
    >>>更多见在下面的关于<<<
    ………………………………………………………………………………
***************************************************************************************************************
*                                               >>>关于<<<
*关于Line2D：                                                                                                    
**a:                                                                                                        
*   >>>from matplotlib.lines import Line2D
*   >>>print(dir(Line2D))    
*   >>>查看实例支持的方法/属性        
*关于Axes:                                                                                                
**a:                                                                                                             
*   >>>from matplotlib.axes import Axes
*   >>>print(dir(Axes)) 
*   >>>查看实例支持的方法/属性
*关于Figure:画布对象
**a:
*   >>>from atplotlib.figure import Figure
*   >>>print(dir(Figure))                                                                                                             
***************************************************************************************************************
"""
print(MyNote)
