# Crawl IEEE Pictures

## 爬虫程序实现目标
批量下载IEEE某篇论文中含有的所有图片，并保存到以论文名命令的文件夹中。
同时下载图片命名的规则为论文中的图题。

## 爬虫程序预先环境概述

1. python >= 3
2. python lib: selenium, re, os, requests, time
3. Browser (Firefox or Chrome)
4. [Browser Drivers](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

## 程序使用教程

### python 环境

安装python3及以上的版本，对于Windows用户到[Python下载地址](https://www.python.org/downloads/),
下载对应的安装包，然后安装并配置python环境。对于Linux用户，一般现在的Linux系统默认自带python3。

pip 安装所需的库

```bash
pip install selenium re os requests time

```

### 浏览器驱动配置

由于IEEE的网页设置的反爬虫机制，是无法像怕取正常的网页一样，因此需要使用模拟浏览器的方式
来获取IEEE文章的内容。采用的selenium来驱动浏览器。因此需要安装浏览器驱动。
安装请参考[selenium Browser Drivers](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)。
注意驱动和浏览器版本要匹配。 简单的来说，不要太新也不要太久的浏览器，应该是能良好支持的。
驱动程序的路径添加到系统环境变量中。浏览器选择Firefox或Chrome, 其他不推荐。

### 爬虫程序文件说明

**IEEE_crawl_pictures.py**: 起初最原始的爬虫程序，可能有Bug,不是那么好用，代码组织比较凌乱。

**IEEE_crawl_pictures_3.py**: 代码组织比较清晰，Bug也改了，适合Linux平台。

**IEEE_crawl_pictures_3_two.py**: 适用于爬去的IEEE论文每个图题对应两个图片连接，适合Linux平台。

**IEEE_crawl_pictures_3_win.py**: 适合Windows平台。


### 使用

1. 在Terminal运行如下命令

```bash
python3 IEEE_crawl_pictures_3.py
```

2. 输入IEEE论文网址  例如：`https://ieeexplore.ieee.org/document/7500038`

3. 自动打开火狐浏览器，并打开IEEE论文网页，喝杯小茶等待等待.....
自动创建以论文名的文件夹，其中包含论文的图片，并以论文中图名命名

## 备注

1. 你需要有访问IEEE论文的权限，否则无法下载论文图片。

2. 该IEEE论文网页版含有图片，对于古老的论文，如果网页版没有图片是无法下载的。
