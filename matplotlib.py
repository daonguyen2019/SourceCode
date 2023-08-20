import matplotlib.pyplot as plt
import numpy as np
nums = np.arrange(5)

#plot method has two option
    #Pyplot API
        plt.plot()
    #Object-Oriented
     
plt.figure(figsize=(2,6), dpi = )
plt.style.available #check style available
plt.style.use('fivethirtyeight')
#https://flatuicolors.com/
plt.plot(nums,nums**3, color = '', linewidth = 
         , linestyle= , marker = , markersize = 
          , markerfacecolor = , label = )
plt.title("titleName", loc = )
plt.xlabel("", labelpad = )
plt.ylabel("", labelpad = )
plt.xticks([list of bin in row])
plt.yticks([list of bin in col],labels = [])
plt.xlim()
plt.ylim()
plt.legend(bbox_to_anchor=(1.05, 1)
           , loc=2
           , borderaxespad=0.
           ,title='FLAG_OWN_REALTY'
          )
plt.hist(data, label = , alpha = )
####-----------------------------------------------
# LOG SCALE
plt.yscale("log")
plt.grid(which='both',axis='y')


###standard procedure to create plot 
        #Object-Oriented
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
axes.spines['left'].set_color('blue') #seting for left axis 
axes.spines['left'].set_linewidth(4) #seting for left axis

axes.set_xlim()
axes.set_ylim()
axes.set_xlabel()
axes.set_ylabel()
axes.set_title()
    fig.subtitle()
axes.legend(loc=(1.5,..)# legend out of the box)
axes.axvline(x=0, ymin=0, ymax=1, **kwargs) 
axes.axhline(y=0, xmin=0, xmax=1, **kwargs)

ax2 = axes.twinx()


###SubPlot
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(12,8))


fig.tight_layout() #fix overlap object, Adjust the padding between and around subplots.
fig.subplots_adjust() #fix overlap object
fig.suptitle()
plt.savefig('name.png', bbox_inches = 'tight' #for export axis, yxis)
