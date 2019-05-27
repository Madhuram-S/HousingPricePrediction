
# Import all dependencies
import os
import tarfile
from six.moves import urllib # ensures compatibility with Py 2.0 and Py 3.0

import pandas as pd


# In[2]:

#sample data to test
datasource_url = "https://github.com/ageron/handson-ml/blob/master/datasets/housing/housing.tgz?raw=true"
dest_datapath = "datasets"
dest_datafilename = "housing.csv"


# In[3]:


# function to download and extract the tar file to destination folder
def fetch_extract_datafile(downloadURL, destpath):
    ''' Function downloads tar file from specified url and extracts the file to the given destination path'''
    
    # check if destination dir exist, if not create it
    if not os.path.isdir(destpath):
        os.makedirs(destpath)
       
    # specify the path and filename where tar file will be downloaded
    tgz_path = os.path.join(destpath, "housing.tgz")
    
    # using urllib download the housing file
    urllib.request.urlretrieve(downloadURL, tgz_path)
    
    # open the tar file and assign it to a handle
    tgz_handle = tarfile.open(tgz_path)
    
    #extract all files
    tgz_handle.extractall(path = destpath)
    
    # close handle
    tgz_handle.close()


# In[5]:


# call fetch and extract function to download and extract data file
#fetch_extract_datafile(datasource_url, dest_datapath)


# In[7]:


#check to see if file is extracted
#os.listdir(dest_datapath)


# In[ ]:




