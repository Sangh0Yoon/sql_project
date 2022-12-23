from django.shortcuts import render
from django.db import connection

def query1(request):
    outputOfQuery1 = []
    with connection.cursor() as cursor:
        sqlQuery1 = "SELECT AVG(hd) FROM pc;"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()

        for temp in fetchResultQuery1:
            outputOfQuery1.append(temp)
    return render(request, 'myApp/query1.html', {'result1': outputOfQuery1})

def query2(request):
    outputOfQuery2 = []
    with connection.cursor() as cursor:
        sqlQuery2 = "SELECT maker, AVG(speed) FROM product p, laptop l WHERE p.model = l.model GROUP BY maker;"
        cursor.execute(sqlQuery2)
        fetchResultQuery2 = cursor.fetchall()

        for temp in fetchResultQuery2:
            outputOfQuery2.append(temp)
    return render(request, 'myApp/query2.html', {'result2': outputOfQuery2})

def query3(request):
    outputOfQuery3 = []
    with connection.cursor() as cursor:
        sqlQuery3 = "SELECT price FROM product, laptop, (SELECT maker FROM product p, laptop l WHERE l.model = p.model GROUP BY maker HAVING cCOUNT(case when type='laptop' then 1 end) = 1) AS oneMaker WHERE laptop.model = product.model AND product.maker = oneMaker.maker;"
        cursor.execute(sqlQuery3)
        fetchResultQuery3 = cursor.fetchall()

        for temp in fetchResultQuery3:
            outputOfQuery3.append(temp)
    return render(request, 'myApp/query3.html', {'result3': outputOfQuery3})

def query4(request):
    outputOfQuery4 = []
    with connection.cursor() as cursor:
        sqlQuery4 = "SELECT DISTINCT pri.model, pri.price FROM printer pri, product pro, (SELECT maker, MAX(price) AS price FROM product pro, printer pri WHERE pro.model = pri.model GROUP BY maker) AS EachMaker WHERE pri.price = EachMaker.price AND pro.maker = EachMaker.maker;"
        cursor.execute(sqlQuery4)
        fetchResultQuery4 = cursor.fetchall()

        for temp in fetchResultQuery4:
            outputOfQuery4.append(temp)
    return render(request, 'myApp/query4.html', {'result4': outputOfQuery4})

def create(request):
    with connection.cursor() as cursor:
        sqlQueryCreateProduct = "CREATE TABLE Product(maker CHAR(20), model INT, type CHAR(20));"
        sqlQueryCreatePc = "CREATE TABLE Pc(model INT, speed FLOAT, ram INT, hd INT, price INT);"
        sqlQueryCreateLaptop = "CREATE TABLE Laptop(model INT, speed FLOAT, ram INT, hd INT, screen INT, price INT);"
        sqlQueryCreatePrinter = "CREATE TABLE Printer(model INT, color BOOLEAN, type CHAR(20), price INT);"

        cursor.execute(sqlQueryCreateProduct)
        cursor.execute(sqlQueryCreatePc)
        cursor.execute(sqlQueryCreateLaptop)
        cursor.execute(sqlQueryCreatePrinter)
        connection.commit()
        connection.close()
    return render(request, "myApp/create.html")

