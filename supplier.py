from conn_ext import cur,conn

def add_supplier(name:str)->None:

    """This function is used to add a supplier
    with its name and contact email is optional"""

    #for check the supplier data if name exist or not
    query = """SELECT name FROM suppliers"""
    cur.execute(query)
    rows=cur.fetchall()
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

        ask = input("Do you have contact email of supplier?y/n :")

        if not ask:
            print("==========================")
            print("Not Entered proper value")
            print("============================")
            add_supplier(name)


        #if email address is availbe
        if ask.lower() == "y":

            contact_email = input("Enter contact Email of supplier:")


            if not contact_email or contact_email.isnumeric()== True:
                print("Not entered the  proper mail")
                add_supplier(name)
            elif "@" not in contact_email or "." not in contact_email:
                print("Entered Not proper Email!")
                add_supplier(name)

            #add the data with name and email
            query = """INSERT INTO suppliers(name,contact_email) 
                VALUES(%s,%s)"""
            cur.execute(query,(name,contact_email))
            conn.commit()
            print("++++++++++++++++++++++++")
            print("Supplier added successfully!")
            print("++++++++++++++++++++++++")
            
            
            
        
        #if no have email
        elif ask.lower() == "n" :
            
            #save data withot email
            query = """INSERT INTO suppliers(name,contact_email) VALUES(%s,%s)"""

            cur.execute(query,(str(name),'NULL'))
            conn.commit()
            
            
            print("=====================")
            print("supplier added!")
            print("======================")
            

        else:
            #no select proper choice
            print("++++++++++++++++++++++++")
            print("You not enter the proper answer!")
            print("++++++++++++++++++++++++")
            add_supplier(name)

    


    
    
    