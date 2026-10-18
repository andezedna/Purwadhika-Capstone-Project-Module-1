# Capstone-Project-Module-1
CRUD Program in Python<br>
<br>
Study Case : Merchant Item Sales<br>
This program's features are Create, Read, Update, and Delete function with regular function.<br>

List of Dictionaries:
1. Distionary of Active Items
2. Dictionary of Inactive Items
3. Dictionary of Active Promotions Based on Item
4. Dictionary of Active Promotions Based on Minimun Total Purchase
5. Dictionary of User's Cart
6. Dictionary of Users' Transactions
7. Dictionary of Merchant's Staff

Primary Key: Item ID & User's Transaction.

Create Function:
1. Adding new item to item's list (Item ID is automatically generated)<br>
   The following are several inputs required for this function:<br>
   Category name, Item name, Item Description, Item Price, and Item Stock.<br>
   
2. Adding new active promo based on item<br>
   Inputs that required for this request are Item ID and value promo its item.<br>
   
3. Adding new active promo based on minimum total purchase<br>
   Inputs that required for this request are minimun total purchase to qualify the promotion and value promo its minimum total purchase.<br>
   
4. Adding item to the cart (if any buyer)<br>
   Inputs that required for this request are Item ID and quantity its item.<br>
<br>
Read Function:<br>
1. Read all active item<br>
2. Read all active promo based on item<br>
3. Read all active promo based on minimum total purchase<br>
4. Read multiple item/s based on search by Item ID/ Item Name/ Category<br>
5. Read user's purchase invoice.<br>
All of the read functions above can display full details of the selected request, if any.<br>
<br>
Update Function:<br>
1. Update part of item<br>
   Update part of item, such as category name, item name, description, price, stock.<br>
2. Delete item<br>
   There is a conditional statement for this function. If the item still has an active promo, there is a notice that if we proceed, the promotion will also be removed.<br>

Delete Function:<br>
1. Delete item from item's list one by one<br>
2. Delete all item in the same category<br>
3. Delete active promo based on item<br>
4. Delete active promo based on minimum total purchase.<br>
<br>
There is a conditional statement for delete function. If the item still has an active promo, there is a notice that if we proceed, the promotion will also be removed.
<br>
How to use this CRUD Program:
This CRUD Program can only be excuted by owner, manager, and staff of the Merchant that already registered in Dictionary of Merchant's Staff. The input consists of a registered username and password. There are differences in access depending on Staff's role.
<br>
The following are the list of usernames and passwords that have been registered:<br>
1. Username: MT.Owner, Password: 240901<br>
2. Username: MT.Manager, Password: 100401<br>
3. Username: MT.Staff1, Password: 230299<br>
4. Username: MT.Staff2, Password: 150700<br>
5. Username: MT.Staff3, Password 051298<br>
6. Username: MT.Staff4, Password: 030801<br>
