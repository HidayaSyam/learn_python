
#%% ===== import ======
import pandas as pd
import matplotlib.pyplot as plt

# %% #==== Basic Data Operations (pandas)====
# %% #_ region[green]
# * from a csv
# pandas is a vital package that allows you to work with data in row col format. Similar to excel...ish.

# be sure to paste in the correct file path to your csv
file_name="OLYMPICS_athlete_events"
data_df=pd.read_csv(f"{file_name}.csv")

# %% #* usefull pandas functions
data_df.head(15) # it will return the first 15 rows
#%%
data_df.tail(15) # it will return the last 15 rows
#%%
data_df.describe() 
#%% 
len(data_df)
#%%
list(data_df) # list all the columns header
# %% #* drop duplicates 
# remove any duplicates person have the same name in the same team,event, and Games
# inplace True it means update the oraginal data frame so no need to  
# data_df =data_df.drop_duplicates .. it will update the actual dataframe
data_df.drop_duplicates(subset=['Name', 'Team', 'Event', 'Games'], inplace=True)

# %% #* drop nulls (1st Attempt from memory) THIS WILL ERROR
# it will cause an error because we have to pass an array for the subset
cleaned_df = data_df.dropna(subset='Medal')
# %% #* drop nulls (after googling pd dropna)
cleaned_df = data_df.dropna(subset=['Medal'])

# %% #* sort_values (use inplace argument. I used to have ugly code like this)
cleaned_df.sort_values(by='Year',inplace=True,ascending=False)

#%% #* Saving data 
cleaned_df.to_csv("my_cleaned_data.csv")
#%% #* convert to list of dictionaries
data = cleaned_df.to_dict(orient='records') # Determines the type of the values of the dictionary.
data[100:101] # it saved as a list

#%% 
cleaned_df.loc[150] # look up by index
cleaned_df.iloc[150] # look up by the row number
#%% #* indexing
cleaned_df.set_index('ID', inplace=True)
#%%
cleaned_df.loc[150] # look up by index
#%%
cleaned_df.iloc[150] # look up by the row number

# %% #* start asking Questions about our data
cleaned_df[cleaned_df['Medal'] == 'Silver']
norus_m_silver_df = cleaned_df[(cleaned_df['Medal'] == 'Silver') & (cleaned_df['Sex']=='M') & (cleaned_df['NOC']!='CAN' )]

# %% #* easy plotting wiht pandas
ax1 = cleaned_df.plot.scatter(x='Height',
                              y='Weight',
                              c='Age',
                              colormap='viridis')
# %% #* add alpha
ax1 = cleaned_df.plot.scatter(x='Height',
                              y='Weight',
                              c='Age',
                              alpha=0.30,
                              colormap='viridis')

 # %% #== Time to try it yourself!
 
 #%% #* add x tick labels
# dont peak https://stackoverflow.com/questions/43578976/pandas-missing-x-tick-labels
fig, ax = plt.subplots()
cleaned_df.plot(kind='scatter',
                x='Height', 
                y='Weight',
                c='Age',
                colormap='viridis',
                ax=ax)

#%% #* make a plot that only shows males
males_df=cleaned_df[cleaned_df['Sex']=='M']
fig, ax = plt.subplots()
males_df.plot(kind='scatter',
                x='Height', 
                y='Weight',
                s=10,
                c='Age',
                cmap='viridis',
                ax=ax)
#%% #* make a plot that only shows males from USA
males_usa_df=cleaned_df[(cleaned_df['Sex']=='M') & (cleaned_df['NOC']=='USA')]
fig, ax = plt.subplots()
males_usa_df.plot(kind='scatter',
                x='Height', 
                y='Weight',
                s=10,
                c='Age',
                cmap='viridis',
                ax=ax)
#%% #* color the plot by medal instead of age
colors = {'Gold':'gold', 'Silver':'silver', 'Bronze':'sienna'}

fig, ax = plt.subplots()
cleaned_df.plot(kind='scatter',
                x='Height', 
                y='Weight',
                s=10,
                c=cleaned_df['Medal'].map(colors),
                ax=ax)
#%% #* get a count of the gold medals by country in a table
#https://datascienceparichay.com/article/pandas-groupby-count-of-rows-in-each-group/
gold_df= cleaned_df[cleaned_df['Medal']=='Gold']
Team_df=gold_df['Team'].value_counts() #grouping by single column

#%% #* make a bar chart out of it ^
Team_df.iloc[:10].plot.bar(x='Team', y='Value')

#%% #* save this table to 
Team_df.to_csv('gold.csv')
# %%
# _ endregion