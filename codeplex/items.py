# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class EmptyItem(scrapy.Item):
    pass
class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
        pj_name=scrapy.Field()
        #pj_user=scrapy.Field()
        pj_desc=scrapy.Field()
        pj_start_date=scrapy.Field()
        pj_tag=scrapy.Field()
        pj_download_times=scrapy.Field()
       # pj_status=scrapy.Field()

class IssueItem(scrapy.Item):
    pj_name=scrapy.Field()
    issue_title=scrapy.Field()
    issue_content=scrapy.Field()
    issue_starter=scrapy.Field()
    issue_start_time=scrapy.Field()
    issue_comment_list=scrapy.Field()

   
class CommitItem(scrapy.Item):
    commit_commitor = scrapy.Field()
    commit_id=scrapy.Field()
    pj_name=scrapy.Field()
    commit_date = scrapy.Field()
    commit_comment =scrapy.Field()
    commit_page_url = scrapy.Field()
    commit_code_url = scrapy.Field()
    #commit_code_store_url = scrapy.Field()

    
