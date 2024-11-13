import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# data preparation and understanding
df = pd.read_csv("housing.csv")
print(df.head())
print(df.info())
print(df.describe())

# Visual inspection of missing values
plt.figure()
sns.heatmap(df.isnull())
plt.title('Missing Values Heatmap')
plt.show()

# Visual inspection of Outlier Detection(each col)
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure()
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot of {column}')
    plt.show()

# Distribution using his-plot

plt.figure()
sns.histplot(df)
plt.title("Distribution of Boston Pricing")
plt.ylim(0, 20)
plt.show()

# Distribution using his-plot
plt.figure()
sns.countplot(df)
plt.title("Count plot of Boston Pricing")
plt.show()

# Correlation Analysis
plt.figure()
corr_matrix=df.corr()
sns.heatmap(corr_matrix,annot=True)
plt.show()

# Investigate Trend
plt.figure()
sns.scatterplot(data=df)
plt.title("Scatter plot of Boston Pricing")
plt.show()

plt.figure()
sns.boxplot(data=df)
plt.title("Box plot of Boston Pricing")
plt.show()
