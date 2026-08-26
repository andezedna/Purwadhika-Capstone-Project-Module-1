# Castone Project Module 1
# by Annisa Andez Aunillah

# Merchant Item Sales
# Merchant's name : MOUNTEA TIME

# ======================================================================== DICTIONARY SECTION ========================================================================

# Dictionary Item
dictMenu={
    'Item ID':['ID1','ID2','ID3','ID4','ID5',
               'ID6','ID7','ID8','ID9','ID10',
               'ID11','ID12','ID13','ID14','ID15'],
    'Category':['Coffee','Coffee','Coffee','Coffee','Coffee',
                'Flavor Things','Flavor Things','Flavor Things','Flavor Things','Flavor Things',
                'Tea Time','Tea Time','Tea Time','Tea Time','Tea Time'],
    'Item':['Americano','Cafe Latte','Cappuccino','Mocha','Aren Latte',
            'Matcha Latte','Red Velvet','Taro Latte','Chocolate','Cookies n Cream',
            'Jasmine Tea','Peach Tea','Lemon Tea','Strawberry Tea','Green Tea'],
    'Status':['Active','Active','Active','Active','Active',
              'Active','Active','Active','Active','Active',
              'Active','Active','Active','Active','Active'],
    'Desc':['House Blend','Freshmilk With Espresso','Freshmilk With Espresso','Espresso+Freshmilk+Choco','Coffee+Freshmilk+Palm Sugar',
            'Matcha With Freshmilk','Red Velvet With Freshmilk','Taro With Fresh Milk','Chocolate With Freshmilk','Freshmilk With Oreo',
            'Original Tea','Tea With Peach Slices','Tea With Lemon Slices','Tea With Strawberry Pieces','Original Green Tea'],
    'Price':[15000,20000,20000,20000,23000,
             25000,25000,27000,25000,29000,
             12000,17000,17000,15000,15000],
    'Stock':[20,20,20,20,20,
            15,15,15,15,20,
            30,25,25,25,20]
}

# Dictionary Item Promo
dictItemPromo={
    'Item ID':[],
    'Value':[],
}

# Dictionary Cart Promo
dictCartPromo={
    'Amount Cart':[],
    'Value':[],
}

# Dictionary for user's cart
dictCart={
        'Category':[],
        'Item':[],
        'QTY':[],
        'Price':[],
        'Total':[]
        }

# Dictionary for user's transcation

dictTsc={'ID Tsc':['TSC1','TSC2','TSC3','TSC4','TSC5'],
           'Total Cart':[52000,55000,87000,150000,22000]}

# Dictionary Staff
dictStaff={
    'First Name':['Bae','Kang','Park','Son','Kim','Kim'],
    'Last Name':['Joohyun','Seulgi','Sooyoung','Seungwan','Yerim','Jiwoo'],
    'Username':['MT.Owner','MT.Manager','MT.Staff1','MT.Staff2','MT.Staff3','MT.Staff4'],
    'Role':['Owner','Manager','Staff','Staff','Staff','Staff'],
    'Password':['240901','100401','230299','150700','051298','030801']
}

# ======================================================================== SUB_MENU FUNCTION SECTION ========================================================================

# Function display_menu() : to Display Menu List
def display_menu():
    print("\n","*"*54,"📝💓 MOUNTEA TIME MENU 💓📝","*"*54,"\n")
    print("-"*140)
    print(f"| {'Item ID':<15}| {'Category':<15}| {'Item':20}| {'Status':<15}| {'Desc':<30}| {'Price':<15}| {'Stock':<15}|")
    print("-"*140)
    if len(dictMenu['Item'])==0:
        print('[‼️] There is no item exist in menu list.')

    # If len(dictMenu['Item'])!=0
    else:
        for i in range(len(dictMenu['Item'])):
            print(f"| {dictMenu['Item ID'][i]:<15}| {dictMenu['Category'][i]:<15}| {dictMenu['Item'][i]:<20}| {dictMenu['Status'][i]:<15}| {dictMenu['Desc'][i]:<30}| Rp {dictMenu['Price'][i]:<12,}| {dictMenu['Stock'][i]:<15}|")

    print("\n\n")

