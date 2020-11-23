"""
Description:
    This is a data processing script for intervention
    data history of bridge. The returned file "test.csv'
    will a test cases for the decision tree algorithms
    to test weather the bridges were repaired or reconstructed.

Input File:
    Bridge Project file For UNL

Output File:
     resultInterventionNODT.csv
"""

import csv
import pandas as pd
import datetime as dt
from collections import namedtuple
from collections import defaultdict
from collections import Counter
import matplotlib.pyplot as plt

__author__= 'Akshay Kale'
__copyright__= 'GPL'
__credit__= []
__email__='akale@unomaha.edu'


def read_workbook(workbookName, worksheetName):
    """
    Description: Reads xls files and returns sheet

    Args:
        workbookName (string): xls filename
        worksheetname (string): worksheet filename

    Returns:
        creates a worksheet (CSV file object)
    """
    path = '/Users/AkshayKale/Documents/github/data/nbi/'
    workbookName = path + workbookName
    csvFileName = worksheetName + '.csv'
    xlsFile = pd.read_excel(workbookName, worksheetName, index_col=None)
    xlsFile.to_csv(csvFileName)

def read_history(workbookName, worksheetName):
    """
    Description: Reads xls files and returns sheet

    Args:
        workbookName (string): xls filename
        worksheetname (string): worksheet filename

    Returns:
        creates a worksheet (CSV file object)
    """
    path = '/Users/AkshayKale/Documents/github/data/nbi/'
    workbookName = path + workbookName
    csvFileName = worksheetName + '.csv'
    xlsFile = pd.read_excel(workbookName, worksheetName, index_col=None)
    xlsFile.to_csv(csvFileName)

def process_history(listOfBridges):
    """
    Descriptions: create a list with the format structure number, year, intervention type

    Args:
        listOfBridges (named tuple): list of intervention histroy of the bridge bridges

    Returns:
        listOfBridgesIntervention (list): returns a list of list
    """

    structureNumber = list()
    structureYear = defaultdict(list)
    for namedTuple in listOfBridges:
        namedTuple = namedTuple._asdict()
        tempList = list()
        attribute = ""
        for keyValue in namedTuple.items():
            # if any of the attributes are Y then print the attribute 
            # ['structureNumber', 'year', 'designClass', 'bridgePrjToPrj', 'cntrlSeq', 'intervention']
            if keyValue[1] == 'Y':
                attribute =  keyValue[0]

        tempList = [namedTuple['id1'],
                    namedTuple['BIR_PRJD_YEAR'],
                    namedTuple['BIR_PRJD_DSGN_CLS'],
                    namedTuple['BIR_PRJD_FORM_PRJ'],
                    namedTuple['BIR_PRJD_RT_008A'],
                    attribute]

        structureNumber.append(namedTuple['id1'])
        structNum = namedTuple['id1']
        structureYear[structNum].append(namedTuple['BIR_PRJD_YEAR'])

        # For all bridge gather all years and then with in that list look for bridges that 1992 and above.
        # year.add(namedTuple['BIR_PRJD_YEAR'])

    #print(structureYear)

    tempYear = []
    for years in structureYear.values():
        tempyr = []
        for year in years:
            if year != '':
                year = int(float(year))
                if year >= 1992:
                    tempyr.append(year)
        tempYear.append(tempyr)

    lenYears = list()
    for years in tempYear:
        lenYears.append(len(years))

    print(Counter(lenYears))
    tempCounter = [length for length in Counter(structureNumber).values()]
    lenCounter = Counter(tempCounter)
    print(lenCounter)
    plt.title("Summary bar chart")
    plt.bar(range(len(lenCounter)), list(lenCounter.values()), align='center')
    plt.xticks(range(len(lenCounter)), list(lenCounter.keys()))
    plt.xlabel('Number of records per length')
    plt.ylabel('Length of bridge records')
    plt.show()

