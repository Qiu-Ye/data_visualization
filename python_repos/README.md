## 最受欢迎的Python仓库

通过GitHub的API调用，自动下载GitHub上星级最高的Python项目信息，并对这些信息进行可视化。

> `https://api.github.com/search/repositories?q=language:python&sort=stars`
>
> 该调用返回GitHub上托管的Python项目情况，并以`stars`数目排序显示最受欢迎的仓库信息。

对信息进行提取，以星级排名最高的仓库为例：

```json
Name: awesome-python
Owner: vinta
Stars: 55866
Repository: https://github.com/vinta/awesome-python
Created: 2014-06-27T21:00:06Z
Updated: 2018-10-06T07:56:56Z
Description: A curated list of awesome Python frameworks, libraries, software and resources
```

使用Pygal可视化仓库：

![](http://pf1jz9eu0.bkt.clouddn.com/18-10-6/37321635.jpg)

在Pygal生成的**svg文件**中，将鼠标指向条形将显示**工具提示**信息。以字典的方式向Pygal传入更多信息，可以创建自定义工具提示。

添加仓库相关联的描述信息，鼠标滑过条形，交互信息会显示该仓库的`starts`数以及其描述信息。

![](http://pf1jz9eu0.bkt.clouddn.com/18-10-6/24594309.jpg)

添加仓库相关联的URL将每个条形都转换为活跃的链接，单击图表中的任何条形，都会通过浏览器跳转到相应项目的GitHub页面。



![](http://pf1jz9eu0.bkt.clouddn.com/18-10-6/30171204.jpg)
