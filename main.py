# Keith Boehler, 23 Jan 2023
import sys
import os
import csv

def dictionary_update(WorkingDict: dict, NewScan: str) -> dict:
    '''
    Purpose: Check if a scanned barcode is unique or increment counter.
    Precondition: Decalred empty or loaded dictionary.
    Postcondition: Dictionary has new entry or existing entry in incement by one.
    Bugs: Does take enter input as argument.
    '''
    if NewScan not in WorkingDict.keys():
        TmpDict = {NewScan : 1}
        WorkingDict.update(TmpDict)
    else:
        WorkingDict[NewScan] = WorkingDict[NewScan] + 1
    return WorkingDict


def peek_dictionary(Dicts: dict) -> None:
    '''
    Purpose: Reusing of loops to print dictionarys.
    Precondition: A dictionary is loaded with data.
    Postcondition: No return. Just nice (debatable) format terminal output of dictionary.
    Bugs: 
    '''
    for Keys, Values in Dicts.items():
        print(Keys, Values)
    print("\n")


def main() -> int:
    print("Starting... ")
    CumulativeDictionary = {}
    MenuOptions = {"Show menu again: ": "m",
                   "Show scans: ": "p",
                   "Write to csv file: ": "w",
                   "Exit program: ": "q"
                    }
    peek_dictionary(MenuOptions)
    Cont = True
    while Cont is True:
        Barcode = input("Scan barcode:  ")
        if Barcode == 'w':
            SavePath = os.getcwd() + "/data/out.csv"
            with open(SavePath, 'w') as CSVHandle:
                Writer = csv.writer(CSVHandle)
                for Row in CumulativeDictionary.items():
                    Writer.writerow(Row)
            CSVHandle.close()
        elif Barcode == 'p':
            print("\n")
            print("Barcode: Amount")
            peek_dictionary(CumulativeDictionary) 
        elif Barcode == 'q':
            sys.exit("Closing program... ")
        elif Barcode == 'm':
            print("\n")
            peek_dictionary(MenuOptions)
        else:
            CumulativeDictionary = dictionary_update(CumulativeDictionary, Barcode)
    
    return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()    
