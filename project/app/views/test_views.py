from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from rest_framework.views import APIView

import json

def test1(request):
    """
    文字列を返すサンプル
    """
    responce = '<h1>test1</test1>'
    return HttpResponse(responce)

def test2(request, request_id):
    """
    int型のURLパラメーターを取得するサンプル
    /test/test2/1/→ 画面に1を表示
    /test/test2/100/ → 画面に100を表示
    """
    responce = request_id
    return HttpResponse(responce)

def test3(request, request_word):
    """
    str型のURLパラメーターを取得するサンプル
    /test/test3/aaa → 画面にaaaを表示
    """
    responce = request_word
    return HttpResponse(responce)

def test4(request):
    """
    getでのクエリパラメータを取得するサンプル
    /test/test4?q=aaa →　画面にaaaを表示
    /test/test4 →　画面に初期値のhogeを表示
    """
    q = request.GET.get(key='q', default='hoge')
    return HttpResponse(q)

def test5(request):
    """
    https://docs.djangoproject.com/en/2.1/ref/request-response/#jsonresponse-objects
    """
    message = 'Jsonを返すサンプル'
    responce = {'message': message}
    return JsonResponse(responce, safe=False)

class test6(APIView):
    """
    postされたJsonを取得して返すサンプル
    /test/test6
    {
        'value1': 'abcde',
        'value2': 12345
    }
    """
    def post(self, request, format=None):
        if request.method == "POST":
            print(request.body)
            request_body = request.body.decode() #byte→str
            params = json.loads(request_body)
            print(params)
            value1 = params['value1']
            value2 = params['value2']

            response = {
                'value': {
                    'key1': value1,
                    'key2': value2
                }
            }
            return JsonResponse(response, safe=False)
        else:
            HttpResponseNotFound('<h1>POST以外無効</h1>')
