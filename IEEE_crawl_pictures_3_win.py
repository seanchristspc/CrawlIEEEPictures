#coding=utf-8
"""
程序功能： 爬取IEEE某一篇论文的所有图片
时间：2020-10-30 13:20
环境: Windows
"""

#导入需要的库
from selenium import webdriver
import re
import os
import requests
import time

class IEEE_DOC():
  """IEEE_DOC 为IEEE文档类"""
  def __init__(self, id_number, title, figures):
    """
    id_number: IEEE文档编号
    title: IEEE文档标题
    figures: IEEE文档所含的图片
    """
    self.id_number = id_number
    self.title = title
    self.figures = figures


class Figure():
  """Figure 为图片类"""
  def __init__(self, caption, link):
    """
    caption: 图片的标题
    link: 图片的链接
    """
    self.caption = caption
    self.link = link


class IEEECrawlPictures():
  """IEEECrawlPictures 为IEEE爬虫类"""
  def __init__(self, url):
    """
    url:爬取论文的链接
    """
    self.url = url


  def get_fig_captions(self,fig_caption_list):
    """获得图片标题"""
    captions=[]
    for fig_caption in fig_caption_list:
        caption_raw=fig_caption.text.split('\\')[0]
        print(re.sub(r'[\/.()\n:]','',caption_raw))
        captions.append(re.sub(r'[\/.()\n:]','',caption_raw))
    return captions

  def get_fig_links(self,fig_href_list):
      """获取图片链接"""
      links=[]
      for fig_link in fig_href_list:
          link=fig_link.get_attribute('href')
          print(link)
          links.append(link)

      return links


  def make_dir(self, new_dir_name):
    """在当前文件夹创建目录并返回目录的路径"""
    #获取当前路径
    current_path=os.getcwd()
    #新的目录路径
    new_dir_path=current_path+"\\"+new_dir_name
    try:
      if not os.path.exists(new_dir_path):
        #目录不存在，则创建
        os.mkdir(new_dir_path)
        #返回目录路径
        return new_dir_path
      else:
        #目录存在，返货目录路径
        return new_dir_path
    except Exception as e:
      raise e

  def create_figures(self, captions, links):
    """创建图片列表"""
    i = 0
    figures=[]
    for i in range(len(captions)):
      fig = Figure(captions[i],links[i])
      figures.append(fig)

    return figures


  def get_IEEE_doc(self):
    driver = webdriver.Firefox()
    driver.get(self.url)

    #延时60s 等待服务器响应
    time.sleep(60)
    #获取文章标题
    title = driver.title
    #获取图片标题标签
    fig_caption_list = driver.find_elements_by_css_selector(".figcaption")
    #获取图片链接
    fig_href_list = driver.find_elements_by_css_selector(".img-wrap a")
    current_url = driver.current_url
    id_number = re.findall(r'\d{6,8}',current_url)


    captions = self.get_fig_captions(fig_caption_list)
    links = self.get_fig_links(fig_href_list)
    #输出获取标题和链接数量
    print("captions number="+str(len(captions)))
    print("links number="+str(len(links)))

    #关闭浏览器
    driver.quit()
    figures = self.create_figures(captions,links)

    ieee_doc=IEEE_DOC(id_number, title, figures)

    return ieee_doc


  def get_new_dir_name(self, title):
    """获取创建目录名""" 
    new_dir_name=re.sub(r'[\/.()&$!@%*:]','',title) 
    return new_dir_name


  def save_pictures(self, ieee_doc):
    """保存图片"""
    print("正在保存图片......")
    new_dir_name = self.get_new_dir_name(ieee_doc.title)
    new_dir_path = self.make_dir(new_dir_name)

    figures = ieee_doc.figures

    i = 0

    for i in range(len(figures)):
      fig = figures[i]
      if len(fig.caption)>50:
        fig.caption=fig.caption[0:49]

      print("="*80)
      print("number: "+str(i))

      path = new_dir_path+"\\"+fig.caption+".gif"
      #输出正在保存图片的链接 图题 保存路径
      print("link:"+fig.link)
      print("caption"+fig.caption)
      print("path:"+path)

      try:
        r = requests.get(fig.link)
        r.raise_for_status()
        with open(path,'wb') as f:
          f.write(r.content)
          f.close()
          print(fig.caption+"\n图片保存成功")
      except Exception as e:
        raise e



if __name__=="__main__":
    #主函数
    # 下载图片网页
    url=input("请输入IEEE网站对应论文的网址:")
    #创建ieee图片爬虫类
    ieee_crawl_picture = IEEECrawlPictures(url)
    #创建IEEE_DOC类
    ieee_doc = ieee_crawl_picture.get_IEEE_doc()
    ieee_crawl_picture.save_pictures(ieee_doc)
    print("document number: "+str(ieee_doc.id_number))
    print("document title: "+ieee_doc.title)

    

