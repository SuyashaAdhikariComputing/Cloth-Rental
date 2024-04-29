
data_dic={}

'''the display fuction contains the code for adding the data in txt
file to list and dictionary and printing the stock available'''

def display_products():
    
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

      #this for loop help to display the items  
    for key,value in data_dic.items():
        print(key,end="\t")
        for i in value:
            print(i,end="\t")
        print("\n")
    print("----"*20)
