from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD



urlpatterns = [
    url(r'^admin/', admin.site.urls),

#�⺻ �ּҷ� ��û�� ������ crawling_App�̶�� ���� ulrs�� ������ �߰� ����� ã�� �Ѵ�.
=======
<<<<<<< HEAD


urlpatterns = [
    url(r'^admin/', admin.site.urls),

#�⺻ �ּҷ� ��û�� ������ crawling_App�̶�� ���� ulrs�� ������ �߰� ����� ã�� �Ѵ�.
=======
# from django.urls import path, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
>>>>>>> upstream/master
    url(r'', include('crawling_App.urls')),
    ]