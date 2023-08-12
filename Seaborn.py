#https://matplotlib.org/stable/tutorials/colors/colormaps.html

import Seaborn as sns
#Scatter plots
sns.scatterplot(x= colName
                ,y= colName
                , data = df
                , hue = colName
                , palette = 
                , size = colName
                , alpha = (0,1)/transparency
                , style = colName
                ,linewidth=0
                )
plt.savefig(name.jpg)

#Distribution Plots
sns.set(style = 'darkgrid')
sns.displot(data=df
            ,x=colName
            ,bins= 
            , kde = True
 )
sns.kdeplot(
    data = 
    , x=''
    , clip = [] # like xlim
    , bw_adjust = 0.3 #Increasing will make the curve smoother.
    , shade = True #fill in shape
)

#Histogram Plots
sns.histplot(data=df
             ,x='Years'
             ,linewidth=2
             ,edgecolor='black'
             ,color='red'
             ,bins=45
             ,alpha=0.4)


#Categorical Plots
   #countplot --> visualization of groupby
   sns.countplot(
        data = 
        , x = colName
        , hue = colName
        , palette = #colScale
        
   )
   #barplot()
   sns.barplot(
          data = 
          , x = colName
          , y = colName continuous values
          , estimator = np.mean #default
          , ci = 'sd'
          , hue = 'division'
   )
   plt.legend(bbox_to_anchor = (1.05,1) #set legend outside of the box)

#Comparison Plots
    sns.boxplot(
            data =
            , y = colName
            , x = colName
            , hue = colName
            , palette = 'Set2'
            )
    sns.catplot(
    data = df
    , x= colName
    , y= colName
    , kind = 'box'
    , row  = colName
    , col = colName
)
#Seaborn Grids
#Matrix Plots --> label index, label columns and numeric values
    sns.heatmap(
            data = 
            , linewidth = 
            , annot = True #show numbers in matrix plot
            
            )
     

