# Import the packages
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use('ggplot')

matplotlib.rcParams['figure.figsize'] = (12, 8)

pd.options.mode.chained_assignment = None

# Read the data
df = pd.read_csv('movies.csv')

# Check for missing data
# Loop through the data
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing * 100)))

# Data Types for our columns
print(df.dtypes)

# Check for Outliers
df.boxplot(column=['gross'])

df.drop_duplicates()

# Order the Data
df.sort_values(by=['gross'], inplace=False, ascending=False)

sns.regplot(x="gross", y="budget", data=df)
sns.regplot(x="score", y="gross", data=df)

# Correlation Matrix between all numeric columns
df.corr(method='pearson')
df.corr(method='kendall')
df.corr(method='spearman')

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)

plt.title("Correlation matrix for Numeric Features")
plt.xlabel("Movie features")
plt.ylabel("Movie features")
plt.show()

# Using factorize - this assigns a random numeric value for each unique categorical value
df.apply(lambda x: x.factorize()[0]).corr(method='pearson')

correlation_matrix = df.apply(lambda x: x.factorize()[0]).corr(method='pearson')
sns.heatmap(correlation_matrix, annot=True)

plt.title("Correlation matrix for Movies")
plt.xlabel("Movie features")
plt.ylabel("Movie features")
plt.show()

correlation_mat = df.apply(lambda x: x.factorize()[0]).corr()
corr_pairs = correlation_mat.unstack()
print(corr_pairs)

sorted_pairs = corr_pairs.sort_values(kind="quicksort")
print(sorted_pairs)

# Taking a look at the ones that have a high correlation (> 0.5)
strong_pairs = sorted_pairs[abs(sorted_pairs) > 0.5]
print(strong_pairs)

# Looking at the top 15 companies by gross revenue
CompanyGrossSum = df.groupby('company')[["gross"]].sum()
CompanyGrossSumSorted = CompanyGrossSum.sort_values('gross', ascending=False)[:15]
CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64')

df['Year'] = df['released'].astype(str).str[:4]

df.groupby(['company', 'year'])[["gross"]].sum()

CompanyGrossSum = df.groupby(['company', 'year'])[["gross"]].sum()
CompanyGrossSumSorted = CompanyGrossSum.sort_values(['gross', 'company', 'year'], ascending=False)[:15]
CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64')

CompanyGrossSum = df.groupby(['company'])[["gross"]].sum()
CompanyGrossSumSorted = CompanyGrossSum.sort_values(['gross', 'company'], ascending=False)[:15]
CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64')

plt.scatter(x=df['budget'], y=df['gross'], alpha=0.5)
plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Budget for Film')
plt.show()

df_numerized = df

for col_name in df_numerized.columns:
    if df_numerized[col_name].dtype == 'object':
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes

df_numerized.corr(method='pearson')
correlation_matrix = df_numerized.corr(method='pearson')
sns.heatmap(correlation_matrix, annot=True)

plt.title("Correlation matrix for Movies")
plt.xlabel("Movie features")
plt.ylabel("Movie features")
plt.show()

for col_name in df.columns:
    if df[col_name].dtype == 'object':
        df[col_name] = df[col_name].astype('category')
        df[col_name] = df[col_name].cat.codes

df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)

sns.swarmplot(x="rating", y="gross", data=df)
sns.stripplot(x="rating", y="gross", data=df)
