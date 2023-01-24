# Keith Boehler, 23 Jan 2023

'''
Purpose: Sanitize user input from a barcode. 
Precondition: Barcode is read in as a string. 
Postcondition: Hidden characters like \t or \n are removed. 
                Barcode is returned as an int.
Bugs: 
'''
def clean_barcode(ScannedBarcode: str) -> int:
    #
    CleanedBarcode = ScannedBarcode.strip("\t")
    return int(CleanedBarcode)

'''
Purpose: Check if a scanned barcode is unique or increment counter.
Precondition: Decalred empty or loaded dictionary.
Postcondition: Dictionary has new entry or existing entry in incement by one.
Bugs: 
'''
def dictionary_update(WorkingDict: dict, NewSca: int) -> dict:
    pass

def main() -> int:
    print("Starting... ")
    CumulativeDictionary = {}
    Barcode = input("Scan barcode:  ")
    Barcode = clean_barcode(Barcode)
    print(Barcode)
    print("Done!")
    return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
