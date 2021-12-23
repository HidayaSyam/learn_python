

#%%
import logging
import time
# def connect_to_api(url:str): # : str the data type of url
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
a_list = ['1','2',3,'5']

#%%
for i in a_list:
    time.sleep(2)
    try:
        # print('count: '+i)
        logging.info("Count: "+ i)
    except Exception as e:
        logging.error(e)
        continue

 # %%
