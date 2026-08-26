# Capstone-Project-Module-1
CRUD Program in Python
Study Case : Merchant Item Sales
This program's features are Create, Read, Update, and Delete function with regular function.

List of Dictionaries: Active Items, Active Promotions Based on Item, Active Promotions Based on Minimun Total Purchase, User's Cart, User's Transactions, and Merchant's Staff.
Primary Key: Item ID & User's Transaction.

Create Function:
Adding new item to item's list (Item ID is automatically generated), adding new active promo based on item, adding new active promo based on minimum total purchase, adding item to the cart (if any buyer).

Read Function:
Read all active item, read all active promo based on item, read all active promo based on minimum total purchase, read multiple item/s based on search by 'ItemID', 'Item Name', and 'Category', read user'spurchase invoice

Update Function:
Update part of item such as category name, item name, description, price, stock. For update price, there is a confirmation if the item have an active promotion.

Delete Function:
Delete item from item'list one by one, delete all item on the same category, delete active promo based on item, delete active promo based on minimum total purchase. For delete item, if the item still have an active promo, there is a notice that if we proceed, the promotion will also be removed.

Note: Only Merchant's Staffs can access this program. Also, there is the difference access depends on Staff'role.
