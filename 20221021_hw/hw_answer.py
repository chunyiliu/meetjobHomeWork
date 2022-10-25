# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:04:33 2022

@author: pei-chen
"""

import db
from datetime import datetime

def addEmployee(name,sex,tel):
    now=datetime.now()
    today=datetime.strftime(now, "%Y-%m-%d")
    sql="insert into employee(name,sex,tel,assume) values('{}','{}','{}','{}')".format(name,sex,tel,today)
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    

def addWorks(employeeid,items,info):
    sql="insert into works(items,info,employeeid) values('{}','{}','{}')".format(items,info,employeeid)
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
    
def allEmplyee():
    sql="select id,name from employee"
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    result=cursor.fetchall()
    for row in result:
        print("員工編號:",row[0])
        print("員工姓名:",row[1])
        print()
        
        
def queryEmployee(employeeid):
    sql="select id,name,sex,assume,tel from employee where id='{}'".format(employeeid)
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    result=cursor.fetchall()
    for row in result:
        print("員工編號:",row[0])
        print("員工姓名:",row[1])
        print("員工性別:",row[2])
        print("就職日:",row[3])
        print("電話:",row[4])
        print()
        break
    else:
        print("沒有這個員工")
        
        
def updateEmployee(employeeid,tel,sex):
    sql="update employee set tel='{}',sex='{}' where id='{}'".format(tel,sex,employeeid)
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
    
    
    
def queryEmployeeWorks(employeeid):
    sql="select employee.name,works.* from employee inner join works on employee.id=works.employeeid where employee.id='{}'".format(employeeid)
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    result=cursor.fetchall()
    for row in result:
        print("員工:",row[0])
        print("工作項目:",row[2])
        print("工作內容:",row[3])
        print()
        break
    else:
        print("尚未指派工作")
        
        
if __name__=='__main__':
    while True:
        item=input("員工系統: a->新增員工 w->新增員工工作 q->查詢 u->修改 e->員工的工作內容 x->離開:")
        
        if item =='x':
            break
        elif item=='a':
            name=input("新員工姓名:")
            sex=input("性別(F/M):")
            tel=input("電話:")
            addEmployee(name, sex, tel)
            allEmplyee()
        elif item=='w':
            allEmplyee()
            empId=input("請輸入員工編號:")
            item=input("請輸入員工事項:")
            info=input("請輸入內容:")
            addWorks(empId, item, info)
        elif item=='q':
            eid=input("請輸入員工編號:")
            queryEmployee(eid)
        elif item=="u":
            allEmplyee()
            eid=input("請輸入員工編號:")
            tel==input("請輸入修改的電話:")
            sex=input("請輸入修改的性別(F/M):")
            updateEmployee(eid, tel, sex)
        elif item=="e":
            employeeid=input("請輸入員工編號:")
            queryEmployeeWorks(employeeid)
            
            
            
            
    
    
    
    
        
        