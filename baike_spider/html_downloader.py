#encoding:utf-8
'''
Created on 2017��5��19��

@author: Teixe
'''
from urllib import request


class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        response = request.urlopen(url)
        if response.getcode() != 200:
            print(response.getcode())
            return None
        return response.read()