# Function add_menu() :  to Add New Menu
def add_menu():
    while True:
        newItem=input('Do you want to add new item? (y/n): ').lower()
        if newItem=="y":
            # Input category name for new item
            while True:
                addCat=input('Input category for new item (max. 15 char): ').title()
                if len(addCat)<=15:
                    dictMenu['Category'].append(addCat)
                    break
                else:
                    print('[‼️] Category name is too long.')

            # Input item name for new item
            while True:
                addItem=input('Input new item name (max. 20 char): ').title()
                if len(addItem)<=20:
                    dictMenu['Item'].append(addItem)
                    break
                else:
                    print('[‼️] Item name is too long.')

            # Input desc for new item
            while True:
                addDesc=input('Input new desc for new item: ').title()
                if len(addDesc)<=30:
                    dictMenu['Desc'].append(addDesc)
                    break
                else:
                    print('[‼️] Desc item is too long.')

            #  Input price for new item
            while True:
                addPrice=int(input('Input price for new item: '))
                if addPrice>0:
                    dictMenu['Price'].append(addPrice)
                    break
                else:
                     print('[‼️] Price format incorrect.')

            #  Input stock for new item
            while True:
                addStock=int(input('Input stock for new item: '))
                if addStock>=0:
                    dictMenu['Stock'].append(addStock)
                    break
                else:
                    print('[‼️] Stock format incorrect.')

            # Add Item Status for New Item
            dictMenu['Status'].append('Active')

            # Add Item ID for New Item
            for i in dictMenu['Item ID']:
                idx=[int(i.replace('ID',''))]
            checking=max(idx)+1
            newItemID='ID'+str(checking)
            dictMenu['Item ID'].append(newItemID)
            
            print(f'[✨] Item {addItem} was successfully added to menu list!')

            # To Display Menu List
            display_menu()

        elif newItem=="n":
            break

        else:
            print('[‼️] You entered wrong code. Please enter y or n.')

# Function add_promo_item() : to Add Promotion Based on Item
def add_promo_item():
    while True:
        newPromo=input('Enter item ID you want to create its promo: ').upper()

        if newPromo in dictItemPromo['Item ID']:
            print('[‼️] You cant add multiple promo.')

        elif newPromo not in dictItemPromo['Item ID']:
            if newPromo in dictMenu['Item ID']:
                ValueItemPromo=int(input('Enter discount amount in %: '))
                ValueItemPromo=ValueItemPromo/100
                dictItemPromo['Item ID'].append(newPromo)
                dictItemPromo['Value'].append(ValueItemPromo)
                print('[✨] Promo was successfully active!')
                diplay_promo_list()
                break

            else:
                print(f"[‼️] Item ID not exist. Please enter the correct Item ID.")

# Function add_promo_cart(): to Add Promotion Based on Total Cart
def add_promo_cart():
    while True:
        ValueTotalCart=int(input('Enter the minimun total purchase to qualify the promotion: '))

        if ValueTotalCart in dictCartPromo['Amount Cart']:
            print('[‼️] You cant add multiple promo with same minimum total purchase.')

        else:
            ValueDisc=int(input('Enter discount amount in %: '))
            ValueDisc=ValueDisc/100
            dictCartPromo['Amount Cart'].append(ValueTotalCart)
            dictCartPromo['Value'].append(ValueDisc)
            print('[✨] Promo was successfully active!')
            diplay_promo_list()
            break

# Function diplay_promo_list() : to Display Promo List
def diplay_promo_list():
    # Display Promotion Based on Item
    print("*"*20,"📝💓 MOUNTEA TIME ITEM PROMO 💓📝","*"*20,"\n")
    print("-"*74)
    print(f"| {'Item ID':<15}| {'Category':<15}| {'Item':<20}| {'Promo':<15}|")
    print("-"*74)
    if len(dictItemPromo['Item ID'])==0:
        print('\n[‼️] There is no active item promotion.')

    # If len(dictItemPromo['Item ID'])!=0
    else: 
        for i in range(len(dictItemPromo['Item ID'])):
            print(f"| {dictItemPromo['Item ID'][i]:<15}| {dictMenu['Category'][dictMenu['Item ID'].index(dictItemPromo['Item ID'][i])]:<15}| {dictMenu['Item'][dictMenu['Item ID'].index(dictItemPromo['Item ID'][i])]:<20}| {(dictItemPromo['Value'][i])*100}%{'':<10}|")

    # Display Promotion Based on Minimun Total Purchase
    print("\n","*"*8,"📝💓 MOUNTEA TIME PROMO WITH MINIMUM TOTAL PURCHASE 💓📝","*"*8)
    if len(dictCartPromo['Amount Cart'])==0:
        print('\n[‼️] There is no active promotion with minimun total purchase.')

    # If if len(dictCartPromo['Amount Cart'])!=0
    else:
        for i in range(len(dictCartPromo['Amount Cart'])):
            print(f"{i+1}. Get discount {(dictCartPromo['Value'][i])*100}% with minimum purchase Rp {dictCartPromo['Amount Cart'][i]:,} 🤩")

    print("\n\n")
