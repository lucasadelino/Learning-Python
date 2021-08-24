#These functions print a fantasy game inventory (modeled as a dict) and add a list of items to an inventory

def display_inventory(inventory): #Displays the inventory passed as argument
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k )
        item_total += v
    print("Total number of items: " + str(item_total))

def add_to_inventory(inventory, added_items): #Adds added_items to inventory and returns inventory
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(stuff) #Checking if display_inventory works

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] 
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv) #Checking if add_to_inventory works