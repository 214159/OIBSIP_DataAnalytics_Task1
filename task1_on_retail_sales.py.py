import pandas as pd
df=pd.read_csv(r"C:\Users\priya\Downloads\retail_sales_dataset.csv",index_col="Date") #load dataset
print(df.head()) #show first 5 rows
print(df.isnull().sum()) #checking null data
#descriptive statistcs
print("THE DESCRIPTIVE STATISTICS:")
print(df.describe())
print("The Mode value: ")
print(df.mode().iloc[0]) #mode value for 1st row
df.to_csv("New_sales_dataset.csv")
#top 10 Customer with Most Spend
Customer_Spend=df.groupby("Customer ID")["Total Amount"].sum()
print(Customer_Spend)
Top_customer=Customer_Spend.nlargest(10)
print(Top_customer)


