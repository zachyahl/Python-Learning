stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, }

def displayInventory(inventory):
    print('Inventory:')
    itemtotal = 0
    for k, v in inventory.items():
        itemtotal = itemtotal + v
        print(str(v) + ' ' + k)

    print ('Total Items: ' + str(itemtotal))

displayInventory(stuff)