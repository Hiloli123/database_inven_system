from conn_ext import cur,conn

def purchase_product(name_of_product:str,name_of_supplier:str,quantity_of_product:int)-> None:

    """This function is used when new purchase.
    It extracts product_id and supplier_id from its name and
    update stock according to given data"""

    #select all things from product
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    product=0
    for data in rows:
        #compare the product name
        if data[1].lower() == name_of_product:
            product+=1
            #take a product id and quantity
            product_id = data[0]
            quantity = data[3]
            
    #if product not found      
    if product == 0:
        print("++++++++++++++++++++++++++++++++++++")
        print("Product name is not available in stock. If it is new product then go to 'Add product' and add product first!")
        print("++++++++++++++++++++++++++++++++++++")
        
        return False

    #for supplier details    
    cur.execute("SELECT * FROM suppliers")
    rows = cur.fetchall()
    supplier=0
    for data in rows:
        #compare the name of supplier if exist
        if data[1] == name_of_supplier:
            supplier_id = data[0]
            supplier += 1

    #if supplier not found
    if supplier == 0:
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("Supplier name is not available in stock. If it is new supplier then go to 'Add supplier' and add supplier first!")
        print("+++++++++++++++++++++++++++++++++++++++")
        
        
        return False
    
    #insert the data in purchases
    query = """INSERT INTO purchases(supplier_id,product_id,quantity) 
            VALUES(%s,%s,%s)"""

    cur.execute(query,(supplier_id,product_id,quantity_of_product))

    #update the products quantity
    query = """UPDATE products 
    SET quantity = %s 
    WHERE name = %s"""
    
    cur.execute(query,(quantity+quantity_of_product, name_of_product))
    conn.commit()

    print("++++++++++++++++++++++++")
    print("Added purchases successfully!")
    print("++++++++++++++++++++++++")

   


    
        

