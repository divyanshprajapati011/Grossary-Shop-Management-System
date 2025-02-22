import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "",
    database = "pythondb"
)
mycursor = db.cursor()

product=[]
price=[]
kart=[]
price=[]
data=[]
quantity=[]
def user():

    def bill(price,customer_name):
        print('================================== BILL =======================================')  
        print('-------------------------------------------------------------------------------')
        print('Costomer Name  :  ',customer_name)
        print('-------------------------------------------------------------------------------')

        for i in kart:
            print(i)        
        print('-------------------------------------------------------------------------------')
        count=0
        for i in price:
            count=count+i
        print('total price = ',count)
        print('-------------------------------------------------------------------------------')
        print('                            THANK YOU FOR SHOPING                              ')
        print('-------------------------------------------------------------------------------')

        
    def costomer():
        print('\n\n======================================== PRODUCT INTERFACE ============================================')
        print('-------------------------------------------------------------------------------------------------------')
        print('\n')
        query = "select id,name,price,quantity from product2"
        mycursor.execute(query)
        data = mycursor.fetchall()
        # print(' id      name     price')
        for i in data:
            # print(i)
            print("Id=",i[0],end="  ")
            print("Name=",i[1],end="  ")
            print("Price=",i[2],end=" ")
            print("Quantity=",i[3]) 

            
            

    def aftershop(price):
        print('-------------------------------------------------------------------------------------------------------')
        print('\npress 1 for  you want to do more shopping ')
        print('press 2 for Bill ')
        print('press 0 for exit')
        choice=int(input('enter your choice : '))
        if choice==1:
            costomer()
            shop()
        elif choice==2:
            customer_name=input('enter your name : ')
            bill(price,customer_name)
        else:
            print('invalid input , please enter valid input')

    def getprice(id1,qty):
        name="select price from product2 where id=("+id1+")"
        mycursor.execute(name)
        data1 = mycursor.fetchone()
        for i in data1:
            j=i
        totalprice=i*qty
        price.append(totalprice)


    def shop():
        id1=input('what you want  ? enter product id ')
        qty  = int(input('enter your Quantity :  '))
        q="select name from product2 where id=("+id1+")"
        mycursor.execute(q)
        data1 = mycursor.fetchall()
        kart.append(data1)
        kart.append(qty)  
        print('Move to cart successfully.....')
        q2= "select total from product2 where id=("+id1+")"
        mycursor.execute(q2)
        data2 = mycursor.fetchone()
        q3= "select quantity from product2 where id=("+id1+")"
        mycursor.execute(q3)
        data3 = mycursor.fetchone()
        for i in data3:
            if i>=qty:
                totalqty=i-qty
                q5= "update product2 set quantity=("+str(totalqty)+") where id=("+id1+")"
                mycursor.execute(q5)
                db.commit()
                getprice(id1,qty)
                for i in price:
                    new=i
                for i in data2:
                    new2=i
                newprice=(new2)-(new)
                q4= "update product2 set total=("+str(newprice)+") where id=("+id1+")"
                mycursor.execute(q4)
                db.commit() 
                q5= "update product2 set quantity=("+str(totalqty)+") where id=("+id1+")"
                mycursor.execute(q5)
                db.commit() 
                aftershop(price)  
            else:
                print('-------------------------------------------------------------------------------')
                print('product quantity is not available')
                print('-------------------------------------------------------------------------------')
                shoping() 
        
    def shoping():        
        print('-------------------------------------------------------------------------------------------------------')
        print('press 1 for do shoping')
        print('press 0 for exit ')
        choice= int (input('enter your choice : '))
        if choice==1:
            shop()
        elif choice==0:
            print('================== THANK YOU =======================')
            exit
        else:
            print('invalid input , please enter valid input')

    costomer()
    shoping()