# Function add_new_promo() :  to Add New Promo
def add_new_promo():
    while True:
        addPromo=int(input("""
        Type of Promo:
        1. Promotion based on item
        2. Promotion based on total cart value
        Enter the number code you want to create its promo: """))

        # If user choose number 1 (User want to add promotion based on item)
        if addPromo==1:
            add_promo_item()
            break

        # If user choose number 2 (User want to add promotion based on total cart)
        elif addPromo==2:
            add_promo_cart()
            break

        else:
            print('[‼️] You entered wrong number. Please enter number code 1-2.')
            
def delete_category():
    while True:
        delCat=input('Enter Category Name you want to delete: ').title()
        if delCat in dictMenu['Category']:
            #idx_cat : Index list from category that will be deleted
            idx_cat=[]

            # idx_item_id : Item ID list from category that will be deleted
            idx_item_id=[]
            for i, j in enumerate(dictMenu['Category']):
                if j==delCat:
                    idx_cat.append(i)
                    idx_item_id.append(dictMenu['Item ID'][i])

            # idx_cat_promo : Item ID that still have an active promotion
            idx_cat_promo=list(set(idx_item_id).intersection(set(dictItemPromo['Item ID'])))

            if len(idx_cat_promo)!=0:
                for i in idx_cat_promo:
                    print(f"[‼️] Item {dictMenu['Item'][dictMenu['Item ID'].index(i)]} still have an active promotion.")

                checking_del_cat=input(f"""
                If you delete this item, its promo will be deleted too.
                Are you sure to delete category {delCat}? (y/n): """).lower()

                if checking_del_cat=="y":
                    for i in idx_cat_promo:
                        CatToPromo=dictItemPromo['Item ID'].index(i)
                        del dictItemPromo['Item ID'][CatToPromo]
                        del dictItemPromo['Value'][CatToPromo]
                    print(f'[✨] Category {delCat} and its promo was successfully deleted!')

                elif checking_del_cat=="n":
                    continue

                else:
                    print('[‼️] Your input is invalid.')
                    continue
            else:
                print(f'[✨] Category {delCat} was successfully deleted!')

            for i in sorted(idx_cat, reverse=True):
                del dictMenu['Item ID'][i]
                del dictMenu['Category'][i]
                del dictMenu['Item'][i]
                del dictMenu['Status'][i]
                del dictMenu['Desc'][i]
                del dictMenu['Stock'][i]
                del dictMenu['Price'][i]

            break
                
        else:
           print('[‼️] Your input is invalid.')

def delete_menu():
    while True:
        delItem=input('Enter item ID you want to delete: ').upper()
        if delItem in dictMenu['Item ID']:
            idx_del_item=dictMenu['Item ID'].index(delItem)
            if delItem in dictItemPromo['Item ID']:
                print(f"[‼️] Item {dictMenu['Item'][dictMenu['Item ID'].index(delItem)]} still have an active promo.")
                checking_del=input(f"""
                If you delete this item, its promo will be deleted too.
                Are you sure to delete item ID {delItem}? (y/n): """).lower()
                if checking_del=="y":
                    idx_del_promo=dictItemPromo['Item ID'].index(delItem)
                    del dictItemPromo['Item ID'][idx_del_promo]
                    del dictItemPromo['Value'][idx_del_promo]
                    print(f"[✨] Item {dictMenu['Item'][dictMenu['Item ID'].index(delItem)]} its promo was successfully deleted from menu & promo list!")
                    break

                elif checking_del=="n":
                    continue
                else:
                    print('[‼️] Your input is invalid.')
                    continue
            else:
                print(f"[✨] Item {dictMenu['Item'][dictMenu['Item ID'].index(delItem)]} was successfully deleted from menu list!")

            del dictMenu['Item ID'][idx_del_item]
            del dictMenu['Category'][idx_del_item]
            del dictMenu['Item'][idx_del_item]
            del dictMenu['Status'][idx_del_item]
            del dictMenu['Desc'][idx_del_item]
            del dictMenu['Stock'][idx_del_item]
            del dictMenu['Price'][idx_del_item]
        
            break

        else:
            print(f'[‼️] Item with Item ID {delItem} not found. Please enter the correct Item ID.')

