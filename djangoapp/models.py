from django.db import models

# Create your models here.

# fname,lname,username,email,phone,gender,address,dob,password,cnpwd
class register(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    dob=models.DateField()
    password=models.CharField(max_length=20)

class fileupload(models.Model):
    filename=models.CharField(max_length=50)
    fileupload=models.FileField(upload_to='djangoapp/static')
    desc=models.CharField(max_length=200)

class employee(models.Model):
    empname=models.CharField(max_length=30)
    email=models.EmailField()
    cmpny_name=models.CharField(max_length=50)
    desig=models.CharField(max_length=50)
    phone=models.IntegerField()

class product(models.Model):
    pname=models.CharField(max_length=30)
    price=models.IntegerField()
    cmpname=models.CharField(max_length=30)
    qty=models.IntegerField()
    expdate=models.DateField()
    desc=models.CharField(max_length=80)

class fileuploadtest(models.Model):
    filename=models.CharField(max_length=50)
    fileupload=models.FileField(upload_to='djangoapp/static')
    desc=models.CharField(max_length=200)

class fileupload(models.Model):
    filename=models.CharField(max_length=50)
    fileupload=models.FileField(upload_to='djangoapp/static')
    desc=models.CharField(max_length=200)

class uploadall_Files(models.Model):
    audio_name=models.CharField(max_length=30)
    audio_file=models.FileField(upload_to='djangoapp/static')
    video_name = models.CharField(max_length=30)
    video_file = models.FileField(upload_to='djangoapp/static')
    pdf_name = models.CharField(max_length=30)
    pdf_file = models.FileField(upload_to='djangoapp/static')

class checkbox_select(models.Model):
    choice=[
        ('kerala','kerala'),#(databse,label(template))
        ('tamil nadu','tamil nadu'),
        ('karnataka','karnataka')
    ]
    fullname=models.CharField(max_length=30)
    state=models.CharField(max_length=20,choices=choice) #select
    english=models.BooleanField(default=False)
    malayalam=models.BooleanField(default=False)
    hindi=models.BooleanField(default=False)


class regmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name

