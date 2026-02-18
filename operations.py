from conn_ext import db_connection

def fetch_daily_summary()->tuple:
    """This functions fetches productname, quantity and sum of price and quantity of daily
    order as per the current date."""

    with db_connection() as conn:
        cur = conn.cursor()
        cur.execute("""SELECT p.name, o.quantity, SUM(p.price * o.quantity) AS revenue
            FROM orders o
            JOIN products p ON p.product_id = o.product_id 
            WHERE o.is_delete = FALSE AND o.purchase_date = CURRENT_DATE
            GROUP BY p.name, o.quantity
            """)
        return cur.fetchall()



def daily_summary()->None | bool:
    """This function gave the daily order summary
    
    retuns:It retuns false if no daily summary."""

    
    rows = fetch_daily_summary()
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
    

def fetch_supplier_purchase()->tuple:
    """This function fetches supplier name, product name,
    number of purchases from supplier and sum of total quantity we purchase."""

    with db_connection() as conn:
        cur = conn.cursor()

        query = """SELECT s.name ,pro.name, COUNT(pro.name), SUM(p.quantity)
                FROM suppliers s
                JOIN purchases p ON s.supplier_id = p.supplier_id
                JOIN products pro ON p.product_id = pro.product_id
                GROUP BY s.name, pro.name
                """
        
        
        cur.execute(query)
        return cur.fetchall()


def supplier_purchase()->None | bool:
    """This function is give the summary of all supplier.
     
    This function calls the diffrent functions as per needs and 
    gave the total trasaction and total units supplies
    
    retuns: It retuns false if the no data found.
    """

    rows = fetch_supplier_purchase()
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

def fetch_products()->tuple:
    """This function fetch name,quantity and price from products.
    
    return: Tuple of the name,quantity and price
    
    """
    with db_connection() as conn:
        cur = conn.cursor()

        query = """SELECT name,quantity,price FROM products"""

        cur.execute(query)
        return cur.fetchall()

def show_products()->None:
    """This Function is showing alailble stock after
    purchases. It shows updated stock after purchased new stock"""

    
    rows = fetch_products()
    #print the products
    print("========================================================")
    print("Product name || Quantity || Price per unit")
    for data in rows:
        print(f"{data[0]}   ||   {data[1]}      ||     {data[2]} ")

def extract_olderdata()->tuple:
    """This function Extract the older data from order grater then 30 days."""
    with db_connection() as conn:
        cur = conn.cursor()

        query = """SELECT purchase_date - CURRENT_DATE  , order_id
                FROM orders
                """
        
        cur.execute(query)
        return cur.fetchall()

def update_olderdata(order_id)->None:
    """This function update the data.
    Args:
        order_id:It update the data is_delete=true when matches the order id.
    """
    with db_connection() as conn:
        cur = conn.cursor()
        query = """UPDATE orders 
            SET is_delete = TRUE 
            WHERE order_id = %s"""
    
        cur.execute(query,(order_id))
        conn.commit()


def set_database()->None:
    """This Function set the database with softdelete 
    more then 30 days older orders
    
    It call the different functions and perform as per requriements."""
  
    #if date is older then 30 then soft delete the data
    rows = extract_olderdata()
    for data in rows:
        if (data[0]> 30):
            order_id = data[1]
            update_olderdata(order_id)

            

    









        

        



        



