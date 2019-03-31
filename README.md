#### # async-proxy-pool

使用方法
---

    # 启动 web
    ./run.sh
    # 启动爬虫
    python start_crawl.py

接口
----
- / 获取真实 ip
- /get/<count:int> 返回指定数量的代理，权值从大到小排序。
- /pop 随机返回一个代理，分三次尝试。
1. 尝试返回权值为 MAX_SCORE，也就是最新可用的代理。
2. 尝试返回随机权值在 (MAX_SCORE -3) - MAX_SCORE 之间的代理。
3. 尝试返回权值在 0 - MAX_SCORE 之间的代理
- /count 返回代理池中所有代理总数
- /count/<score:int> 返回指定权值代理总数
- /clear/<score:int> 删除权值小于等于 score 的代理



参考api
---

- https://httpbin.org/get    
- http://httpbin.org/ip

参考
---
- [async-proxy-pool](https://github.com/chenjiandongx/async-proxy-pool)
