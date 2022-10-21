import db
import time

while True:
    
    code=input("請選擇今日服務: 1. 新增員工資料, 2. 新增工作項目, 3. 修改員工資料, 4. 查詢員工資料, 5.查詢員工工作項目 0.離開,  您的選擇:")
    print()
    
    if code == "0":
        print("掰掰")
        break
    
    if code == "1":
        print("請依序填入:員工姓名, 性別('F','M'), 電話")
        employeeName=input("請填入員工姓名:")
        employeeSex=input("請填入員工性別:")
        employeeTel=input("請填入員工電話:")
        employeeTime=time.strftime('%Y/%m/%d')
    
        
        sql="insert into employee(name,sex,tel,assume) values ('{}','{}','{}','{}')".format(employeeName,employeeSex,employeeTel,employeeTime)
        
        cursor=db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        print()
        
    if code == "2":
        print("請依序填入:工作項目, 工作詳述, 負責員工編號")
        jobItem=input("請填入工作項目:")
        jobDetail=input("請填入工作詳述:")
        jobEmployee=input("請填入負責員工編號:")
    
        
        sql="insert into works(items,info,employeeid) values ('{}','{}','{}')".format(jobItem,jobDetail,jobEmployee)
        
        cursor=db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        print()
        
    if code == "3":   
        employeeId=input("請輸入欲修改的員工編號:")
        employeeTel=input("請輸入電話:")
        employeeSex=input("請輸入性別:")   
        
        sql="update employee set tel='{}', sex='{}' where id='{}'".format(employeeTel,employeeSex,employeeId)
        
        cursor=db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()    
        print()
    
    if code == "4":
        employeeId=input("請輸入欲查詢的員工編號:")
        
        sql="select e.name, e.sex, e.tel from employee e where id='{}'".format(employeeId)
        
        cursor=db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()    
        
        employeeData=cursor.fetchall()
        
        for row in employeeData:
            # print(row)
            print(f'員工姓名 : {row[0]}')
            print(f'員工性別 : {row[1]}')
            print(f'員工電話 : {row[2]}')
        print()
    
    if code == "5":
        employeeId=input("請輸入欲查詢的員工編號:")
        
        sql="select e.name, w.items, w.info from employee e,works w where e.id=w.employeeid and e.id='{}'".format(employeeId)
        
        cursor=db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()    
        
        employeeData=cursor.fetchall()
        
        for row in employeeData:
            # print(row)
            print(f'員工姓名 : {row[0]}')
            print(f'工作項目 : {row[1]}')
            print(f'工作詳述 : {row[2]}')
        print()
    
    
db.conn.close()    