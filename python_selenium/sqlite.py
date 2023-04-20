import sqlite3

def show():
    connection=sqlite3.connect("C:/Users/HÜMEYRA/Desktop/python_selenium/ptyhonSelenium/python_selenium/chinook/chinook.db")
    #test= connection.execute("select * from customer")
    test= connection.execute("select FirstName ,LastName from customers")
    for  line in test:
        print(line[0])
    connection.close()
    
show()