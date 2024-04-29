import sys
import rent
import return_items
import display_items

def main_():
    
    continue_loop=True
    while (continue_loop==True):
        success=False
        while (success==False):
            try:
                
                option=int(input('''\nSelect a desirable option
                  (1)|| press 1 to see costume details
                  (2)|| press 2 to rent a costume
                  (3)|| press 3 to return a costume
                  (4)|| press 4 to exit \nEnter a option:  '''))
                success=True

                if option==1:
                    display_items.display_products()
                   
                elif option==2:
                    print("\nLet's rent the costume\n")
                    rent.display()
                    
                    
                elif option==3:
                    print("\nLet's return the costume\n")
                    return_items.take_data()
                    
                    
                elif option==4:
                    sys.exit("\n   Thank you for using our application\n")
                    continue_loop=False
                    
                
                else:
                    print("\nInvalid input !!! \n    Please select the value as per the provided option")

            except ValueError:
                   print("please enter valid input")        

main_()
