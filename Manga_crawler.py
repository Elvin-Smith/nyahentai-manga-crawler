import requests
import re
from bs4 import BeautifulSoup
import os
import batch as batch





class crawler:
    def __init__(self): 
        self.headers={
                        'Cookie':'',
                        'User-Agent':''
                    }
        
        
    def get_page_url(self,url):
        response=requests.get(url=url,headers=self.headers)
        #soup返回是list
        soup = BeautifulSoup(response.content, 'html.parser')
        #list拼接成str
        string_html=" ".join(map(str,soup.find_all(id="post-comic")))
        pattern = re.compile(r'src="https:(.*?).webp',re.S)
        pattern_book = re.compile(r'<img alt="(.*?) Page',re.S)
        res=re.findall(pattern,string_html)
        book_name=re.findall(pattern_book,string_html)
        return res ,book_name
        

    def filter_filename(self,filename):
        # 定义非法字符的正则表达式
        illegal_chars = r'[<>:"/\\|?*\x00-\x1F]'
        # 使用正则表达式替换非法字符为空字符串
        filtered_filename = re.sub(illegal_chars, '', filename)
        return filtered_filename
    
    def Creat_Url(self,res):
        url="https:"+res+".webp"
        return url
