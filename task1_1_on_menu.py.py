import pandas as pd
df=pd.read_csv(r"C:\Users\priya\Downloads\menu.csv") #load dataset
print(df.head()) #show first 5 rows
print(df.isnull().sum()) #checking null data
#descriptive statistcs
print("THE DESCRIPTIVE STATISTICS:")
print(df.describe())
print("The Mode value: ")
print(df.mode().iloc[0]) #mode value for row
df.to_csv("New_menu_dataset.csv")

