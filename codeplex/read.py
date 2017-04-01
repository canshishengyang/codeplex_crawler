import os
import db_operation
import fileinput
import udload2
from udload2 import upload_to_commonstorage
from db_operation import connect_db
from db_operation import insert_into_db
from db_operation import select_name_from_projects 
if __name__=='__main__':
    filesdirs = os.listdir('full')
    db = db_operation.connect_db()
    for filedir in filesdirs:
        print filedir
        if os.path.isdir('full/'+filedir) == True:
            files = os.listdir('full/'+filedir)
            project_name = filedir
           # print file
#            result = select_name_from_projects(db,project_name)  
#            print result
            
            if len(files) > 0:
                for _file in files:
  #                  file_object = open(filedir+'/'+files[0])
                    try:
#                        if len(result)!=0:
#                            insert_into_db(db,'Files',
#                                'id,name,url,pj_id',
#                                r"0,'"+project_name
#                                +"','"+_file
#                                +"',"+str(result[0][0]))
#                            pass
#                        if db == None:
#                            db = connect_db()
                            #print 'full/'+filedir+'/'+_file
                        upload_to_commonstorage('full/'+filedir+'/'+_file)                            
                                              
                        
                                             
                       # print 'desc: ',desc
                        
                       # print 'ptype: ',ptype
                        
                        
                       
                    except Exception,e:
                        print e
                       
                                     
                                          
                    finally:
                        pass
       #                 file_object.close()
        
