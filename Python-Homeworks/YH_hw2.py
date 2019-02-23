"""
The Purchase History.txt file keeps daily sales records of a school canteen. Each day is separated by “DAY” annotation. For each day, a list of products purchased by a student at one time and her/his id is stored. A student may have purchased some products at different times on the same day. In the example below, student2 bought some products at different times on the fifth day. The PriceList.txt file keeps the price of the products.
DAY#5
STUDENT2- COKE, HAMBURGER, TOAST, CAKE, CHOCOLATE
STUDENT1- PEACH JUICE, CHIPS
STUDENT2- TEA, CAKE, CHIPS
DAY#6
….
Initially, assume that you do not know the following:
• how many different products are sold in this canteen?
• how many different days are there in the file?
• how many students are there?
You should obtain these information from the file and adding a new day and/or new sales information to the file should not be a problem.
You must first present a menu to the user and the users should be able to make selection from this menu. The following are the menu items:
• In the first option, you must show a list of products and prices that the user can purchase.
• In the second option, you must show the total sales and the best-selling product and the number of sales of best-selling product.
NOTE: There can be multiple best-selling products, so you must show them all.
• In the third option, you must ask the user to select a day and show the total sales, the best-selling products and number of sales of best-selling products on the selected day.
NOTE: You must show the range of days the user can select You should check that the selected day is in this range (1-?). Instead of a question mark, you must write the total number of days in the file.
• In the fourth option, you must ask the user to enter a student ID and show the total payment amount of selected student
NOTE: You must show the range of student ids the user can select. You should check that the selected id is in this range (1-?). Instead of a question mark, you must write the total number of students in the file.
This menu screen must be displayed again after each selection result until the user enters 0.
IMPORTANT NOTE: You can read the file up to 2 times. You are not allowed to use data types (tuples, dictionaries..)

"PriceList.txt"
BISCUIT#2
COKE#4
TEA#1
HAMBURGER#10
CHIPS#5
COFFEE#2
CHOCOLATE#2
PEACH JUICE#3
SANDWICH#7
CAKE#4
TOAST#5

"PurchaseHistory.txt"
DAY#1
STUDENT1-PEACH JUICE, CHIPS, BISCUIT, COKE
STUDENT2-COKE
STUDENT3-TEA, SANDWICH,COFFEE,CAKE
STUDENT4-CHIPS, CHOCOLATE, COKE, COFFEE 
STUDENT5-COFFEE, CHOCOLATE
STUDENT6-HAMBURGER, CHIPS, COFFEE
DAY#2
STUDENT5- HAMBURGER, COKE, CHIPS
STUDENT4- COFFEE, BISCUIT, TOAST 
STUDENT1- CHIPS, CHOCOLATE, COKE, COFFEE, SANDWICH, PEACH JUICE, BISCUIT
STUDENT2- TEA, BISCUIT, CHOCOLATE, TOAST
STUDENT3- CHIPS, SANDWICH, PEACH JUICE
DAY#3
STUDENT4- CHIPS, COKE, CAKE, HAMBURGER
STUDENT3- SANDWICH, PEACH JUICE, CHOCOLATE
STUDENT5- COFFEE, CAKE
DAY#4
STUDENT5- SANDWICH, PEACH JUICE, CHIPS
STUDENT4- COKE, HAMBURGER, BISCUIT
STUDENT3- TOAST, CAKE, TEA, CHOCOLATE, CHIPS
STUDENT2- COFFEE, BISCUIT, CHOCOLATE, TOAST, COKE
DAY#5
STUDENT3- SANDWICH, PEACH JUICE, CHOCOLATE, CHIPS, TEA 
STUDENT2- COKE, HAMBURGER, TOAST, CAKE, CHOCOLATE 
STUDENT1- PEACH JUICE, CHIPS
STUDENT2- TEA, CAKE, CHIPS
STUDENT3- COFFEE, CHOCOLATE ,COKE
STUDENT4- CAKE, COFFEE, TEA 
STUDENT5- COFFEE, TEA, TOAST, CAKE, CHIPS, COKE, CHOCOLATE
STUDENT6- HAMBURGER, CHIPS, COKE
DAY#6
STUDENT5- TEA, CAKE, BISCUIT
STUDENT4- PEACH JUICE, COKE, CHIPS, BISCUIT, TEA, CAKE 
STUDENT3- HAMBURGER, CHIPS, COKE, TOAST
DAY#7
STUDENT2- BISCUIT, CHOCOLATE, BISCUIT, TEA
STUDENT4- COFFEE, BISCUIT
STUDENT5- TEA, TOAST, CHOCOLATE
"""

#Yusuf HAYIRLI
Product_List=[] # Product List .
Price_List=[] # Price List .
STD_LIST=[] # To Find Last_Student
MSP_List=[] # Most Selling Product(s)
MSP_Count=0 # Most Selling Product's count ( sales)
Total_Revenue=0 # To find Total Revenue.
Last_Student=0 # To find how many day in there.
Last_Day=0 # To find how many day in there.
file=open("PriceList.txt","r+") # Open and Read "PriceList.txt"
lines=file.readlines()
for i in range(len(lines)): # DISPLAYS Products and Prices...
    line=lines[i].split("#")
    Product_List.append(line[0])
    Price_List.append(int(line[1]))
