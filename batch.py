import os
from PIL import Image

#图像预处理包括修改图像格式、编号
class proimage():
    def __init__(self): 
        self.path = "K:\\Crawler\\Majə"
    
    #读取文件夹下图像
    def read(self):
        filelist=os.listdir(self.path)
        return filelist
    
    def setpath(self,path):
        self.path =path

    def webp2jpg(self,filelist):
        #查找图像方式不同，该函数只查找所有.webp格式的文件
        for item in filelist:
             if item.endswith('.webp') :                 
                  src = os.path.join(os.path.abspath(self.path), item)
                  print("src=",src)
                  im=Image.open(src)
                  im.load()
                  save_name=src.replace('webp','jpg')
                  im.save('{}'.format(save_name),'JPEG')
                  os.remove(src)               

if __name__ == '__main__':
    newtype = proimage()
    filelist=newtype.read()
    newtype.webp2jpg(filelist)
