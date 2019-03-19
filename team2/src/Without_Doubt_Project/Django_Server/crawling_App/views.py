#-------------------------------------ICON_SCORE-------------------------------------------
import json, time, datetime
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.icon_service import IconService
from iconsdk.builder.call_builder import CallBuilder

<<<<<<< HEAD
#-------------------------------------Server-------------------------------------------
# �����ͺ��̽� ���̺� �� �߰�
from .models import Receive_Google_Data, Receive_Naver_Data, Missing_Data
#Ŭ���̾�Ʈ�� ��û�� ������� �����ֱ� ���� render ���̺귯�� �߰�
from django.shortcuts import render
#���������� ���� �޼����� ������ֱ� ���� HttpResponse ���̺귯�� �߰�
from django.http import HttpResponse
#Local Ÿ������ UTC Ÿ�������� ��ȯ�ϱ� ���� ���̺귯�� �߰�
from datetime import timedelta

#-------------------------------------ICON_SCORE_option-------------------------------------------
_score_address = "cxb7ef03fea5fa9b2fe1f00f548d6da7ff2ddfebd5"
_keystore_address = "hx226e6e4340136836b36977bd76ca83746b8b071c"
node_uri = "https://ctz.solidwallet.io/api/v3"
=======

#-------------------------------------Server-------------------------------------------
from .models import Receive_Google_Data, Receive_Naver_Data
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max
#from django_pandas.io import read_frame
#from django_pandas.managers import DataFrameManager
#from IPython.display import display


#-------------------------------------ICON_SCORE_option-------------------------------------------
_score_address = "cxd8477e0e67273112e64ed81ab5b578bb4f997da6"
_keystore_address = "hx055ca4808e82f7c0e4eafa884cefcfec15e8387b"
node_uri = "http://localhost:9000/api/v3"
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
icon_service = IconService(HTTPProvider(node_uri))


#-------------------------------------Naver RT-------------------------------------------
<<<<<<< HEAD
#���̹� �ǽð� �˻��� ��� ����

#index��� �޼ҵ带 ����
def index(request):

#realtime.html���� get����� ���� �Էµ� ���� �ҷ����� �κ�
    userdate = request.GET.get("userdate")
    usertime = request.GET.get("usertime")


#������ �����͸� ���ھ� �Ķ���Ϳ� �´� ���·� �����ϴ� �۾�
#��¥�� �ð� ������ �Է��� �ִ°��
    if userdate and usertime :
#��¥ ������ XXXX-XX-XX���¸� XXXXXXXX������ ����
        split_Date = userdate.split('-')
        split_Time = usertime.split(':') 
#�ð� ������ XX:XX���¸� XXXX������ ����
        input_Date = "".join(split_Date)
        input_Time = "".join(split_Time)

#5�д����� �˻��Ҽ� �ְ� �ϱ����ؼ� 5�� ���� �������� 0�� �ƴѶ� ���� �޼��� ���
        if int(input_Time) % 5 != 0:
            error = 2
#urls.py�� ���� ���� ������� ��û�� realtime.html���ø��� ������ �˸��� error �Ķ���͸� ������.
            return render(request, 'crawling/realtime.html', {'error' : error})

#2019-02-00~2020-02-00���� ��¥ ������ �����ش�. 
#�Ʒ� ��¥�� �����Ͽ� ���ϴ� ������ �������� �� �ִ�.
        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:

#���� Ÿ������ utcŸ�������� �����ϴ� �κ�
#���� ��¥�� �ð��� ���� datatime�������� ����� 9�ð���ŭ �� �ð��� ���Ѵ�.
            now = userdate + " " + usertime + ":00"
            now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')  
            now = now - timedelta(hours=9)

