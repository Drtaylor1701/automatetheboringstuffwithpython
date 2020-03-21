#! /usr/bin/env python3

def printTable(tableData):
    colWidths = [0] * len(tableData)
    print(colWidths)

    listIndex = 0
    for entry in tableData:
        colWidths[listIndex] = max(len(x) for x in tableData[listIndex])
        listIndex += 1

    print(colWidths)

    outputTable = []
    for entry in tableData:
        for item in entry:
            outputTable.append(item.rjust(8))
            
    print(outputTable)
    rows = len(outputTable)/len(tableData)
    rows = int(rows)
    columns = len(tableData)
    print(rows)
    print(columns)

    base = 0
    for i in range(rows):
        print(outputTable[base], outputTable[base + rows], outputTable[base + (rows * 2)])
        base += 1

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print(printTable(tableData))
