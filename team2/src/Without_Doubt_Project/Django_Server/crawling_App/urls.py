#url ����� ����ϱ� ���� conf.urls ���̺귯������ url�� �ҷ��´�.
from django.conf.urls import url
from . import views

urlpatterns = [
#�⺻�ּ� 127.0.0.1:8000/ ���� url ��û�� ���� ��쿡 views.py ������ input �Լ��� ����Ѵ�.
    url(r'^$', views.input),				
#127.0.0.1:8000/realtime.html/ ���� url ��û�� ���� ��쿡 views.py ������ index �Լ��� ����Ѵ�.
    url(r'^realtime.html$', views.index),
#127.0.0.1:8000/realtime_google.html/ ���� url ��û�� ���� ��쿡 views.py ������ index2 �Լ��� ����Ѵ�.
    url(r'^realtime_google.html$', views.index2),
#127.0.0.1:8000/realtime_Top20.html/ ���� url ��û�� ���� ��쿡 views.py ������ top �Լ��� ����Ѵ�.
    url(r'^realtime_Top20.html$', views.top),
#127.0.0.1:8000/realtime_Top20_google.html/ ���� url ��û�� ���� ��쿡 views.py ������ top2 �Լ��� ����Ѵ�.
    url(r'^realtime_Top20_google.html$', views.top2),
]