"""
Title: Script for creating training and testing data
Author: Akshay Kale
Description:
    Creating training and testing dataset for the decision tree algorithm
    The script takes NDOTdataset and decision_tree.csv (preprocessed), and
    creates a training and testing dataset
"""

__author__ = ' Akshay Kale'
__copyright__ = 'GPL'
__email = 'akale@unomaha.edu'

import os
import csv
from collections import namedtuple
from collections import defaultdict
import random

def read_csv(csvfile, path):
    """
    Description:  reads csv files and converts them into list of lists
    Args:
        csvfile (string): path of the csv file
    Returns:
        listOfLists (list): returns a list of records
    """
    listOfLists = list()
    fullCsvfilePath = path + csvfile
    with open(fullCsvfilePath, 'r') as csvFile:
        csvReader =  csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
        for row in csvReader:
            listOfLists.append(row)
    return listOfLists, header


def extract_structure_numbers(ndotListOfLists):
    """
    Description: extracts structure number from list of lists and convert them into a set
    Args:
        ndotListOfLists (list): list of bridges from NDOT repair and reconstruction
    Returns:
        listOfStructureNumber (set): returns a list of strucutre Numbers
     """
    listOfStructureNumbers = defaultdict()
    for row in ndotListOfLists:
        if row[2] in ['REPLACE', 'WIDEN - REHAB', 'REPAIR']:
            listOfStructureNumbers[row[0]] = row[2]
    return listOfStructureNumbers


def split_dataset(ndotListOfLists, nbiListOfLists, states='ALL'):
    """
    Description:  splits data set into training and testing dataset with testing dataset as nbiListOFLists
    Args:
        ndotListOfLists (list): list of bridges from NDOT repair and reconstruction
        nbiListOfLists (list): list of bridges from NBI data
    Returns:
        listOfTraining (list): returns a list of records
        listOfTesting (list): returns a list of records
    """
    trainingSet = list()
    testingSet = list()
    ndotSet = extract_structure_numbers(ndotListOfLists)
    for row in nbiListOfLists:
        structureNumber = row[14]
        if structureNumber in ndotSet.keys():
            row[-7] = 'Yes'
            row[-6] = 'Yes'
            row[-5] = 'Yes'
            testingSet.append(row)
        else:
            if row[-7] == 'Yes' or row[-6] == 'Yes' or row[-5] == 'Yes':
                row[-7] = 'Yes'
                row[-6] = 'Yes'
                row[-5] = 'Yes'
            trainingSet.append(row)
    return trainingSet, testingSet

def prepare_dataset(ndotListOfLists, nbiListOfLists, states='ALL'):
    """
    Description: prepares a training testing dataset by combining two datasets
    Args:
        ndotListOfLists (list): list of bridges from NDOT repair and reconstruction
        nbiListOfLists (list): list of bridges from NBI data
    Returns:
        listOfJoinedDataset (list): returns a list of records
    """
    joinedDataset = list()
    ndotSet = extract_structure_numbers(ndotListOfLists)
    print(len(ndotSet))
    print(ndotSet)
    for row in nbiListOfLists:
        structureNumber = row[14]
        if structureNumber in ndotSet.keys():
           joinedDataset.append(row)
    return joinedDataset


def remove_records(listOfRecords, testingSet, indexes):
    """
    Description:
        Saves list of records into newfile

    Args:
        csvFilename (string): csvfilename

    Returns:
        listOfRecords (list): list of intervention records
        csvfile (string): name of the csvfile
        fieldnames (list): listOfFieldNames
    """
    newListOfRecords = list()
    for idx in indexes:
        newListOfRecords.append(listOfRecords[idx])

    for idx in indexes:
        listOfRecords.pop(idx)

    for row in newListOfRecords:
        row[-7] = 'No'
        row[-6] = 'No'
        row[-5] = 'No'
        testingSet.append(row)

    return listOfRecords, testingSet


def to_csv(listOfRecords, csvfile, fieldnames):
    """
    Description:
        Saves list of records into newfile

    Args:
        csvFilename (string): csvfilename

    Returns:
        listOfRecords (list): list of intervention records
        csvfile (string): name of the csvfile
        fieldnames (list): listOfFieldNames
    """

    with open(csvfile, 'w') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        csvWriter.writerow(fieldnames)
        for record in listOfRecords:
            csvWriter.writerow(record)
    return True

def main():
    """
    Driver function
    """
    ndotFile = 'resultInterventionNDOT.csv'
    datasetFile = 'decision_tree.csv'
    pathDecisionTree = '../../../data/nbi/dataDecisionTree/'
    pathNDOTFile = ''

    # Step 1: read csv files
    ndotListOfLists, ndotHeader  = read_csv(ndotFile, pathNDOTFile)
    nbiListOfLists, nbiHeader = read_csv(datasetFile, pathDecisionTree)

    # Step 2: prepare files 
    joinedDataset = prepare_dataset(ndotListOfLists, nbiListOfLists)

    #trainingSet, testingSet = split_dataset(ndotListOfLists, nbiListOfLists)

    #lengthTraining = len(trainingSet)
    #lengthTesting = len(testingSet)

    #seqsIndex = random.sample(list(range(lengthTraining)), k=lengthTesting)
    #trainingSet, testingSet = remove_records(trainingSet, testingSet, seqsIndex)

    #csvfilename = 'decision_tree_new.csv'
    #testingCsvfilename = 'decision_tree_testing.csv'

    #to_csv(trainingSet, csvfilename, nbiHeader)
    #to_csv(testingSet, testingCsvfilename, nbiHeader)

if __name__ =='__main__':
    main()
