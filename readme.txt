IEEE python 论文抓取图片使用说明
1. 安装python (python 3.7.9)
2. 安装python 库 selenium requests re  （命令行安装 例如：pip install selenium）
3. 安装火狐浏览器（firefox 78） 
4. 配置火狐浏览器驱动 
	驱动文件名为 geckodriver.exe
	配置系统环境环境 path，在path后添加geckodriver.exe所在的路径。
5.使用说明
	双击IEEE_craw_pictures_3_win.py文件
	输入IEEE论文网址 		例如：https://ieeexplore.ieee.org/document/7500038
	自动打开火狐浏览器，并打开IEEE论文网页，喝杯小茶等待等待.....
	自动创建以论文名的文件夹，其中包含论文的图片，并以论文中图名命名

6.结束