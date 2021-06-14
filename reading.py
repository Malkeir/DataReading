"""----------------------------------------------------------------------------------------------------------------
Author:Benjamin Dorr
FileName: FileReading.py
Definition: With in this file this will be a class that will either take in a directory of a folder that contains
multiple documents or a single doc of .pdf, .docx, .exl .txt, .jSON, .

----------------------------------------------------------------------------------------------------------------"""

# all the imports that are needed for this class to work

import os
import sys
import requests
import json
import pandas as pd

"""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Author:Benjamin Dorr
Class Name: FileReading
Definition: With in this class there will be a key paring system that will be done for the initialization so that 
there are different whys for the objects to be structure so there will be objects that have different function calls
also there will be. the same this will be done with the class so there is a key paring system for the lambda functions.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
class DocReading:

    """
    Author: Benjamin Dorr
    MethodName: __init__
    Definition: this is call is the initialization of the reading doc file. this will get the
    dic of key functions.
    """
    def __init__(self):
            readinginfo =None
            FileType = None
            currentAttribute = None
            Key =None
    """*****************************************************************************************************************
    Author:Benjamin Dorr
    MethodName: lambdalist
    Definitions: this function is call in the initialization of the object to assign the list of lambda functions to a
    variable so it will be able to uses the data and process the files properly. It wll call itself so that
    to look at the Key the was found right before that it was call so that it will get the right key paring system so
    that the correct function are done.
    all lambda functions and what they do:
        -Parsing a word document or pdf for set key words and the word or txt file
        -find words that have a set group of letters in them
        -Reading an exel document
            -reading a select row of an exel doc
            -reading a select column of a exel doc
            -searching for a cell in the exel doc
            -write to set select rows of columns of a exel doc
            -create an exel doc
                -be able to write to a newly created exel doc
            -organise a set row or columns
            - change the and manipulate the exel columns and rows
        -Read a jason file
            -search and return set variables in a json file
            -create an entirely new json file from an exel document
    multiple documents or a single doc of .pdf, .docx, .exel .txt, .jSON
    *****************************************************************************************************************"""

    def lambdadic(self):
        lamdic = {
            # Json file reading/data reading
            0: {0: lambda: self.readinginfo[int(input("get var in json"))],
                1: lambda: self.readinginfo(input("value of key")),
                2: lambda: self.readinginfo.get(input("lss")), 3: lambda: open(input('filename?:',"w")(lambda x: x.write(self.readinginfo)))},

            # reading of .txt files
            4: {0: lambda: self.readinfo.get((input("get var in json"))), 1: lambda: print("holder"),
                2: lambda: print("holder"), 3: lambda: print("holder"),
                4: lambda: print("holder"), 5: lambda: print("holder"),
                6: lambda: print("holder")},

            # reading of docx files
            2: {0: lambda: self.readinfo.get((input("get var in json"))), 1: lambda: print("holder"),
                2: lambda: print("holder"), 3: lambda: print("holder"),
                4: lambda: print("holder"), 5: lambda: print("holder"),
                6: lambda: print("holder")},
            # reading of .exel files
            3: {0: lambda: self.readinfo.get((input("get var in json"))), 1: lambda: print("holder"),
                2: lambda: print("holder"), 3: lambda: print("holder"),
                4: lambda: print("holder"), 5: lambda: print("holder"),
                6: lambda: print("holder")},

            # reading of pdf files
            4: {0: lambda: self.readinfo.get((input("get var in json"))), 1: lambda: print("holder"),
                2: lambda: print("holder"), 3: lambda: print("holder"),
                4: lambda: print("holder"), 5: lambda: print("holder"),
                6: lambda: print("holder")},

            5: {0: lambda: self.readinginfo.json()(lambda: self.lambdalist()),
                1: lambda x: self.KeyDetrmination.get(1),
                2: lambda x: self.KeyDetermination.get(2), 3: lambda x: self.KeyDetermination.get(3),
                4: lambda x: self.KeyDetermination.get(4)},

            # reading of .csv files
            6: {0: lambda: self.readinfo.get((input("get var in json"))), 1: (lambda: print("holder")),
                2: lambda: print("holder"), 3: lambda: print("holder"),
                4: lambda: print("holder"), 5: lambda: print("holder"),
                6: lambda: print("holder")}}

        # in the function above this is where recursion happens for webreading of different file types.
        return lamdic

    """****************************************************************************************************************
    Author:Benjamin Dorr
    MethodName: KeyDetermination
    Definition: Within the method it will look at the objects directory that was passed in and see if it is a folder
    or just a single from file. if its a single file there will be a check to see what the file type is and this
    will give back the right key for selecting the correct lambda functions it they lambda list section
    ****************************************************************************************************************"""

    def KeyDetermination(self):
        keyoptions = {".json": 0, ".txt": 1,
                      ".docx": 3, ".exel": 4,
                      ".csv": 6, "websitepull": 5}

        self.Key = keyoptions.get(self.FileType)

    """**************************************************************************************************************
       Author:Benjamin Dorr
       MethodName: readOptions
       Definition: This is called from the read method this will allow you to see what options you have to choose
       from what you want to do with the file. do you want to read it and just display to console. have that data be 
       passed to another program? or parse the data and display it? or call the write function to write data to 
       another file. 

       web is chosen: -> gets format of data -> calls KeyDetermination to get data types data methods -> passes in data 
       of read data into option of what you wanted to do with data 

       **************************************************************************************************************"""

    def readOptions(self):
        lamdic = self.lambdadic()
        choices = lamdic.get(self.Key)
        print(choices)
        v = input("what would you like to do:")
        options = choices.get(int(v))
        print(options())

    # https://api.opendota.com/api/heroStats

    """**************************************************************************************************************
    Author:Benjamin Dorr
    MethodName: read
    Definition: this method is the users input for what function they want to call for the file that they have input
    from here it will have available to based on the functioning input from the key that was created and from the
    lambda key  pairing system.
    **************************************************************************************************************"""

    def read(self):
        direct = input("give directory to file or folder: ")
        if direct[0:5] == "https":
            self.readinginfo = requests.get(direct)
            self.FileType = ".json"
            self.readinginfo=(self.readinginfo.json())

            self.KeyDetermination()
            self.readOptions()
        else:
            if os.path.exists(direct):

                for root,dir,file in os.walk(direct):
                    name,ext = os.path.splitext(root)
                    self.FileType = ext
                    self.KeyDetermination()
                    self.readinginfo = open(root)
            else:
                self.read()


def __main__():
    holder = DocReading()
    holder.__init__()
    holder.read()


    return 1
__main__()