
# fetch the index value
cells = [['A1','A2','A3'], ['B1','B2','B3']]
print(cells[0])

# Get the second the list value 
print(cells[1][2])

# for loop

cells = [['A1','A2','A3'], ['B1','B2','B3']]

for x in cells:
    print('Element:', x)
    

for x in cells:
    for y in x:
        print("Element",y )
    

for x in cells:
    for y in x:
        print(y, '', end='' )
    print()
        