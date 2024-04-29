import rent
import os
import datetime
items=[]#this store items
brand={}#this store brand name with items as key
price={}#this store price with items as key
quantity={}#this store quantity with items as key
data_again=[]#this store data from data.txt
write_li=[]#this store

#this functionn is used to store data from data file
def take_data():

    file = open("data.txt","r")
    data = file.read()
    #print(data)
    book_data=data.split("\n")
    file.close()
    while '' in book_data:
        book_data.remove('')
    #print(book_data)

    for i in range(len(book_data)):

        #print(book_data[i].split(","))
        data_again.append(book_data[i].split(","))
    print("\n")
    #print (data_again)

        
        
    for i in range(len(data_again)):

        b=data_again[i][0]
        items.append(b)
    #print (items)

    for i in range(len(items)):

        key=items[i]
        brand[key]=(data_again[i][1])
        split_p=(data_again[i][2])
        #price_split=(''.join(split_p.split('$')))
        price[key]=split_p
        quantity[key]=(data_again[i][3])
    #print(price)
    book_data.clear()
    to_return()
 
def to_return():

    try:
        id_=int(input("\n\t\tEnter the customer ID: "))
        
        name=str(id_)+'.txt'
        wr=open(name,"r")
        file=wr.read()
        detail=file.split("\n")
        wr.close()

        #print(detail)
        while '' in detail:

            detail.remove('')
        
        data_price=detail[5]
        store_price=data_price.split(":")
        price_costum=store_price[-1]

        date=detail[6]
        actual=date.split(":")
        return_date=actual[-1]#contains return date from bill

        data_costume=detail[2].split(":")
        a=data_costume[1]
        data=(a.replace("[",''))
        data2=(data.replace("]",''))
        data3=(data2.replace("'",''))
        data4=(data3.replace("'",''))
        data5=(data4.replace(' ',''))
        actual_costume=(data5.split(","))#contail costumes of bill
        
        while '' in actual_costume:

            actual_costume.remove('')
        #changing str to date
        date_time_obj = datetime.datetime.strptime(return_date, '%Y/%m/%d')

        ask=(input("\n\nDo you want to return the costume Y/N ").upper())

        if (ask=="Y"):

            print("\n")
            print("++++"*20)
            print("\t\t\tBill Details")
            print("++++"*20)

            #to print bill details
            for i in detail:
                print("\n")

                if i==detail[2] or i==detail[3]:

                    s=i.split(":")
                    print(s[0],end=" ")
                    fi=(s[1].replace('[', ''))
                    fi2=(fi.replace(']', ''))
                    print(":"+fi2)
                    
                if i==detail[5]:

                    a=i.split(":")
                    print(a[0],end=" ")
                    print(":$"+a[1])
                    
                if i==detail[0]or i==detail[1] or i==detail[4]or i==detail[6]:
                   print(i)

            print("\nPlease remember your ID for Return process")
            print("     12 rupee will be added per day when the return date is exceded")
                
            print("++++"*20)

            todays_date=datetime.datetime.now()#today's date

            #update quantity
            for j in actual_costume:
            
                print("\n\nEnter the quantity you borrowed of ",j)
                
                qty=int(input(" "))

                present=quantity[j]
                change=int(present)+int(qty)
                quantity[j]=(change)

            if (todays_date<=date_time_obj):#if time dont exceed
                
                print("\nSince you returned in time pay $"+ price_costum)
                print("\n\n\t\tYou have successfully returned a costume")
      
            else:#if time exceeds 5 days

                difference=todays_date-date_time_obj
                add=12*(int(difference.days))
                final_price=add+int(price_costum)
                print("\nSince you returned in time pay $"+ final_price)
                print("\n\n\t\tYou have successfully returned a costume")


        elif (ask=="N"):#executes if n
            pass
        

        else:#executes if not y or n
            print ("\n\n\t\tEnter answer in y or n")
            to_return()
            
        for i in items:

            item_data=i
            brand_data=str(brand[item_data])
            price_data=str(price[item_data])
            quantity_data=str(quantity[item_data])
            combine=item_data+","+brand_data+","+price_data+","+quantity_data
            write_li.append(combine)#contains data to write in txt file
        
        #to write data in txt file
        file1= open("data.txt","w")
        for i in write_li:

            file1.write(i)
            file1.write("\n")
        file1.close()
        write_li.clear()
        items.clear()
        brand.clear()
        price.clear()
        quantity.clear()
        data_again.clear()
        os.remove(name)

    except :#this line is for the exception 
        print("Invalid!!! input")
        to_return()

