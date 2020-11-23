"""
Description: Summary analysis of training data annd test data
    The goal of the script is to understand that if the test data is the representation of the training data.

Author: Akshay Kale
"""

import os
import csv
import numpy as np
from collections import defaultdict
from collections import namedtuple
import matplotlib.pyplot as plt

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'

# TODO():
    # 1. Read the training data 
    # 2. Read the testing data 

def read_csv(path, csvFile):
    """
    description:
        Returns a list of records in the csvfile

    args:
        path (string): path of the csvfile
        csvfile (string): name of the csvfile

    returns:
        listOfRecords (namedtuple): listOfRecords
    """
    listOfRecords = list()
    with open(csvFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        header = next(csvReader)
        if header[0] == '':
            header[0] = 'id'
        header = [col.replace(" ", "") for col in header]
        header = [col.replace(".", "") for col in header]
        header = [col.replace(":", "") for col in header]
        Record = namedtuple('Record', header)
        for row in csvReader:
            record = Record(*row)
            listOfRecords.append(record)
    return listOfRecords



def createListedAttribute(namedTuple, attr):
    listOfAttrVals = list()

    for record in namedTuple:
        record = record._asdict()
        listOfAttr = record[attr]
        lastItem = convertStringToList(listOfAttr)
        listOfAttrVals.append(lastItem)

    return listOfAttrVals


def createListedAttributeSingle(namedTuple, attr):
    listOfAttrVals = list()

    for record in namedTuple:
        record = record._asdict()
        if record[attr] != "":
            lastItem = float(record[attr])
            listOfAttrVals.append(lastItem)

    return listOfAttrVals


def convertStringToList(listOfAttr):
    """
    description:
        Returns a list from the string

    args:
        path (string): path of the csvfile
        csvfile (string): name of the csvfile

    returns:
        listOfRecords (list): listOfRecords
    """
    listOfAttr = listOfAttr.strip("[")
    listOfAttr = listOfAttr.strip("]")
    listOfAttr = listOfAttr.split(",")
    listOfAttr = [int(item) for item in listOfAttr]
    lastItem = listOfAttr[-1]

    return lastItem

def compareGroups(group1, group2, attr):
    treatments = [group1, group2]
    fig, ax = plt.subplots()
    bp = ax.boxplot(treatments)
    ax.set_xlabel('Groups')
    ax.set_ylabel('Values')
    plt.show()


def main():
    path = "../../data/nbi/dataDecisionTree/"
    csvFileTrain = 'decision_tree.csv'
    csvFileTest = 'decision_tree_testing.csv'
    os.chdir(path)

    trainTuple = read_csv(path, csvFileTrain)
    testTuple = read_csv(path, csvFileTrain)

    # Attribute of train tuple
    listOfAdtTrain = createListedAttribute(trainTuple, 'adt')
    listOfAdttTrain = createListedAttribute(trainTuple, 'adtt')

    # Attribute of train tuple
    listOfMaxlengthTrain = createListedAttributeSingle(trainTuple, 'currentmaxlenspan')
    listOfPrecipitationTrain = createListedAttributeSingle(trainTuple, 'precipitation')
    listOfSnowfallTrain = createListedAttributeSingle(trainTuple, 'snowfall')
    listOfFreezeThawTrain = createListedAttributeSingle(trainTuple, 'freezethaw')

    # Attribute of test tuple
    listOfAdt = createListedAttribute(testTuple, 'adt')
    listOfAdtt = createListedAttribute(testTuple, 'adtt')

    # Attribute of test tuple
    listOfMaxlength = createListedAttributeSingle(testTuple, 'currentmaxlenspan')
    listOfPrecipitation = createListedAttributeSingle(testTuple, 'precipitation')
    listOfSnowfall = createListedAttributeSingle(testTuple, 'snowfall')
    listOfFreezeThaw = createListedAttributeSingle(testTuple, 'freezethaw')

    compareGroups(listOfAdt, listOfAdtTrain, 'Average Daily Traffic')
    compareGroups(listOfAdtt, listOfAdttTrain, 'Average Daily Truck Traffi')
    compareGroups(listOfSnowfall, listOfSnowfallTrain, 'Snowfall')
    compareGroups(listOfFreezeThaw, listOfFreezeThawTrain, 'Freezethaw')
    compareGroups(listOfPrecipitation, listOfPrecipitationTrain, 'Freezethaw')


if __name__ =="__main__":
    main()
