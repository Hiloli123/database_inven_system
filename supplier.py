from conn_ext import db_connection

def fetch_suppliers():
        """Fetch all suppliers name from supplier table"""

        with db_connection() as conn:
            cur = conn.cursor()
            query = """SELECT name FROM suppliers"""
            cur.execute(query)
            return cur.fetchall()
        
def persist_new_supplier(name:str,contact_email:str)->None:
    """Insert a new supplier in supplier table
    Args:
        name(str):Name of the supplier
        contact_email(str): Contact Email of the supplier"""

    with db_connection() as conn:
        cur = conn.cursor()

        query = """INSERT INTO suppliers(name,contact_email) 
                    VALUES(%s,%s)"""
        cur.execute(query,(name,contact_email))
        conn.commit()

def add_supplier(name:str)-> bool :
    """This function is check the supplier exist or not.
     
     This function is check the supplier name in 
     database and if not available then add to a database.
     
     Args:
        name(str):It is the name of the supplier.
        
    retuns: It returns False when no add the supplier else it
        retuns None
    """

    #for check the supplier data if name exist or not
    rows = fetch_suppliers()

    supplier = 0

    for data in rows:
        #compare the name
        if data[0].lower() == name.lower():
            supplier+=1
            print("=============================")
            print("Supplier name is already Exist!")
            print("=================================")
            
            return False
        
    #if not exist in data then add it
    if supplier == 0:
        add_new_supplier(name)
        

def add_new_supplier(name:str)->None:
    """This Function is added the new supplier
    
    This function handle the inputs if supplier's
    contact email have or not and take the details and
    add the supplier in supplier table.
    
    Args:
        name(str):name of the supplier
         
    retuns: It retuns the none """


            
    while True:
        try:
            #enter the choice yes or no
            ask = input("Do you have contact email of supplier?y/n: ")
            if ask.lower().strip() == "y" or ask.lower().strip() == "n":
                break
        except Exception as e:
            print("Not Entered proper choice!")

    
    #if email address is availbe
    if ask.lower().strip() == "y":

        contact_email = input("Enter contact Email of supplier:")
        

        if not contact_email or contact_email.isnumeric()== True:
            print("Not entered the  proper mail")
            add_new_supplier(name)

        elif "@" not in contact_email or "." not in contact_email:
            print("Entered Not proper Email!")
            add_new_supplier(name)

        #add the data with name and email
        persist_new_supplier(name,contact_email)
        
        print("++++++++++++++++++++++++")
        print("Supplier added successfully!")
        print("++++++++++++++++++++++++")
             
    
    #if no have email
    elif ask.lower().strip() == "n" :

        #save data withot email
        persist_new_supplier(name,contact_email=None)
        
        
        print("=====================")
        print("supplier added!")
        print("======================")
        

            
        


    
    
    