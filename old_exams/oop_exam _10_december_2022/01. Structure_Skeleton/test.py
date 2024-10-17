# from project.booths.booth import Booth
from project.christmas_pastry_shop_app import ChristmasPastryShopApp
# from project.delicacies.delicacy import Delicacy
# from project.delicacies.gingerbread import Gingerbread
# from project.delicacies.stolen import Stolen
#
# shop = ChristmasPastryShopApp()
# print(shop.add_delicacy('Stolen', 'Cheesecake', 12.0))
# print(shop.add_delicacy('Stolen', 'Cake', 12.0))
# print(shop.add_delicacy('Gingerbread', 'Ginger', 12.0))
# print('========================================')
#
# print(shop.add_booth('Private Booth', 5, 12))
# print(shop.add_booth('Private Booth', 6, 1))
# print(shop.add_booth('Private Booth', 7, 13))
# print(shop.reserve_booth(10))
# print('========================================')
#
# print(shop.order_delicacy(5, 'Cheesecake'))
# print(shop.order_delicacy(6, 'Cheesecake'))
# print(shop.order_delicacy(7, 'Cheesecake'))
# print('========================================')
# for b in shop.booths:
#     print(b.is_reserved)
#     print(b.delicacy_orders[0].name)
# print('========================================')
# print(shop.leave_booth(5))
# print(shop.leave_booth(6))
# print(shop.get_income())

shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())

