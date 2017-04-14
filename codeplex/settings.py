# -*- coding: utf-8 -*-

# Scrapy settings for codeplex project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'codeplex'

SPIDER_MODULES = ['codeplex.spiders']
NEWSPIDER_MODULE = 'codeplex.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'codeplex (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_TIMEOUT=1800
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
TAGS={'.Net':'%2c.NET%2c','.Net2':'%2c.NET%202.0%2c','.Net3.5':'%2c.NET%203.5%2c','.Net4':'%2c.NET%204.0%2c',
                'ASP':'%2cASP.NET%2c','ASP_MVC':'%2cASP.NET%20MVC%2c','CSharp':"%2cC%23%2c",'Nuke':"%2cDotNetNuke%2c" ,
                    'Framework':"%2cFramework%2c",'Game':'%2cgame%2c','Js':'%2cjavascript%2c','JQuery':"%2cjQuery%2c",'Library': '%2cLibrary%2c',
                        'LINQ':"%2cLINQ%2c",'MVC':'%2cMVC%2c','Powershell':"%2cpowershell%2c",'Sharepoint':"%2cSharepoint%2c", 'Sharepoint2010': "%2cSharePoint%202010%2c",
                            'Sliverlight':"%2cSilverlight%2c","SQL_Server":"%2cSQL%20Server%2c", "Tools":"%2cTools%2c","VB_NET":"%2cVB.NET%2c","VS":"%2cVisual%20Studio%2c", "WPF":"%2cWPF%2c",
                                "XNA":"%2cXNA%2c" }
STORE_SQL = True
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'codeplex.middlewares.CodeplexSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
 #   'codeplex.middlewares.MyCustomDownloaderMiddleware': 200,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'codeplex.pipelines.CodeplexPipeline': 300,
    'codeplex.pipelines.CodesPipeline':400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
FILES_STORE = './codes'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"