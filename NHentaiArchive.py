# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 00:18:34 2018

@author: HateNoSaiShi
"""

import os
import shutil



def GetAuthor(title):
    author = title.split('[')[1].split(']')[0]
    return author

#===
    
def GetAllComicTitle(path = r'E://touhou//doujin//待归档爬虫//'):
    return os.listdir(path)

#===
    
def CreateFolder(folder_name, path = r'E://touhou//doujin//红字本//'):
    to_create_path = path + folder_name
    folder = os.path.exists(to_create_path)
    if not folder:
        os.makedirs(to_create_path)          
    
#===

def MoveComic(old_path, new_path):
    shutil.copytree(old_path, new_path)
    
#===

def main():
    old_path_prefix = r'E://touhou//doujin//待归档爬虫//'
    new_path_prefix = r'E://touhou//doujin//红字本//'
    comic_title_list = GetAllComicTitle()
    for title in comic_title_list:
        author = GetAuthor(title)
        CreateFolder(author)
        temp_old_path = old_path_prefix + title
        temp_new_path = new_path_prefix + author + '//' + title
        try:
            MoveComic(temp_old_path, temp_new_path)
        except:
            print(title, 'exists!')
        
        
        
#=====
if __name__ == '__main__':
    main()
