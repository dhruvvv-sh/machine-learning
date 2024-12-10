import pandas as pd
dataset = {
    'cals' : ["data1","data2","data3"],
    'duration': [50, 40, 45]
}
s = {
    'calls' : ["person1","person2","person3"],
    'duration' : [30,40,50]
}
df = pd.DataFrame(s)
df1 = pd.DataFrame(dataset,index=["day1","day2","day3"])
print(df1)
print(df.loc[0])


