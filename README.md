# ProxyPool


## MySQL进行存储和读取proxy（简陋自用代理池）

> 其中setting中配置自己的 mysql信息 


## 此mysql要提前创建好数据库中的表
==命令如下==
```mysql
create table proxyPool (
    id int(10) Primary Key AUTO_INCREMENT,
    score int(10) not null default 10,
    proxy char(50) not null unique
) character set utf8;
```


## 安装依赖
> requests pymysql flask concurrent parsel faker