def read_csv(csvFileName):
    """
    Description:
        Returns a list of intervention bridge projects

    Args:
        csvFileName (string): csvfilename

    Returns:
        listOfProjects (list): list of named tuple with essential attributes
    """
    listOfProjects = list()
    with open(csvFileName, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
        # Fix empty header name (Doesn't allow to create namedtuple)
        if header[0] == '':
            header[0] = 'id'
            header[1] = 'id1'
        # Get rid of header names with spaces
        header = [col.replace(" ", "") for col in header]
        header = [col.replace(":", "") for col in header]
        Record = namedtuple('Record', header)
        for row in csvReader:
            if row[-1] != '':
                #print(row[-1])
                record = Record(*row)
                listOfProjects.append(record)
    return listOfProjects


def to_csv(listOfRecords, csvfile, fieldnames):
    """
    Description:
        Saves list of records into newfile

    Args:
        listOfRecords (list): list of intervention records
        csvfile (string): name of the csvfile
        fieldnames: header column names

    Returns:
        status of the process of sacing files
    """
    with open(csvfile, 'w') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        csvWriter.writerow(fieldnames)
        for record in listOfRecords:
            csvWriter.writerow(record)
    return True


def fix_date(date):
    """
    Description:
        Converts into datetime format and fixes missing date value.

    Args:
        date (string)

    Returns:
        date (datetime)
    """
    if date == '':
        # IMPORTANT FIX NEEDED
        # Can't have null values replaced with current datetime
        return dt.datetime.now()
    return dt.datetime.strptime(date, "%m/%d/%Y")


def get_bridges_hist(listOfProjects, startYear, endYear):
    """
    Description:
        Returns a list of the Project between years provided

    Args:
        listOfProject (list): list of the named tuples that include
        essential attributes.
        1. structureNumber
        2. intervention

    Returns:
        bridgeInterventionList (list): list of structure number with intervention status
    """
    bridgeInterventionList = list()
    counterYes = 0
    counterNo = 0
    for record in listOfProjects:
        structureNumber = record.id1
        year = record.Year
        if year != 'BIR_PRJD_YEAR' and year != '':
            year = int(float(year))
            if startYear < year < endYear:
                action = 'Yes'
                counterYes = counterYes + 1
            else:
                action = 'No'
                counterNo = counterNo + 1

            bridgeRec = [structureNumber, year, action]
            bridgeInterventionList.append(bridgeRec)
    return bridgeInterventionList


def get_bridges(listOfProjects, startYear, endYear):
    """
    Description:
        Returns a list of the Project between years provided

    Args:
        listOfProject (list): list of the named tuples that include
        essential attributes.
        1. structureNumber
        2. intervention

    Returns:
        bridgeInterventionList (list): list of structure number with intervention status
    """
    bridgeInterventionList = list()
    for record in listOfProjects:
        structureNumber = record.id1
        date = record.ConstructionEndDate
        date = fix_date(date)
        year = date.year
        action = record.ProposedAction
        if startYear < year < endYear:
            bridgeRec = [structureNumber, year, action]
            bridgeInterventionList.append(bridgeRec)
    return bridgeInterventionList



def main():
    """
    Driver program
    """
    # Read xls file and create CSV file of the spreadsheet
    workbookName = "Bridge Projects and History for UNL.xlsx"
    #worksheetName = "Hist of Bridges by SN"
    worksheetName = "ProjectData"
    historyWorksheet = 'HistData'

    read_workbook(workbookName, worksheetName)
    read_history(workbookName, historyWorksheet)

    # Read CSV File
    #csvFileName = worksheetName + '.csv'
    historyCsvFileName = historyWorksheet + '.csv'

    #startYear = 2015
    #endYear = 2018
    #listOfProjects = read_csv(csvFileName)

    listOfBridges = read_csv(historyCsvFileName)
    print(process_history(listOfBridges))

    ## Save CSV File Copy
    #listOfRecords = get_bridges(listOfProjects, startYear, endYear)

    #newCsvFile ='resultInterventionNDOT.csv'
    #fieldnames = ['structureNumber', 'intervention']
    #to_csv(listOfRecords, newCsvFile, fieldnames)


if __name__ =='__main__':
    main()
