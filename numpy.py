import numpy as np #numerical python
pip install numpy --upgrade
np.set_printoptions(suppress = True) #apply to all workbook


arr = np.array([list1],[list2])
arr.shape #Return the shape of an array.

arr[num] #return row of array
arr[num][col] = arr[row,col] #return value in the matrix
arr[:,col] #: through all rows
arr[-1] #return the last row
arr+2 # every of arr plus 2

arr[1] #--> return 1 row
arr[1:] #--> retiurn 1 row but in a matrix type, pay attention to the number of square backets
arr[start:end:step,start:end:step]
variable_name.squeeze() = np.squeeze(variable_name) #used to remove dimensions of size 1 from the input array 'a'
 
np.zeros(10) #create an array of 10 zeros
np.ones(10) #create an array of 10 ones
np.full(shape=(2,3),fill_value = '')
np.zeros_like(arrA) #--> rerurn new array with the same set

np.arange(10,51,2) #Create an array of all the even integers from 10 to 50
np.arrage('2018-06-01','2018-06-23',7,dtype = 'datetime64[D]') #create an array of datetime
np.arange(0,9).reshape(3,3) #create a matrix
    #np.eye(3)
np.arange(...,dtype = 'datetime64[Y]')
np.linspace(0,1,20) #Create an array of 20 linearly spaced points between 0 and 1
np.array_equal() #True if two arrays have the same shape and elements, False otherwise.

np.random.rand() #generate a random number between 0 and 1
np.random.randn(25) #generate an array of 25 random numbers sampled from a standard normal distribution

from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

array_RG = gen(pcg(seedNumber)) # The seed only lasts for a single method before it gets reset
array_RG.random()
array_RG.integers(10)
array_RG.normal()
array_RG.poisson(size = 10, lam = 15)
array_RG.binomial(n = 100, p = 0.7, size = (5,10))


np.mean(matrixA)
np.mean(matrixA, axis = 0/1) #avg by column/row (=1)
np.average() #flexible with weighted 
np.var()
np.std()
np.cov()
np.corrcoef()
np.histogram(matrixA,bins=, range = (1,7))  

#NaN equivalents
np.nanmean()


np.median()
np.min() #return min
np.minimum(arrA[0], arrA[1]) #return Element-wise minimum of array elements.
np.ptp(arrA, axis = ) #ptp = peak to peak, Range of values (maximum - minimum) along an axis.
np.percentile(sample, [75,25], interpolation = 'midpoint/higher/lower')
np.quantile(arrA,0.7)
np.count_nonzero()
np.isnan().sum() #-->return number of NaN: Not a nunber
np.reshape() #flattened array to the matrix, not a transitioned matrix
np.transpose()
np.delete(array, obj=0/1..., axis = ) #Delete both rows & column
np.sort()  #arr.sort() --> it is inplace
np.argsort() #return positions
np.where(condition, value1, value2)
    #data['cabin_null'] = np.where(data['cabin'].isnull(), 1, 0)#flag missing value
np.argwhere() #Find the indices of array elements that are non-zero, grouped by element.
np.random.shuffle(array) #shuffles the array along the first axis of a multi-dimensional array
    #from numpy.random import shuffle

#Casting
arrA.astype(dtype = np.int32/np.str/np.float32) #string --> float --> integer

#Stripping : remove specific parts of string
np.chararray.strip(array, 'string to removed')

#Stacking: placing multiple objects on top of one another to create a bigger(larger) object
np.stack(array1, array2, axis = )
np.vstack  #vertical stack
np.hstack #horizontal stack
np.dstack #depth stack

#Concatenate
np.concatenate(Array1, Array2, axis = )

#Unique
np.unique()
np.unique(Array, return_counts = True)
 
 




1 in range(1,16) # return True






