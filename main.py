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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting... ")

    Barcode = input("Scan barcode:  ")
    Barcode = clean_barcode(Barcode)
    print(Barcode)
    print("Done!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
