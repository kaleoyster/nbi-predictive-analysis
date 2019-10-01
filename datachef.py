""" 
Description:
    This script will contain functions to create a timeseries format of the NBI data. This script will also, intergrate other datasources like precipitation dataset from CDC, population dataset, and weather data (number of snowfall and number of freeze thaw) from infobridge.com

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

    def convertStringListtoList(List):
        """ 
        description: The function converts list of string into a list of list.
        
        input-type: list - [list]
        return-type: list - [list]

        """
        return  [int(item.strip(" ").strip("'")) for item in List[1:-1].split(',')]


