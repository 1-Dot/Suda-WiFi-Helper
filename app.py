import sys

import requests
import wmi
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMenu, QSystemTrayIcon

account = '0123456789'
password = 'password123456'
operator = 'cucc'  # 移动：zgyd；电信：ctc；联通：cucc


def monitor_wifi_event():
    global account, password, operator
    c = wmi.WMI()
    watcher = c.Win32_NetworkAdapterConfiguration.watch_for(
        notification_type="Modification",
        delay_secs=1,
    )
    status = None
    while True:
        event = watcher()
        if 'Wi-Fi' in event.Description:
            if event.IPEnabled == status:
                continue
            status = event.IPEnabled
            if event.IPEnabled:
                # print("WiFi 已连接，尝试登录校园网")
                ipv4 = event.IPAddress[0]
                requests.get(
                    'http://10.9.1.3:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C0%2C'
                    + account
                    + '%40'
                    + operator
                    + '&user_password='
                    + password
                    + '&wlan_user_ip='
                    + ipv4
                    + '&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.3&v=1480'
                )
            # else:
            # print("WiFi 已断开")


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon("icon.png"))
        self.setToolTip("1Sufi")

        menu = QMenu(parent)
        name_action = menu.addAction("1Sufi")
        name_action.setEnabled(False)
        menu.addSeparator()
        exit_action = menu.addAction("退出")
        exit_action.setIcon(QIcon("exit.png"))
        exit_action.triggered.connect(QCoreApplication.quit)
        self.setContextMenu(menu)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tray_icon = TrayIcon()
    tray_icon.show()

    import threading

    wifi_thread = threading.Thread(target=monitor_wifi_event, daemon=True)
    wifi_thread.start()

    sys.exit(app.exec())