#������ �ð��뿡�� ��¥�� �ð��� �����Ѵ�.
            nowDate = now.strftime('%Y%m%d')
            nowTime = now.strftime('%H%M')
          
            params = {
                "_Call_date": nowDate,
                "_Call_time": nowTime,
=======

def index(request):
    userdate = request.GET.get("userdate")
    usertime = request.GET.get("usertime")

    if userdate and usertime :
        split_Date = userdate.split('-')
        split_Time = usertime.split(':')
        input_Date = "".join(split_Date)
        input_Time = "".join(split_Time)

        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:

            params = {
                "_Call_date": "".join(input_Date),
                "_Call_time": "".join(input_Time),
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
                "_Call_div": "NAVER"
            }

            Inquiry = CallBuilder() \
                .from_(_keystore_address) \
                .to(_score_address) \
                .method("inquiry_RT") \
                .params(params) \
                .build()
<<<<<<< HEAD
            response = icon_service.call(Inquiry)

#���� �����Ͱ� ���ھ �������� �ʴ� ���
            if response == "":
                
                error = 1
#urls.py�� ���� ���� ������� ��û�� realtime.html���ø��� ������ �˸��� error �Ķ���͸� ������.
                return render(request, 'crawling/realtime.html', {'error' : error})
#���� �����Ͱ� ���ھ �����ϴ� ���
            else:
#������ �����͸� posts��� ������ ��´�.
                posts = json.loads(response)
#Missing_Data ���̺��� �������� ������ missing�̶�� ������ ��´�.
                missing = Missing_Data.objects.filter(key1=input_Date ,Type="N")
#urls.py�� ���� ���� ������� ��û�� realtime.html���ø��� �ǽð� �˻� ������ ��� posts ������ ��¥ ���� ��� date, �ð� ���� ��� time ����, �������� ��� missing������ �Բ� �����ش�.
                return render(request, 'crawling/realtime.html', {'posts': posts, 'date': userdate, 'time': usertime, 'missing':missing})

#���� 2019-02-00~2020-02-00�� ������ �ʰ��Ͽ��� ���
        else: 
            error = 2
#urls.py�� ���� ���� ������� ��û�� realtime.html���ø��� ������ �˸��� error �Ķ���͸� ������.
            return render(request, 'crawling/realtime.html', {'error' : error})

#��¥�� �ð� ������ �Է��� ���� ���
    elif userdate == None or usertime == None:
#utcŸ���� �ð��� ���� Ÿ���� �ð��� ���Ѵ�.
        now = datetime.datetime.utcnow()
        nowDate = now.strftime('%Y%m%d')
        nowTime = now.strftime('%H%M')

        localnow = datetime.datetime.now()
        localnowDate = localnow.strftime('%Y%m%d')
        localnowTime = localnow.strftime('%H%M')


#����ð��� 5�� ����� ����� �ش�.
#����ð��� 5�� ����� ���� �����Ͱ� ������Ʈ ���� ���� ��츦 ������ ����ð� 5������ �����͸� ���Ѵ�.
#����ð��� 5�� ����� �ƴ� ��� 5�� ���� ������ ��ŭ ���ش�.

        if int(nowTime) % 100 == 0 :
            realTime = int(nowTime) - 45
        elif int(nowTime) % 5 == 0 :
            realTime = int(nowTime) - 5
        elif int(nowTime) % 5 == 1 :
            realTime = int(nowTime) - 1
        elif int(nowTime) % 5 == 2 :
            realTime = int(nowTime) - 2
        elif int(nowTime) % 5 == 3 :
            realTime = int(nowTime) - 3
        elif int(nowTime) % 5 == 4 :
            realTime = int(nowTime) - 4

# *** UTC�ð� 0000���̸� -5�� ����Ǿ����
#���� ���� ũ�Ѹ� ������忡 ���� 26�п� ���� �������� ��� ���̺��� �ϳ��� ����� ����ó�� �� �� �ִ�.
         

#00��09�� ������ ��쿡�� ���������� ġȯ�� ��� ���ڸ��� ����Ǿ������ ������ 000�� �߰��Ѵ�.
        if realTime <= 9:
            realTime = "000" + str(realTime)
#09��59�� ������ ��쿡�� ���������� ġȯ�� ��� 800���� ����Ǿ������ ������ 00�� �߰��Ѵ�.
        elif realTime <= 59 and realTime >= 10:
            realTime = "00" + str(realTime)
#09��59�� ������ ��쿡�� ���������� ġȯ�� ��� ���ڸ��� ����Ǿ������ ������ 0�� �߰��Ѵ�.
        elif realTime <= 959 and realTime >= 60:
            realTime = "0" + str(realTime)

        params = {
            "_Call_date": nowDate,
            "_Call_time": realTime,
            "_Call_div": "NAVER"

#�׽�Ʈ�� ��¥, �ð��� (�����Ͱ� ����ִ�.)
            #"_Call_date": "20190308",
            #"_Call_time": "0723",
=======

            response = icon_service.call(Inquiry)
            posts = json.loads(response)
            return render(request, 'crawling/realtime.html', {'posts': posts})
        else:
            posts = str(Receive_Naver_Data.objects.last())
            # return render(request, 'crawling/realtime, {'posts' : posts})
            return HttpResponse("No data aaa" + userdate)


    elif userdate == None or usertime == None:
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y%m%d')
        nowTime = now.strftime('%H%M')
        # return HttpResponse("No data aaa" + nowDate + nowTime)
        realTime = int(nowTime) - 1
        shit = str(realTime)
        params = {
            "_Call_date": nowDate,
            "_Call_time": shit,
            "_Call_div": "NAVER"
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
        }

        Inquiry = CallBuilder() \
            .from_(_keystore_address) \
            .to(_score_address) \
            .method("inquiry_RT") \
            .params(params) \
            .build()

        response = icon_service.call(Inquiry)
<<<<<<< HEAD

#����ð��� 5�� ����� ����� �ش�.
#����ð��� 5�� ����� ���� �����Ͱ� ������Ʈ ���� ���� ��츦 ������ ����ð� 5������ �����͸� ���Ѵ�.
#����ð��� 5�� ����� �ƴ� ��� 5�� ���� ������ ��ŭ ���ش�.

        if int(localnowTime) % 100 == 0 :
            realTime = int(nowTime) - 45
        elif int(localnowTime) % 5 == 0 :
            localrealTime = int(localnowTime) - 5
        elif int(localnowTime) % 5 == 1 :
            localrealTime = int(localnowTime) - 1
        elif int(localnowTime) % 5 == 2 :
            localrealTime = int(localnowTime) - 2
        elif int(localnowTime) % 5 == 3 :
            localrealTime = int(localnowTime) - 3
        elif int(localnowTime) % 5 == 4 :
            localrealTime = int(localnowTime) - 4

#���� ���� ũ�Ѹ� ������忡 ���� 26�п� ���� �������� ��� ���̺��� �ϳ��� ����� ����ó�� �� �� �ִ�.
         

#00��09�� ������ ��쿡�� ���������� ġȯ�� ��� ���ڸ��� ����Ǿ������ ������ 000�� �߰��Ѵ�.
        if localrealTime <= 9:
            localrealTime = "000" + str(localrealTime)
#09��59�� ������ ��쿡�� ���������� ġȯ�� ��� 800���� ����Ǿ������ ������ 00�� �߰��Ѵ�.
        elif localrealTime <= 59 and localrealTime >= 10:
            localrealTime = "00" + str(localrealTime)
#09��59�� ������ ��쿡�� ���������� ġȯ�� ��� ���ڸ��� ����Ǿ������ ������ 0�� �߰��Ѵ�.
        elif localrealTime <= 959 and localrealTime >= 60:
            localrealTime = "0" + str(localrealTime)

#UTC�ð����� 15:00�� ������ ��¥���� �Ϸ縦 �߰��Ѵ�.            
#        if realTime >= 1500:
#           nowDate = int(nowDate) + 1
#UTCŸ������ asia/seoulŸ�������� �����ϱ� ���� 9�ð��� �߰����ش�.
#        realTime = (int(realTime) + 900) % 2400
#00��09�� ������ ��쿡�� ���������� ġȯ�� ��� ���ڸ��� ����Ǿ������ ������ 000�� �߰��Ѵ�.
#        if realTime <= 9:
#            realTime = "000" + str(realTime)
#09��59�� ������ ��쿡�� ���������� ġȯ�� ��� 800���� ����Ǿ������ ������ 00�� �߰��Ѵ�.
#        elif realTime <= 59 and realTime >= 10:
#            realTime = "00" + str(realTime)
#09��59�� ������ ��쿡�� ���������� ġȯ�� ��� ���ڸ��� ����Ǿ������ ������ 0�� �߰��Ѵ�.
#        elif realTime <= 959 and realTime >= 60:
#            realTime = "0" + str(realTime)


#���� ���ھ��� �ֱٽð��� ���� �������� ���� ���
        if response == "":
#��ȭ�鿡 �˻��� ��¥,�ð��� �Բ� �ֱ� ���� �������� �ʴٴ� �޼����� ������ش�.
            return HttpResponse("Recent Data (" + str(localnowDate) + " " + str(localrealTime) + ") is Empty")

        posts = json.loads(response)

#datetime�Լ��� ������ ��¥�� �ð������� ���������� ����� �ֱ����� �˸´� ������ ������ �����Ѵ�.
#XXXX XX XX�� ù��° �ڸ� ���� �׹�° �ڸ��� temp1������ ��´�.
        temp1 = str(localnowDate)[0:4]
#XXXX XX XX�� �ټ���° �ڸ� ���� ������° �ڸ��� temp2������ ��´�.
        temp2 = str(localnowDate)[4:6]
#XXXX XX XX�� �ϰ���°�ڸ� ���� ������° �ڸ��� temp3������ ��´�.
        temp3 = str(localnowDate)[6:8]
#�� ������ ������ ������ XXXX-XX-XX���·� �����
        convert_date = temp1 + "-" + temp2 + "-" + temp3

#XXXX�� ù��° �ڸ����� �ι�° �ڸ��� temp1������ ��´�
        temp1 = str(localrealTime)[0:2]
#XXXX�� ����° �ڸ����� �׹�° �ڸ��� temp2������ ��´�
        temp2 = str(localrealTime)[2:4]
#�� �ΰ��� ������ ������ XX:XX���·� �����.
        convert_time = temp1 + ":" + temp2

        missing = Missing_Data.objects.filter(key1=localnowDate,Type="N")

#urls.py�� ���� ���� ������� ��û�� realtime.html���ø��� �ǽð� �˻� ������ ��� posts ������ �˸��� ���·� ���� ��¥, �ð� ����, ������ ������ �Բ� �����ش�.
        return render(request, 'crawling/realtime.html', {'posts' : posts, 'date': convert_date,'time':convert_time,'missing':missing})


#-------------------------------------Google RT-------------------------------------------
#���� �ǽð� �˻��� ��� ����

#index2��� �޼ҵ带 ����
def index2(request):

#realtime_google.html���� get����� ���� �Էµ� ���� �ҷ����� �κ�
    userdate = request.GET.get("userdate")
    usertime = request.GET.get("usertime")

#������ �����͸� ���ھ� �Ķ���Ϳ� �´� ���·� �����ϴ� �۾�
#��¥�� �ð� ������ �Է��� �ִ°��
    if userdate and usertime :
#��¥ ������ XXXX-XX-XX���¸� XXXXXXXX������ ����
        split_Date = userdate.split('-')
        split_Time = usertime.split(':')
#�ð� ������ XX:XX���¸� XXXX������ ����
        input_Date = "".join(split_Date)
        input_Time = "".join(split_Time)

#5�д����� �˻��Ҽ� �ְ� �ϱ����ؼ� 5�� ���� �������� 0�� �ƴѶ� ���� �޼��� ���
        if int(input_Time) % 5 != 0:
            error = 2
#urls.py�� ���� ���� ������� ��û�� realtime_google.html���ø��� ������ �˸��� error �Ķ���͸� ������.
            return render(request, 'crawling/realtime_google.html', {'error' : error})

#2019-02-00~2020-02-00���� ��¥ ������ �����ش�. 
#�Ʒ� ��¥�� �����Ͽ� ���ϴ� ������ �������� �� �ִ�.
        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:
            
#���� Ÿ������ utcŸ�������� �����ϴ� �κ�
#���� ��¥�� �ð��� ���� datatime�������� ����� 9�ð���ŭ �� �ð��� ���Ѵ�.
            now = userdate + " " + usertime + ":00"
            now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')  
            now = now - timedelta(hours=9)

#������ �ð��뿡�� ��¥�� �ð��� �����Ѵ�.
            nowDate = now.strftime('%Y%m%d')
            nowTime = now.strftime('%H%M')

            params = {
                "_Call_date": nowDate,
                "_Call_time": nowTime,
=======
        posts = json.loads(response)
        # userdate = Receive_Naver_Data.objects.last().date - recent DB data call
        # posts = list(Post.objects.filter(date=userdate))
        return render(request, 'crawling/realtime.html', {'posts': posts})


#-------------------------------------Google RT-------------------------------------------

def index2(request):
    userdate = request.GET.get("userdate")
    usertime = request.GET.get("usertime")

    if userdate and usertime :
        split_Date = userdate.split('-')
        split_Time = usertime.split(':')
        input_Date = "".join(split_Date)
        input_Time = "".join(split_Time)

        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:

            params = {
                "_Call_date": "".join(input_Date),
                "_Call_time": "".join(input_Time),
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
                "_Call_div": "GOOGLE"
            }

            Inquiry = CallBuilder() \
                .from_(_keystore_address) \
                .to(_score_address) \
                .method("inquiry_RT") \
                .params(params) \
                .build()
<<<<<<< HEAD
            response = icon_service.call(Inquiry)

#���� �����Ͱ� ���ھ �������� �ʴ� ���
            if response == "":
                error = 1
#urls.py�� ���� ���� ������� ��û�� realtime_google.html���ø��� ������ �˸��� error �Ķ���͸� ������.
                return render(request, 'crawling/realtime_google.html', {'error' : error})
#���� �����Ͱ� ���ھ �����ϴ� ���
            else:
#������ �����͸� posts��� ������ ��´�.
                posts = json.loads(response)
#Missing_Data ���̺��� �������� ������ missing�̶�� ������ ��´�.
                missing = Missing_Data.objects.filter(key1=input_Date ,Type="N")
#urls.py�� ���� ���� ������� ��û�� realtime_google.html���ø��� �ǽð� �˻� ������ ��� posts ������ ��¥ ���� ��� date, �ð� ���� ��� time ����, �������� ��� missing������ �Բ� �����ش�.
                return render(request, 'crawling/realtime_google.html', {'posts': posts, 'date': userdate, 'time': usertime,'missing':missing})

#���� 2019-02-00~2020-02-00�� ������ �ʰ��Ͽ��� ���
        else: 
            error = 2
#urls.py�� ���� ���� ������� ��û�� realtime_google.html���ø��� ������ �˸��� error �Ķ���͸� ������.
            return render(request, 'crawling/realtime_google.html', {'error' : error})

#��¥�� �ð� ������ �Է��� ���� ���
    elif userdate == None or usertime == None:
#utcŸ���� �ð��� ���� Ÿ���� �ð��� ���Ѵ�.
        now = datetime.datetime.utcnow()
        nowDate = now.strftime('%Y%m%d')
        nowTime = now.strftime('%H%M')

        localnow = datetime.datetime.now()
        localnowDate = localnow.strftime('%Y%m%d')
        localnowTime = localnow.strftime('%H%M')

#����ð��� 5�� ����� ����� �ش�.
#����ð��� 5�� ����� ���� �����Ͱ� ������Ʈ ���� ���� ��츦 ������ ����ð� 5������ �����͸� ���Ѵ�.
#����ð��� 5�� ����� �ƴ� ��� 5�� ���� ������ ��ŭ ���ش�.

        if int(nowTime) % 100 == 0 :
            realTime = int(nowTime) - 45        
        elif int(nowTime) % 5 == 0 :
            realTime = int(nowTime) - 5
        elif int(nowTime) % 5 == 1 :
            realTime = int(nowTime) - 1
        elif int(nowTime) % 5 == 2 :
            realTime = int(nowTime) - 2
        elif int(nowTime) % 5 == 3 :
            realTime = int(nowTime) - 3
        elif int(nowTime) % 5 == 4 :
            realTime = int(nowTime) - 4

#00��09�� ������ ��쿡�� ���������� ġȯ�� ��� ���ڸ��� ����Ǿ������ ������ 000�� �߰��Ѵ�.
        if realTime <= 9:
            realTime = "000" + str(realTime)
#09��59�� ������ ��쿡�� ���������� ġȯ�� ��� 800���� ����Ǿ������ ������ 00�� �߰��Ѵ�.
        elif realTime <= 59 and realTime >= 10:
            realTime = "00" + str(realTime)
#09��59�� ������ ��쿡�� ���������� ġȯ�� ��� ���ڸ��� ����Ǿ������ ������ 0�� �߰��Ѵ�.
        elif realTime <= 959 and realTime >= 60:
            realTime = "0" + str(realTime)

        params = {
            "_Call_date": nowDate,
            "_Call_time": realTime,
            "_Call_div": "GOOGLE"

#�׽�Ʈ�� ��¥, �ð��� (�����Ͱ� ����ִ�.)
            #"_Call_date": "20190227",
            #"_Call_time": "0853",
=======

            response = icon_service.call(Inquiry)
            posts = json.loads(response)
            return render(request, 'crawling/realtime_google.html', {'posts': posts})
        else:
            posts = str(Receive_Google_Data.objects.last())
            # return render(request, 'crawling/realtime, {'posts' : posts})
            return HttpResponse("No data aaa" + userdate)


    elif userdate == None or usertime == None:
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y%m%d')
        nowTime = now.strftime('%H%M')
        # return HttpResponse("No data aaa" + nowDate + nowTime)
        realTime = int(nowTime) - 1
        shit = str(realTime)
        params = {
            "_Call_date": nowDate,
            "_Call_time": shit,
            "_Call_div": "GOOGLE"
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
        }

        Inquiry = CallBuilder() \
            .from_(_keystore_address) \
            .to(_score_address) \
            .method("inquiry_RT") \
            .params(params) \
            .build()

        response = icon_service.call(Inquiry)
<<<<<<< HEAD

#����ð��� 5�� ����� ����� �ش�.
#����ð��� 5�� ����� ���� �����Ͱ� ������Ʈ ���� ���� ��츦 ������ ����ð� 5������ �����͸� ���Ѵ�.
#����ð��� 5�� ����� �ƴ� ��� 5�� ���� ������ ��ŭ ���ش�.
        if int(localnowTime) % 100 == 0 :
            realTime = int(nowTime) - 45    
        elif int(localnowTime) % 5 == 0 :
            localrealTime = int(localnowTime) - 5
        elif int(localnowTime) % 5 == 1 :
            localrealTime = int(localnowTime) - 1
        elif int(localnowTime) % 5 == 2 :
            localrealTime = int(localnowTime) - 2
        elif int(localnowTime) % 5 == 3 :
            localrealTime = int(localnowTime) - 3
        elif int(localnowTime) % 5 == 4 :
            localrealTime = int(localnowTime) - 4

#���� ���� ũ�Ѹ� ������忡 ���� 26�п� ���� �������� ��� ���̺��� �ϳ��� ����� ����ó�� �� �� �ִ�.
         
#00��09�� ������ ��쿡�� ���������� ġȯ�� ��� ���ڸ��� ����Ǿ������ ������ 000�� �߰��Ѵ�.
        if localrealTime <= 9:
            localrealTime = "000" + str(localrealTime)
#09��59�� ������ ��쿡�� ���������� ġȯ�� ��� 800���� ����Ǿ������ ������ 00�� �߰��Ѵ�.
        elif localrealTime <= 59 and localrealTime >= 10:
            localrealTime = "00" + str(localrealTime)
#09��59�� ������ ��쿡�� ���������� ġȯ�� ��� ���ڸ��� ����Ǿ������ ������ 0�� �߰��Ѵ�.
        elif localrealTime <= 959 and localrealTime >= 60:
            localrealTime = "0" + str(localrealTime)


#���� ���ھ��� �ֱٽð��� ���� �������� ���� ���
        if response == "":
#��ȭ�鿡 �˻��� ��¥,�ð��� �Բ� �ֱ� ���� �������� �ʴٴ� �޼����� ������ش�.
            return HttpResponse("Recent Data (" + str(nowDate) + " " + str(realTime) + ") is Empty")

        posts = json.loads(response)

#datetime�Լ��� ������ ��¥�� �ð������� ���������� ����� �ֱ����� �˸´� ������ ������ �����Ѵ�.
#XXXX XX XX�� ù��° �ڸ� ���� �׹�° �ڸ��� temp1������ ��´�.
        temp1 = str(localnowDate)[0:4]
#XXXX XX XX�� �ټ���° �ڸ� ���� ������° �ڸ��� temp2������ ��´�.
        temp2 = str(localnowDate)[4:6]
#XXXX XX XX�� �ϰ���°�ڸ� ���� ������° �ڸ��� temp3������ ��´�.
        temp3 = str(localnowDate)[6:8]
#�� ������ ������ ������ XXXX-XX-XX���·� �����
        convert_date = temp1 + "-" + temp2 + "-" + temp3

#XXXX�� ù��° �ڸ����� �ι�° �ڸ��� temp1������ ��´�
        temp1 = str(localrealTime)[0:2]
#XXXX�� ����° �ڸ����� �׹�° �ڸ��� temp2������ ��´�
        temp2 = str(localrealTime)[2:4]
#�� �ΰ��� ������ ������ XX:XX���·� �����.
        convert_time = temp1 + ":" + temp2

        missing = Missing_Data.objects.filter(key1=localnowDate,Type="G")

#urls.py�� ���� ���� ������� ��û�� realtime_google.html���ø��� �ǽð� �˻� ������ ��� posts ������ �˸��� ���·� ���� ��¥, �ð� ����, ������ ������ �Բ� �����ش�.
        return render(request, 'crawling/realtime_google.html', {'posts' : posts, 'date': convert_date,'time':convert_time,'missing':missing})


#-------------------------------------Naver Top20-------------------------------------------
#���̹� ���� TOP20 ��� ����

#top �̶�� �޼ҵ� ����
def top(request):

#realtime_Top20.html���� get����� ���� �Էµ� ���� �ҷ����� �κ�
    userdate = request.GET.get("userdate")

#������ �����͸� ���ھ� �Ķ���Ϳ� �´� ���·� �����ϴ� �۾�
#������ �Է��� �ִ°��
    if userdate:
#��¥ ������ XXXX-XX-XX���¸� XXXXXXXX������ ����
        split_Date = userdate.split('-')
        input_Date = "".join(split_Date)

#2019-02-00~2020-02-00���� ��¥ ������ �����ش�. 
#�Ʒ� ��¥�� �����Ͽ� ���ϴ� ������ �������� �� �ִ�.
        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:

#Receive_Naver_Data��� ���̺��� key1�÷��� input_Date������ ��ġ�ϴ� ���� N_Rating������ �����Ͽ� temp_posts������ ��´�.
            temp_posts = list(Receive_Naver_Data.objects.filter(key1=input_Date).order_by('-N_Rating'))
#������ �����͸� 20���� �����Ѵ�.
            posts = temp_posts[0:20]
#���� �����Ͱ� �������� ���� ���
            if len(posts) <= 1 :
                error = 1
#urls.py�� ���� ���� ������� ��û�� realtime_Top20.html���ø��� ������ �˸��� error �Ķ���͸� ������.
                return render(request, 'crawling/realtime_Top20.html', {'error' : error})
#���� �����Ͱ� �����ϴ� ���
            else :
#urls.py�� ���� ���� ������� ��û�� realtime_Top20.html���ø��� �ǽð� �˻� ������ ��� posts ������ ��¥ ���� ��� userdate ������ �Բ� �����ش�.
                return render(request, 'crawling/realtime_Top20.html', {'posts': posts, 'date': userdate})

#���� 2019-02-00~2020-02-00�ǹ����� �ʰ��Ͽ��� ���
        else:
            error = 2
#urls.py�� ���� ���� ������� ��û�� realtime_Top20.html���ø��� ������ �˸��� error �Ķ���͸� ������.
            return render(request, 'crawling/realtime_Top20.html', {'error' : error})

#������ �Է��� ���� ���
#���� �ֱٵ����͸� ������ֱ� ���� ���
    else:
#Receive_Naver_Data ���̺� �ƹ� ���� ����Ǿ� ���� ������ Ȯ���Ѵ�.
        check = Receive_Naver_Data.objects.all()

#���� ���� �����Ѵٸ�.
        if check :
#Receive_Naver_Data��� ���̺��� ���� �ֱٿ� ����� ���� key1�÷��� ������� userdate�� ��´�
            userdate = Receive_Naver_Data.objects.last().key1

#���̺��� ������ ��¼������ ���������� ����� �ֱ����� �˸´� ������ ������ �����Ѵ�.
#XXXX XX XX�� ù��° �ڸ� ���� �׹�° �ڸ��� temp1������ ��´�.
            temp1 = str(userdate)[0:4]
#XXXX XX XX�� �ټ���° �ڸ� ���� ������° �ڸ��� temp2������ ��´�.
            temp2 = str(userdate)[4:6]
#XXXX XX XX�� �ϰ���°�ڸ� ���� ������° �ڸ��� temp3������ ��´�.
            temp3 = str(userdate)[6:8]
#�� ������ ������ ������ XXXX-XX-XX���·� �����
            convert_date = temp1 + "-" + temp2 + "-" + temp3

#Receive_Naver_Data��� ���̺��� key1�÷��� userdate������ ��ġ�ϴ� ���� N_Rating������ �����Ͽ� temp_posts������ ��´�.
            temp_posts = list(Receive_Naver_Data.objects.filter(key1=userdate).order_by('-N_Rating'))
#������ �����͸� 20���� �����Ѵ�.
            posts = temp_posts[0:20]
#urls.py�� ���� ���� ������� ��û�� realtime_Top20.html���ø��� �ǽð� �˻� ������ ��� posts ������ ������ ��¥�������� convert_date������ �Բ� �����ش�.
            return render(request, 'crawling/realtime_Top20.html', {'posts': posts,'date':convert_date})
#���� ���̺� �ƹ� ���� ����Ǿ� ���� �ʴٸ�
        else :
#���������� �ƹ� �����Ͱ� ���ٴ� �޼��� ���
            return HttpResponse("DB is Empty")

#-------------------------------------Google Top20-------------------------------------------
#���� ���� TOP20 ��� ����

#top �̶�� �޼ҵ� ����
def top2(request):
    
#realtime_Top20_google.html���� get����� ���� �Էµ� ���� �ҷ����� �κ�
    userdate = request.GET.get("userdate")

#������ �����͸� ���ھ� �Ķ���Ϳ� �´� ���·� �����ϴ� �۾�
#������ �Է��� �ִ°��
    if userdate:
#��¥ ������ XXXX-XX-XX���¸� XXXXXXXX������ ����
        split_Date = userdate.split('-')
        input_Date = "".join(split_Date)

#2019-02-00~2020-02-00���� ��¥ ������ �����ش�. 
#�Ʒ� ��¥�� �����Ͽ� ���ϴ� ������ �������� �� �ִ�.
        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:

#Receive_Google_Data��� ���̺��� key1�÷��� input_Date������ ��ġ�ϴ� ���� G_Rating������ �����Ͽ� temp_posts������ ��´�.
            temp_posts = list(Receive_Google_Data.objects.filter(key1=input_Date).order_by('-G_Rating'))
#������ �����͸� 20���� �����Ѵ�.
            posts = temp_posts[0:20]
#���� �����Ͱ� �������� ���� ���
            if len(posts) <= 1 :
                error = 1
#urls.py�� ���� ���� ������� ��û�� realtime_Top20_google.html���ø��� ������ �˸��� error �Ķ���͸� ������.
                return render(request, 'crawling/realtime_Top20_google.html', {'error' : error})
#���� �����Ͱ� �����ϴ� ���
            else :
#urls.py�� ���� ���� ������� ��û�� realtime_Top20_google.html���ø��� �ǽð� �˻� ������ ��� posts ������ ��¥ ���� ��� userdate ������ �Բ� �����ش�.
                return render(request, 'crawling/realtime_Top20_google.html', {'posts': posts, 'date': userdate})

#���� 2019-02-00~2020-02-00�ǹ����� �ʰ��Ͽ��� ���
        else:
            error = 2
#urls.py�� ���� ���� ������� ��û�� realtime_Top20_google.html���ø��� ������ �˸��� error �Ķ���͸� ������.
            return render(request, 'crawling/realtime_Top20_google.html', {'error' : error})

#������ �Է��� ���� ���
#���� �ֱٵ����͸� ������ֱ� ���� ���
    else:
#Receive_Google_Data ���̺� �ƹ� ���� ����Ǿ� ���� ������ Ȯ���Ѵ�.
        check = Receive_Google_Data.objects.all()

#���� ���� �����Ѵٸ�.
        if check :
#Receive_Google_Data��� ���̺��� ���� �ֱٿ� ����� ���� key1�÷��� ������� userdate�� ��´�
            userdate = Receive_Google_Data.objects.last().key1

#���̺��� ������ ��¼������ ���������� ����� �ֱ����� �˸´� ������ ������ �����Ѵ�.
#XXXX XX XX�� ù��° �ڸ� ���� �׹�° �ڸ��� temp1������ ��´�.
            temp1 = str(userdate)[0:4]
#XXXX XX XX�� �ټ���° �ڸ� ���� ������° �ڸ��� temp2������ ��´�.
            temp2 = str(userdate)[4:6]
#XXXX XX XX�� �ϰ���°�ڸ� ���� ������° �ڸ��� temp3������ ��´�.
            temp3 = str(userdate)[6:8]
#�� ������ ������ ������ XXXX-XX-XX���·� �����
            convert_date = temp1 + "-" + temp2 + "-" + temp3

#Receive_Google_Data��� ���̺��� key1�÷��� userdate������ ��ġ�ϴ� ���� G_Rating������ �����Ͽ� temp_posts������ ��´�.
            temp_posts = list(Receive_Google_Data.objects.filter(key1=userdate).order_by('-G_Rating'))
#������ �����͸� 20���� �����Ѵ�.
            posts = temp_posts[0:20]
#urls.py�� ���� ���� ������� ��û�� realtime_Top20_google.html���ø��� �ǽð� �˻� ������ ��� posts ������ ������ ��¥�������� convert_date������ �Բ� �����ش�.
            return render(request, 'crawling/realtime_Top20_google.html', {'posts': posts,'date':convert_date})
#���� ���̺� �ƹ� ���� ����Ǿ� ���� �ʴٸ�
        else :
#���������� �ƹ� �����Ͱ� ���ٴ� �޼��� ���
            return HttpResponse("DB is Empty")

#-------------------------------------Main Template-------------------------------------------

#urls.py�� ���� ���� ������� ��û�� index.html ���ø��� �����ش�.
=======
        posts = json.loads(response)
        # userdate = Receive_Naver_Data.objects.last().date - recent DB data call
        # posts = list(Post.objects.filter(date=userdate))
        return render(request, 'crawling/realtime_google.html', {'posts': posts})


def top(request):
    userdate = request.GET.get("userdate")
    if userdate == None:
        userdate = Receive_Naver_Data.objects.last().key1
        temp_posts = list(Receive_Naver_Data.objects.filter(key1=userdate).order_by('-N_Rating'))
        posts = temp_posts[0:20]

    elif int(userdate) >= 20190200 and int(userdate) <= 20200200:
        temp_posts = list(Receive_Naver_Data.objects.filter(key1=userdate).order_by('-N_Rating'))
        posts = temp_posts[0:20]

    else:
        return render(request, 'crawling/realtime_Top20.html')

    return render(request, 'crawling/realtime_Top20.html', {'posts': posts})


def top2(request):

    userdate = request.GET.get("userdate")
    if userdate == None:
        userdate = Receive_Google_Data.objects.last().key1
        temp_posts = list(Receive_Google_Data.objects.filter(key1=userdate).order_by('-G_Rating'))
        posts = temp_posts[0:20]

    elif int(userdate) >= 20190200 and int(userdate) <= 20200200:
        temp_posts = list(Receive_Google_Data.objects.filter(key1=userdate).order_by('-G_Rating'))
        posts = temp_posts[0:20]

    else:
        return render(request, 'crawling/realtime_Top20_google.html')

    return render(request, 'crawling/realtime_Top20_google.html', {'posts': posts})


>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
def input(request):
    return render(request, 'crawling/index.html')



