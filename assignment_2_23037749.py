# %%
import pandas as pd

# %%
from tqdm.notebook import tqdm

# %%

df = pd.read_csv('D:\\uberr.csv', sep=',') 

df.head()

# %%
df = df.drop(df.index[-1])

# %%
#Function 
def convert_column_to_datetime(df, column_name):
    """
    Convert a column of date strings in a DataFrame to datetime objects.

    Args:
    - df (DataFrame): The input DataFrame.
    - column_name (str): The name of the column to convert.

    Returns:
    - DataFrame: The DataFrame with the converted datetime objects.
    """
    df[column_name] = pd.to_datetime(df[column_name])
    return df

df = convert_column_to_datetime(df, 'START_DATE*')
print(df['START_DATE*'])


# %%

# Create a histogram for the 'CATEGORY*' column
plt.figure(figsize=(10, 6))
df['CATEGORY*'].value_counts().plot(kind='bar', color='skyblue')

plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Histogram of Category')
plt.xticks(rotation=45)

plt.show()

# %%
df.isnull().sum()

# %%
df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors='coerce')
plt.scatter(df['START_DATE*'], df['MILES*'])
plt.xlabel('Start Date*')
plt.ylabel('Miles*')
plt.title('Start Date vs Distance Scatterplot')
plt.show()


# %%
#Describe for Miles column
df['MILES*'].describe()

# %%
import matplotlib.pyplot as plt
df = df[:-1]
trip_distances = df['MILES*']
plt.figure(figsize=(8, 6))  # Set the figure size

# Custom bins for better visualization
bins = [0, 5, 10, 15, 20]

plt.boxplot(trip_distances, widths=0.5)  # Set the width of the boxes
plt.xticks([1], ['Trip Distance (Miles)'])
plt.title('Box Plot of Trip Distances')
plt.ylabel('Miles')
plt.show()


