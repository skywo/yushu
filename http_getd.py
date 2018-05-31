import requests

#获取文件报文，并且判断是否返回json格式
#添加未找到数据时的响应
class HTTP:
    def get(self,url,return_json=True):
        r=requests.get(url)
        if r.status_code==200:
            if return_json:
                return r.json()
            else:
                return r.text
        else:
            if return_json:
                return {}
            else:
                return ""
