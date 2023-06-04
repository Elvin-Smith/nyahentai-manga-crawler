import requests
import re
from bs4 import BeautifulSoup
import os
import batch as batch





class crawler:
    def __init__(self): 
        self.headers={
                        'Cookie':'_im_vid=01H1ZSX6KM0XABSHJ59AD0TGZ6; _gid=GA1.2.841562950.1685768281; _ga_X42TH49BB5=GS1.1.1685802236.5.1.1685807531.0.0.0; _ga=GA1.2.1589795454.1685768276',
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.35'
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