# Function delete_promo(): to Delete Promo
def delete_promo():
    while True:
        delPromo=int(input("""
        Type of Promo:
        1. Promotion basen on item
        2. Promotion based on total cart value
        Enter the number code you want to create its promo: """))
    
        # If user choose number 1 (User want to add promotion basen on item)
        if delPromo==1:
            delete_promo_item()
            break

        elif delPromo==2:
            delete_promo_cart()
            break

        else:
            print('[‼️] You entered wrong number. Please enter number code 1-2.')

# Function delete_promo_item() :  to Delete Promo Based on Item
def delete_promo_item():
    while True:
        delPromoItem=input('Enter item ID you want to delete its promotion: ').upper()
        if delPromoItem not in dictMenu['Item ID']:
            print(f'[‼️] Item with Item ID {delPromoItem} not found. Please enter the correct Item ID.')

        elif delPromoItem not in dictItemPromo['Item ID']:
            print(f"[‼️] There are no active promotion for item {dictMenu['Item'][dictMenu['Item ID'].index(delPromoItem)]}.")

        # If delPromoItem in dictItemPromo['Item ID]:
        else:
            idx_del_promo=dictItemPromo['Item ID'].index(delPromoItem)
            del dictItemPromo['Item ID'][idx_del_promo]
            del dictItemPromo['Value'][idx_del_promo]
            print(f'[✨] Active promo on item {dictMenu['Item'][dictMenu['Item ID'].index(delPromoItem)]} was successfully deleted !')
            break

# Function delete_promo_cart() :  to Delete Promo Based on Minimun Total Purchase
def delete_promo_cart():
    while True:
        delPromoCart=int(input('Enter minimun total purchase promotion you want to delete: '))
        if delPromoCart not in dictCartPromo['Amount Cart']:
            print(f'Minimun total purchase {delPromoCart} not found. Please enter the correct minimum total purchase promotion.')

        # If delPromoItem in dictCartPromo['Amount Cart']
        else: 
            idx_promo_cart=dictCartPromo['Amount Cart'].index(delPromoCart)
            del dictCartPromo['Amount Cart'][idx_promo_cart]
            del dictCartPromo['Value'][idx_promo_cart]
            print(f'[✨] Active promo with minimum total purchase Rp {delPromoCart:,} was successfully deleted !\n')
            break

# Function display_cart() : Display User's Cart
def display_cart():
    # User Cart Calculation
    global total_shop
    total_shop=0
    for i in range(len(dictCart['Item'])):
        total_shop+=dictCart['QTY'][i]*dictCart['Price'][i]

    valueCartPromo=[]
    for i in dictCartPromo['Amount Cart']:
        if total_shop>i:
            valueCartPromo=[i]

    for i in dictTsc['ID Tsc']:
        idx_tsc=[int(i.replace('TSC',''))]
    checking=max(idx_tsc)+1
    newTSC='TSC'+str(checking)
    dictTsc['ID Tsc'].append(newTSC)
    
    print('*'*24,'🛒🛒🛒🛒🛒 HELLO, THIS IS YOUR CART! 🛒🛒🛒🛒🛒','*'*24,'\n')
    print(f'Transaction ID : {newTSC}\n')
    print('-'*96)
    print(f'| {'Category':<15}| {'Item':<20}| {'QTY':<15}| {'Price':<15}| {'Total':<20}|')
    print('-'*96)
    for i in range(len(dictCart['Item'])):
        print(f'| {dictCart['Category'][i]:<15}| {dictCart['Item'][i]:<20}| {dictCart['QTY'][i]:<15}| Rp {dictCart['Price'][i]:<12,.0f}| Rp {dictCart['Total'][i]:<17,.0f}|')
    print('-'*96)

    # Qualifying Promotion
    if len(valueCartPromo)>0:
        choosenPromo=max(valueCartPromo)
        idx_choosen_promo=dictCartPromo['Value'][dictCartPromo['Amount Cart'].index(choosenPromo)]
        print(f"{'':<58}{'Purchase Total':<15}| Rp {total_shop:<17,.0f}|")
        total_shop=total_shop*(1-idx_choosen_promo)
        print(f"{'':<58}{'Discount':<15}| {idx_choosen_promo*100:.0f}%{'':<17}|")

    print(f"{'':<58}{'Payment Total':<15}| Rp {total_shop:<17,.0f}|")
    
