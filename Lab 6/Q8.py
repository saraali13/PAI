import pandas as pd

#CSV files were submittd on GCR
Product_df=pd.read_csv("products.csv")
Order_df=pd.read_csv("orders.csv")

print("Rows of Product Df:\n",Product_df.head(5))
print("\n",Product_df.tail(10))

print("Rows of Order Df:\n",Order_df.head(5))
print("\n",Order_df.tail(10))


merged_df=pd.merge(Order_df,Product_df,on="ProductID")
merged_df["Revenue"]=merged_df["Quantity"]*merged_df["Price"]
revenue=merged_df["Revenue"].sum()
print(f"Total Revenue: {revenue}\n")


sales=merged_df.groupby("ProductName")["Quantity"].sum()
best_5_sales=sales.nlargest(5)
low_5_sales=sales.nsmallest(5)
print("Top 5 best selling products: \n",best_5_sales)
print("Top 5 lowest selling products: \n",low_5_sales)

best_selling = Product_df[Product_df["ProductName"].isin(best_5_sales.index)]["Category"]
most_common_category = best_selling.mode().values[0]
print("Most Common Category Among Best-Selling Products: ", most_common_category)


average_price = Product_df.groupby("Category")["Price"].mean()
print("\nAverage Price by Category:\n", average_price)


merged_df["Order Date"]= pd.to_datetime(merged_df["Order Date"])
merged_df["Day"]=merged_df["Order Date"].dt.day
merged_df["Month"]=merged_df["Order Date"].dt.month
merged_df["Year"]=merged_df["Order Date"].dt.year

revenue_day = merged_df.groupby("Day")["Revenue"].sum()
revenue_month = merged_df.groupby("Month")["Revenue"].sum()
revenue_year = merged_df.groupby("Year")["Revenue"].sum()

best_day = revenue_day.idxmax()
best_month = revenue_month.idxmax()
best_year = revenue_year.idxmax()

print(f"Best Day for Revenue: {best_day}")
print(f"Best Month for Revenue: {best_month}")
print(f"Best Year for Revenue: {best_year}")


monthly_revenue = merged_df.groupby("Month")["Revenue"].sum().reset_index()
monthly_revenue_df = pd.DataFrame(monthly_revenue, columns=["Month", "Revenue"])
print("Monthly Revenue DataFrame:\n", monthly_revenue_df)


print("Null values in Products DataFrame:\n", Product_df.isnull().sum())
print("Null values in Orders DataFrame:\n", Order_df.isnull().sum())
