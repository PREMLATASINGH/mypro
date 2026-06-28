import numpy as np
import pandas as pd
data={
    'student':['raja','arun','rani','ravi'],
    'marks':[80,89,79,70]


}
df=pd.DataFrame(data)
print(df)
print(df.info())
print(df.describe())
print(df.columns)
print(df.head(2))
print(df.sort_values(by='marks',ascending=False))
print(df.sort_values(by='marks',ascending=True))
print(df.sort_values(by='student',ascending=False))
print(df.sort_values(by='student',ascending=True))