# Function user_cart() : to Add item on User's cart
def user_cart():
    while True:
        # If user want to add item to cart
        addCart=input("Do you want to add an item to your cart? (y/n): ").lower()
        if addCart=="y":
            pass
        elif addCart=="n":
            break
        else:
            continue

        # Add Item to the Cart
        while True:
            itemCart=input('Enter item ID you want to add to your cart : ').upper()
            if itemCart in dictMenu['Item ID']:
                dictCart['Category'].append(dictMenu['Category'][dictMenu['Item ID'].index(itemCart)])
                dictCart['Item'].append(dictMenu['Item'][dictMenu['Item ID'].index(itemCart)])
                break
            else: #dictMenu['Item ID'].index(dictItemPromo['Item ID'][i]
                print(f'[‼️] Item with Item ID {itemCart} not found. Please enter the correct Item ID.')

        # Add QTY Item to the Cart
        while True:
            QTYCart=int(input(f'Enter the quantity of item {dictMenu['Item'][dictMenu['Item ID'].index(itemCart)]} you want to buy: '))
            if QTYCart<=dictMenu['Stock'][dictMenu['Item ID'].index(itemCart)]:
                dictCart['QTY'].append(QTYCart)
                dictMenu['Stock'][dictMenu['Item ID'].index(itemCart)]-=QTYCart
                break
            else:
                print('Insufficient stock. Please reduce the quantity or choose another item.')

        # If item have an active promotion
        if itemCart in dictItemPromo['Item ID']:
            itemDisc=dictItemPromo['Value'][dictItemPromo['Item ID'].index(itemCart)]
            nettPrice=round(dictMenu['Price'][dictMenu['Item ID'].index(itemCart)])*(1-itemDisc)
            dictCart['Price'].append(nettPrice)

        else:
            nettPrice=(dictMenu['Price'][dictMenu['Item ID'].index(itemCart)])
            dictCart['Price'].append(nettPrice)

        dictCart['Total'].append(nettPrice*QTYCart)
                      
        display_cart()

# Function user_payment() : to Payment
def user_payment():
    global total_shop

    for key in dictCart:
        dictCart[key].clear()
    
    while True:
        addPayment=int(input("""
        Payment Type:
        1. Cash
        2. Cashless
        Enter the payment type you want to choose: """))

        # If user choose payment type: Cash
        if addPayment==1:
            total_shop=total_shop-total_shop%1000+round((total_shop%1000)/100)*100
            dictTsc['Total Cart'].append(total_shop)
            while True:
                userPayment=int(input('Submit the payment: '))
                if userPayment>total_shop:
                    print(f'Thank you for shopping at Mountea Time. Your change Rp {(userPayment-total_shop):,}')
                    break
                elif userPayment==total_shop:
                    print(f'Thank you for shopping at Mountea Time. You have the exact amount, there is no change.')
                    break
                else:
                    print(f'Your payment is short by Rp {(total_shop-userPayment):,}')
                    total_shop-=userPayment
            
            return
        # If user choose payment type: Cashless
        elif addPayment==2:
            dictTsc['Total Cart'].append(total_shop)
            while True:
                userPayment=int(input('Submit the payment: '))
                if userPayment==total_shop:
                    print(f'Thank you for shopping at Mountea Time.')
                    break
                # If userPayment!=total_shop
                else:
                    print(f'You entered incorrect amount.')

            return

        else:
           print(f'[‼️] Number code not found. Please enter the correct number code from Payment Type List.')


