from conn_ext import *

def add_product(name:str)->None:

    """This function add a new product if not exist or
    if exist then update the product"""

    query = """SELECT name,quantity FROM products"""

    cur.execute(query)

    rows = cur.fetchall()

    product=0

    for data in rows:
        #compare a name if product is availble
        if data[0].lower() == name:
            old_quan = data[1]
            
            product+=1

            print("===========================")
            print("Add the Quantity? y/n: ")
            print("============================")

            #enter the choice yes or no
            ask = input("Enter Your choice: ")

            #if yes
            if ask.lower() == "y":
                new_quantity = int(input("How Many New Quantity you added?:"))

                if (not new_quantity or new_quantity<=0):
                    print("++++++++++++++++++++++")
                    print("You not Entered Proper choice!")
                    print("++++++++++++++++++++++++++++")
                    add_product(name)

                query = """INSERT INTO products(name,quantity) 
                VALUES(%s,%s)
                ON CONFLICT(name) 
                DO UPDATE SET 
                quantity = EXCLUDED.quantity"""

                quantity = old_quan + new_quantity

                cur.execute(query,(name,quantity))
                conn.commit()
                
                print("++++++++++++++++++++++++")
                print("product Updated succesfully!")
                print("++++++++++++++++++++++++")

            #if no
            elif ask.lower() == "n":
                return False
                        

            else:
                print("Not Enter the proper Choice!")
                add_product(name)

    

    if product == 0:

        #if product name not avilable then add the data
        try:
            price = float(input("Enter the Product price: "))
        except Exception as e:
            print("Not Entered proper value of price!")
            add_product(name)


        if not price:
            print("Not Entered Price!")
            add_product(name)

        choice = input("Do you Want Add the Quantity? y/n: ")
        if (not choice or choice.strip()==""):
            print("Not entered Proper Choice. enter only Y or N")

        if choice.lower()=="y":
            quen = int(input("Enter the Quantity of Product: "))
            if (not quen or quen<=0):
                print("Not Entered proper Quantity!")
                add_product(name)

        elif choice.lower() == "n":
            #default quantity when not entered
            quen = 1 

        else:
            print("++++++++++++++++++++")
            print("Not Enter Proper choice!")
            add_product(name)

        #if quantity is added then add the new data
        query = """INSERT INTO products (name,price,quantity)
        VALUES(%s,%s,%s)"""

        cur.execute(query,(name,price,quen))
        conn.commit()
        
        print("==============================")
        print("Product Added Succesfully!")
        print("=================================")





    