file.close() # Closing File : "PriceList.txt"
file=open("PurchaseHistory.txt","r+") # Open and Read File : "PurchaseHistory.txt"
lines=file.readlines() # Iterates txt's lines.
Sold_List=[0 for col in range(len(Product_List))] # Fully 0 list as lenght of Product_List.
for line in lines:
    if "DAY" in line:
        Last_Day+=1 # to find Last_Day
    if "STUDENT" in line:
        x=line[7]
        STD_LIST.append(int(x)) # STD_LIST to find Last_Student
    a=line.split(",")
    for i in range(len(Product_List)):
        for j in range(len(a)):
            if Product_List[i] in a[j]:
                Sold_List[i]+=1 # How many sold products as lenght of product list.
for k in range(len(Price_List)):
    Total_Revenue+=Price_List[k]*Sold_List[k] # Calculating Total_Revenue
Last_Student=max(STD_LIST) # Last_Student
MSP_Count=max(Sold_List) # Most Selling Product's count
for i in Sold_List: 
    if i==max(Sold_List):
        a=Sold_List.index(i)
        MSP_List.append(Product_List[a]) # Most Selling Products List to display most selling products
Student_Payment=[0 for col in range(Last_Student)]
Daily_Rev_List=[0 for col in range(Last_Day)]
k=-1 # Day counter. Starts with -1 to make first index 0.
for i in range(len(lines)): ############## Student Payment(s)...
    if "DAY" in lines[i]:
        k+=1 # Day counter.
    if "STUDENT" in lines[i]:
        line=lines[i].split(",")
        for r in line:
            for j in range(len(Product_List)): 
                if Product_List[j] in r:
                    Student_Payment[int(lines[i][7])-1]+=Price_List[j]
                    Daily_Rev_List[k]+=Price_List[j] #Daily Revenue Keeper.
Whole_File=[] # File to List to make it easy to work on it.
for i in range(len(lines)): # Dividing days with "," to define parts of days . 
    if "DAY" in lines[i]:
        Whole_File.append(",") # List
    if "STUDENT" in lines[i]:
        Whole_File.append(lines[i])
Whole_File[0]=" "
Whole_File+=[","] # To apply "DAY" if section.
STACK_List=[] # Dividing parts by Daily Sale Counts as lenght of Product and Price List .
Counter_List=[0 for col in range(len(Product_List))]
for i in Whole_File:
    if i==",": # Seperating by ","'s and stack  
        STACK_List.append(Counter_List)
        Counter_List=[0 for col in range(len(Product_List))]
    else:
        for j in range(len(Product_List)):
            if Product_List[j] in i:
                Counter_List[j]+=1
file.close() # Closing file : "PurchaseHistory.txt"
choice=-1
while choice!="0": # Testing/Execution Part .
    print("press 1 to product and price list")
    print("press 2 to total revenue and most selling product(s) in total")
    print("press 3 to daily revenue and most selling product(s) in a day")
    print("press 4 to total payment for a student")
    print("press 0 to exit")
    choice=input("choice:")
    if choice=="1": # DISPLAYS Products and Prices ...
        print("PRODUCT","   ","PRICE")
        for i in range(len(Product_List)):
            print(Product_List[i],(12-len(Product_List[i]))*" ",Price_List[i])
        print("\n")
    elif choice=="2": # DISPLAYS Total Revenue, Most Selling Product and it's count.
        print("Total Revenue = ",Total_Revenue)
        print("Most Selling Product(s) in TOTAL (",MSP_Count,"sales)")
        print(MSP_List)
        print("\n")
    elif choice=="3": # DISPLAYS Daily Revenue for a Spesific Day.
        print("Select day between 1 and",Last_Day)
        day=input("day=")
        if day<"1" or day>str(Last_Day): # If Entry is not valid...
            print("Your input is invalid, enter properly ! \n")
            continue
        day=int(day)
        Daily_Products=[] # To collect all daily most selling products
        for i in range(len(Product_List)): #Daily Most Selling Products for specific day.
            if STACK_List[day-1][i]==max(STACK_List[day-1]):
                Daily_Products.append(Product_List[i])
        print("Day",day,"Total Revenue = ",Daily_Rev_List[day-1])
        print("Most selling product(s) (",max(STACK_List[(day-1)]),"sales)")
        for j in range(len(Daily_Products)):
            print(Daily_Products[j])
        print("\n")
    elif choice=="4": # DISPLAYS Student Payments for a Specific Student.
        print("Select student id between 1 and",Last_Student,"\n")
        student=input("student id = ")
        if student<"1" or student>str(Last_Student): # If Entry is not valid...
            print("Your input is invalid, enter properly ! \n")
            continue
        student=int(student)
        print("Total payment of student",student,"=",Student_Payment[(student-1)],"\n")
    else:
        if choice!="0":
            print("Your input is invalid, enter properly ! \n") # If Entry is not valid...
            continue
