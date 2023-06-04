import Search_with_tag as swt
import batch as batch
import sys
import Manga_crawler
import os
import requests


tag="hairy"


newtag=swt.Tag_Search()
new_crawler=Manga_crawler.crawler()

page=134
while (page<=134):
	page_s="%d"%page
	url="https://nyahentai.re/genre/"+tag+"/page/"+page_s+"/"
	trytimes=1
	succs=False
	while succs==False and trytimes<=3 :
		rurl_list=newtag.get_allurl_current_page(url)
		    #	注意此处也可能是302等状态码
		if newtag.status == 200:
			succs=True
		else:
			trytimes=trytimes+1
			
	if  succs==False:
		sys.exit()
	for url in rurl_list:
		res,book_name = new_crawler.get_page_url(url)
		Name=new_crawler.filter_filename(book_name[0])
		File_Path="K:\\Manga\\"+Name
		if not os.path.exists(File_Path):
			os.mkdir(File_Path)
		pagenum=1
		for page in res:
			
			page_s="%d"%pagenum
			url=new_crawler.Creat_Url(page)
			filename = Name+page_s+".webp"
			filepath= "K:\\Manga\\"+Name+"\\" + filename
			
			for i in range(trytimes):
				try:					
					print(url)
					res_1 = requests.get(url)
		    		#	注意此处也可能是302等状态码
					if res_1.status_code == 200:
						succs=True
						break
				except:
	    			#logdebug(f'requests failed {i}time')
					print(f'requests failed {i} time')
					succs=False
			if i==2 & succs==True:
				sys.exit()
			with open(filepath, 'wb') as f:
				f.write(res_1.content)
				print(filepath)
				pagenum=pagenum+1


		newtype = batch.proimage()
		newtype.setpath(File_Path)
		filelist=newtype.read()
		newtype.webp2jpg(filelist)
	page=page-1



	    
	    
	    
	    
		
	
		
		

