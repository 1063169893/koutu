# -*- coding: UTF-8 -*-
from flask import Flask, request
from flask_cors import CORS
import json

import urllib
import urllib.request
import urllib.parse
# import urllib2
import sys
import ssl

app = Flask(__name__)
CORS(app, supports_credentials=True)
# 只接受POST方法访问

host = 'https://perdc.market.alicloudapi.com'
path = '/bodyseg'
method = 'POST'
appcode = '4ddb8ca5787e4615bb7051039eff8b4c'
querys = ''
bodys = {}
url = host + path

@app.route("/test_1.0", methods=["POST"])
def check():
    # 默认返回内容
    return_dict = {"return_code": "200",
                   "return_info": "处理成功", "result": False}
    # 判断传入的json数据是否为空
    if request.get_data() is None:
        return_dict["return_code"] = "5004"
        return_dict["return_info"] = "请求参数为空"
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的参数
    get_Data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)
    src = get_Data.get("src")
    typename = get_Data.get("type")
    # 对参数进行操作
    return_dict["result"] = tt(src, typename)
    print('return_dictreturn_dict', return_dict)
    bsreg = json.dumps(return_dict["result"], ensure_ascii=False)
    
    return json.loads(bsreg)

# 功能函数


def tt(src, typename):
    bodys['src'] = src
    bodys['type'] = typename
    post_data = urllib.parse.urlencode(bodys).encode("utf-8")
    # print('post_data', post_data)
    request = urllib.request.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    request.add_header(
        'Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    # ctx = ssl.create_default_context()
    # ctx.check_hostname = False
    # ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request)
    content = response.read()
    if (content):
      print(content.decode('UTF-8'))
      return content.decode('UTF-8')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5870)
