import menu_item
from menu_item import MenuItem

menu_item1 = MenuItem('Bakso', 5)
menu_item2 = MenuItem('Nasi Padang', 3)
menu_item3 = MenuItem('Mie Ayam', 4)
menu_item4 = MenuItem('Nasi Goreng', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items :
    print(str(index) +'.'+ menu_item.info())
    index += 1

print('--------------------')

order = int(input('Silahkan masukkan nomor urut menu untuk memesan :'))

selected_menu = menu_items[order]

#Terima Input dari console

count = int(input('Jumlah pesanan (diskon 10% untuk pembelian 3 item atau lebih) :'))

result = selected_menu.get_total_price(count)

print('Total harga adalah $'+str(result))