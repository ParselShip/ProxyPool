# ProxyPool


## MySQL进行存储和读取proxy（简陋自用代理池）

> 其中setting中配置自己的 mysql信息 
```Python
HOST = 添加mysql ip 
USER = 用户名
PASSWORD = 密码
DB = 操作数据库
```


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
> 安装依赖命令
> pip install -r requirements.txt

## 使用说明
> 进入到当前目录

> 启动 python q05scheduler.py 而后挂起
> python q04api.py 
