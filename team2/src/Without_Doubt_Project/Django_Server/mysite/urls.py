from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),

#�⺻ �ּҷ� ��û�� ������ crawling_App�̶�� ���� ulrs�� ������ �߰� ����� ã�� �Ѵ�.
    url(r'', include('crawling_App.urls')),
    ]