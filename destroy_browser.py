import sys
import time

import requests


def destroy_page(phone, mins: int):
    print(f"{60 * mins}s后回收{phone}的浏览器")
    time.sleep(60*mins)
    url = "http://127.0.0.1:1234/api/DestroyPage"
    data = {
        "phone": int(phone)
    }
    headers = {
        "content-type": "application/json"
    }
    res = requests.post(url, headers=headers,  json=data)
    print(res.text)


if __name__ == '__main__':
    args = sys.argv
    destroy_page(args[1], int(args[2]))
