# table data
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    y = 0
    for x in data[1]:
        if len(x) > y:
            y = len(x)
    print(y)

printTable(tableData)