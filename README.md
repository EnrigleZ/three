# 如何配置这个东西
## 下载代码
这个页面右上角有个绿色的 `"Clone or Download"` Button。点一下再点 `"Download ZIP"` 就行，全套安排上了。

## 需要的配置
+ 安装 *Python 3.6*
+ 安装一个 *Google Chrome*
+ 确保第一点搞定后，用 *pip* 安装一些程序需要的别的工具，这些都好说

## 尝试在命令行运行 

```Shell
python three.py
```
如果这一步都有问题的话，大概率是缺点东西

## 功能

直接运行以后，会出现一个 Chrome 窗口，然后就自动按照我的逻辑发送请求。

全部结束后会把文件保存到 `"output/"` 文件夹下。

## 代码具体是什么意思

`fetch_weather` 函数是爬取天气信息，来自 [天气后报](http://www.tianqihoubao.com)。
`fetch_pollution` 函数是获取 PM2.5 等污染物信息，来自 [aqistudy](https://www.aqistudy.cn/historydata/monthdata.php?city=%E8%A5%BF%E5%AE%89)。

其他的可以先看代码的注释。