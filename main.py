from product import add_product
from inventory_system import create_inventorysys
from supplier import add_supplier
from add_purchase import purchase_product
from operations import create_order,daily_summary,supplier_purchase,set_database,show_products
import logging
from conn_ext import conn

logger = logging.getLogger("SimpleLogger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("db_errors.log")
logger.addHandler(file_handler)


def main():

    """This Function is for calling all function as per
    User requirements and handle all error and 
    when error occures print error log and
    User message and it called itself for prevent the crash app."""
    
    
    create_inventorysys()
    set_database()
    print("======INVENTORY SYSTEM===========")
    print("=====================================")
    print("Select your choice:")
    print("1.Add Products/Update Quantity")
    print("2.Add a new Suppliers")
    print("3.Add a new Purchase")
    print("4.Order")
    print("5.Daily Order Summary")
    print("6.Supplier Purchase summary")
    print("7.Show Available Products Stock")
    print("8.Exit the system")
    print("=====================================")

    try:
        choice = int(input("Enter Choice: "))

        if not choice or choice=="" or choice <= 0:
            print("++++++++++++++++++++++++")
            print("Please enter the  proper choice!")
            print("++++++++++++++++++++++++")
            main()
    except TypeError:
        logger.error("This is a Type error %s",TypeError)
        print("++++++++++++++++++++++++")
        print("Wrong Choice Entered!")
        print("++++++++++++++++++++++++")
        main()
    except Exception as e:
        logger.error("This is an Unexpected error %s",e)
        print("++++++++++++++++++++++++")
        print("Wrong Choice Entered!")
        print("++++++++++++++++++++++++")
        main()
 
    if choice == 1:

        try:
 
            name = input("Enter product name: ")

            if (not name or name.strip()=="" or name.isnumeric()==True):
                print("++++++++++++++++++++++++")
                print("Empty product or price not allowed!")
                print("++++++++++++++++++++++++")
                logger.error("Name and Price of product not entered")
                main()

            else:

                add = add_product(name)
            

                if add == False:
                    main()
           
                main()


        except TypeError:
            logger.error("This is a Type error %s",TypeError)
            print("++++++++++++++++++++++++")
            print("Not Enter the proper value")
            print("++++++++++++++++++++++++")
            main()
        except Exception as e:
            logger.error("This is an Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Error",e)
            print("++++++++++++++++++++++++")
            main()
        

    elif choice == 2:

        try:

            name = input("Enter Supplier name: ")

            if (not name or name.strip()=="" or name.isnumeric()==True):

                print("++++++++++++++++++++++++")
                print("Supplier name is not Allowed!")
                print("++++++++++++++++++++++++")
                
                main()
            
            else:
                supplier = add_supplier(name)
                
                if supplier == False:
                    main()
                
                main()

        
        except TypeError as e:
            logger.error("This is a Type error %s",TypeError)
            print("++++++++++++++++++++++++")
            print("Not Enter the proper value",e)
            print("++++++++++++++++++++++++")
            main()
        except Exception as e:
            logger.error("This is an Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Error",e)
            print("++++++++++++++++++++++++")
            main()
        

    elif choice == 3:

        try:

            name_of_product = input("Enter the product name: ")

            name_of_supplier = input("Enter the supplier name: ")

            quantity_of_product = int(input("Enter Quantity of product: "))

            if (not name_of_product or not name_of_supplier or not quantity_of_product
                or name_of_product.strip()=="" or name_of_supplier.strip=="" or quantity_of_product<=0
                or name_of_product.isnumeric()==True or name_of_supplier.isnumeric()==True):

                print("====================================")
                print("You Don't Entered the value which needed!")
                print("======================================")

                main()
            else:

                purchase = purchase_product(name_of_product,name_of_supplier,quantity_of_product)
                
                if purchase == False:
                    main()
                
                main()
            

        except ValueError:
            logger.error("This is a Type error %s",ValueError)
            print("++++++++++++++++++++++++")
            print("Not Enter the proper value")
            print("++++++++++++++++++++++++")
            main()
        except Exception as e:
            logger.error("This is an Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Unexpected Error",e)
            print("++++++++++++++++++++++++")
            main()

    elif choice == 4:

        try:

            name = input("Enter product name: ")

            quantity = int(input("Enter the product Quantity :"))

            if (not name or not quantity or name.strip()=="" or quantity<=0 or name.isnumeric()==True):
                print("==============================")
                print("Name or Quantity is invalid!")
                print("==========================")
                main()

            else:
                order = create_order(name,quantity)
            

                if order == False:
                    main()
                
                main()
        
        except TypeError:
            logger.error("This is a Type error %s",TypeError)
            print("++++++++++++++++++++++++")
            print("Not Enter the proper value")
            print("++++++++++++++++++++++++")
            main()
        except Exception as e:
            logger.error("Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Error",e)
            print("++++++++++++++++++++++++")
            main()
        

    elif choice == 5:
        try:
            d_summary = daily_summary()
            

            if d_summary == False:
                main()
            else:
                main()
            
        except TypeError:
            logger.error("This is a Type error %s",TypeError)
            print("++++++++++++++++++++++++")
            print("Not Enter the proper value")
            print("++++++++++++++++++++++++")
            main()
        except Exception as e:
            logger.error("Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Error",e)
            print("++++++++++++++++++++++++")
            main()

    elif choice == 6:
        try:
            s_purchase = supplier_purchase()
            
            if s_purchase == False:
                main()
            else:
                main()
            
        except TypeError:
            logger.error("This is a Type error %s",TypeError)
            print("++++++++++++++++++++++++")
            print("Not Enter the proper value")
            print("++++++++++++++++++++++++")
            main()
        except Exception as e:
            logger.error("This is an Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Error ",e)
            print("++++++++++++++++++++++++")
            main()

    elif choice == 7:
        try:
            show_products()
            main()
        except Exception as e:
            logger.error("This is an Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Error ",e)
            print("++++++++++++++++++++++++")
            main()


    elif choice == 8:
        if conn:
            conn.close()
            return
        return
        

    else:
        print("++++++++++++++++++++++++")
        print("Not Enter the proper value")
        print("++++++++++++++++++++++++")
        logger.error("Entered the not allowed value")
        main()



if __name__=="__main__":
    main()
    




