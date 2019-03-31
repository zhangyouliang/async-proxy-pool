#### # async-proxy-pool

使用方法
---

    # 启动 web
    ./run.sh
    # 启动爬虫
    python start_crawl.py

接口
----
- /getProxy 获取代理列表(默认显示1个)
- / 获取真实 ip
- /get 获取请求信息



参数说明:

- count 数量
- type 类型 (0 高匿，1 匿名，2 透明 3 无效代理)
- protocol 协议 (0 http,1 https)
- country 国家 
- area 区域
- updatetime 更新时间
- speed 连接速度
- score 积分(满分 10分)


参考api
---

- https://httpbin.org/get    
- http://httpbin.org/ip

参考
---
- [async-proxy-pool](https://github.com/chenjiandongx/async-proxy-pool)
