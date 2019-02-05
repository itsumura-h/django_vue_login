from django.urls import include, path, re_path
from . import views

api_patterns = [
    path('login', views.login_views.Login.as_view())
]

test_patterns = [
    #文字列を返すサンプル
    path('test1', views.test_views.test1),
    #int型のURLパラメーターを取得するサンプル
    path('test2/<int:request_id>', views.test_views.test2),
    #str型のURLパラメーターを取得するサンプル
    path('test3/<str:request_word>', views.test_views.test3),
    #クエリパラメーターを取得するサンプル
    path('test4', views.test_views.test4),
    #Jsonを返すサンプル
    path('test5', views.test_views.test5),
    #Postされた内容を取得して返すサンプル
    path('test6', views.test_views.test6.as_view()),
]

urlpatterns = [
    path('api/', include(api_patterns)),
    path('test/', include(test_patterns)),

    # templates
    re_path(r'^', views.template_views.FrontendAppView.as_view()),
]