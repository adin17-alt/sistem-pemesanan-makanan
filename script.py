import menu_item
from menu_item import MenuItem

menu_item1 = MenuItem('Bakso', 5)
menu_item2 = MenuItem('Nasi Padang', 3)
menu_item3 = MenuItem('Mie Ayam', 4)
menu_item4 = MenuItem('Nasi Goreng', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

for menu_item in menu_items :
    print(menu_item.info())


print('--------------------')