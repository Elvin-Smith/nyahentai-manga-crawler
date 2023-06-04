import requests
import re
from bs4 import BeautifulSoup


class Tag_Search():
    def __init__(self): 
        self.tag="hairy"
        self.page_num="134"
        self.status=0
        self.headers={
                        'Cookie':'',
                        'User-Agent':''
                    }

    def Creat_url(self,page_current):
        url="https://nyahentai.re/genre/"+self.tag+"/page/"+page_current+"/"
        return url
    
    def get_allurl_current_page(self,url):
        response=requests.get(url=url,headers=self.headers)
        self.status=response.status_code
        soup = BeautifulSoup(response.content, 'html.parser')
        string_html=" ".join(map(str,soup.find_all(class_="post-list")))
        pattern = re.compile(r'href="(.*?)">',re.S)
        res=re.findall(pattern,string_html)
        return res
        

