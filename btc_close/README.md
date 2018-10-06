## 交易收盘价走势

分析**Json**格式的交易收盘价数据，并使用Python的可视化包**Pygal**对结果进行数据可视化，以探索价格变化的周期性。

> JSON（JavaScript Object Notation）文件：一种由Douglas Crockford构想和设计、轻量级的数据交换语言，该语言以易于让人阅读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。尽管JSON是JavaScript的一个子集，但JSON是独立于语言的文本格式，并且采用了类似于C语言家族的一些习惯。JSON 数据格式与语言无关，脱胎于 JavaScript，但目前很多编程语言都支持 JSON 格式数据的生成和解析。JSON 的官方 MIME 类型是 application/json，文件扩展名是 .json。
>

**绘制收盘价折线图**：

![](http://pf1jz9eu0.bkt.clouddn.com/18-10-6/32905253.jpg)

为了验证周期性假设，需要先使用对数变换剔除非线性趋势，得到**收盘价对数变换折线图**：

![](http://pf1jz9eu0.bkt.clouddn.com/18-10-6/95453304.jpg)

**收盘价月/周/星期均值**：

![](http://pf1jz9eu0.bkt.clouddn.com/18-10-6/64860335.jpg)

![](http://pf1jz9eu0.bkt.clouddn.com/18-10-6/27402765.jpg)

![1538793985950](C:\Users\QiuYe\AppData\Local\Temp\1538793985950.png)

生成数据仪表盘，将前面绘制的图整合在一起，生成一个完整的html文件，方便进行长期管理、检测和分析。

![](http://pf1jz9eu0.bkt.clouddn.com/18-10-6/17078274.jpg)



