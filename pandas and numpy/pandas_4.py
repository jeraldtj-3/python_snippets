import pandas as pd  
import seaborn as sns 

import numpy as np 
df = sns.load_dataset('titanic' ) 


df.info();

# series 
df['survived']

# dataframe 
# in reverse direction 
df[['survived']][10:100][::-1]


# jump of 2 
list(df['age'][::2])

# statistical information 
df.describe()

# filter out the categorical column 
print(df.dtypes)
# finding the object types 
df.dtypes[df.dtypes == 'object'] 

# getting the data
object_columns = df.dtypes[df.dtypes == 'object'].index
categorical_df = df[object_columns]


print(categorical_df.describe())

# getting columns 
df.columns

# getitng two colums 
df[['sex', 'who']]


# findng boolean for null vlaues 
df['age'].isnull() 

# rows where age is null 
age_null_indices = np.where(df['age'].isnull() == True)   # row indexes 

# using iloc : integer loc 
df.iloc[age_null_indices]

# checking 
df.iloc[1]  # a series object 

# two rows 
df.iloc[[1,2]] 

# person name who has paid highest amount 
df[df['fare']== max(df.fare)] 

# persons having age 24 
df[df['age'] == 24]['embark_town']

df[df['deck'].isna()]['age']

# multiple conditions 
df[(df['survived'] == 0)  & (df['sex'] == 'male') ]


df['new_col'] = 'thomas'



# converting list into series 
l = [23,4,2,4] 
se = pd.Series(l)
print(se)

# dictionary to series 
d = {'name':'thomas', 'age': 35, 'marks' : 24}
pd.Series(d)

# dictioary to dataframe 
pd.DataFrame(d, index = [0])

# numpy array to dataframe 
arr = np.random.randn(3,4)
pd.DataFrame(arr)

# Giving indexes 
my_series = pd.Series(np.array([1,2,32]), index = ['a','b','c'])
# using loc 
my_series.loc[['a','c']]


# iloc takes the default indices 

arr = np.random.randint(3,6,(4,5))
newdf = pd.DataFrame(arr, index = ['a','b','c','d'], columns = ['f1','f2','f3','f4','f5'])

# extracting subset 
newdf.loc['c':,['f3','f4']]

# adding new column 
newdf['f1+f2'] = newdf['f1'] + newdf['f2']

# droping column  ( axis = 0 meand row)
newdf.drop('f1', axis = 1)

newdf.drop('f2', axis = 1, inplace = True)


# dropiing rows 
newdf.drop('c')

newdf.drop('d', inplace = True)



########################3333
np.random.seed(23) 
arr = np.random.randn(4,5)
newdf = pd.DataFrame(arr, index = ['a','b','c','d'], columns = ['f1','f2','f3','f4','f5'])

# assignmet
negatives = newdf.values[newdf.values<0]

for col in newdf.columns:
    for ind in newdf.index:
        print(newdf[ind][col])
            

##########################################################################################
###########    DROPPING AND THRESHOLD  ####################


d = {'key1':[1,2,3,4,np.nan], "key2":['thomas','steve',32,3,2], 'key3':[np.nan, np.nan, np.nan, 3,2]}
df = pd.DataFrame(d)

# droping the nan vlaued rows 
df.dropna()   # droping the rows 
df.dropna(axis = 1) # droping the column 

# over rows 
df.dropna(thresh=2)
df.dropna(thresh = 3)

df.dropna(axis = 1, thresh = 3)
df.dropna(axis = 1, thresh = 4)
df.dropna(axis = 1 , thresh = 5)

# filling na values 
df.fillna('missing')

df.fillna(value  = df['key1'].mean())


# custom imputation code 
######################### group by and multi index 
d1 = {
      'name ': ['thomaskutty', 'sudh', 'vishal', 'umag', 'stella'], 
      "mail_id":['thomas@gmail.com', 'sugh23@gmail.com', 'vishal#@gmail.com', 'umag234@gmail.com', 'stellathoma@gmail.com'],
      'salary': [100, 200,300, 500, 200]
      
      }
df1  = pd.DataFrame(d1)

df1.groupby('mail_id').mean()

n = df1.groupby('mail_id').mean().describe()
n

######### transpose function  and concatenating the dataframes 
arr1 = np.random.randn(3,4)
arr2 = np.random.randn(3,4)
arr3 = np.random.randn(3,4)


df1 = pd.DataFrame(arr1, columns = ['a', 'b', 'c','d'], index = [0,1,2])
df2 = pd.DataFrame(arr2, columns = ['a', 'b', 'c','d'], index = [0,1,2])
df3 = pd.DataFrame(arr3, columns = ['a', 'b', 'c','d'], index = [0,1,2])


####### stacking and horizontal concatenation 

df4 = pd.concat([df1, df2,df3])   # vertical concatenation : row wise concatenation 
df5 = pd.concat([df1,df2,df3], axis = 1)   # horizontal concatenation  : column wise 

# gives all the records which have index label 0 
df4.loc[0]

# similarly for columns 
df5['a']

df5.iloc[:,5]

##################### merge operation 

df1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
df2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})



pd.merge(df1,df2, on  = ['key1','key2']) 


#####################   joins #####################
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

df2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

df1.join(df2)

# apply functions / 
# interview questions 

# 
















