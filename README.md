# Suda-WiFi-Helper

苏州大学校园网自动登录解决方案

每次连接 WiFi 时均会向 `http://10.9.1.3:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C0%2C{ACCOUNT}%40{OPERATOR}&user_password={PASSWORD}&wlan_user_ip={IPV4}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.3&v=1480` 发送请求以实现自动登录

## 使用

```
pip install -r requirements.txt
```

修改 `app.py` 9~11 行的 `account` `password` `operator` 为登录信息

运行 `launch.cmd`，可通过托盘区域图标退出

可将 `path\to\launch.cmd` 或 `path\to\pythonw.exe path\to\app.py` 加到系统启动项中
