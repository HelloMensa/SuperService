# SuperService
各种无厘头的小功能




TODO LIST: 


1. linux自启动配置

启动命令行包括如下：
-----------------------------------
spawn-fcgi -d /root/ssweb -f /root/ssweb/code.py -a 127.0.0.1 -p 9002
nginx
ssserver -c /etc/shadowsocks.json -d start --user ssuser
-----------------------------------
可参考：http://www.centoscn.com/CentOS/2015/0318/4911.html

nginx及spawn-fcgi配置当前进程运行用户 【降权】

2. python sqlite 访问类库
3. python 文件系统访问API

4. vps上自动获取git最新代码部署，类持续集成

