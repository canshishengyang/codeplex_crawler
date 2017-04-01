# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from codeplex.db_operation import connect_db
from codeplex.db_operation import insert_into_db
from codeplex.db_operation import select_field_from_table
from codeplex.db_operation import delete_from_table

import time
from codeplex.DAO import if_commit_exists
from codeplex.DAO import if_issue_exists
from codeplex.DAO import if_project_exists
from codeplex.DAO import select_id_by_pjname
from codeplex.DAO import if_file_exists
from codeplex.DAO import selectMD5


from codeplex.udload2 import upload_to_commonstorage
from scrapy.pipelines.files import FilesPipeline

from scrapy.utils.python import to_bytes
from codeplex.items import CommitItem
from codeplex.items import IssueItem
from codeplex.items import ProjectItem


from codeplex.signCalc import calcmd5
from scrapy.exceptions import DropItem
import hashlib
import functools
import logging
import scrapy
import hashlib
import os.path

class CodeplexPipeline(object):
    logger=logging.getLogger()
    db=connect_db()
    def process_item(self, item, spider):
        if isinstance(item,ProjectItem):
           
            result = if_project_exists('Codeplex_projects',item['pj_name'])
           
            md5 = calcmd5(item['pj_name'],item['pj_desc'],item['pj_download_times'])
            if not result:
                insert_into_db(self.db,'Codeplex_projects',"id,pj_name,pj_desc,pj_type,pj_download_times,pj_start_date",
                                "0,'"+item['pj_name']+
                                    "','"+item['pj_desc']+
                                       "','"+ " .net "
                                        "',"+item['pj_download_times']+
                                          ",'"+item['pj_start_date']+"','"+md5+"'")  
                return item     
            else:
                
                md5now = selectMD5('Codeplex_projects',md5)
                
                if not md5now:
                    delete_from_table(self.db,'Codeplex_projects','pj_name',item['pj_name'])
                    insert_into_db(self.db,'Codeplex_projects',"id,pj_name,pj_desc,pj_type,pj_download_times,pj_start_date",
                                "0,'"+item['pj_name']+
                                    "','"+item['pj_desc']+
                                       "','"+ " .net "
                                        "',"+item['pj_download_times']+
                                          ",'"+item['pj_start_date']+"','"+md5+"'")  
                else: 
                    raise DropItem("Project exists!!")
        elif isinstance(item,IssueItem):
        #    self.logger.info("Issue start_time:"+item['issue_start_time'])
        #    self.logger.info("Issue issue_title:"+item['issue_title'])
        #    self.logger.info("Issue issue_content:"+item['issue_content'])
        #    self.logger.info("Issue issue_starter:"+item['issue_starter'])
            
            id = select_id_by_pjname(item['pj_name'])
            if not id:
               pass
            else:
               result = if_issue_exists('Codeplex_issues',id[0][0],item['issue_title'])
                 
               if not result:
                    insert_into_db(self.db,'Codeplex_issues',"id,issue_title,issue_content,issue_starter,issue_start_time,pj_id",
                                "0,'"+str(item['issue_title']).replace("'","''")+
                                    "','"+str(item['issue_content']).replace("'","''")+
                                        "','"+item['issue_starter']+
                                            "','"+item['issue_start_time']+
                                               "'," +str(id[0][0]))
               return item        
        elif isinstance(item,CommitItem):
            
            id = select_id_by_pjname(item['pj_name'])
            if not id:
                pass
            else:
                result = if_commit_exists('Codeplex_commits',id[0][0],item['commit_id'])
          
                if not result:
       #             time.sleep(2)
                    insert_into_db(self.db,'Codeplex_commits',"id,commit_id,commit_commitor,commit_comment,commit_date,pj_id",
                                                      "0,'"+item['commit_id']+"','"+item['commit_commitor']+"','"+str(item['commit_comment']).replace("'","''")+"','"+item['commit_date']+"',"+str(id[0][0]))
                                              
            return item          
        else:
            raise DropItem('drop item Item')        
class CodesPipeline(FilesPipeline):
    logger=logging.getLogger()
  
    def get_media_requests(self, item, info):
     
        if isinstance(item,ProjectItem):
            self.logger.info("get media requests ProjectItem")
        elif isinstance(item,IssueItem):
            self.logger.info("get media requests IssueItem")
        elif isinstance(item,CommitItem):
            self.logger.info("get media requests CommitItem "  + item['commit_code_url'])
            yield scrapy.Request(item['commit_code_url'])
            
        else:
            self.logger.info("get media requests notypes")
        #    scrapy.Request(item['commit_code_url'])
        #    raise DropItem('drop item file')    
        
    def file_path(self, request, response=None, info=None):
        url = request.url
        media_guid = hashlib.sha1(to_bytes(url)).hexdigest()  # change to request.url after deprecation
       # media_ext = os.path.splitext(url)[1]  # change to request.url after deprecation
              # return 'full/%s%s' % (media_guid, ".zip")
        return './full/%s%s' % (media_guid, ".zip")
      
    def item_completed(self, results, item, info):
        db=connect_db()
        if isinstance(item,CommitItem):
            for tp in results:
               if tp[0]==True:
                    id = select_id_by_pjname(item['pj_name'])
                    if not id:
                        pass
                    else:
                       
                        if not if_file_exists('Codeplex_files',id[0][0],item['commit_id']):
                            
                           
                            upload_to_commonstorage('./codes/full/'+str(tp[1]['path']).split('/')[-1])
                            insert_into_db(db,'Codeplex_files',
                                                    "id,file_url,pj_id,commit_id", 
                                                        "0,'"+str(tp[1]['path']).split('/')[-1]+
                                                            "','"+str(id[0][0])+"','"+item['commit_id']+"'")
        else:
            pass
        return item