# Function update_menu() : To Update Menu
def update_menu():
    while True:
        updt_item_id=input('Enter item ID you want to update: ').upper()
        if updt_item_id in dictMenu['Item ID']:
            updt_menu=int(input("""
            Part of Menu:
            1. Category Name
            2. Item Name
            3. Desc Item
            4. Price Item
            5. Stock Item
            
            Choose part of menu you want to update: """))

            # If user choose to update Category Name of Item
            idx_updt_item=dictMenu['Item ID'].index(updt_item_id)
            if updt_menu==1:
                while True:
                    updt_cat=input(f"Enter new category name for item {dictMenu['Item'][idx_updt_item]} (max. 15 char): ").title()
                    if len(updt_cat)<=15:
                        dictMenu['Category'][idx_updt_item]=updt_cat
                        print(f"[✨] Category name update successful. Item {dictMenu['Item'][idx_updt_item]}'s category name now is {updt_cat}.")
                        break
                    else:
                        print('[‼️] Category name is too long.')

                break

            # If user choose to update Item Name
            elif updt_menu==2:
                while True:
                    updt_item_name=input(f"Enter new item name for item {dictMenu['Item'][idx_updt_item]} (max. 20 char): ").title()
                    if len(updt_item_name)<=20:
                        dictMenu['Item'][idx_updt_item]=updt_item_name
                        print(f"[✨] Item name update successful. Item {dictMenu['Item'][idx_updt_item]}'s category name now is {updt_item_name}.")
                        break
                    else:
                        print('[‼️] Item name is too long.')

                break

            # If user choose to update Desc Item
            elif updt_menu==3:
                while True:
                    updt_item_desc=input(f"Enter new desc for item {dictMenu['Item'][idx_updt_item]}: ").title()
                    if len(updt_item_desc)<=30:
                        dictMenu['Desc'][idx_updt_item]=updt_item_desc
                        print(f"[✨] Desc item update successful. Item {dictMenu['Item'][idx_updt_item]}'s desc now is {updt_item_desc}.")
                        break
                    else:
                        print('[‼️] Desc item is too long.')

                break

            # If user choose to update Price Item
            elif updt_menu==4:
                if updt_item_id in dictItemPromo['Item ID']:
                    checking_updt=input(f"""
                    [‼️] Item {dictMenu['Item'][dictMenu['Item ID'].index(updt_item_id)]} still have an active promo. 
                    
                    Will you still proceed with the price update? (y/n) : """).lower()
                    if checking_updt=="y":
                        while True:
                            updt_price=int(input(f"Enter new price for item {dictMenu['Item'][idx_updt_item]}: "))
                            if updt_price>0:
                                dictMenu['Price'][idx_updt_item]=updt_price
                                print(f"[✨] Price item update successful. Item {dictMenu['Item'][idx_updt_item]}'s price now is Rp {updt_price:,}.")
                                break
                            else:
                                print('[‼️] Price format incorrect.')

                        break
                        
                    elif checking_updt=="n":
                        continue

                    else:
                        f'[‼️] Your input is incorret. Please enter y or n.'

                # if updt_item_id not in dictItemPromo['Item ID']
                else:
                    while True:
                        updt_price=int(input(f"Enter new price for item {dictMenu['Item'][idx_updt_item]}: "))
                        if updt_price>0:
                            dictMenu['Price'][idx_updt_item]=updt_price
                            print(f"[✨] Price item update successful. Item {dictMenu['Item'][idx_updt_item]}'s price now is Rp {updt_price:,}.")
                            break
                        else:
                            print('[‼️] Price format incorrect.')
                    
                    break
            # If user choose to update Stock Item
            elif updt_menu==5:
                while True:
                    check_stock=input("""
                    Type of Update Stock:
                    1. Increase Stock (I)
                    2. Decrease Stock (D)

                    Enter I for increase stock, enter D for decrease stok: """).upper()
                    if check_stock=="I":
                        i_stock=int(input(f"Enter amount of stock to be added for item {dictMenu['Item'][idx_updt_item]}: "))
                        dictMenu['Stock'][idx_updt_item]+=i_stock
                        print(f"[✨] Stock update successful. Item {dictMenu['Item'][idx_updt_item]}'s stock now is {dictMenu['Stock'][idx_updt_item]}.")
                        break
                    elif check_stock=="D":
                        while True:
                            i_stock=int(input(f"Enter amount of stock to be reduced for item {dictMenu['Item'][idx_updt_item]}: "))
                            if i_stock>dictMenu['Stock'][idx_updt_item]:
                                print(f"Only {dictMenu['Stock'][idx_updt_item]} items remain in stock. Please dont enter a quantity exceeding the maximum.")
                            else:
                                dictMenu['Stock'][idx_updt_item]-=i_stock
                                print(f"[✨] Stock update successful. Item {dictMenu['Item'][idx_updt_item]}'s stock now is {dictMenu['Stock'][idx_updt_item]}.")
                                break
                
                    else:
                        print(f'[‼️] Your input is incorret. Please enter the correct code from the List.')

                break

            # If user not choose 1-5
            else:
                print(f'[‼️] Your input is incorret. Please enter the correct number code from the List.') 
        
        # If updt_item_id not in dictMenu['Item ID'] & dictDelMenu['Item ]
        else:
            print(f'[‼️] Item with Item ID {updt_item_id} not found. Please enter the correct Item ID.')

