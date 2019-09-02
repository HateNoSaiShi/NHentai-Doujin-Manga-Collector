# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 00:05:25 2018

@author: HateNoSaiShi
"""

from urllib import request 
from bs4 import BeautifulSoup as bs
import os
import time
import shutil
import re
import requests

def ValidateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "", title) 
    return new_title

#===
    
def GetBeautifulSoup(gallery_id):
    url = "https://nhentai.net/g/" + str(gallery_id)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
              } 
    ##request_object = request.Request(url = url, headers = headers)
    ##res = request.urlopen(request_object).read().decode('utf-8')
    res = requests.get(url, headers = headers).text
    html = bs(res, 'lxml')
    return html
    
#===

def GetAttributes(html):
    title = html.find('h2').text
    illustration_list = html.find_all(class_ = 'thumb-container')
    num_of_illus = len(illustration_list)
    temp_src = illustration_list[0].find(class_ = 'lazyload').attrs['data-src']
    download_model_id = temp_src.split('galleries/')[1].split('/')[0]
    res_dic = {
                  'title': title,
                  'illustration_num': num_of_illus,
                  'download_model_id': download_model_id
              }
    return res_dic
    
#===

def CreateFolder(folder_name, path = r'E://touhou//doujin//待归档爬虫//'):
    to_create_path = path + folder_name
    folder = os.path.exists(to_create_path)
    if not folder:
        os.makedirs(to_create_path)          
    else:
        shutil.rmtree(to_create_path)
        os.makedirs(to_create_path)
    return to_create_path

#===

def DownloadQuest(gallery_id, path = r'E://touhou//doujin//待归档爬虫//'):
    html = GetBeautifulSoup(gallery_id)
    attr_dic = GetAttributes(html)
    folder_name = ValidateTitle(attr_dic['title'])
    download_model_id = attr_dic['download_model_id']
    num = attr_dic['illustration_num']
    download_path = CreateFolder(folder_name, path)
    download_url_prefix = 'https://i.nhentai.net/galleries/'
    download_url_suffix1 = '.jpg'
    download_url_suffix2 = '.png'
    download_url_suffix3 = '.gif'
    for i in range(num):
        illus_number = i + 1
        try:
            # if jpg
            download_url = download_url_prefix + download_model_id + '/' + str(illus_number) + download_url_suffix1
            file_name = download_path + '//' + str(illus_number) + download_url_suffix1
            request.urlretrieve(download_url, filename=file_name, reporthook=None, data=None)
        except:
            try:
                # if png
                download_url = download_url_prefix + download_model_id + '/' + str(illus_number) + download_url_suffix2
                file_name = download_path + '//' + str(illus_number) + download_url_suffix2
                request.urlretrieve(download_url, filename=file_name, reporthook=None, data=None)
            except:
                # if gif
                download_url = download_url_prefix + download_model_id + '/' + str(illus_number) + download_url_suffix3
                file_name = download_path + '//' + str(illus_number) + download_url_suffix3
                request.urlretrieve(download_url, filename=file_name, reporthook=None, data=None)
    print('complete ' + folder_name + str(gallery_id))
    print('')
    return 0
    
    
#====
if __name__ == '__main__':
    _list= [182108]

    for id in _list:
        is_unfinished = 1
        while (is_unfinished):
            try:
                is_unfinished = DownloadQuest(id)
            except:
                print('Error')
                time.sleep(5)
                
