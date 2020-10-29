"""
Description:
    This is a data processing script for integrating results with already existing
    allBridge.csv file which contains the results from randomforest and flowchart.
Flow Dependency: integrate_all_results(interventionNDOT.csv) -> allBridge.csv

Input File:
    interventionNDOT.csv
    allBridge.csv
"""

import csv
import os
import pandas as pd
from collections import namedtuple
from collections import defaultdict

__author__ = 'Akshay Kale'
__copyright__= 'GPL'
__credit__ = []
__email__ ='akale@unomaha.edu'


def read_csv(csvfile):
    """
    Description:
        read interventionNDOT.csv file and create a dictionary
        then read all bridge and fill allbridge.csv according to interventionNDOT.csv

    """
    listOfProjects = list()
    with open(csvfile) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
        for row in csvReader:
            listOfProjects.append(row)
    return listOfProjects

def create_dict(listOfProjects):
    """
    Description:
        creating

    """
    dictionary = defaultdict()
    for row in listOfProjects:
        structureNumber = row[0]
        year = row[1]
        intervention = row[2]
        dictionary[structureNumber] = intervention

    return dictionary

def add_NDOT_intervention(listOfInterventions, dictionary):
    """
    Description:
        creating

    """
    counterYes = 0
    counterNo = 0
    listOfLists = list()
    for row in listOfInterventions:
        structureNumber = row[0]
        ndot = dictionary.get(structureNumber)
        if ndot != None:
            if ndot in ['REPLACE', 'WIDEN - REHAB', 'REPAIR']:
                ndot = 'Yes'
            else:
                ndot = 'No'
            if row[1] == ndot:
                #print(row, ndot)
                counterYes = counterYes + 1
            else:
                counterNo = counterNo + 1

        row.append(ndot)
        listOfLists.append(row)
    print(counterNo, counterYes)
    return listOfLists

def to_csv(listOfRecords, csvfile, fieldnames):
    """
    Description:
        Saves list of records into newfile

    Args:
        csvFileName (string): csvfilename

    Returns:
        listOfRecords (list): list of intervention records
        csvfile (string): name of the csvfile
        fieldnames: header column names
    """
    with open(csvfile, 'w') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        csvWriter.writerow(fieldnames)
        for record in listOfRecords:
            csvWriter.writerow(record)
    return True


def main():
    path = '/Users/AkshayKale/Documents/github/data/nbi'
    allbridgeFile = 'allBridgesCopy.csv'
    interventionNDOTFile = 'interventionNDOT.csv'

    listOfProjects = read_csv(interventionNDOTFile)
    NDOTDict = create_dict(listOfProjects)

    listOfInterventions = read_csv(allbridgeFile)
    listOfRecords = add_NDOT_intervention(listOfInterventions, NDOTDict)
    fieldnames = ['structureNumber', 'flowChartResult', 'randomForest', 'NDOTResult']

    csvfilename = 'resultsFlRfNDOT.csv'
    to_csv(listOfRecords, csvfilename, fieldnames)


if __name__=='__main__':
    main()