def search_menu():
    search_input=int(input("""
    Keyword's search:
    1. Item ID
    2. Category
    3. Item Name

    Choose keyword you want to search by: """))

    if search_input==1:
        while True:
            search_item_id=input('Enter Item ID you want to search: ').upper()
            if search_item_id in dictMenu['Item ID']:
                print(f"""
                Here are the item's details you are looking for:
                Item ID         : {search_item_id}
                Category Name   : {dictMenu['Category'][dictMenu['Item ID'].index(search_item_id)]}
                Item Name       : {dictMenu['Item'][dictMenu['Item ID'].index(search_item_id)]}
                Item Desc       : {dictMenu['Desc'][dictMenu['Item ID'].index(search_item_id)]}
                Item Price      : Rp {dictMenu['Price'][dictMenu['Item ID'].index(search_item_id)]:,}
                Item Stock      : {dictMenu['Stock'][dictMenu['Item ID'].index(search_item_id)]}""")

                if search_item_id in dictItemPromo['Item ID']:
                    print(f"\t\tPromo Value     : {dictItemPromo['Value'][dictItemPromo['Item ID'].index(search_item_id)]*100}%")
                else:
                    print("\t\tPromo Value     : -\n")
                    
                break

            else :
                print(f'[‼️] Item with Item ID {search_item_id} not found. Please enter the correct Item ID.')

    elif search_input==2:
        while True:
            search_cat=input('Enter Category Name you want to search: ').title()
            if search_cat in dictMenu['Category']:
                # idx_item_id : Item ID list from category that will be search
                idx_item_id=[]
                idx_cat=[]
                for i, j in enumerate(dictMenu['Category']):
                    if j==search_cat:
                        idx_cat.append(i)
                        idx_item_id.append(dictMenu['Item ID'][i])
                
                # idx_cat_promo : Item ID have an active promotion
                idx_cat_promo=list(set(idx_item_id).intersection(set(dictItemPromo['Item ID'])))

                print("Here are the item's details you are looking for:")
                for i in idx_cat:
                    print(f"""
                    Item ID         : {dictMenu['Item ID'][i]}
                    Category Name   : {dictMenu['Category'][i]}
                    Item Name       : {dictMenu['Item'][i]}
                    Item Desc       : {dictMenu['Desc'][i]}
                    Item Price      : Rp {dictMenu['Price'][i]:,}
                    Item Stock      : {dictMenu['Stock'][i]}""")
                    if j in idx_cat_promo:
                        print(f"\t\t    Promo Value     : {dictItemPromo['Value'][dictItemPromo['Item ID'].index(j)]*100}%\n")
                    else:
                        print("\t\t    Promo Value     : -")
                break

            else:
                 print(f'[‼️] Category {search_cat} not exist. Please enter the correct Category Name.')

    elif search_input==3:
        while True:
            search_item_name=input('Enter Item Name you want to search: ').title()
            if search_item_name in dictMenu['Item']:
                idx_item_name=dictMenu['Item'].index(search_item_name)
                print(f"""
                Here are the item's details you are looking for:
                Item ID         : {dictMenu['Item ID'][idx_item_name]}
                Category Name   : {dictMenu['Category'][idx_item_name]}
                Item Name       : {dictMenu['Item'][idx_item_name]}
                Item Desc       : {dictMenu['Desc'][idx_item_name]}
                Item Price      : Rp {dictMenu['Price'][idx_item_name]:,}
                Item Stock      : {dictMenu['Stock'][idx_item_name]}""")

                if dictMenu['Item ID'][idx_item_name] in dictItemPromo['Item ID']:
                    print(f"\t\tPromo Value     : {dictItemPromo['Value'][dictItemPromo['Item ID'].index(search_item_id)]*100}%")
                else:
                    print(f"\t\tPromo Value     : -\n")
                break

            else :
                print(f'[‼️] Item {search_item_name} not found. Please enter the correct Item Name.')

    else:
        print(f'[‼️] Your input is incorret. Please enter the correct code from the List.')

