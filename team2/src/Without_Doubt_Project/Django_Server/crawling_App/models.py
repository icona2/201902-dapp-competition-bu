from django.db import models
<<<<<<< HEAD

#���� TOP20�� ���� ���̺� ����
#key1(������, �⺻���� 0) : ��¥  , G_Word(������, �ִ���� 200) : �˻��� , G_Rating(������, �⺻���� 0) : ������ ����
=======
#from django_pandas.managers import DataFrameManager


>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
class Receive_Google_Data(models.Model) :
    key1 = models.IntegerField(default=0)
    G_Word = models.CharField(max_length=200)
    G_Rating = models.IntegerField(default=0) 

<<<<<<< HEAD
# �������� ���� ȣ���Ҷ� G_Word�� Ÿ��Ʋ�� ��½�Ų��.        
    def __str__(self):
        return self.G_Word

#������ TOP20�� ���� ���̺� ����
#key1(������, �⺻���� 0) : ��¥  , N_Word(������, �ִ���� 200) : �˻��� , N_Rating(������, �⺻���� 0) : ������ ����
=======
 #   objects = DataFrameManager()
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.G_Word


>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
class Receive_Naver_Data(models.Model):
    key1 = models.IntegerField(default=0)
    N_Word = models.CharField(max_length=200)
    N_Rating = models.IntegerField(default=0)

<<<<<<< HEAD
# �������� ���� ȣ���Ҷ� N_Word�� Ÿ��Ʋ�� ��½�Ų��.
    def __str__(self):
        return self.N_Word

#�������� ���� ���̺� ����
#key1(������, �⺻���� 0) : ��¥  , Word(������, �ִ���� 200) : �����ܾ� , Type(������, �ִ���� 200) : ������ ��
class Missing_Data(models.Model):
    key1 = models.IntegerField(default=0)
    Word = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)

# �������� ���� ȣ���Ҷ� Word�� Ÿ��Ʋ�� ��½�Ų��.
    def __str__(self):
        return self.Word
=======
#    objects = DataFrameManager()

    def publish(self):
        self.save()

    def __str__(self):
        return self.N_Word

>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
