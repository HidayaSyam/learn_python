
# ======== PYTHON 101 ==========
# %% #_ region[grey]
# ==== Comments ====
# * staring a line with a # make it a comment in python.
# # Meaning this line will not be ran
var1 = 2 + 2
# ==== Cell Execiton (shift+enter) ====
# %% #* the '#%%' is a special command in VS Code.
#           It allows us to run code in chunks

# ter

# we can do this by hitting shift+enter
print("Just testing things")

# * That should have opened an "Interactive" window.
# If it didnt then check your vs code settings > key shortcuts.
#   The main command you want shift+enter mapped to is:
#       Jupyter: Run Selection/line in Interactive Window

# %% #* Enough set up, lets write some code
# * lets make our first variable named "my_first_var"
my_first_var = 2 + 2
my_first_var  # then print it
# %%
# * we can reference our fist variable in making a new variable
my_first_var = my_first_var + 4
print(my_first_var)
# _ endregion

# %% #==== DataTypes ====
# %% #_ region[purple]
# * well wasnt that fun, but now for some more boring stuff... sorry
# Let talk about datatypes...

# %%#= integers
some_int = 50
# "type" is a built in python function that tells us what datatype an object it. Very helpful
type(some_int)

# %%#= floats
number = 1.5
print(number)
type(number)

# %%#*  converting ints to floats
some_int = float(some_int)

# %%#* rounding floats to ints
print(round(1.3))
type(round(1.7))

# %%#* converting numbers to strings
num = str(1.2)
# looks the same but its a string, basically a series of characters
print("my favorite number is: " + num)
type(num)
# %% # soo if we ran this we get an error
num + 2

# %%#= strings
some_text = 'aberlknsdlkjasdfg,m234587hajkn24j'
print(some_text)

# %%
# * we can get just a certain "slice" of the string by indicating which charaters we want in []
print(some_text[5])
print(some_text[0:10])  # note the first charcter is the 0 index
print(some_text[0])
print(some_text[0] + "bc")  # and we can cobine strings with '+'

# %% #= lists
# * a list is just just a comma seperated collection of objects
a_list = [1, 2.4, '5.7', True, None, ['a', 'b', 'c'], {"key": 'vlue'}]
print(a_list)

# %% #* lists can contain other lists
print(a_list[-1:])
print(a_list[:3])
len(a_list)  # len is another helpful function that shows us how many objects are in a list

# %%
len('abcd')  # also works on strings, fyi

# %%#= dates
# * here we gave the datetime module a nickname 'dt' so we dont have to type it everytime we use it
import datetime as dt
# generally you import at the top of the file.. but oh well

day = dt.datetime.now()  # * now this is called a dot function.
# previously we use a function like 'len()' by placing a the objects or paramters into the ().
# with a dot fucntion, we place just put the function after the object, seperated by a '.'
# like this. Here we have a datetime object called 'day' and use a dot function called 'weekday' on it
type(day)
# %%
dayofweek = day.weekday()
print(dayofweek)
print(type(dayofweek))  # since were here anyways
print(day)
print(type(day))  # since were here anyways

# %%#* this is an example of conditional statements. they run certain lines of code based on a given criterian
if dayofweek == 1:
    its_tuesday = True
    its_monday = False
elif dayofweek == 0:
    it_tuesday = False
    its_monday = True
else:
    its_tuesday = False
    its_monday = False

print((its_tuesday))   # this is a boolean, its either True or False
type(its_monday)

# %%#* that if else is ugly and error prone.  This is a great use case for a 'match' statement
#! however this is only avaliable python version 3.10.. I am currently running 3.7
# match dayofweek:
#     case 0:
#         its_monday = True
#     case 1:
#         its_tuesday = True
#     case 2:
#         its_wednesday = True
#     ...
#     case _:
#         print('no day found)

# %%#* truthy and falsey
if its_tuesday:
    print('sweet, its taco tuesday')
else:
    if 0:
        print('lets go get pizza')
    else:
        print('yuck just a salad...')
# %% #= booleans
print(1 == 1)  # the double equal sign is essentially asking "is this equal to this?"
print(True == (1 == 3))
print(dayofweek)

var1 = 0
if var1:
    print(var1)
else:
    # google python "falsish and trueish values"
    print('wait why did it print this?')

# %%
a_list = [0, 1, -1, None, False, True, "random", [1, 2], {'test': 'value'}]
for item in a_list:
    print(item)
    # chekc if item is truthy or falsey
    if item:
        print('this is truthy')
    else:
        # google python "falsish and trueish values"
        print('this is falsey')

# %% #= dictionaries
# * a collection of key value pairs
my_dictionary = {'key': 'value', 'another': 1, 'and_another': ['a', 'list']}
dir(my_dictionary)
# %%
my_dictionary['another']

# %%
# _ endregion

# %% #==== Basic Data Operations (pandas)====
# %% #_ region[green]ion
# * from a csv
# pandas is a vital package that allows you to work with data in row col format. Similar to excel...ish.
import pandas as pd

# be sure to paste in the correct file path to your csv
data_df = pd.read_csv("")

# %% #* usefull pandas functions
data_df.head(15)
data_df.tail(15)
data_df.describe()
len(data_df)
list(data_df)
# %% #* drop duplicates
data_df.drop_duplicates(subset='WELL_ID', inplace=True)

# %% #* drop nulls (1st Attempt from memory) THIS WILL ERROR
cleaned_df = data_df.dropna(subset='API_NB')
# %% #* drop nulls (after googling pd dropna)
cleaned_df = data_df.dropna(subset=['API_NB', 'WELL_ID'])

# %% #* sort_values (use inplace argument. I used to have ugly code like this)
cleaned_df.sort_values(by='MAX_DLY_GROSS_OIL_PROD',
                       inplace=True, ascending=False)

# %% #* saving data
cleaned_df.to_csv("./outputs/my_cleaned_data.csv")

# %% #* convert to list of dictionaries
data = cleaned_df.to_dict(orient='records')
data[100:103]

# %% #* indexing
cleaned_df.set_index('API_NB', inplace=True)
cleaned_df.loc['30713001100']  # lookup by the index
cleaned_df.iloc[150]  # lookup by the row number

# %% #* easy plotting wiht pandas
ax1 = cleaned_df.plot.scatter(x='MAX_DLY_GROSS_OIL_PROD',
                              y='MAX_DLY_GROSS_GAS_PROD',
                              c='MAX_DLY_WATER_PROD',
                              colormap='viridis')

# %%
# * Bar chart from cleaned df
# * x Spud date as a timeline, y Cum gross td water, colorby County name

# bring in the data
data_df = pd.read_csv()


# %%
# _ endregion

# %% #==== Getting the Data====
# we already saw how to get data from a csv, now lets look at other sources
# %%
# _ region[blue]
import pandas as pd
import traceback2 as traceback

# * also functions and errror handling

# %% #* from an API

import print_cat_facts as pcf

# * also for loops

for i in range(3):
    if i == 1:
        break
    pcf.print_cat_fact(mode='print', i=i, sleep=2)
print('done')

# %% #* while loops
i = 0
while i < 10:
    i += 1
    print_cat_fact('print', i)
# %%
# _ endregion