def insert(request):
    with connection.cursor() as cursor:
        sqlQueryInsertProduct = "INSERT INTO Product VALUES" \
                                "('A',1001,'pc'),('A',1002,'pc'),('A',1003,'pc')," \
                                "('A',2004,'laptop'),('A',2005,'laptop'),('A',2006,'laptop')," \
                                "('B',1004,'pc'),('B',1005,'pc'),('B',1006,'pc')," \
                                "('B',2007,'laptop'),('D',1007,'pc'),('D',1008,'pc')," \
                                "('D',1009,'pc'),('D',1010,'pc'),('D',3004,'printer')," \
                                "('D',3005,'printer'),('E',2001,'laptop'),('E',2002,'laptop')," \
                                "('E',2003,'laptop'),('E',3001,'printer'),('E',3002,'printer')," \
                                "('E',3003,'printer'),('F',2008,'laptop'),('F',2009,'laptop')," \
                                "('G',2010,'laptop'),('H',3006,'printer'),('H',3007,'printer');"
        sqlQueryInsertPc    = "INSERT INTO PC VALUES" \
                               "(1001,2.66,1024,250,2114),(1002,2.10,512,250,995)," \
                               "(1003,1.42,512,80,478),(1004,2.80,1024,250,649)," \
                               "(1005,3.20,512,250,630),(1006,3.20,1024,320,1049)," \
                               "(1007,2.20,1024,200,510),(1008,2.20,2048,250,770)," \
                               "(1009,2.00,1024,250,650),(1010,2.80,2048,300,770)," \
                               "(1011,1.86,2048,160,959),(1012,2.80,1024,160,649),(1013,3.06,512,80,529);"
        sqlQueryInsertLaptop = "INSERT INTO Laptop VALUES " \
                               "(2001,2.00,2048,240,20.1,3673),(2002,1.73,1024,80,17.0,949)," \
                               "(2003,1.80,512,60,15.4,549),(2004,2.00,512,60,13.3,1150)," \
                               "(2005,2.15,1024,120,17.0,2500),(2006,2.00,2048,80,15.4,1700)," \
                               "(2007,1.83,1024,120,13.3,1429),(2008,1.60,1024,120,15.4,900)," \
                               "(2009,1.60,512,80,14.1,680),(2010,2.00,2048,160,15.4,2300);"
        sqlQueryInsertPrinter = "INSERT INTO Printer VALUES" \
                                "(3001,true,'ink-jet',99),(3002,false,'laser',239)," \
                                "(3003,true,'laser',899),(3004,true,'ink-jet',120)," \
                                "(3005,false,'laser',120),(3006,true,'ink-jet',100)," \
                                "(3007,true,'laser',200);"

        cursor.execute(sqlQueryInsertProduct)
        cursor.execute(sqlQueryInsertPc)
        cursor.execute(sqlQueryInsertLaptop)
        cursor.execute(sqlQueryInsertPrinter)
        connection.commit()
        connection.close()
    return render(request, "myApp/insert.html")

def drop(request):
    with connection.cursor() as cursor:
        sqlQueryDropProduct = "DROP TABLE Product;"
        sqlQueryDropPc = "DROP TABLE Pc;"
        sqlQueryDropLaptop = "DROP TABLE Laptop;"
        sqlQueryDropPrinter = "DROP TABLE Printer;"

        cursor.execute(sqlQueryDropProduct)
        cursor.execute(sqlQueryDropPc)
        cursor.execute(sqlQueryDropLaptop)
        cursor.execute(sqlQueryDropPrinter)
        connection.commit()
        connection.close()
    return render(request, "myApp/drop.html")

def check(request):
    outputOfProducts = []
    outputOfPcs = []
    outputOfLaptops = []
    outputOfPrinters = []
    with connection.cursor() as cursor:
        sqlQueryProducts = "SELECT * FROM product;"
        cursor.execute(sqlQueryProducts)
        fetchResultProducts = cursor.fetchall()

        sqlQueryPc = "SELECT * FROM pc;"
        cursor.execute(sqlQueryPc)
        fetchResultPc = cursor.fetchall()

        sqlQueryLaptop = "SELECT * FROM laptop;"
        cursor.execute(sqlQueryLaptop)
        fetchResultLaptop = cursor.fetchall()

        sqlQueryPrinter = "SELECT * FROM printer;"
        cursor.execute(sqlQueryPrinter)
        fetchResultPrinter = cursor.fetchall()

        connection.commit()
        connection.close()


        for temp in fetchResultProducts:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputOfProducts.append(eachRow)

        for temp in fetchResultPc:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3],
                       'price': temp[4]}
            outputOfPcs.append(eachRow)

        for temp in fetchResultLaptop:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3],
                       'screen': temp[4], 'price': temp[5]}
            outputOfLaptops.append(eachRow)

        for temp in fetchResultPrinter:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2],
                       'price': temp[3]}
            outputOfPrinters.append(eachRow)
        return render(request, 'myApp/check.html', {'product': outputOfProducts,
                                                         'pc': outputOfPcs,
                                                         'laptop': outputOfLaptops,
                                                         'printer': outputOfPrinters})
def assignment(request):
    return render(request, "myApp/assignment.html")

