# dataframe
import numpy
import pandas
myarray = numpy.array([[1, 2, 3, 'test'], [4, 5, 6, 'test'], ['test', 'test', 'test', 'test']])
rownames = ['a', 'b', 'test']
colnames = ['one', 'two', 'three', 'test']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)