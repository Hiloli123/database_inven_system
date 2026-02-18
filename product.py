from conn_ext import db_connection

def fetch_products()->tuple:
    """This function is fetch name and quantity of products from products table"""

    with db_connection() as conn:
        cur = conn.cursor()
        query = """SELECT name,quantity FROM products"""
        cur.execute(query)
        return cur.fetchall()
    
def persist_update_quantity(name:str, quantity:int)->None:
    """This function update the quantity of the product
    Args:
        name(str):name of the product
        quantity(int):Quantity of the product
    """

    with db_connection() as conn:
        cur = conn.cursor()

        query = """INSERT INTO products(name,quantity) 
        VALUES(%s,%s)
        ON CONFLICT(name) 
        DO UPDATE SET 
        quantity = EXCLUDED.quantity"""

        cur.execute(query, (name, quantity))
        conn.commit()

def persist_new_product(name:str, price:float, quen:int)->None:
    """This function add the new product.
    
    Args:
        name(str):Name of the product
        price(float):Price of the product
        quen(int): Product quantity
    """

    with db_connection() as conn:
        cur = conn.cursor()

        query = """INSERT INTO products (name,price,quantity)
        VALUES(%s,%s,%s)"""

        cur.execute(query, (name, price, quen))
        conn.commit()

def add_product(name:str)-> None:
    """This function check if the product exist or not.
    
    If product name is exist then it call all_quantity() function.
    and if name not exist then it call add_new_product() function.
    
    Args:
        name(str):Name of the product
        
    """

    rows = fetch_products()

    product=0

    for data in rows:
        #compare a name if product is availble
        if data[0].lower() == name:
            old_quan = data[1]
            
            product+=1

            add_quantity(name,old_quan)

    if product == 0:
        add_new_product(name)

def add_quantity(name:str,old_quan:int)->None | bool:
    """This Function is for add the quantity
    
    This function ask for the add quantity and add in the old
    quantity and call the persist_update_quantity()
    function for the update the quantity of the product
    
    Args:
        name(str): Name of the product
        old_quan(int): It is Existing quantity which product alreay have.

    return: It return false when the user want no add the quantity.
    """

    print("===========================")
    print("Add the Quantity? y/n: ")
    print("============================")
    
    while True:
        try:
            #enter the choice yes or no
            ask = input("Enter Your choice: ")
            if ask.lower().strip() == "y" or ask.lower().strip() == "n":
                break
        except Exception as e:
            print("Not Entered proper choice!")
    
    
    #if yes
    if ask.lower().strip() == "y":

        while True:
            try:
                new_quantity = int(input("How Many New Quantity you added?:"))
                if new_quantity > 0:
                    break
            except Exception as e:
                print("Enter Wrong Choice!")


        quantity = old_quan + new_quantity

        persist_update_quantity(name,quantity)

        
        print("++++++++++++++++++++++++")
        print("product Updated succesfully!")
        print("++++++++++++++++++++++++")

    #if no
    elif ask.lower().strip() == "n":
        return False
                

def add_new_product(name:str)->None: 
    """This function add the new product inputs and validation.
    
    This function ask the price nad quantity of product call the
    diffrent function based upon inputs.

    Args:
        name(str): Name of the product."""  

    #if product name not avilable then add the data
    while True:
        try:
            price = float(input("Enter the Product price: "))
            if price > 0:
                break
        except Exception as e:
            print("Not Entered proper value of price!")
    

    while True:
        try:
            choice = input("Do you Want Add the Quantity? y/n: ")
            if choice == "y" or choice=="n":
                break
        except Exception as e:
            print("Not Entered proper choice!")
    
    
    if choice.lower()=="y":
        while True:
            try:
                quen = int(input("Enter the Quantity of Product: "))
                if quen > 0:
                    break
            except Exception as e:
                print("Enter Wrong Choice!")

        
    elif choice.lower() == "n":
        #default quantity when not entered
        quen = 1 

    
    #if quantity is added then add the new data
    persist_new_product(name,price,quen)
    
    print("==============================")
    print("Product Added Succesfully!")
    print("=================================")  

def update_product(quantity:int,name:str)->None: 
    """This function add the quantity of the procucts.
    
    Args:
        quantity(int):Quantity of the product.
        name:Name of the product."""  

    with db_connection() as conn:
        cur = conn.cursor()
        query = """UPDATE products 
                    SET quantity = %s 
                    WHERE name = %s"""
                    
        cur.execute(query,(quantity,name))
        conn.commit()

def order_add(id:int,quantity:int,FALSE:bool)->None:
    """This function add the order in ordertable.
    
    Args:
        id(int): Product id .
        quantity(int):Quantity of the product
        False(bool):for soft deleteing use the false."""

    with db_connection() as conn:
        cur = conn.cursor()
        query = """INSERT INTO orders(product_id, quantity,is_delete) 
                    VALUES(%s,%s,%s)"""

        cur.execute(query,(id,quantity,FALSE))
        conn.commit()
                
def fetch_all_product()->tuple:
    
    """This function is fetch name ,id and quantity of products from products table"""

    with db_connection() as conn:
        cur = conn.cursor()
        query = """SELECT * FROM products"""
        cur.execute(query)
        return cur.fetchall()

def create_order(name:str,quantity:int)->bool | None:
    """This function is for create order from name and 
    quantity of product. 
    
    It checks the product and stock of the product
    available as per the order. If it available then it
    confirm the order.
    
    Args:
        name(name): Name of the product
        quantity(int):Quantity of the procut.
        
    retuns: It returns false if the product or stocks not availbe as per the order."""

    #extract product name and quantity
    
        
    rows = fetch_all_product()
    counter=0
    for data in rows:
        if (data[1] == name):
            counter+=1
            #cheack the quantity
            if(data[3] >= quantity) :
                new_quantity=data[3]-quantity
                update_product(new_quantity,name)
                
                #update the quantity after order
                order_add(data[0],quantity,False)
                
                
                print("++++++++++++++++++++++++")
                print("Order is Confirm!")
                print("++++++++++++++++++++++++")

            #if no quantity is sufficient
            else:
                print("++++++++++++++++++++++++")
                print("Quantity is not sufficient!")
                print("++++++++++++++++++++++++")
                
                return False
    #if no product name match
    if (counter == 0):
        print("++++++++++++++++++++++++")
        print("Product is not available")
        print("++++++++++++++++++++++++")
        

        return False
        





    