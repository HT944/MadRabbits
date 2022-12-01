import sys
import time

import requests


def cron(bean, expiration):
    time.sleep(10)
    url = "http://127.0.0.1:1234/cron"
    data = {
        "BeanCron": bean,
        "ExpirationCron": expiration
    }
    headers = {
        "content-type": "application/json"
    }
    res = requests.post(url, headers=headers, json=data)


if __name__ == '__main__':
    args = sys.argv
    cron(args[1], args[2])
