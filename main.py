from product import add_product,create_order
from inventory_system import create_inventorysys
from supplier import add_supplier
from add_purchase import purchase_product
from operations import daily_summary,supplier_purchase,set_database,show_products
import logging


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

    while True:

        try:
            choice = int(input("Enter Choice: "))
            break
        except Exception as e:
            print("Wrong Choice Entered!")
            logger.error("Wrong Choice")
        
 
    if choice == 1:
        input_active = True

        while input_active:

            try:
                name = input("Enter product name: ")

                if (name.strip()=="" or name.isnumeric()):
                    input_active = True
                else:
                    input_active=False

            except Exception as e:
                print("Wrong input Entered!")
                logger.error("Wrong Choice")

        try:

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
            logger.exception("This is an Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Error",e)
            print("++++++++++++++++++++++++")
            main()
        

    elif choice == 2:
        input_active = True

        while input_active:

            try:

                name = input("Enter Supplier name: ")

                if (name.strip()=="" or name.isnumeric()):
                    input_active = True
                else:
                    input_active=False

            except Exception as e:
                print("Wrong input Entered!")
                logger.error("Wrong input entered")
            
        try:
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
            logger.exception("This is an Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Error",e)
            print("++++++++++++++++++++++++")
            main()
        

    elif choice == 3:
        input_active = True

        while input_active:

            try:

                name_of_product = input("Enter the product name: ")

                name_of_supplier = input("Enter the supplier name: ")

                quantity_of_product = int(input("Enter Quantity of product: "))

            

                if (name_of_product.strip()=="" or name_of_supplier.strip()=="" or quantity_of_product<=0
                or name_of_product.isnumeric() or name_of_supplier.isnumeric()):
                    input_active = True
                else:
                    input_active=False

            except Exception as e:
                print("Wrong Input Entered!")
                logger.error("Wrong Input Entered")

        try:

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
            logger.exception("This is an Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Unexpected Error",e)
            print("++++++++++++++++++++++++")
            main()

    elif choice == 4:
        input_active = True

        while input_active:

            try:

                name = input("Enter product name: ")

                quantity = int(input("Enter the product Quantity :"))

                if (not name or not quantity or name.strip()=="" or quantity<=0 or name.isnumeric()==True):
                    input_active = True
                else:
                    input_active=False

            except Exception as e:
                print("Wrong Choice Entered!")
                logger.error("Wrong Choice")

        try:

            
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
            logger.exception("Unexpected error %s",e)
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
            logger.exception("Unexpected error %s",e)
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
            logger.exception("This is an Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Error ",e)
            print("++++++++++++++++++++++++")
            main()

    elif choice == 7:
        try:
            show_products()
            main()
        except Exception as e:
            logger.exception("This is an Unexpected error %s",e)
            print("++++++++++++++++++++++++")
            print("Error ",e)
            print("++++++++++++++++++++++++")
            main()


    elif choice == 8:
        
        return
        

    else:
        print("++++++++++++++++++++++++")
        print("Not Enter the proper value")
        print("++++++++++++++++++++++++")
        logger.error("Entered the not allowed value")
        main()



if __name__=="__main__":
    main()
    




