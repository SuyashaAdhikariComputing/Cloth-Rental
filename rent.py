
import datetime
import random

data_dic={} #this is the dictionary to store data in file
total_rent=[]#this store the name of the costume rented
choose_count=[]# this store the id of costume rented
quantity=[] # this store the quantity of the costume rented
detail=[]#this contain detail of bill
brand=[]#this stores choosed brand

'''the display fuction contains the code for adding the data in txt
file to list and dictionary and printing the stock available'''

def display():
    
    count=0# this variable shows the amount of costume present
    print("----"*20)
    print("ID\tCostume Name\t\tBrand\t\tPrice\tQuantity")
    print("----"*20+"\n")
    file = open("data.txt","r")#opens file in read mode
    data = file.read()
    book_data=data.split("\n")
    #print(book_data)
    file.close()

    while '' in book_data:
        book_data.remove('')
    
    for i in range(len(book_data)):
        count = count+1
        #print(book_data[i].split(","))
        '''stores the data in the form of dictionary the count acts as key and
         rest of the data as values'''
        data_dic[count]=book_data[i].split(",")
        
    for key,value in data_dic.items():
        print(key,end="\t")
        for i in value:
            print(i,end="\t")
        print("\n")
    print("----"*20)
    validate(count)# introducing count in function validate

'''This function contains the code for comparing if the entered id match the data in the
text file and if matched then it is checked if the quantity is matched. If everything
is found to be valid then the quantity entered is substracted from the quantity in txt
file and the update data is replaced in the list'''
def validate(c):
    count=c
    #print(c)
    #print(book_dic)
    try:
        option = int(input("\n\nEnter the costume id: "))
    
        'exicutes only when id is available'
        if option > 0 and option <= count:
            choose_count.append(option)#add the id chosed in the list choose_count
            print("\n\nYou can rent the costume")
            
            try:
                qty = int(input("\n\nEnter the required quantity: "))
                select = data_dic[option]#store the values of the id(key) that is choosed

                if qty>0:
                    
                    if int(select[-1]) >= qty:#compare the last data of the list
                        
                        quantity.append(qty)#add the qty chosed in the list quantity
                        total_rent.append(select[0])#add the costume name chosed in the list total_rent
                        brand.append(select[1])
                        print("\n\nSucessfully booked")
                        update=int(select[-1])-qty#decrease the qty
                        select[-1]=update#replace the decreased value in the list
                        update_stock()#calling function update_stock
                        rent_more()#calling the function rent_more
                        
                    else:
                        print("\n\nQuantity above available stock")
                        if len(choose_count)>1:
                            choose_count.remove(-1)
                        else:
                            choose_count.clear()
                        display()#calling the function display
                else:
                    print("quantity can't be negative")
                    display()
                    
            except:
                print("\n\t\tQuantity must be in number")
                if len(choose_count)>1:
                    choose_count.remove(-1)
                else:
                    choose_count.clear()
                display()
                   
        else:
            print("\n\nInvalid Input. Enter the correct costume id")
            display()#calling the function display
    except:
        print("\n\nInvalid Input. Enter the correct data")
        display()


''' this function contains code to write the updated data in the file'''
def update_stock():
    f=open("data.txt","w")#opening file in write mode
    for key,value in data_dic.items():
        d=value
        for i in d:
          if i==d[-1]:#if the data is last item in d 
              f.write(str(i))
          else:#if data is not last item in d
              f.write(str(i))
              f.write(",")
        f.write("\n")
        f.close#close the file

'''this has code if user want to rent more'''
def rent_more():
    count=len(data_dic)
    ask=(input("Do you want to rent more costume Y/N: ").upper())#store in lowercase
    if ask=="Y":
        validate(count)
        
    elif(ask=="N"):
        bill()
        
    else:
        print("enter answer as Y or N")
        rent_more()
    
'''this function is created for the bill and write the data in txt file'''
def bill():
    opt=choose_count#stores the id of costume
    total_price=0
    for i in opt:
        data=data_dic[i]#store the value of certain id(key)stored in opt
        list_price=data[-2]#store the secondlast item of list
        actual_price=(''.join(list_price.split('$')))#remove $ sign from the list_price
        for j in quantity:
            price=j*float(actual_price)#float is used incase the value is in decimal
        total_price=total_price+price
    
        
    name=input("Enter your name: ")
    x = datetime.datetime.now()#has current date and time
    return_date=x + datetime.timedelta(days=5)#add 5 days to current date and time



    print("\n\n")
    print("++++"*20)
    print("\t\t\t\tBill Details")
    print("++++"*20)

    a=random.getrandbits(8)

    print("\nThe ID is: ",a)

    detail.append("The ID is: "+str(a))
        
    print("\nCustomer name: ",name)
    
    detail.append("Customer name: "+str(name))
    
    print("\nThe product rented is: ",end=" ")
    for i in total_rent:
        print(i,end=" ")
    print ("\n")
    
    detail.append("The product rented is: "+str(total_rent))

    print("The brand of the costume is: ",end=" ")
    for i in brand:
        print(i,end=" ")
    print("\n")
        
    detail.append("The brand of the costume is: "+str(brand))
    
    print("The issue date is: ",x.strftime("%x"))#print data in day month year format
    
    detail.append("The issue date is:"+str(x.strftime("%Y/%m/%d")))
    
    print("\nThe price for the product is: ","$"+str(total_price))
    
    detail.append("The price for the product is: "+str(total_price))
    
    print("\nReturn date is: ",return_date.strftime("%x"))
    
    detail.append("Return date is:"+str(return_date.strftime("%Y/%m/%d")))

    print("\n\n Please remember your ID for Return process")
    print("     12 rupee will be added per day when the return date is exceded")

    print("\n")
    print("++++"*20)
    
    
    
    name=str(a)+'.txt'
    # this write the bill details in custom file
    wr=open(name,"w")
    for i in detail:
        wr.write(i)
        wr.write("\n")
    wr.close()
    detail.clear()
    total_rent.clear()
    choose_count.clear()
    quantity.clear()
    
    
    

    
    

    
    

