#-*- coding=utf-8 -*-
import requests
import io
import sys

class manu:
    def __init__(self,PageNumber,List):
        self.PageNumber=PageNumber
        self.List=List
    
    def get_page(self):
        

def get_file_from_url(url,filename):
    r=requests.get(url=url)
    r.encoding='gbk'
    fileHandle=open(file,'wb')
    fileHandle.write(r.text.encode('utf-8'))
    fileHandle.close()

def get_manu_from_file(filename):
    
