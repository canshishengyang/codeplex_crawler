from codeplex.spiders.codeplexSpider import codeplexSpider

class NetCrawler(codeplexSpider):
   name=".Net"
   tagName="%2c.NET%2c"
class Net2Crawler(codeplexSpider):
   name='.Net2'
   tagName="%2c.NET%202.0%2c"
class Net3_5Crawler(codeplexSpider):
   name='.Net3.5'
   tagName="%2c.NET%203.5%2c"
class Net4Crawler(codeplexSpider):
   name='.Net4'
   tagName="%2c.NET%204.0%2c"
class ASPCrawler(codeplexSpider):
   name='ASP'
   tagName="%2cASP.NET%2c"    
class ASP_MVC_Crawler(codeplexSpider):
   name='ASP_MVC'
   tagName="%2cASP.NET%20MVC%2c"
class CSharp_Crawler(codeplexSpider):
   name='CSharp'
   tagName= "%2cC%23%2c"
class Nuke_Crawler(codeplexSpider):
   name='Nuke'
   tagName ="%2cDotNetNuke%2c" 
class Framework_Crawler(codeplexSpider):
   name = 'Framework'
   tagName ="%2cFramework%2c" 
class Game_Crawler(codeplexSpider):
   name= 'Game'
   tagName ="%2cgame%2c"
class Js_Crawler(codeplexSpider):
   name = 'Js'
   tagName = "%2cjavascript%2c"
class JQuery_Crawler(codeplexSpider):
   name = 'JQuery'
   tagName = "%2cjQuery%2c"
class Library_Crawler(codeplexSpider):
   name = 'Library'
   tagName = "%2cLibrary%2c"
class LINQ_Crawler(codeplexSpider):
   name = 'LINQ'
   tagName = "%2cLINQ%2c"
class MVC_Crawler(codeplexSpider):
   name = 'MVC'
   tagName = "%2cMVC%2c"
class Powershell_Crawler(codeplexSpider):
   name = 'Powershell'
   tagName = "%2cpowershell%2c"
class Sharepoint_Crawler(codeplexSpider):
   name = 'Sharepoint'
   tagName = "%2cSharepoint%2c"
class Sharepoint2010_Crawler(codeplexSpider):
   name = 'Sharepoint2010'
   tagName = "%2cSharePoint%202010%2c"
class Sliverlight_Crawler(codeplexSpider):
   name = 'Sliverlight'
   tagName = "%2cSilverlight%2c"
class Sqlserver_Crawler(codeplexSpider):
   name = "SQL_Server"
   tagName = "%2cSQL%20Server%2c"
class Tools_Crawler(codeplexSpider):
   name = "Tools"
   tagName = "%2cTools%2c"
class VBNET_Crawler(codeplexSpider):
   name = "VB_NET"
   tagName = "%2cVB.NET%2c"
class VS_Crawler(codeplexSpider):
   name = "VS"
   tagName = "%2cVisual%20Studio%2c"
class WPF_Crawler(codeplexSpider):
   name = "WPF"
   tagName = "%2cWPF%2c"
class XNA_Crawler(codeplexSpider):
   name = "XNA"
   tagName = "%2cXNA%2c"
class ALL_Crawler(codeplexSpider):
   name = "ALL"
   tagName = ""