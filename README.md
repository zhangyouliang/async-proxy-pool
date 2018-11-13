#### # 代理池子



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