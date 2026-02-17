from conn_ext import cur,conn


def create_order(name:str,quantity:int)->None:

    """This function is for create order from name and 
    quantity of product. It checks existing stock and then confirm the 
    order."""

    #extract product name and quantity
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    counter=0
    for data in rows:
        if (data[1] == name):
            counter+=1
            #cheack the quantity
            if(data[3] >= quantity) :
                
                #update the quantity after order
                query = """UPDATE products 
                SET quantity = %s 
                WHERE name = %s"""
                
                cur.execute(query,(data[3]-quantity,name))

                query = """INSERT INTO orders(product_id, quantity,is_delete) 
                VALUES(%s,%s,%s)"""

                cur.execute(query,(data[0],quantity,False))
                conn.commit()
                
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

    


def daily_summary()->None:

    """This function gave the daily order summary"""

    cur.execute("""SELECT p.name, o.quantity, SUM(p.price * o.quantity) AS revenue
        FROM orders o
        JOIN products p ON p.product_id = o.product_id 
        WHERE o.is_delete = FALSE AND o.purchase_date = CURRENT_DATE
        GROUP BY p.name, o.quantity
        """)
    
    rows = cur.fetchall()
    #if no data in day
    if len(rows) == 0:
        print("******************")
        print("No Data!!")
        print("******************")
        return False
    print("===========================================")
    #print the data with total
    total = 0
    print("product   ||  Quantity  || Revenue  ")
    for data in rows:
        print(f"{data[0]}     ||    {data[1]}  ||    {data[2]} ")
        total+= data[2]
    
    print("===========================================")
    print("Total Revenue of the day is: ",total)
    print("==================================")
    



def supplier_purchase()->None:

    """This function is give the summary of all supplier and 
    which supplier total trasaction and total units supplies"""


    query = """SELECT s.name ,pro.name, COUNT(pro.name), SUM(p.quantity)
            FROM suppliers s
            JOIN purchases p ON s.supplier_id = p.supplier_id
            JOIN products pro ON p.product_id = pro.product_id
            GROUP BY s.name, pro.name
            """
    
    
    cur.execute(query)
    
    rows = cur.fetchall()
    #if not purchases availble

    if len(rows) == 0:
        print("******************")
        print("No Data!!")
        print("******************")
        return False
    
    #print the data
    print("========================================================")
    print("supplier name || product name|| Numbers of purchases || total quantity")
    for data in rows:
        print(f"{data[0]}   ||   {data[1]}      ||     {data[2]}          ||        {data[3]}")

    print("=========================================================")

def show_products()->None:
    """This Function is showing alailble stock after
    purchases. It shows updated stock after purchased new stock"""

    query = """SELECT name,quantity,price FROM products"""

    cur.execute(query)
    rows = cur.fetchall()
    #print the products
    print("========================================================")
    print("Product name || Quantity || Price per unit")
    for data in rows:
        print(f"{data[0]}   ||   {data[1]}      ||     {data[2]} ")


def set_database()->None:

    """This Function set the database with softdelete 
    more then 30 days older orders"""

    query = """SELECT purchase_date - CURRENT_DATE  , order_id
            FROM orders
            """
    
    cur.execute(query)
    
    #if date is older then 30 then soft delete the data
    rows = cur.fetchall()
    for data in rows:
        if (data[0]> 30):
            order_id = data[1]

            query = """UPDATE orders 
            SET is_delete = TRUE 
            WHERE name = %s"""
    
            cur.execute(query,(order_id))

    









        

        



        



