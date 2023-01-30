# Keith Boehler, 23 Jan 2023
import sys
'''
Purpose:  
Precondition: 
Postcondition: 
Bugs: 
'''
def menu_options(KeybordInput: str) -> bool:
    if KeybordInput == 's':
        pass #save_scans()
    elif KeybordInput == 'q':
        return False #sys.exit("Exiting program... ")


'''
Purpose: Check if a scanned barcode is unique or increment counter.
Precondition: Decalred empty or loaded dictionary.
Postcondition: Dictionary has new entry or existing entry in incement by one.
Bugs: 
'''
def dictionary_update(WorkingDict: dict, NewScan: str) -> dict:
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
        if Barcode == 's' or Barcode == 'p' or Barcode == 'q':
            Cont = menu_options(Barcode)
        else:
            CumulativeDictionary = dictionary_update(CumulativeDictionary, Barcode)
        print(CumulativeDictionary)
    print("Done!")
    return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()    
