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
                )
plt.savefig(name.jpg)

#Distribution Plots
sns.set(style = 'darkgrid')
sns.displot(data=df
            ,x='salary'
            ,bins= 
            , kde = True
 )
sns.kdeplot(
    data = 
    , x=''
    , clip = []
    , bw_adjust = 0.3
    , shade = True #fill in shape
)

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
    sns.box_plot(
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
     

