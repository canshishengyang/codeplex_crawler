# -*- coding: UTF-8 -*-
import scrapy.spider
import urlparse
import logging
import json
import os
import time
import sys

from codeplex.items import ProjectItem
from codeplex.items import CommitItem
from codeplex.items import IssueItem
from codeplex.items import EmptyItem
class codeplexSpider(scrapy.Spider):
    name='codeplexSpider'
    tagName=''
    logger = logging.getLogger()
    
    def start_requests(self):
     
            reload(sys)  
            sys.setdefaultencoding('utf8')  
            page = 0
         
      
           # list_url = r"http://www.codeplex.com/site/search?query=&sortBy=DownloadCount&tagName="+self.tagName+r"&licenses=|&refinedSearch=true&size=100&page="
           # list_url = list_url + str(page)
        
            list_url = r"https://www.codeplex.com/site/search?query=&sortBy=DownloadCount&tagName=%2cpowershell%2c&licenses=|&refinedSearch=true&page=2"
            yield scrapy.Request(list_url,callback=self.parseProjectList,meta={'page':page,'list_url':list_url},dont_filter=False)
         
    
    def parseProjectList(self,response):
            project_list=response.xpath("//body/form[@id='aspnetForm']/div[5]/div[1]/div[2]/table[@id='search_directory']/tr/td[1]")
           
            for pj in project_list:
                Pj_Item = ProjectItem()
                if len(pj.xpath("div/h3/a/text()").extract())==0:
                    yield EmptyItem()
                    break
                pj_name = pj.xpath("div/h3/a/text()").extract()[0]
                Pj_Item['pj_name']=pj_name
                pj_desc = pj.xpath("div/p[1]/text()").extract()[0]
                Pj_Item['pj_desc']=pj_desc
            
                pj_page_url = pj.xpath("div/h3/a/@href").extract()[0]
           
                Pj_Item['pj_download_times']=pj.xpath("div/p[@class='search_info']/span[2]/text()").extract()[0]    
                Pj_Item['pj_start_date']=pj.xpath("div/p[@class='search_info']/span[3]/text()").extract()[0]
                Pj_Item['pj_tag'] = self.tagName
        
                #self.logger.info("page_url: " + pj_page_url)
                netloc = urlparse.urlparse(str(pj_page_url))[1]
                commit_page = 0
                commits_url = urlparse.urlunparse(( 'http',
                                                 netloc,
                                                    '/SourceControl/list/changesets?size=100&page=','','','',))
                issue_page = 0
                issues_url = urlparse.urlunparse(('http', 
                                                netloc, 
                                                    '/workitem/list/basic',
                                                       '',
                                                          'field=CreationDate&direction=Descending&issuesToDisplay=Open&keywords=&emailSubscribedItemsOnly=false&size=50&page=',
                                                             ''))
            

                
                yield scrapy.Request(pj_page_url,callback=self.paseProjectPage,meta={'pj_item':Pj_Item,
                                                                    'commits_url':commits_url,'issues_url':issues_url,
                                                                        'commit_page':commit_page,'issue_page':issue_page},dont_filter=False)
            list_url= response.meta['list_url']
            page = response.meta['page']
            page = int(page) + 1
            next = response.xpath("//body/form/div[@id='wrap']/div[@id='sub_heading']/div[@id='left_column_search']/ul[2]/ul[1]/li[@class='last']/text()").extract()
            if len(next)==0:
                yield scrapy.Request(list_url+str(page),callback = self.parseProjectList,meta={'page':page,'list_url':list_url},dont_filter=False)
            
    def paseProjectPage(self,response):
    
        Pj_Item = response.meta['pj_item']
        #the date of last update of the project
        pj_date=response.xpath("//body/form[1]/div[5]/div[3]/div[1]/table[1]/tr[2]/td/span/text()").extract()
        #the status present
        pj_status=response.xpath("//body/form[1]/div[5]/div[3]/div[1]/table[1]/tr[3]/td/text()").extract()
        #download times of the project
        pj_download_times=response.xpath("//body/form[1]/div[5]/div[3]/div[1]/table[1]/tr[4]/td/text()").extract()


        
        yield Pj_Item
        yield scrapy.Request(response.meta['commits_url']+str(response.meta['commit_page']),callback=self.paseCommitList,meta={'pj_item':Pj_Item,'commit_page':response.meta['commit_page'],'commits_url':response.meta['commits_url']},dont_filter=False)
        yield scrapy.Request(response.meta['issues_url']+str(response.meta['issue_page']),callback = self.parseIssuesList,meta={'pj_item':Pj_Item,'issue_page':response.meta['issue_page']},dont_filter = False)
    def paseCommitList(self,response):
        project = response.meta['pj_item']
        commits = response.xpath("//body/form[@id='aspnetForm']/div[@id='wrap']/div[@id='left_column_source_code']/table[@id='source_code']/tr")
        if len(commits)==0:
            return 
        index = 0
        for commit in commits:
            if index >=len(commits):
                break;
            Commit_Item = CommitItem()
            if commits.index(commit)==0:
                continue
            commit_page_url = commit.xpath("td/a/@href").extract()[0]
            commit_id = commit.xpath("td/a/text()").extract()[0]
            
            commit_commiter = ''
            if len(commit.xpath("td/a/text()").extract())== 2:
                commit_commiter = commit.xpath("td/a/text()").extract()[1]
                print commit_commiter+"         1"
            else:
                commit_commiter = commit.xpath("td/span/@title").extract()[0]
                print commit_commiter+"         0"
            
            commit_date = commit.xpath("td[2]/span").xpath('string(.)').extract()[0]
            commit_comment =commit.xpath("td[3]/p[@class='changesetComment']/text()").extract()[0]
            
           
            scheme = 'http'
            netloc = 'download-codeplex.sec.s-msft.com'
            path = '/Download/SourceControlFileDownload.ashx'
            params = ''
            query = 'ProjectName='+str(commit_page_url).replace("http://","").split('.')[0]+ '&changeSetId='+str(commit_page_url).split('/')[-1]#+'&RepositoryName='+str(commit_url).split('/')[-3]+'&OwnerName='+str(commit_url).split('/')[-4]
            fragment = ''
            fragment = ''
            urlpart=(scheme,netloc,path,params,query,fragment,)
            commit_code_url =  urlparse.urlunparse(urlpart)
            
            Commit_Item['pj_name'] = project['pj_name']
            Commit_Item['commit_commitor'] = commit_commiter
            Commit_Item['commit_id'] = commit_id
            Commit_Item['commit_date'] = str(commit_date)
            Commit_Item['commit_comment'] = commit_comment
            Commit_Item['commit_page_url'] = commit_page_url
            Commit_Item['commit_code_url'] = commit_code_url
            yield Commit_Item
            next = response.xpath("//body/form/div[@id='wrap']/div[@id='left_column_source_code']/ul/ul[1]/li[@class='last']/text()").extract()
            if len(next)==0:
                page = response.meta['commit_page']
                url = response.meta['commits_url']
                page = int(page)+1
                yield scrapy.Request(url+str(page),callback=self.paseCommitList,meta={'commits_url':url,'commit_page':page,'pj_item':project},dont_filter=False)
    def parseIssuesList(self,response):
        project = response.meta['pj_item']
        issues_list = response.xpath("//body/form[@id='aspnetForm']/div[@id='wrap']/div[@id='left_column']/div")
        if len(issues_list)==0:
            yield EmptyItem() 
        else:
            for issue in issues_list:
            
                Issue_Item = IssueItem()
                if len( issue.xpath("div[2]/h3/a/text()").extract()) == 0:
                    yield EmptyItem()
                    break

                issue_title = issue.xpath("div[2]/h3/a/text()").extract()[0]
                issue_content = issue.xpath("div[2]/p[@class='wordwrap']/text()").extract()[0]
                issue_starter = issue.xpath("div[2]/p[@class='issue_id']/a[1]/text()").extract()[0]
                issue_start_time = issue.xpath("div[@class='issue_post_content']/p[2]/span[2]/text()").extract()[0]

                Issue_Item['issue_start_time'] = issue_start_time
                Issue_Item['issue_title'] = issue_title
                Issue_Item['issue_content'] = issue_content
                Issue_Item['issue_starter'] = issue_starter
                Issue_Item['pj_name'] = project['pj_name']

                issue_page_url = issue.xpath("div[2]/h3/a/@href").extract()[0]
          
                yield scrapy.Request(issue_page_url,callback = self.parseIssuePage,meta={'Issue_Item':Issue_Item},dont_filter=False)
    def close(spider, reason):
        os.system("./delete")
        return super(codeplexSpider, spider).close(reason)      
    def parseIssuePage(self,response):
        Issue_Item = response.meta['Issue_Item']

      
        comment_list=response.xpath("//body/form/div[@id='wrap']/div[@id='left_column']/div[@id='comments']/div[@id='CommentsList']/div")
        issue_comment_list = []
        if len(comment_list)==0:
           pass
        else:
            for comment in comment_list:
                if len(comment.xpath("p[1]/a/text()").extract())==0:
                    continue
                comment_commenter = comment.xpath("p[1]/a/text()").extract()[0] 
                comment_content = comment.xpath("div[1]/div[1]").xpath('string(.)').extract()[0] 
                comment_time = comment.xpath("p[1]/span/text()").extract()[0]
                com_dict = {'comment_commenter':comment_commenter,'comment_content':comment_content,'comment_time':comment_time}
                issue_comment = json.dumps(com_dict)
                issue_comment_list.append(issue_comment)
   
        Issue_Item['issue_comment_list'] = issue_comment_list
        yield Issue_Item
        