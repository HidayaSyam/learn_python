#%%

import datetime as dt

#%%
x = 2+2
# %%

my_first_var = 3 + 3
my_first_var


# %% #==== DataTypes ====
# * well wasnt that fun, but now for some more boring stuff... sorry
# Let talk about datatypes...

var_int = 5
type(var_int)

# %%
var_float = 3.5
print (var_float)
type(var_float)

# %%#* converting int to float
print (float(var_int))
var_int = float(var_int)
type(var_int)
print (var_int)
# %%#* Rounding  the float
print (round(1.3))
print (round(1.5))
print (round(1.34663,3))
print (round(5.73743,3))

# %%#* converting float to string
num = str(var_float)
#* if I didn't convert the float to a string it will cause an error 
print ("the number is converted to string. " + num)
type(num)
# %%
var_dic = str({1:"b"})
#* iconvert the dic to string it will 
print ("the number is converted to string. " + var_dic)
type(var_dic)

# %%
some_text = "jsdahflLKkasdhfsjkdhfsjdf,.askdjflasdfasdf"
#* get certain slice from the string
print (some_text[5])
print (some_text[0])
print (some_text[0:3])
print (some_text[15:])
print (some_text[0]+"HMMMMMMMMMMMM")

# %% #= lists
# * a list is just just a comma seperated collection of objects
a_list = [1, 2.4, '5.7', True, None, ['a', 'b', 'c'], {"key": 'value'}]
print(a_list)
# %%
print(a_list[-1:]) #{"key": 'value'}  return list 
print(a_list[:3]) # 1,2.4,'5.4' return list of values 
print(a_list[-4: -2 ]) # if we want check the result we -4 - -2 = +2 [True,None] 
print(a_list[-5:-6])# empty list
#print(a_list[-8]) out of range
print(a_list[-6:])
print(a_list[:-3])
print(a_list[3:-2])

len(a_list) 



# %% #* ============ dictionaries =============================

person = {
         "Name": "Hidaya",
         "LastName": "Syam",
         "Location":"Jordan",
         "Age": 23,
         "Hobbies":["Drawing","Reading", "Coding?L"]
         
         }
#* add attr
#%%
person["FullName"] = person["Name"] + " " + person["LastName"]
person["DelItem"] = "Delete thisItem"
# person["FullName"] = person["Name"] + " " + person["LastName"]
print(person)
#%%
#* The pop() method removes the item with the specified key name:
person.pop("Age")
print(person)
#%%
#* The popitem() method removes the last inserted item :
person.popitem()
print(person)
#%%
#* The del () method removes the item with the specified key name also del the whole dictionary:
del person["FullName"]
print(person)
del person
#%%
#* The clear() keyword empties the dictionary:
person = {
         "Name": "Hidaya",
         "LastName": "Syam",
         "Location":"Jordan",
         "Age": 23,
         "Hobbies":["Drawing","Reading", "Coding?L"]
         
         }
person.clear()
print(person)
#* k = key -> v = value loop through dictionary k and v as an items
# person.iteritems() in python 2
for k , v in person.items():
    print(k + " " + str(v))

#%% #* get all keys from dictionary
person.keys()
for k  in person.keys():
    print(k )

#%% #* convert dict values to list
person_values = person.values()
person_values =list(person_values)
print(person_values)

# %%#* dates 
day =dt.datetime.now().weekday()
print(day)

#%% Conditional statement
x=0
if day == 1:
    print("Tuesday")
elif (day == 2):
    print("Wensday")
elif (day == 3):
    x=3
    print("Thuresday")
elif (day == 4):
    print("Friday")
print(x)
# %% #* Match statement in python 3.10
# match day:
#     case 0:
#         print("Monday")
#     case 1:
#         print("Tuesday")
#     case 2:
#         print("Wednesday")
#         .
#         .
#         .
#         . 
#     case _:
#         print("anyday")
        
#%% #* truthy and Falsy 
if 0: # all the numbers are true except 0 
    print("lets eat Pizz")
else: 
    print("lets eat Choclate")
# %%
a_list = [-1,1,0, True, False,"random","",[],{}, None, [1,2,5], {"key":"value"}]
count = 0
for item in a_list:
    count=count + 1
    if item:
        print(str(count) + " this is truthy")
    else:
        print(str(count) +" this is falsy")
    
# %%
