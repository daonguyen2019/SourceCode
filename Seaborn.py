#https://matplotlib.org/stable/tutorials/colors/colormaps.html
import Seaborn as sns
sns.set_theme() #get default theme
sns.set(style = 'darkgrid')
sns.axes_style() #return all style available
sns.set_style()
sns.despine() #default remove top and right spine, sns.despine(bottom = True)
sns.set_palette()
sns.color_palette("blues)

1.relplot (relational)
    - scatterplot
    -lineplot
            #REL PLOTS
            sns.relplot(data = df
                        , x = colName
                        , y = colName
                        , kind = 'scatter'
                        , hue = colName
                        , col = colName #--> break into seperate charts into columns
                        , row = colName #--> break into seperate charts into rows
                        , height = 2 #height of each figure
                        , aspect = 1 #width of each figure = aspect * height
            )                  
2.displot (distributions)
    -histplot
    -kdeplot
    -ecdfplot
    -rugplot
            #DIST PLOTS   
            sns.displot(
                data = 
                , kind = 'hist'
                , x = colName
                , hue = colName
                , col = colName #split chart to different column
                , row = colName #split chart to different rows
                , height =  #control size
                , aspect =  #control size    
            )    
3.catplot (categorical)
    -stripplot
    -swarmplot
    -boxplot
    -violinplot
    -pointplot
    -barplot
                #CAT PLOTS
                sns.catplot(
                    data = df
                    , kind = 'box'
                    , x= colName
                    , y= colName
                    , row  = colName
                    , col = colName
                )
#-----------------------------------------------------------------------
#SCATTER PLOTS

sns.scatterplot(data = df
                ,x= colName
                ,y= colName
                , hue = colName
                , style = colName #style and hue can be same column
                , size = colName
                , palette = 
                , alpha = (0,1)/transparency
                ,linewidth=0
                )
#LINE PLOTS
sns.lineplot(data = df  #default take mean 
            , x = colName
            , y = 'colName
            , estimator = 'mean' #mean is default
            , hue = colName
            , style = colName
            , ci=None #get rid of confident interval
            )

#HISTOGRAM PLOTS
sns.histplot(data=df
             ,x=colName
             , hue = colName
             , multiple = 'stack' #default, 'dodge': size by size, 
             , bins=number
             , kde = True #
             ,linewidth=2
             ,edgecolor='black'
             ,color='red'
             ,alpha=0.4
             )

#KDE PLOTS             
sns.kdeplot(
    data = 
    , x=colName
    , y = colName
    , clip = [] # like xlim
    , bw_adjust = 0.3 #Increasing will make the curve smoother.
    , shade = True #fill in shape
)
#CATEGORICAL PLOTS
#COUNTPLOT --> visualization of groupby
sns.countplot(
        data = 
        , x = colName
        , hue = colName
        , palette = #colScale
   )
#BOX PLOTS - Comparison Plots
sns.boxplot(
            data =
            , y = colName
            , x = colName
            , hue = colName
            , palette = 'Set2'
)   
#BAR PLOTS
sns.barplot(
          data = 
          , x = colName
          , y = colName continuous values
          , estimator = np.mean #default
          , ci = 'sd'
          , hue = 'division'
)

#Seaborn Grids
#Matrix Plots --> label index, label columns and numeric values
    sns.heatmap(
            data = 
            , linewidth = 
            , annot = True #show numbers in matrix plot
            
            )
     

plt.savefig(name.jpg)
plt.legend(bbox_to_anchor = (1.05,1) #set legend outside of the box)