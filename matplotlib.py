
import matplotlib.pyplot as plt
import numpy as np
nums = np.arrange(5)

#Pyplot API
#figure is thought as canvas
#axes is a one chart that include all from lables, axis, text mark, border, 
#plt.figure() --> create new figure - canvas that seperate the chart

###SubPlot
plt.figure(figsize = )
plt.subplot(nrows=1, ncols=3, index=1, sharex = #axes , sharey = #axes) #add sharex, sharey to share same scales for different axes
plt.suptitle()#title for whole figure/canvas
--------------------------------------------
plt.figure(figsize=(2,6), dpi = )
plt.style.available #check style available
plt.style.use('fivethirtyeight')
#https://flatuicolors.com/
plt.plot(x #df.index can be automatically used for x
        ,y
        , color = ''
        , linewidth = 
        , linestyle= 'dashed'#dotted,;,:,.- 
        , marker = 
        , markersize = 
        , markerfacecolor = 
        , label = )
#-----------BAR CHART------------------
plt.bar(x #df.index can be used for x
        ,height
        , width = 0.8
        , color = 
        , bottom = 0 #other series, bar on bar
        , align = 'edge' #show 2 bar chart 
        
        )
 
#create a side by side bar by using width and edit in x with plus width
    width = 0.3
    rock = ax.bar(x = df.index, height = 'Rock', data = df, label = 'Rock %', width=width)
    jazz = ax.bar(x = df.index+width, height = 'Jazz', data = df, label = 'Jazz %', width=width)
#Create a stacked bar chart
    ax.bar(df.index, df['Country'],label = 'Country')
    ax.bar(df.index, df['Rock'],label = 'Rock', bottom = df['Country'])
 
plt.barh()        
plt.hist(data
        , bins = 
        , color = 
        , label =
        , alpha = 0.5 #blur the histogram
        , ec='black' #seperate bin with the vertical lines
        )

plt.scatter(x, y
            ,color = 
            ,marker = 
            ,label = 
            )
#------PIE chart ---------------------------------
plt.pie(x
        , labels =
        , autopct = "%1.1f%%" #show percentage for pie chart
        , shadow = True
        , explode = #tuple (0,0,0.1,0)
        
        )   
    wed, lab, val = ax.pie(x='Women',labels = 'Age',data = df, autopct = "%1.1f%%")
    ax.set_aspect('equal')
    wed[0].set_facecolor('y')
    
#--------------
plt.title("titleName", loc = "center", fontsize = )
plt.xlabel("", labelpad = 10 # space from label to axis)
plt.ylabel("", labelpad = )
plt.xticks([list of bin in row], labels = ) #ticks in the axis, how to divide the axis
plt.yticks([list of bin in col],labels = [])
plt.xlim()
plt.ylim()
plt.legend(bbox_to_anchor=(1.05, 1),shadow = True ,loc="upper right", borderaxespad=0.,title='')
plt.savefig('name.png', bbox_inches = 'tight' #for export axis, yxis)
plt.yscale("log") # LOG SCALE
plt.grid(which='both',axis='y')


###SubPlot #Object-Oriented
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(12,8))
fig.tight_layout() #fix overlap object, Adjust the padding between and around subplots.
fig.subplots_adjust() #fix overlap object
fig.suptitle()#title for whole figure/canvas


###standard procedure to create plot By Object-Oriented
fig=plt.figure(figsize = , dpi = )
axes = fig.add_axes() #ax = fig.add_subplot()
axes.plot(x,y)
axes.plot(
     x
    ,y
    ,color = #google hex color picker
    ,lw/linewidth= #linewidth
    ,ls/linestyle= ''
    ,marker = 
    ,ms/markersize = 
    ,markerfacecolor = 
    ,markeredgewidth = 
    ,markeredgecolor = 
    
    )
Axes.invert_yaxis()
axes.spines['left'].set_color('blue') #seting for left axis 
axes.spines['left'].set_linewidth(4) #seting for left axis

axes.set_xlim()
axes.set_ylim()
axes.set_xlabel()
axes.set_ylabel()
axes.set_title()
axes.legend(loc=(1.5,..)# legend out of the box)
axes.axvline(x=0, ymin=0, ymax=1, **kwargs) 
axes.axhline(y=0, xmin=0, xmax=1, **kwargs)
axes.autoscale(axis = , tight = )
axes.set(xlabel,ylabel)
axes.set_xticks(df.index+width/2)
axes.set_xticklabels(df.index) #Set the xaxis' tick labels with list of string labels.
axes.tick_params(left=False, bottom = False, labelrotation = 90)





#Time series
from matplotlib import dates
axes.xaxis.set_major_locator(dates.WeekdayLocator(byweekday = 0)) #auto set weekday
axes.xaxis.set_major_formatter(dates.DateFormatter('%a-%B-%d'))
axes.xaxis.set_minor_locator(dates.Monthlocator())
axes.xaxis.set_minor_formatter(dates.DateFormatter('\n]n%b'))
axes.xaxis.grid(True)
axes.yaxis.grid(True)
ax2 = axes.twinx()


###########Line2D
from matplotlib.lines import Line2D
from matplotlib.text import Text
from matplotlib.patches import FancyBboxPatch
from matplotlib.text import Annotation
from matplotlib.legend import Legend
from matplotlib.patches import Rectangle


np.random.seed(15)
x=np.linspace(1,40,10)
y1=x/(np.random.rand(10)*2)
y2=x/(np.random.rand(10)*3)

line1=Line2D(x,y1,label = 'line1')
line2=Line2D(x,y2,label = 'line2')

fig,ax = plt.subplots()
fig.set_size_inches(15,5)

ax.add_line(line1) 
ax.add_line(line2)
l1= ax.lines[0]
l2= ax.lines[1]

l1.set_lw(3) #set for the linewidth
l1.set_color('r')
l1.set_marker('*')
l1.set_markersize(20)
l1.set_markerfacecolor('white')
l1.set_markevery(4) #every 4 value with marker

l2.set_alpha(0.5) #set for the line
l2.set_linestyle('--')

ax.autoscale()
ax.set_title('Some lines charts')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')

fig.savefig('test2.png',dpi=350, transparent=False)

########### Text, annotation

txt1=Text(x=0.5,y=0.5,text = 'dude')
txt2=Text(x=0.2,y=0.2,text = 'another dude')
fig, ax = plt.subplots()

t1=ax._add_text(txt1)
t2=ax._add_text(txt2)

t1.set_color('r')
t1.set_size(24)
t1.set_alpha(0.8)
t1.set_family('sans-serif')
t1.set_rotation(45)
t1.set_style('italic')
t1.set_weight('bold')

t2.set_bbox(dict(facecolor = 'black', boxstyle = 'darrow, pad = 0.4', alpha = 0.7))

annot = Annotation('Due', xy =(0.5,0.2), xytext = (0.5,0.8), arrowprops=dict(width=1))
ad1=ax._add_text(annot)

##Set annotation 
    val = df['Petal length'].values
    p_min = val.min()
    p_max = val.max()
    x_min = val.argmin()
    x_max = val.argmax()
    min_annotation = ax.annotate(str(p_min), 
                             xy = (x_min, p_min), 
                             xytext=(x_min+10, p_min+2), 
                            arrowprops=dict(arrowstyle='->'))

    min_annotation.set(size=22, color='w')
    min_annotation.set_bbox(dict(facecolor='r', boxstyle='round, pad=0.3', lw=0))

    # Let's tickle the arrow little
    min_annotation.arrow_patch.set_connectionstyle('angle, angleA=-90')
    min_annotation.arrow_patch.set_lw(2)
    min_annotation.arrow_patch.set_linestyle('dashed')
    min_annotation.arrow_patch.set_color('red')
    
    max_annotation = ax.annotate(str(p_max),
                            xy=(x_max, p_max),
                            xytext=(x_max-10, p_max-2),
                            arrowprops=dict(arrowstyle='->'))
    max_annotation.set(color='w', size=22)
    max_annotation.set_bbox(dict(facecolor='green', lw=0, boxstyle='round, pad=0.3'))

    max_annotation.arrow_patch.set_connectionstyle('angle, angleA=90')
    max_annotation.arrow_patch.set_color('green')
    max_annotation.arrow_patch.set_linestyle('dashed')
    max_annotation.arrow_patch.set_lw(2)

    for p in rock.patches: #rock is a bar axes
        t = ax.annotate(str(p.get_height())+'%', (p.get_x(), p.get_height()+2))
        t.set(color='black', size=8)
        t.set_bbox(dict(facecolor='white', boxstyle='circle',lw=1, edgecolor='red'))


## Legend
legend = ax.legend()
legend.texts[1].set(color = 'r',alpha = 0.5)
legend.legendPatch.set_boxstyle('round,pad=0.5, rounding_size = 2')
legend.legendPatch.set_facecolor('#FFe0B2')
legend.set_bbox_to_anchor([0.75,0.9])

## Axis/tick
fig, ax = plt.subplots(figsize = (12,4))
ax.get_children() #get all objects
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('r')
ax.spines['left'].set(lw=2,ls='--')
x_label = ax.set_xlabel('X axis')
x_label.set_size(20)
x_label.set_fontweight('bold')
x_label.set_color('blue')
ax.tick_params(
          axis = 'x'
        , labelcolor ='red'
        , labelsize=14
        , top=False
        , bottom=True
        , labeltop=False
        , labelbottom=True
)
ax.tick_params(left=False, bottom = False) #remove tick params
ax.set_xticks([0,1,4,12]) #set xtick locator
