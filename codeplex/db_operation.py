#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import time
import random
import sys

"""
    Configure settings
"""
DB_IP='172.18.100.15'
DB_NAME='savannah_gnu'
DB_VM_NAME='db_sf_338'
DB_USER='savannah'
DB_PASS ='_savannah'

"""
    connect to database
    Parameters:
        db_ip, ip address of database
        db_user, username of database
        db_pass, password of database
        db_name, name of database
    Return:
        a handle of the connected database if success
        or None
"""
def delete_from_table(db,scheme,colunm,text):
    db=connect_db()
    cursor=db.cursor()
    sql=r"DELETE FROM "+scheme+" WHERE "+ colunm +r" like '"+ text +r"'"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print result
    except Exception,e:
        print e
        return ''
    return result

def connect_to_db(db_ip,db_user,db_pass,db_name):
    try:

        db = MySQLdb.connect(db_ip,db_user,db_pass,db_name)
        db.set_character_set('utf8')

        if db == None:
            return None
    
        return db
    except Exception as e:
        print(e)
        return None


"""
    Connect to database with default setting
    Parameters:
    Return:
        a handle of the connected database if success
        or None
"""
def connect_to_db_simple():
    db = None
    count = 5
    while True:
        count = count - 1
        db = connect_to_db(DB_IP,DB_USER,DB_PASS,DB_NAME)
        if db is not None or count < 0:
            break

        random.seed()
        time.sleep(random.randint(1, 5))
    return db


#=============================================================#
#select one field value from  table
#@para db, database pointer
#@para table_name, table name
#@para field_name, the name of indexed field,
#       value is static_dot_uri or static_path_image_uri
#@para r_id, index a record
#@return value of indexed field
#=============================================================#
def select_name_from_projects(db,name):
    cursor = db.cursor()
    sql = r"select id from ProjectInfo where name like '%"+name+r"%'"
    print sql
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print result
    except Exception,e:
        print e
        return ''
    return result


def select_field_from_table(db,table_name,field_name,r_id):    
    cursor = db.cursor()
    
    sql="select %s from %s where id = %s;"%(field_name,table_name,r_id)
    
    try:
       cursor.execute(sql)
       result=cursor.fetchall()
     #  result=str(result[0])
    #   result=result.split('(')[1].split(',')[0]
       
    except Exception as e:
        print("error to task table:",e)

        return ''

    return result

def select_field_by_vmip(db,table_name,field_name,ip):
    cursor=db.cursor()
    sql="select %s from %s where vm_ip = '%s';"%(field_name,table_name,ip)

    print(sql)
    try:
       cursor.execute(sql)
       result=cursor.fetchall()
       if(len(result)>0):
           result=str(result[0])
           result=result.split('(')[1].split(',')[0]
       else:
            result=''
    except Exception as e:
        print("error to task table:",e)
        return ''

    return result

#=========================================================#
#insert a record with field=value
#@para db, db handle
#@para field, field name
#@para value, field value
#=========================================================#
def insert_into_db(db,table_name,field,value):
    cursor = db.cursor()
    sql="insert into %s (%s) values (%s);"%(table_name,field,value)
    

    try:
        print sql
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print('some exception has happened when insert into db',e)
        sys.exit()
        return False

def update_project_record(scheme,id,pj_name,pj_desc,pj_type,pj_download_times,pj_date,md5):
    db= connect_db()
    sql = r"update "+scheme+r" set pj_name= '"+pj_name+r"',pj_desc = '"+pj_desc+r"',pj_type = '"+pj_type+r"',pj_start_date = '"+pj_date+r"',MD5 = '"+md5+"',"+"update_time = '"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"' where id ="+str(id) + r";"
    print sql
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

    
    except Exception,e:
        print e 

#========================================================#
#update a record with field=value
#@para db, db handle
#@para table_name, table name
#@para field, field name
#@para value, field value
#@para r_id, index of record
#========================================================#
def update_one_record(db,table_name,field,value,r_id):
    cursor=db.cursor()
    sql="update %s set %s = '%s' where id = %s;"%(table_name,field,value,r_id)

    #print sql
    try:
        cursor.execute(sql)
    except Exception as e:
        print ('some exception has happened when update db',e)
        return

#==========================================================#
#update table 'vm' by ip address
#==========================================================#
def update_one_vm(db,table_name,field,value,ip):
    cursor=db.cursor()
    sql="update %s set %s = '%s' where vm_ip = '%s';"%(table_name,field,value,ip)
    #print sql
    try:
        cursor.execute(sql)
    except Exception as e:
        print( 'some exception has happened when update db',e)
        return

    
#===========================================================#
#update a record in task table with new values of dot&svg uris
#@para db, handle of db
#@para r_id, index of a record
#@para dot_uri, uri of static call graph dot file
#@para svg_uri, uri of static call svg file
#===========================================================#
def update_one_record_simple(db,r_id,dot_uri,svg_uri):
    cursor=db.cursor()
    sql="update %s set %s = '%s', %s = '%s' where id = %s;"%(TABLE_TASK_NAME,FN_S_DOT_URI,dot_uri,FN_S_SVG_URI,svg_uri,r_id)

    #print sql
    try:
        cursor.execute(sql)
    except Exception as e:
        print('some exception has happened when update db',e)
        return

#=========================================
# this is  the 




#test function of db operations
#=========================================

#if __name__=='__main__':
def connect_db():
    db =  connect_to_db(DB_IP,DB_USER,DB_PASS,DB_NAME)
    if db == None:
        print('fail  \n')
   
       # insert_into_db(db,'ProjectInfo',
        #       r'id,name,description,members,type',
         #      r"0,'3DLDF','I am a project testing message','members','official'") 
#        result = select_field_from_table(db,'ProjectInfo','*',4)
        #print '\n'
       # print result
    return db
if __name__=='__main__':
    update_project_record('Codeplex_projects',183,'wangtua','desc','sta',0,'as','adfsasf')
#============================================================#
#db=connect_to_db(DB_IP,DB_USER,DB_PASS,DB_NAME)
#
#if(db == None):
#    print 'connect to db error'
#else:
#    result=select_field_froim_table(db,TABLE_TASK_NAME,"static_dot_uri",338)
#    #print select_field_from_table(db,TABLE_TASK_NAME,"")
#    print result
#    db.close()
#
#==================================================================#
#db=connect_to_db(DB_IP,DB_USER,DB_PASS,DB_NAME)
#if (db == None):
#    print 'failed to connect to db'
#else:
#    #insert_into_db(db,'dynamic_dot_uri','20bd793e141d9b5967f1061f483b27eb')
#    #update_one_record(db,'dynamic_dot_uri','44ffbad6fe4adbb347a67fa87ffafab9',1)
#    update_one_record_simple(db,338,'30f714a740a51560f0fda4513eedfa23','601197cff878760874ea019cea30e4a1')
#    db.close()
#==================================================================#

 

#===============


