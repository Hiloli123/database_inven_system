from conn_ext import conn,cur

def create_inventorysys():

    """This function created a all teables in database 
    which needed in inventory system management"""

    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products
    (
        product_id SERIAL PRIMARY KEY NOT NULL,
        name TEXT NOT NULL UNIQUE,
        price NUMERIC(10,2), 
        quantity INT 
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS suppliers
    (
        supplier_id SERIAL PRIMARY KEY NOT NULL,
        name TEXT NOT NULL UNIQUE,
        contact_email TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS purchases
    (
        purchase_id SERIAL PRIMARY KEY NOT NULL,
        supplier_id INT NOT NULL,
        product_id INT NOT NULL,
        quantity INT,
        purchase_date DATE DEFAULT CURRENT_DATE,
        CONSTRAINT fk_products_purchase
            FOREIGN KEY(product_id) 
            REFERENCES products(product_id),
        CONSTRAINT fk_supplier_purchase
            FOREIGN KEY(supplier_id) 
            REFERENCES suppliers(supplier_id)
                
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders
    (
        order_id SERIAL PRIMARY KEY NOT NULL,
        product_id INT,
        quantity INT,
        purchase_date DATE DEFAULT CURRENT_DATE,
        is_delete BOOLEAN DEFAULT FALSE,
        CONSTRAINT fk_products_order 
            FOREIGN KEY(product_id) 
            REFERENCES products(product_id)
        
    )
    """)

    conn.commit()

    




