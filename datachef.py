""" 
Description:
    This script will contain functions to create a timeseries format of the NBI data. This script will also, intergrate other datasources like precipitation dataset from CDC, population dataset, and weather data (number of snowfall and number of freeze thaw) from infobridge.com

The idea is to create a dish, which is appetitzing, 
To break the monotony we make refer to things differently:
    1. inital datafile = ingridients 
    2. final datafile = dish
    3. function = cook
    4. preprocess = 
    5. chop
    6. Mix =
    7. Garnish = 
    9. Season = mapping functions
    10. plotting functions = presentation


gathering data, combine, season, 

process 1 is creating a time-series dataset.
    1. require all the functions to prepare timeseries data
    2. 



1.  CreateTimeseries
2.  CreateTimeseriesLifeCycle
3.  retDeckProctectionName
4.  Mappingfunctions
5.  

Creating cookbook is basically creating a pipeline -> 

Limitation or Things to add:
    This function are not thoroughly checked using unit testing. If want to make sure these functions work all the time, you're welcome to join this adventure to make this cookbook.

Author: Akshay S. Kale
Python Version: 3.6.4

"""

import pandas as pd
import numpy as numpy

class DataChef():
    """
     Description: The class contain functions to clean, process, and tranform the dataset.

    """

    def __init__(self):
        pass
   
    def gather
    def convertStringListtoList(List):
        """ 
        description: The function converts list of string into a list of list.
        
        input-type: list - [list]
        return-type: list - [list]

        """
        return  [int(item.strip(" ").strip("'")) for item in List[1:-1].split(',')]


