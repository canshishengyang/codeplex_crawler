import os
import sys
import logging


if __name__ == '__main__':
    logger = logging.getLogger()
    
    os.system('scrapy crawl '+'.Net')
  #  settings = get_project_settings()

    
  #  alltags = settings.getdict('TAGS')
  #  print 'ALL TAGS WE CAN CRWAL: '
  #  for tag in alltags:
  #      print tag,
  #  print ''
  #  print 'INPUT THE TAG YOU WANT TO CRAWL:'
  #  tager = raw_input()
  #  print tager
   