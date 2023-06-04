import requests
import re
from bs4 import BeautifulSoup


class Tag_Search():
    def __init__(self): 
        self.tag="hairy"
        self.page_num="134"
        self.status=0
        self.headers={
                        'Cookie':'_im_vid=01H1ZSX6KM0XABSHJ59AD0TGZ6; _gid=GA1.2.841562950.1685768281; _ga_X42TH49BB5=GS1.1.1685846370.6.1.1685846371.0.0.0; _ga=GA1.2.1589795454.1685768276',
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.35'
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
        