def admin():
    def valiadate():
        choice=int(input('enter your choice : '))
        if choice==1:
            m=int(input('how many add product : '))
            for i in range(m):
                print('---------------------------------------------------------------------')
                name=input('enter your product name : ')
                price=input('enter your product price : ')
                Quantity=input('enter your product Quantity : ')
                total=int(price)*int(Quantity)
                query="insert into product2(name,price,quantity,total) values(%s,%s,%s,%s)"
                values=(name,price,Quantity,total)
                mycursor.execute(query,values)
                db.commit()
            menu()
        elif choice==2:
            query="select * from product2"
            mycursor.execute(query)
            data = mycursor.fetchall()
            for i in data:
                print('ID = ',i[0],end="  ")
                print('Name = ',i[1],end="  ")
                print('Price = ',i[2],end="  ")
                print('Quantity = ',i[3],end="  ")
                print('Total = ',i[4])
            print('---------------------------------------------------------------------')
            menu()
        elif choice==3:
            print('---------------------------------------------------------------------')
            query="select * from product2"
            mycursor.execute(query)
            data = mycursor.fetchall()
            for i in data:
                print('ID = ',i[0],end="  ")
                print('Name = ',i[1],end="  ")
                print('Price = ',i[2],end="  ")
                print('Quantity = ',i[3],end="  ")
                print('Total = ',i[4])
            print('---------------------------------------------------------------------')

            print('---------------------------------------------------------------------')
            id1=input('which product thier you can update .....? ')
            print('---------------------------------------------------------------------')
            print('press 1 for update price')
            print('press 2 for update Quantity')
            print('press 0 for main menu ')
            print('---------------------------------------------------------------------')
            n=int(input('enter your choice : '))
            print('---------------------------------------------------------------------')
            if n==1:
                newprice=input('enter your new price : ')
                qty=input('enter your new qty : ')
                total=int(newprice)*int(qty)
                query="update product2 set price=%s,total=%s where id=%s"
                values=(newprice,str(total),id1)
                mycursor.execute(query,values)
                db.commit()
            elif n==2:
                price=input('enter your new price : ')
                newQuantity=input('enter your new Quantity : ')
                total=int(price)*int(newQuantity)
                query="update product2 set quantity=%s,total=%s where id=%s"
                values2=(newQuantity,total,id1)
                mycursor.execute(query,values2)
                db.commit()
            elif n==0:
                menu()
            else :
                print('invalid input please enter correct input')    
            print('---------------------------------------------------------------------')
            menu()
        elif choice==4: 
            
            print('---------------------------------------------------------------------')
            query="select * from product2"
            mycursor.execute(query)
            data = mycursor.fetchall()
            for i in data:  
                print('ID = ',i[0],end="  ")
                print('Name = ',i[1],end="  ")
                print('Price = ',i[2],end="  ")
                print('Quantity = ',i[3],end="  ")
                print('Total = ',i[4])
            print('---------------------------------------------------------------------')
            print('if you can delete all entries..? , so press 1 : ')
            print('if you can delete perticular entries..? , so press 2 : ')
            print('---------------------------------------------------------------------')
            j=int(input('enter your choice : '))
            if j==1:
                    query="delete from product2" 
                    mycursor.execute(query)
                    db.commit()
                    print('entry deleted is successfull ')
                    menu()
            elif j==2:
                    product01=input('enter your product which you can delete : ')
                    query="delete from product2 where name=('"+product01+"')"
                    value3=(product01)
                    mycursor.execute(query,value3)
                    db.commit()
                    print('entry deleted is successfull ')
                    menu()
            elif j==3:
                    exit
            else:
                    print('---------------------------------------------------------------------')
                    print('====== please enter correct input ======= ')
        elif choice==0:
            print('---------------------------------------------------------------------')
            print('================ Thank you for using this App.=======================')
            print('---------------------------------------------------------------------')
            exit
        else:
            print("invalid input , please enter current input .....")
            print('---------------------------------------------------------------------')
            menu()

    def menu():
        print("========================= Main Menu =================================")
        print("1. add product")
        print("2. show product")
        print("3. update product")
        print("4. delete product ")
        print("0. exit appliction ")
        print('---------------------------------------------------------------------')
        valiadate()
    menu()

def choice():
    n=int(input('enter your choice : '))
    if n==1:
        admin()
    elif n==2:
        user()
        
    elif n==3:
        print('---------------------------------------------------------------------')
        print('             THANK YOU FOR USING THIS APPLICATION                    ')
        print('---------------------------------------------------------------------')

        exit
    else:
         print('wrong input , please enter valid input :')
    
def shop():
    print('\n\n=================== WELCOME TO MY SHOP ========================')
    print('---------------------------------------------------------------')
    print('press 1 for admin : ')
    print('press 2 for User  : ')
    print('press 3 for exit  : ')
    print('---------------------------------------------------------------')
    choice()
shop()

