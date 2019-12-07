#! /usr/bin/env python3

def printTable(tableData):
    colWidths = [0] * len(tableData)
    print(colWidths)

    listIndex = 0
    for list in tableData:
        colWidths[listIndex] = max(len(x) for x in tableData[listIndex])
        listIndex += 1

    print(colWidths)

    outputTable = []
    for entry in tableData:
        for item in entry:
            outputTable.append(item)
    
    return outputTable
    padding = " "
    index = 0
    for list in tableData:
        print(list[0]) + (padding * (maxlen(list[index])), end='')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print(printTable(tableData))
