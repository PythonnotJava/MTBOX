print(
     '---------------------------------------------- matplotlib.pyplot API Getting Started study--------------------------------------------')
MyNote = """
     *a:
         >>>The default parameters are all set by me
     *b:
         >>> Some parameters can be abbreviated
plt.figure(figsize=(9, 9), dpi=1000) -> create canvas
     figsize-> canvas size
     dpi -> pixel density
plt.plot(x, y, linestyle='-', color='green', linewidth=3, label='cos(x)', fillstyle='full', markersize=20) -> line chart
     linestyle-> image type (abbreviation is ls)
     color-> image color (the abbreviation is c, of course, the color can also be abbreviated; example: c='r'->c='red', the parameter can also be a string in the form of 0 to 1 floating point number, the larger the color darker, c='1'->c='black')
     linewidth-> image line thickness (abbreviation is lw)
     label-> image title (requires plt.legend() to display)
     fillstyle-> point filling method, left/right/full/bottom/top/none are optional
     markersize-> point size
     *a:
         The >>>plot function can create multiple plots on the same canvas, for example: plot(x1, y1, 'r--',... x2, y2, 'g--', ...) represents two Different parameter configurations of the graph line, the return value is two graph line instances
plt.scatter(x, y, color='red', label='scatter image', s=5) -> scatter plot
     s-> point size
plt.xlim(a, b) -> limit the x coordinate range
plt.ylim(a, b) -> limit the range of y coordinates
     a-> min value
     b -> max value
plt.xlabel('X Point', color='r') -> x-axis label
plt.ylabel('Y Point', color='y') -> y-axis label
plt.grid(color='red', lw=3, ls=':', alpha=0.5, axis='y') -> gridded canvas
     alpha->transparency
     axis-> grid line selection (only the y-axis is displayed here, the default is all)
plt.axhline(y=0, lw=5, ls='--', c='r')-> Draw a horizontal reference line parallel to the x-axis
plt.axvline(x=0, lw=5, ls='--', c='y')-> Draw a horizontal reference line parallel to the y-axis
plt.axvspan(xmin=-7, xmax=7, fc='r', alpha=0.5) -> Draw a reference area perpendicular to the x-axis
     xmin-> can be considered as the starting point
     xmax-> can be considered as the end point
     fc (full name is facecolor) -> area color
     alpha->transparency
The usage of plt.axhspan is the same as above
plt. annotate(
     text='It is the point by two funcs: (0, 0)',
     xy=(0, 0),
     xytext=(2.5, -1),
     fontsize=64,
     color='b',
     arrowprops=dict(arrowstyle='->',connectionstyle='arc3',color='b'
     ))-> arrow comment
     text->Note content
     xy-> point to coordinates
     xytext->starting point coordinates
     fontsize-> font size
     color -> color
     arrowprops-> Arrow properties
plt.text(x, y, s='y=f(x)', fontdict=dict(weight='bold', size=64), c='r')-> no text
     x->text x-coordinate
     y->text y coordinate
     s-> text content
plt.title(label='Using so fluently!!!', fontdict=dict(weight='bold', size=64, loc='left'))->title (multiple titles can be used outside a canvas)
     loc->header location
plt.legend(line=[line1, line2, ...], name=['name1', 'name2', ...], loc=1, bbox_to_anchor=(0.91, 0, 0.3, 1), title='This is the name of the box.',
  shadow=True, mode='expand', fancybox=True, nloc=3, fontsize=48, borderaxespad=0.3， frameon=True, framealpha=1.0) -> graph column
     *a:
         >>>The line and name here are just random parameter names (does not exist)
     line-> match the corresponding graph line according to the instance
     name-> instance matches the new name of the corresponding graph line
     loc-> position, where 1 is equivalent to 'upper right'
     bbox_to_anchor-> The percentage of the box's positioning coordinates in the canvas (left, right, top, bottom)
     title-> the title of the box
     shadow-> box border shadow effect
     nloc-> The number of columns of the legend, generally 1
     fancybox-> Whether to make the corners of the legend box rounded
     fontsize-> font size
     borderaxespad-> distance between axes and legend border
     frameon-> Whether to display the frame
     framealpha-> frame transparency (0~1)
     mode-> box border shape (expand here is to let the box expand directly to both sides of the canvas)

plt.bar(x, height, width=0.5, align='center', color=colors, tick_label=list('ABCDEFGH'), hatch='\\o', label='random simulation', bottom=0) -> Histogram (vertical histogram)
     x-> default bottom variable name
     height-> variable value
     width-> the thickness of the column
     align-> The position of the variable name at the bottom, centered by default, of course it can also start from edge->left edge
     color-> column color (can also be a list)
     tick_label-> Replace bottom variable name
     hatch-> resident style
     label-> image title (requires plt.legend() to display)
     bottom -> baseline

plt.bar(x, height, width=0.5, align='center', yerr=std_, color=colors,
error_kw=dict(elinewidth=2, ecolor='yellow', capsize=3), tick_label=['park{}'.format(s) for s in range(1, 6)])-> error bar histogram
     error_kw-> Dictionary of attributes of error bars
     yerr-> A list of error data corresponding to each group

plt.barh(y, width, height=0.5, align='center', color='0.5', tick_label=list('ABCDEFGH'), hatch='\\\o') -> bar chart (horizontal column picture)
     y-> default bottom variable name
     width-> variable value
     height-> column thickness
     align-> The position of the variable name at the bottom, centered by default, of course it can also start from edge->left edge
     color-> column color (can also be a list)
     tick_label-> Replace bottom variable name
     hatch-> resident style

plt.barh(y, width, height=bar_width, align='center', color=colors, xerr=std_err, tick_label=['error{}'.format(s) for s in range(5)])-> Error bar bar chart (similar to error bar histogram)
plt.hist(x, bins=bin_, align='mid',histtype='bar', color='r', rwidth=0.5) -> histogram
     x->variable for statistics
     bins-> The interval of the statistical variable
     align-> variable position
     history-> histogram type
     color-> histogram color
     rwidth-> the thickness of the histogram column
Stacked chart -> two bars
plt.bar(x, y, align='center', color='blue', tick_label=list('ARCADE'), label='Data 1', width=0.5, hatch='\\')
plt.bar(x, y1, align='center', color='pink', bottom=y, label='data 2', width=0.5, hatch='\\')
     The second bar is stacked on the first bar, the principle is the bottom parameter, so that the new bar is located at the value of the previous bar
Stacked bar chart -> two barh
plt.barh(y=x, width=y, height=0.7, color='blue', tick_label=list('ABCDE'), label='Data 1', hatch='\\')
plt.barh(y=x, width=y, height=0.7, color='green', left=y, label='data 2', hatch='\\')
     The principle is the same as above, except that left is used instead of bottom parameter
Side-by-side stacked chart -> two bars
plt.bar(x, y, width=0.3, tick_label=list('ABCDE'), color='r', align='center', label='data A', hatch='\\')
plt.bar(x+width, y1, width=0.3, color='b', align='center', label='data A', hatch='\\')
     x-> array form, which can be calculated, while the list cannot
     x+width-> This will be together, otherwise there will be a gap
Side by side bar chart -> two barh
plt.barh(y, width=y, height=0.3, align='center', color='red', tick_label=list('ABCDE'), label='data 1', hatch='\\')
plt.barh(y=x+height, width=y1, height=0.3, align='center', color='y', label='data 2', hatch='\\o')
     The principle is similar to the above

plt.pie(x, explode=explode, labels=labels, autopct='%3.8f%%', startangle=45, shadow=True, colors=colors,
  radius=2, pctdistance=0.5, labeldistance=0.7) -> pie chart
     x -> amount of variable
     explode-> The gap between blocks, after being assigned a value, is a split pie chart
     labels-> variable name
     colors-> The color corresponding to the pie assigned by the variable
     autopct-> the exact digit of the variable proportion
     startangle-> When the first variable starts to distribute the pie, it is equivalent to the angle of the x-axis (counterclockwise is positive)
     shadow-> Whether there is a ghosting effect
     radius-> radius
     pctdistance-> proportion relative to the distance from the origin
     labeldistance-> The variable name is equivalent to the distance from the origin
Multiple plt.pie(x, autopct='%3.2f%%', radius=0.7,
     pctdistance=0.75, colors=outer_c, textprops=dict(color='w'),
     wedgeprops=dict(width=0.3, edgecolor='w'), shadow=True, explode=expe)-> Embedded circular pie chart (the two parameters shadow and exeplode are not recommended here, because the effect picture is not good-looking)
     textprops-> percentage text configuration
     wedgeprops-> sliced pie chart configuration, where the width represents the completeness of each block (fan shape)
plt.polar(theta, r, color='yellow', lw=2, marker='o', mfc='red', ms=22, ls='--)-> polar plot (polar coordinates)
     theta-> point angle and corresponding number
     r-> distance from point to pole
     color-> the connection color of the point
     lw-> the line width of the connection
     marker-> point style
     mfc->point color
     ms->radius of the point
     ls-> line style (linestyle)
plt.scatter(x, y, s=numpy.power(10*a+20*b, 2), c=numpy.random.rand(100), cmap=mpl.cm.RdYlBu, marker='o') -> Bubble chart (scatter plot)
     x -> the value of the x-axis
     y -> the value of the y axis
     s-> scatter size
     c-> the color of the scatter mark
     cmap-> A color mapping table that maps floating-point numbers to colors
     marker-> point style
plt.stem(x, y, linefmt='--', markerfmt='*', basefmt='-.', bottom=0.) -> Swab plot: shows a bunch of variables equivalent to a common standard discrete form
     x-> The position of the cotton swab on the x-axis
     y-> cotton swab length
     linefmt-> swab style
     markerfmt-> style of cotton swab points
     basefmt-> The style of the baseline where the common standard is located
     bottom-> the baseline where the common standard is located
plt.boxplot(x, whis=whis, sym='o', widths=width, labels=labels, patch_artist=True, notch=True, vert=False, showfliers=False, meanprops=dict(color='r') ) -> Boxplot
     x-> a list (array) of each set of data
     whis-> The multiple of the interquartile interval, used to determine the range size of the data that must be included
     sym-> outlier style
     widths-> the width of the box
     labels-> the name of each set of data
     notch-> When set to True, it will make the box appear V-shaped concave
     patch_artist-> The color of each group of data boxes (when set to True, this function can be regarded as an object bplot, and use the following *a color matching)
     vert-> When set to False, a horizontal boxplot is displayed
     When showfliers->False, do not show outliers
     showmeans-> Whether to display the mean in the form of points
     meanprops-> configuration of mean points
     *a:
         >>>for patch, color in zip(bplot['boxes'], colors):
         >>> patch.set_facecolor(color)

plt.errorbar(x, y, fmt='ro--', yerr=0.2, xerr=0.02, ecolor='y', elinewidth=4, ms=5, mfc='c', mec='r', capthick=1, capsize=2)-> error bar graph
     fmt-> style, the default value here means that the blue o-shaped points are connected by dotted lines
     yerr -> y-axis error
     xerr -> x-axis error
     ecolor-> error bar color
     elinewidth-> error bar thickness
     ms -> data point size
     mfc-> data point color
     mec-> data point edge color
     capthick-> error bar boundary bar thickness
     capsize-> error bar boundary bar size

plt.yticks(list(a1), list('ABCDE'), rotation=-90)-> y-axis variable name positioning and variable name, the variable name is equivalent to the function of the tick_label parameter, and rotation is the rotation angle of the title
plt.xticks(list(a2),list('ABCDE'), rotation=-90)-> x-axis variable name positioning and variable name, the variable name is equivalent to the role of the tick_label parameter, rotation is the rotation angle of the title
     list(a1)-> axis variable name positioning (that is, the list of values on the original axis)
     list('ABCDE')-> replace the original value on the axis with xxx
plt.stackplot(x, y, y1, ..., labels=['func(x)', 'func(a)', 'func(t)'], colors=['red', 'green', ' gray']) -> stacked line chart
     labels-> label
     colors-> the color of each polyline
plt.broken_barh(xranges=[(30, 100), (180, 50), (260, 70)], yrange=(20, 8), facecolor=['red', 'red', 'gray']) -> Interrupted bar chart
     xranges-> A list consisting of each part, for example: [(2, 50), (30, 10)] means that there are two parts, the first one starts from 2 and extends by 50 distances
     yrange-> width, for example: (20, 8) means starting from 20, width 8
     facecolor (or fc or facecolors) -> can be a single color, or a sequence of colors, representing the color of each part
plt.step(x, y, color='y', where='mid', lw=5, ls='--') -> step diagram
     where-> point determines the image according to the selection of parameters
plt.hist(x=[scoresT, scoresT1], bins, color=['y', 'b'], rwidth=1, histtype='bar', hatch='\\o', stacked=True)-> Stacked (tied) histogram
     x-> stacked data list
     bins-> classification interval
     colors-> the color of each part
     stacked-> stacked: True means stacked graph, False means juxtaposed graph
     histtype->histogram type, when the value is stepfilled, it is a stepped histogram
plt.table(cellText=[['class{}'.format(ti) for ti in range(1, 6)], stu],
           cellLoc='center',
           colWidths=[0.3] * 5,
           colLabels=labels,
           colColours=colors,
           rowLabels=['class', 'number of students'],
           rowLoc='left',
           loc='bottom')-> table
     cellText-> a list of lists consisting of the values corresponding to each row of labels
     cellLoc-> the position of the text of the column label in the cell
     colWidth-> cell width
     colLabel-> column label
     colColour-> column label cell color
     rowLabel-> list of row labels
     rowLoc-> row label text position in the cell
     loc-> The overall positioning of the table

plt.subplot(nrows, ncols, index, polar=True)-> subplot function (equivalent to dividing multiple sub-canvases on one canvas)
     *a:
         >>>subplot parameters: nrows, ncols, index are just codes, and they need to be replaced by numbers when inputting. Written in the form of nrows=5, an error will be reported
plt.subplots(nrows=1, ncols=2, figsize=(8, 4), sharey='all', sharex='all')-> Create a canvas at the same time, and divide the canvas into nrows*cols sub-canvas
     nrows-> the number of rows to split the canvas
     ncols-> the number of columns to separate the canvas
     figsize-> canvas size
     sharex-> sub-canvas shared x-axis scale standard mode
     sharey-> sub-canvas shared y-axis scale standard mode
     *a:
         The >>>subplots function returns two values, the first is the original canvas fig, and the second is the array ax composed of equally divided sub-canvas instances, represented by ax[1][2] (or a[1, 2]) The third sub-canvas from the left in the second row
     *b:
         >>>For the canvas instance fig, you can use fig.subplots_adjust(wspace=0, hspace=0)-> to set the size of the blank space between the subplots
         >>> hspace-> Vertical space size, when set to 0, no space
         >>> wsapce-> Horizontal blank size, when set to 0, no blank
     *c:
         >>>If you want to make one sub-canvas and another sub-canvas have the same axis scale, you can use subplot to get this canvas, use sharex or sharey when selecting parameters, and set the value as an instance of another sub-canvas Just do it, for example:
         ax2 = plt.subplot(345, sharex=ax1)

plt.tick_params(axis='both', width=5, colors='y', length=12, labelsize=16, labelbottom=True,
                 labeltop=True, labelleft=True, labelright=True, left=True, right=True, bottom=True, top=True)-> operations related to axis scale
     axis-> select the coordinate axis of the operation
     width-> tick width
     colors-> tick mark and scale number color
     length-> tick length
     labelsize-> scale number size
     labelbottom/labeltop/labelleft/;abelright-> Whether to display the scale numbers at the bottom/top/left/right
     left/right/top/bottom-> Whether to display the left/right/top/bottom scale
plt.subplots_adjust(wspace=0, hspace=0)-> Set the size of the blank space between different subplots
     hspace-> vertical blank size, when set to 0, no blank
     wsapce-> Horizontal blank size, when set to 0, no blank
plt.axes(arg=[0.5, 0., 0.3, 0.3], frameon=True, facecolor='w', aspect='equal')-> coordinate axis operation
     arg-> [left, bottom, width, height] of the canvas where the coordinate axis is located
     frameon-> Set it to True to display the outer frame of the coordinate axis, and vice versa
     facecolor-> axis background color
     aspect-> controls the aspect ratio of the axes. This parameter may distort the image, i.e. the pixels are not square
plt.axis([xmin.xmax, ymin, ymax)-> Relocate the axis coordinate range
plt.setp(obj, visible=True) -> set
     obj-> set object (can be a sub-canvas, can be a label of a sub-canvas, can be a title of a sub-canvas, the line width of a normal canvas, etc.)
     visible-> display or hide the scale
plt.gca()-> Get the current canvas (it returns an Axes instance)
     *a:
         >>>Axes instance can use object.spines['direction'].set_color('color')
         >>> direction-> specify the axis, there are four values left/top/bottom/right to choose from
         >>> color-> Specifies the color of the axis. When it is set to none, the coordinate axis of this direction is hidden
     *b:
         >>>Axes instance can use object.spines['direction'].set_position(('data', 0)) to change the axis position
plt.pcolor([x, y], edgecolors='k', linewidths=5) -> Helps create pseudo-color plots with irregular rectangular grids (two-dimensional plots)
     [x, y] -> two-dimensional array
plt.colorbar(mappable=cs)-> color scale
     mappable-> annotation object
plt.contour(*args, cmap=mpl.cm.hot) -> contour line
     variadic arg ->
     cmap-> use color map

plt.clabel(CS, fmt='%3.2f', colors='r', fontsize=16)-> isoline label
     CS-> The object of the outline of the line to be marked, that is, the instance returned by plt.contour(*args, cmap=mpl.cm.hot)
     fmt-> standard data exact value
plt.imshow(X, cmap=mpl.cm.hot)-> display image
     X-> The BGR array that makes up the picture
     cmap-> Use the color mapping table, here becomes the color displayed in the picture
plt.savefig(road) -> save the picture
     road (here is just the code name) -> storage path plus picture name. Format (for supported formats, please check print(help(plt.savefig)))
Unified keyword arguments supported by some functions:
     line (line is just a code name, the same below) -> We are familiar with lw/ls/color/marker…………
     font-> The lfamily/size/color/weight we are familiar with…………
If you don't want to specify the value of certain properties in the function, such as font size, background color, or uniform line thickness/color, etc., you can use the following solutions:
     plt.rcParams[key] = value
     mpl.rcParams[key] = value
     mpl.rc(...)
Three modes of color:
     Hex mode -> #RRGGBB string
     HTML/CSS mode -> English name of color (some can be abbreviated)
     Decimal mode -> (R, G, B) tuple, each value of the tuple belongs to the range of 0~1
Methods supported by sub-canvas instances:
     plot/scatter/polar and other drawing functions
     set_title-> sub-canvas title
     set_xlabel/set_ylabel-> sub-canvas axis label
     set_ylim/set_xlim-> sub-canvas coordinate axis limit range
     tick_params-> equivalent to the usage of plt.tick_params
     set_x(y)ticks (a sequence of replaced x(y) axis scale values)+set_x(y)ticklabels (a sequence of replaced x(y) axis scale values)
     >>>See below for more about<<<
     ………………………………………………………………………
***************************************************** ***************************************************** ************
* >>>About<<<
*About Line2D:
**a:
* >>>from matplotlib.lines import Line2D
* >>>print(dir(Line2D))
* >>>View the methods/properties supported by the instance
*About Axes:
**a:
* >>>from matplotlib.axes import Axes
* >>>print(dir(Axes))
* >>>View the methods/properties supported by the instance
*About Figure: canvas object
**a:
* >>>from atplotlib.figure import Figure
* >>>print(dir(Figure))
***************************************************** ***************************************************** ************
"""
print(MyNote)