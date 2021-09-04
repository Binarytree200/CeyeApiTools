# CeyeApiTools
  CeyeApiTools 一个便捷的CeyeDNSlog返回信息监听工具

#### CEYE.IO介绍

  [CEYE.IO](http://ceye.io/)平台，通过自己的 DNS 服务器和 HTTP 服务器监控 DNS 查询和 HTTP 请求。它可以帮助安全研究人员在测试漏洞（例如 SSRF/XXE/RFI/RCE）时收集信息。

  对于每个用户，有一个随机六个字符来与ceye.io组合成的子域名，可以在个人资料页面中找到。记录子域和以下的所有 DNS 查询和 HTTP 请求。例如，`b182oj`是某人的唯一标识符代码，`b182oj.ceye.io`是他/她的子域。对于所有的DNS 请求和HTTP请求`b182oj.ceye.io`和`*.b182oj.ceye.io`将被记录。所有记录都可以从服务器导出，通过处理这些访问日志，研究人员能够确认和改进他们的研究。

#### CeyeApiTools介绍

  CeyeApiTools是根据[CEYE.IO](http://ceye.io/)平台开放出的API接口演化出的，一款便捷查询返回信息监听记录的小工具。（PS：主要原因是我比较懒所以才写的）

##### 使用方法

```
python CeyeApiTools.py -t ”你的ceye api token” -m ”你要查询的类型 DNS or HTTP” -f ”url匹配规则”
```

例如：

![image](https://github.com/Binarytree200/CeyeApiTools/blob/main/image/image.PNG)



同时原始数据会保存在执行CeyeApiTools.py文件的目录下log.txt文件内
