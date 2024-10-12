#general
#--------------Set------------------
set().difference() #dfference of 2 set


 

#=============================
string.replace(oldvalue, newvalue, count)
list.reverse() #reverse the order




#=============Useful library=====================
###WordCloud
from wordcloud import WordCloud
title = df['title'].dropna()
title_corpus = ' '.join(title)
title_wordcloud = WordCloud(background_color='white', height=2000, width=4000, max_words= 200).generate(title_corpus)
plt.figure(figsize=(16,8))
plt.imshow(title_wordcloud, interpolation= "bilinear")
plt.axis('off')
plt.show()
#-------------------














