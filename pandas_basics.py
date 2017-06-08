import pandas as pd
print pd.__file__
data = pd.Series([0.25,0.5,0.75,1.0])
print data
print data.values
print data.index

'''Series with explicit index'''
data = pd.Series([0.25,0.5,0.75,1.0], index=['a','b','c','c'])
print data

'''Series with dictionary'''
population_dict = {'CA':1234,'TX':4566,'NY':1429}
population = pd.Series(population_dict)
print "{} {} {}".format(population,population['CA'],population['CA':'NY'])