# ======================================================================== EMPLOYEE LOGIN'FUNCTION SECTION ========================================================================

def user_login():
    print("Welcome! Please Login First...")
    while True:
        username=input('Enter your username: ')
        password=input('Enter your password: ')
        if username in dictStaff['Username']:
            if dictStaff['Password'][dictStaff['Username'].index(username)]==password:
                print('Login successful!')
                user_main_menu(username)
                break
            else:
                print('[‼️] Wrong password. Please try again.')

        else:
            print('[‼️] Username not found. Please try again.')


def user_main_menu(a):
    role=dictStaff['Role'][dictStaff['Username'].index(a)]
    first_name=dictStaff['First Name'][dictStaff['Username'].index(a)]
    last_name=dictStaff['Last Name'][dictStaff['Username'].index(a)]

    print(f'[🚀] Welcome {first_name} {last_name}!\n')

    if role=='Owner' or role=='Manager':
        main_menu()
        
    # If dictStaff['Role'][role]=='Staff'
    else:
        staff_main_menu()

# ======================================================================== MAIN MENU'S FUNCTION SECTION ========================================================================

# To Display Main Menu, access for role Owner & Manager
def main_menu():
    # Display Main Menu
    print("="*44,"✨ WELCOME TO MOUNTEA TIME! 🍵🧋✨","="*44)
    user=int(input("""
    Our Main Menu :
    1. Display Menu List
    2. Display Active Promo
    3. Search Item
    4. Add New Menu
    5. Add New Promo
    6. Update Menu
    7. Delete Category
    8. Delete Menu
    9. Delete Promo
    10. Exit Program

    Enter the number code you want to run: """))
    # If user want to Display Menu List
    if user==1:
        display_menu()
        main_menu()

    # If user want to Display Active Promo
    elif user==2:
        diplay_promo_list()
        main_menu()
    
    elif user==3:
        search_menu()
        main_menu()

    # If user want to Add New Menu
    elif user==4:
        add_menu()
        main_menu()

    # If user want to Add New Promo
    elif user==5:
        add_new_promo()
        main_menu()

    # If user want to Update Menu
    elif user==6:
        update_menu()
        main_menu()

    # If user want to Delete Category
    elif user==7:
        delete_category()
        main_menu()

    # If user want to Delete Menu
    elif user==8:
        delete_menu()
        main_menu()

    # If user want to Delete Promo
    elif user==9:
        delete_promo()
        main_menu()

    # If user want to Exit Program
    elif user==10:
        print("="*33,"👋👋👋 Thank you for visiting Mountea Time. See you again! 👋👋👋","="*33)

    # Else (not choose number 1-10)
    else:
        print("[‼️] You entered wrong number. Please enter number code 1-10.")
        main_menu()

def staff_main_menu():
    while True:
        # Display Main Menu
        print("="*44,"✨ WELCOME TO MOUNTEA TIME! 🍵🧋✨","="*44)
        user=int(input("""
        Our Main Menu :
        1. Display Menu List
        2. Display Active Promo
        3. Search Item
        4. Buy Item
        5. Exit Program

        Enter the number code you want to run: """))
        # If user want to Display Menu List
        if user==1:
            display_menu()

        # If user want to Display Active Promo
        elif user==2:
            diplay_promo_list()
        
        elif user==3:
            search_menu()

        # If user want to Add New Menu
        elif user==4:
            user_cart()
            if len(dictCart['Item'])>0:
                user_payment()
            else:
                print('[‼️] Your cart is empty.')
            
        # If user want to Exit Program
        elif user==5:
            print("="*33,"👋👋👋 Thank you for visiting Mountea Time. See you again! 👋👋👋","="*33)
            break

        # Else (not choose number 1-5)
        else:
            print("[‼️] You entered wrong number. Please enter number code 1-5.")

# ======================================================================== EMPLOYEE LOGIN'FUNCTION SECTION ========================================================================

print(user_login())

# =================================================================================================================================================================================
