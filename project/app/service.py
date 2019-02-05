import json

def get_from_json_post(request, key):
    """
    postでjsonで投げられたリクエストパラメータからkeyに一致するものを返す

    request: request
    key:     string
    """
    request_body = request.body.decode() #byte→str 変換
    params = json.loads(request_body)
    return params[key]