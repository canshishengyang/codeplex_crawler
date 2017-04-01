
# -*- coding: UTF-8 -*-
import MySQLdb
from codeplex.db_operation import connect_db
from codeplex.db_operation import insert_into_db
from codeplex.db_operation import select_field_from_table

def select_id_by_pjname(name):
        db=connect_db()
        cursor = db.cursor()
        sql = r"select id from Codeplex_projects where pj_name like '"+name+r"';"
        print sql
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print result
            return result
        except Exception,e:
            print e
            return ''
def selectMD5(scheme,MD5):
    db=connect_db()
    cursor=db.cursor()
    sql = r"select id from "+scheme+r" where MD5 like '"+MD5 +r"'"
    try:
        cursor.execute(sql)
        cursor.fetchall()
        return result;
    except Exception,e:
        print e 
        return ''
def if_project_exists(scheme,name):
        db=connect_db()
        cursor=db.cursor()
        sql=r"select pj_name from " + scheme + r" where pj_name like '"+name+r"'"
        print sql
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception,e:
            print e
            return '' 
def if_issue_exists(scheme,pj_id,name):
        db=connect_db()
        cursor=db.cursor()
        sql=r"select issue_title from "+scheme+r" where issue_title like '"+name+r"' and pj_id=%d"%(pj_id)
        print sql
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception,e:
            print e
            return ''   
def if_file_exists(scheme,pj_id,commit_id):
    db=connect_db()
    cursor=db.cursor()
    sql=r"select commit_id from "+scheme+r" where commit_id like '"+commit_id+r"' and pj_id=%d"%(pj_id)
    print sql
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception,e:
        print e
        return ''
def if_commit_exists(scheme,pj_id,commit_id):
    db=connect_db()
    cursor=db.cursor()
    sql=r"select commit_id from "+scheme+r" where commit_id like '"+commit_id+r"' and pj_id=%d"%(pj_id)
    print sql
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception,e:
        print e
        return '' 
if __name__=='__main__':
	print select_id_by_pjname('asd')