"""
Description:
    This scripts provides analysis
Author: Akshay
"""

__author__ = ' Akshay Kale'
__copyright__ = 'GPL'
__email = 'akale@unomaha.edu'

import os
import csv
from collections import namedtuple
from collections import defaultdict
import random

def read_csv(csvfile):
    """
    Description:  reads csv files and converts them into list of lists
    Args:
        csvfile (string): path of the csv file
    Returns:
        listOfLists (list): returns a list of records
    """
    listOfLists = list()
    with open(csvfile, 'r') as csvFile:
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


def split_dataset(ndotListOfLists, nbiListOfLists):
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



def convert_string_to_list(listOfStrings):
    """
    Description:
       Compare the five point summary of the training data attrbutes and testing data

    Args:
        listOfStrings (list): A list of uncleaned list (list is represented as string)

    Returns:
        listOflist (list): A cleaned list of lists
    """

    listOfList = []

    return listOfList

def compare_attributes(trainingData, testingData, attributeName):
    """
    Description:
       Compare the five point summary of the training data attrbutes and testing data

    Args:
        trainingData (list):
        testingData (list):
        attributeName (list):

    Returns:
    """
    trainingAttribute = list()
    testingAttribute = list()

    for trainVal, testVal in zip (training):
        newListOfRecords.append(listOfRecords[idx])

    for idx in indexes:
        listOfRecords.pop(idx)

    for row in newListOfRecords:
        row[-7] = 'No'
        row[-6] = 'No'
        row[-5] = 'No'
        testingSet.append(row)

    return , testingSet


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
    trainingFile = 'decision_tree.csv'
    testingFile = 'decision_tree_testing.csv'

    trainingData, ndotTrainHeader  = read_csv(trainingFile)
    testingData, nbiTrainHeader = read_csv(testingFile)


#    lengthTraining = len(trainingSet)
#    lengthTesting = len(testingSet)
#
#    seqsIndex = random.sample(list(range(lengthTraining)), k=lengthTesting)
#    trainingSet, testingSet = remove_records(trainingSet, testingSet, seqsIndex)
#
#    csvfilename = 'decision_tree_new.csv'
#    testingCsvfilename = 'decision_tree_testing.csv'
#
#    to_csv(trainingSet, csvfilename, nbiHeader)
#    to_csv(testingSet, testingCsvfilename, nbiHeader)

if __name__ =='__main__':
    main()
