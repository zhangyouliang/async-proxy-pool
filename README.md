#### # 代理池子

    ## 获取代理列表
    http://127.0.0.1:8000/?types=2&count=5
    
- count 数量
- type 类型 (0 高匿，1 匿名，2 透明 3 无效代理)
- protocol 协议 (0 http,1 https)
- country 国家 
- area 区域
- updatetime 更新时间
- speed 连接速度
- score 积分(满分 10分)


        https://httpbin.org/get
        
        {
        "args": {}, 
        "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8", 
            "Cache-Control": "max-age=0", 
            "Connection": "close", 
            "Host": "httpbin.org", 
            "Upgrade-Insecure-Requests": "1", 
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
        }, 
        "origin": "112.65.147.114", 
        "url": "https://httpbin.org/get"
        }


        http://httpbin.org/get
        {
        "args": {}, 
        "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
            "Accept-Encoding": "gzip, deflate", 
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8", 
            "Cache-Control": "max-age=0", 
            "Connection": "close", 
            "Host": "httpbin.org", 
            "Upgrade-Insecure-Requests": "1", 
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
        }, 
        "origin": "112.65.147.114", 
        "url": "http://httpbin.org/get"
        }
        
        
        http://httpbin.org/ip
        {
            origin: "112.65.147.114"
        }

接口
----

    # 默认显示1个
    http://127.0.0.1:8000/
    [["61.142.72.150", 33270, 10], ["1.198.73.168", 9999, 10]]