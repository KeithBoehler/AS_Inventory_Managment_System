# Keith Boehler, 23 Jan 2023
import sys
import os
from pprint import pprint
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

def main() -> int:
    print("Starting... ")
    CumulativeDictionary = {}
    Cont = True
    while Cont is True:
        Barcode = input("Scan barcode:  ")
        if Barcode == 'w':
            SavePath = os.getcwd() + "/data/out.csv"
            CSVHandle = csv.writer(open(SavePath, "w"))
            for Key, Val in CumulativeDictionary.items():
                CSVHandle.writerow([Key, Val])
        elif Barcode == 'p':
            pprint(CumulativeDictionary, depth=2, indent=4) 
        elif Barcode == 'q':
            sys.exit("Closing program... ")
        else:
            CumulativeDictionary = dictionary_update(CumulativeDictionary, Barcode)
    
    return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()    
