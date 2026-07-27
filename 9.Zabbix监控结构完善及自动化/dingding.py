#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import sys
import datetime

# 替换为你的钉钉Webhook
WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=077b85e688773c61eee322fd23050b1f58d50c02930ede18b8843cc85c722410"

def send_ding_msg(title, content):
    headers = {"Content-Type": "application/json;charset=utf-8"}
    msg_data = {
        "msgtype": "text",
        "text": {
            "content": f"【Zabbix监控告警】{title}\n{content}"
        },
        "at": {
            "isAtAll": True
        }
    }
    res = requests.post(url=WEBHOOK, data=json.dumps(msg_data), headers=headers)
    log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_text = f"\n{log_time} 发送结果：{res.json()}\n标题：{title}\n内容：{content}\n"
    with open("/var/log/zabbix/dingding.log", "a+", encoding="utf-8") as f:
        f.write(log_text)

if __name__ == "__main__":
    sendto = sys.argv[1]
    alert_title = sys.argv[2]
    alert_content = sys.argv[3]
    send_ding_msg(alert_title, alert_content)
