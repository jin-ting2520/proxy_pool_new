ProxyPool 爬虫代理IP池 优化增强
=======

### ProxyPool

[原作者项目地址](https://github.com/jhao104/proxy_pool) 感谢jhao104之前项目贡献，因原项目停更，根据自己需求修改了下  

修复：  
&emsp;&emsp;1、去除imp依赖报错  
&emsp;&emsp;2、代理地区获取失败  
&emsp;&emsp;3、ProxyValidator中httpTimeOutValidator、httpsTimeOutValidator代理使用错误  
&emsp;&emsp;4、docker运行时报错，sh: can't open 'start.sh': No such file or directory

新增：  
&emsp;&emsp;1、随机user_agents列表更新   
&emsp;&emsp;2、代理源更新，部分代理源需要外网或代理访问   
&emsp;&emsp;3、新增WebRequest.Session方法，解决简易反爬虫，用于需要传递Cookie才能显示完整内容的网站   
&emsp;&emsp;4、PROXY_FETCHER列表自动加载，不再需要手动新增，会扫描proxyFetcher.py中的所有方法，所以不用的注释掉   
&emsp;&emsp;5、重构getCount方法    
&emsp;&emsp;6、get、pop、all新增返回ip:port列表，对应gettxt、poptxt、alltxt    
&emsp;&emsp;7、get、pop、all、gettxt、poptxt、alltxt新增查询参数，更便捷    
&emsp;&emsp;8、获取http代理的匿名级别  
&emsp;&emsp;9、抓取代理时新增代理选项(setting.py配置)，适合国内用户拉取国外网站  
&emsp;&emsp;10、新增日志文件配置(setting.py配置)，适合机器硬盘小的用户，可只输出到控制台，不输出到文件  
&emsp;&emsp;11、新增proxy_type字段，用于标识该代理的类型，去除https字段  
&emsp;&emsp;12、ProxyValidator代理测试时采用随机user_agent  
&emsp;&emsp;13、实现socks4/socks5代理的抓取和检测  
&emsp;&emsp;14、将docker内项目根目录挂载到宿主机  
&emsp;&emsp;15、count方法修改，新增爬取全部代理数和存活率  
&emsp;&emsp;16、引入quickjs模块，使其支持js运算  
&emsp;&emsp;17、重构proxy采集/检查的定时任务逻辑    
&emsp;&emsp;18、使用异步工作协程和aiohttp重构proxy检测逻辑，大幅度提高检测速度    

```
结果示例
/count
{
  "count": "2411/378242 有效率：0.64%",
  "proxy_type": {
    "http": 1833,
    "https": 115,
    "socks4": 1431,
    "socks4tohttps": 93,
    "socks5": 1101,
    "socks5tohttps": 96
  },
  "source": {
    "customProxy01": "2338/374780 有效率：0.62%",
    "freeProxy02": "98/300 有效率：32.67%",
    "freeProxy03": "46/228 有效率：20.18%",
    "freeProxy04": "23/50 有效率：46.00%",
    "freeProxy05": "58/126 有效率：46.03%",
    "freeProxy07": "14/300 有效率：4.67%",
    "freeProxy08": "8/200 有效率：4.00%",
    "freeProxy09": "34/90 有效率：37.78%",
    "freeProxy10": "1/280 有效率：0.36%",
    "freeProxy11": "77/1273 有效率：6.05%",
    "freeProxy12": "1/175 有效率：0.57%",
    "freeProxy13": "2/11 有效率：18.18%",
    "freeProxy14": "20/20 有效率：100.00%",
    "freeProxy15": "16/20 有效率：80.00%",
    "freeProxy16": "26/60 有效率：43.33%"
  }
}


/get
{
  "anonymous": 2,
  "check_count": 1,
  "fail_count": 0,
  "last_status": true,
  "last_time": "2025-05-14 05:01:07",
  "proxy": "123.154.30.68:8085",
  "proxy_type": [
    "http"
  ],
  "region": "浙江省温州市 联通",
  "source": "customProxy01"
}
```

## 运行项目
### Windows中运行需要python版本3.12及以下，3.13部分依赖安装报错。其他系统无要求
#### 不管哪种方式运行，请提前安装好redis  

### 源代码运行 <br/><br/>
##### 下载代码:

* git clone

```bash
git clone https://github.com/jin-ting2520/proxy_pool_new.git
```

##### 安装依赖:

```bash
pip install -r requirements.txt
```

##### 更新配置:

```python
# setting.py 为项目配置文件

# 配置API服务
HOST = "0.0.0.0"               # IP
PORT = 5000                    # 监听端口
# 配置数据库

# 修改pwd
DB_CONN = 'redis://:pwd@127.0.0.1:6379/0'

# 抓取代理时使用的代理是否使用代理
USE_PROXY = True
# 抓取代理时使用的代理
PROXIES = {'http': "http://127.0.0.1:7897", 'https': "http://127.0.0.1:7897"}

# 是否将日志输出到文件
INPUT_LOG_FILE = True
# 日志文件保存日期
LOG_FILE_SAVE_DATE = 1
```

#### 启动项目:

```bash
# 启动调度程序
python proxyPool.py schedule

# 启动webApi服务
python proxyPool.py server

```
<br/>

### Docker 运行

```
# 必须拉取源代码
git clone https://github.com/jin-ting2520/proxy_pool_new.git
# 启动之前注意修改setting.py文件中的代理配置以及下方命令中redis的password
docker run -v $PWD/proxy-pool-new:/proxy-pool-new --env DB_CONN=redis://:password@172.17.0.1:6379/0 -p 5010:5010 --name proxy_pool_new ywtm/proxy_pool_new:latest
```
### docker-compose 运行

项目目录下运行: 
```
git clone https://github.com/jin-ting2520/proxy_pool_new.git
cd proxy_pool_new
# 启动之前注意修改setting.py文件中的代理配置
docker-compose up -d
```

### 使用

* Api

启动web服务后, 默认配置下会开启 http://127.0.0.1:5010 的api接口服务:

| api      | method | Description         | params                           |
|----------| ---- |---------------------|----------------------------------|
| /        | GET | api介绍               | None                             |
| /get     | GET | 随机获取一个代理            | 可选参数: 见下表                        |
| /gettxt  | GET | 随机获取一个代理,ip:port格式  | 可选参数: 见下表 |
| /pop     | GET | 获取并删除一个代理           | 可选参数: 见下表 |
| /poptxt  | GET | 获取并删除一个代理,ip:port格式 | 可选参数: 见下表 |
| /all     | GET | 获取所有代理              | 可选参数: 见下表 |
| /alltxt  | GET | 获取所有代理,ip:port格式    | 可选参数: 见下表 |
| /count   | GET | 查看代理数量              | None                             |
| /delete  | GET | 删除代理                | `?proxy=host:ip`                 |
| /cleardb | GET | 清空代理                | None                  |  

* 查询可选参数  

| 参数名        | 参数可选值                                                                              | 说明                                                                                                                                                                                                                                        |
|--------------|------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type         | http, httptohttps,<br/>https, <br/>socks4,socks4tohttps,<br/>socks5, socks5tohttps | 获取代理类型<br/>http: http代理连接http网站<br/>httptohttps: http代理连接https网站<br/>https: https代理连接https网站<br/>socks4: socks4代理连接http网站<br/>socks4tohttps: socks4代理连接https网站<br/>socks5: socks5代理连接http网站<br/>socks5tohttps: socks5代理连接https网站          |
| region       | 目前只支持中文 e.g. 香港                                                                    | 代理地区                                                                                                                                                                                                                                      |
| anonymous    | 0，1，2                                                                              | HTTP代理匿名级别<br/>0（透明代理）<br/>1（匿名代理）<br/>2（高匿代理）                                                                                                                                                                                            |  

* 爬虫使用  

　　如果要在爬虫代码中使用的话， 可以将此api封装成函数直接使用，例如：  
```python
import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
            html = requests.get('http://www.example.com', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 删除代理池中代理
    delete_proxy(proxy)
    return None
```

### 扩展代理

　　项目默认包含几个免费的代理获取源，但是免费的毕竟质量有限，所以如果直接运行可能拿到的代理质量不理想。所以，提供了代理获取的扩展方法。

　　添加一个新的代理源方法如下:

* 1、首先在[ProxyFetcher](fetcher/proxyFetcher.py)类中添加自定义的获取代理的静态方法，
该方法需要以生成器(yield)形式返回`host:ip`格式的代理，例如:

```python

class ProxyFetcher(object):
    # ....

    # 自定义代理源获取方法
    @staticmethod
    def freeProxyCustom1():  # 命名不和已有重复即可

        # 通过某网站或者某接口或某数据库获取代理
        # 假设你已经拿到了一个代理列表
        proxies = ["x.x.x.x:3128", "x.x.x.x:80"]
        for proxy in proxies:
            yield proxy
        # 确保每个proxy都是 host:ip正确的格式返回
```

* 2、添加好方法后，会自动加载，无需配置。  
　`schedule` 进程会每隔一段时间抓取一次代理，下次抓取时会自动识别调用你定义的方法。

<br/> 

### 优惠流量卡
<a href ="https://h5.lot-ml.com/ProductEn/Index/b7e168241f1ef901"><img src="https://dlink.host/1drv/aHR0cHM6Ly8xZHJ2Lm1zL2kvYy83ZjRlNDlmOGFhMzc4ZTM3L0VZalVkY2NsZEpCSWlWMklUbkNNWWtvQmtsNHA4SDV5Q1JRNDhDaEZ0aktoRGc_ZT1UNXFOY0s" height = "400"> ></a>
<a href ="https://hy.yunhaoka.com/#/pages/micro_store/index?agent_id=00fa48ad87cedd71b967e505d8255dd7"><img src="https://dlink.host/1drv/aHR0cHM6Ly8xZHJ2Lm1zL2kvYy83ZjRlNDlmOGFhMzc4ZTM3L0VTYXpzXy1SaUtwRmh3MDAzVWY3YV9nQncxZDFBNWJCblA0UEtIbWRPMXhlRGc_ZT1hMlhMQXc" height = "400"> ></a>


