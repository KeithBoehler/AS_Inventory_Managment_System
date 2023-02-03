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

def undo_scan(Dictionary2Correct, Barcode2Correct, Ammount2Correct=1):
    '''
    Purpose: Delete extra / erroneous barcode scans with the ability to choose how many
    Precondition: loaded dictionary (Dictionary2Correct) and a barcode string (Barcode2Correct) to be deleted.
    with a specified amount of barcode scans user wants to delte
    Postcondition: Dictionary2Correct will be updated by deleting an entry if the value is one or decrementing if value > 1
    '''
    if Barcode2Correct in Dictionary2Correct.keys():
        if Dictionary2Correct[Barcode2Correct] > 1:
            Dictionary2Correct[Barcode2Correct] = Dictionary2Correct[Barcode2Correct] - Ammount2Correct
        else:
            del Dictionary2Correct[Barcode2Correct]
    else:
        print("Corrected barcode is not in dictionary... ")

    return Dictionary2Correct


def main() -> int:
    print("Starting... ")
    CumulativeDictionary = {}
    MenuOptions = {"Show menu again: ": "m",
                   "Show scans: ": "p",
                   "Delete scans: ": "d",
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
        elif Barcode == 'd':
            ErrorBarcode = input("Barcode you want to delete: ")
            DecrimentQuantity = int(input("Amount you want to delete: "))
            CumulativeDictionary = undo_scan(CumulativeDictionary, ErrorBarcode, DecrimentQuantity)
        else:
            CumulativeDictionary = dictionary_update(CumulativeDictionary, Barcode)
    
    return 0
"""
Bugs: NO ERROR HANDLING
In the future we would like to implement:
    error handling: unknown inputs such as ENTER, and other keys with no assigned function
    Auto Saving: save write to disk every so often
    Counter: if every counter modulo 5 write to disk0
    Load CSV: in case you don't finish scanning have a file you can load for later
"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()    
