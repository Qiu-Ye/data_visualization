## 西安市2017-2018年度气温分析

在[气象网站](https://rp5.ru/%E8%A5%BF%E5%AE%89%E5%A4%A9%E6%B0%94_)上获取西安市一年的气温数据（CSV格式），从中提取出每一天的最高温和最低温，并将这些数据进行可视化。

> CSV 文件：A **CSV** is a comma separated values **file** which allows data to be saved in a table structured**format**. CSVs look like a garden-variety spreadsheet but with a .**csv** extension. Traditionally they take the form of a text **file** containing information separated by commas, hence the name.



从文件中提取数据集后，用**matplotlib**绘制气温图标折线图。

![](http://img.qiuye.online/18-10-5/74754486.jpg)



通过给图表区域着色可以使得温度变化更加直观，但建议将着色区域的透明度设置的低一些，这样会让填充区将两个数据系列连接起来的同时不分散观察者的注意力。