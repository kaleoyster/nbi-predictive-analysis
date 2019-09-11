""" 
Description:
    Something fun is about to happen

Author: Akshay S. Kale
Python Version: 3.6.4

"""

import pandas as pd
import numpy as numpy

class DataPrep():
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


