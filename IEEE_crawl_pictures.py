#!/usr/bin/env python3

#encoding=utf-8
"""
time: 2020-10-30 13:45
linux 
"""
from selenium import webdriver

import re
import os
import requests
import time
def get_fig_captions(fig_caption_list):
    """获得图片标题"""
    captions=[]
    for fig_caption in fig_caption_list:
        caption_raw=fig_caption.text.split('\\')[0]
        captions.append(re.sub(r'[:*.()\n]','',caption_raw))
    return captions

def get_fig_links(fig_href_list):
    """获取图片链接"""
    links=[]
    for fig_link in fig_href_list:
        link=fig_link.get_attribute('href')
        links.append(link)

    return links

def make_dir(dir_name):
    """当前目录创建文件夹"""
    #获取当前路径
    current_dir=os.getcwd()
    dir_path=current_dir+"/"+dir_name

    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            return dir_path
        return dir_path

    except Exception as e:
        raise e


def save_pictures(dir_name,links,captions):
    """保存图片"""
    dir_path=make_dir(dir_name)
    print("links number="+str(len(links)))
    print("captions number="+str(len(captions)))
    i=0
    for i in range(len(captions)):
        link=links[i]
        caption=captions[i]
        path=dir_path+'/'+caption+'.gif'
        print("="*50)
        print(i)
        print("link:"+link)
        print("caption:"+caption)
        print("path:"+path)
        try:
            r = requests.get(link)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print(caption+"图片保存成功！")
        except Exception as e:
            raise e

if __name__=="__main__":
    #主函数
    # 下载图片网页
#    url="https://ieeexplore.ieee.org/document/5256191/figures#figures"
    
    url=input('输入IEEE论文网址:')
    driver = webdriver.Firefox()
    driver.get(url)
    #等待40s登录
    time.sleep(40)
    dir_name=re.sub(r':.\/&%$@()','',driver.title)
    print('dir_name:'+dir_name)

    #得到图片标题
    fig_caption_list=driver.find_elements_by_css_selector(".figcaption")

    #得到图片链接
    fig_href_list=driver.find_elements_by_css_selector(".img-wrap a")
    captions=get_fig_captions(fig_caption_list)
    links=get_fig_links(fig_href_list)
    driver.quit()
    save_pictures(dir_name,links,captions)

