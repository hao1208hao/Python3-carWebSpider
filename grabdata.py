# coding: UTF-8 
import urllib.request, urllib.parse, urllib.error
import http.cookiejar
#import urllib2,urllib,cookielib,re
from bs4  import BeautifulSoup 
import codecs
from  datetime  import  * 
#import phpserialize
import re
#import  time

#from sql import MSSQL
import pymysql.cursors

if __name__ == "__main__":
    
    LOGIN_URL = 'http://www.cvchome.com/product/index.php?cid=247'
    
    user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    
    url = 'http://www.cvchome.com/product/index.php?cid=247'

    request = urllib.request.Request(LOGIN_URL,"", headers)
    try:
        res = urllib.request.urlopen(LOGIN_URL).read()
        data = res.decode('utf-8')
        #print(data)
    except urllib.error.URLError as e:
        print(e.code, ':', e.reason)
    #处理BOM头
    if data[:3] == codecs.BOM_UTF8: 
        data = data[3:]
    #print(data.decode())
    #beautifulsoup 解析
    soup = BeautifulSoup(data, "html.parser")
    tr=soup.find_all('div', attrs={'class':'title'})
    ##########################①拿到所有车型
    # 1 是大类名
    # 2是品牌首字母
    # 3是品牌名
    # 4是车型名
    # 5是车类型名
    # 6是具体车型
    #print(tr[1].find_all('a'))
    for i in tr[1].find_all('a'):
       #print("①-----------"+i.get('title'))
       need1 = i.get('title')
       res = urllib.request.urlopen(i.get('href')).read()
       data = res.decode('utf-8')
       #解析左侧列表
       soup = BeautifulSoup(data, "html.parser")
       tr=soup.find_all('div', attrs={'class':'l_fl_list'})
       tree=(tr[0].find_all('dd', attrs={'class':'tree-cate'}))
       #A-Z
       for j in tree:
          
          #print("②-----------"+j.i.contents[0])
          need2 = j.i.contents[0]
          cate=j.find_all('a', attrs={'class':'cate-name'})
          for k in cate:
              #print("③-----------"+k.get('title'))
              need3 = k.get('title')
              items=j.find_all('dl', attrs={'class':'items'})
              for l in items:
                  itemsa=l.find_all('a')
                  for m in itemsa:
                      #print("④-----------"+m.get('title')+m.font.contents[0])
                      need4 = m.get('title')
                      need5 = m.font.contents[0]
                      paramURL = m.get('href').split('?')[1].split('#')[0]
                      #print('id集合-----'+paramURL)
                      paramList = paramURL.split('&')
                      catid = paramList[0].split('=')[1]   #车大类ID
                      brandid = paramList[1].split('=')[1]  #品牌ID
                      brandsn = paramList[2].split('=')[1]  #车型ID

                      #print('车大类ID==='+catid+'    品牌ID==='+brandid+'   车型ID==='+brandsn)

                  
                      res = urllib.request.urlopen(m.get('href')).read()
                      data1 = res.decode('utf-8')
                      #print(data1)
                      soup1 = BeautifulSoup(data1, "html.parser")                 
                      # item=soup1.find('div', attrs={'class':'dl_cx'})
                      # c1=item.find('div', attrs={'class':'c1'})
                      # print("⑥-----------"+c1.find_all('div', attrs={'class':'about'})[0].find('a').contents[0])
                      totalpage='';
                      if(soup1.find('cite')):
                          totalpage=soup1.find('cite').contents[0].split('/')[1].replace('页','')
                      else:
                          totalpage=1

                      #re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
                      #拿到第五级分页，从第一页逐页查询
                      #print("href-----------"+m.get('href').split('#')[0])
                      if(int(totalpage)>2):
                          for i in range(0,int(totalpage)):
                        
                             res = urllib.request.urlopen(m.get('href').split('#')[0]+'&page='+str(i+1)).read()
                             data1 = res.decode('utf-8')
                             #print(data1)
                             soup1 = BeautifulSoup(data1, "html.parser")                 
                             item=soup1.find_all('div', attrs={'class':'dl_cx'})
                             #c1=item.find_all('div', attrs={'class':'c1'})
                             #循环每一页的列表
                             for n in item:
                                #print("⑤-----------"+n.find_all('div', attrs={'class':'about'})[0].find('a').contents[0])
                                #print("⑥-----------"+n.find_all('div', attrs={'class':'about'})[0].find('a').get('href'))
                                res = urllib.request.urlopen(n.find_all('div', attrs={'class':'about'})[0].find('a').get('href').replace('show','show_param')).read()
                                data1 = res.decode('utf-8')        
                                soup1 = BeautifulSoup(data1, "html.parser")                 
                                #print(soup1.find('div', attrs={'class':'cs'}))



                                #print("①-----------"+need1)
                                #print("②-----------"+need2)
                                #print("③-----------"+need3)
                                #print("④-----------"+need4)
                                
                                print('===================此款车开始======================')
                                print('车大类ID==='+catid+'    品牌ID==='+brandid+'   车型ID==='+brandsn)


                                #http://www.cvchome.com/product/show.php?itemid=10130   详情url
                                detailURL = n.find_all('div', attrs={'class':'about'})[0].find('a').get('href')                                
                                detailID = detailURL.split('?')[1].split('=')[1]
                                print("详细最终ID==="+detailID)
                                
                                listName = n.find_all('div', attrs={'class':'about'})[0].find('a').contents[0]
                                carParam = soup1.find('div', attrs={'class':'cs'})

                                print("车大类名==="+need1+'    品牌首字母==='+need2+'   品牌名==='+need3+'    车型名==='+need4)
                                print("车型小类名==="+need5+'    具体车型名==='+listName)                                
                                

                                about = soup1.find('div', attrs={'class':'cs'}).find('div',attrs={'class':'about'})
                                arr = about.find_all('div',attrs={'class':'content'})
                               
                                engienType = (str)(arr[5].find_all('dt')[0])    #发动机型号
                                engienType = engienType.replace('<dt><span>','').replace('</dt>','').replace('</span>','')
                                print('发动机型号==='+engienType)


                                print('===================此款车完成======================')
                                
                                #print('车参数==='+str(carParam)

                                a = int(catid)
                                b = int(brandid)
                                c = int(brandsn)
                                d = int(detailID)
                                
                                sql = " INSERT INTO cardata(catid,brandid,brandsn,itemid,carname,brandshortname,brandname,cartypename,cartype,detailcarname,engine) values('%d','%d','%d','%d','%s','%s','%s','%s','%s','%s','%s')"
                                #print(sql)
                                data = (a,b,c,d,need1,need2,need3,need4,need5,listName,engienType)
                                #print(data)
                                mssql = pymysql.Connect(host='localhost', port=3306, user="root", password="", db="testjava",charset='utf8')
                                cursor = mssql.cursor()
                                cursor.execute(sql % data)
                                mssql.commit()

                                print("===============成功插入数据库===============+"+str(cursor.rowcount))
                                #mssql.ExecQuery(sql % data)
                                #self.userlist = mssql.resList


                                
                                
                                #拿到每个详情页
                                #break
                             #break
                      #print(item.find('div', attrs={'class':'c1'}))
                      #print(item.find('div', attrs={'class':'c2'}))
                      #break
                # break
          #print(cate)
           #break
 
   
