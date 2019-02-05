from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from rest_framework.views import APIView
import json

from ..models import User, LoginToken
from ..service import get_from_json_post

class Login(APIView):
    def post(self, request, format=None):
        # リクエストボディのJSONを読み込み、メールアドレス、パスワードを取得
        try:
            email = get_from_json_post(request, 'email')
            password = get_from_json_post(request, 'password')
        except:
            # JSONの読み込みに失敗
            return JsonResponse({'value': {'message': 'Post data injustice'}}, status=400)

        # メールアドレスからユーザを取得
        if not User.objects.filter(email=email).exists():
            # 存在しない場合は403を返却
            return JsonResponse({'value': {'message': 'Login failure mail.'}}, status=403)

        user = User.objects.get(email=email)

        # パスワードチェック
        if not check_password(password, user.password):
            # チェックエラー
            return JsonResponse({'value': {'message': 'Login failure password.'}}, status=403)

        # ログインOKの場合は、トークンを生成
        token = LoginToken.create(user)

        # トークンを返却
        return JsonResponse({'value': {'token': token.token}})
