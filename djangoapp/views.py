import json
from rest_framework.views import APIView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def first(request):
    return HttpResponse("my first Django page")

def second(request):
    return HttpResponse("My Second Djange page")

def third(request):
    return render(request,'third.html')

def reg(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        username=request.POST.get('username')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        pwd=request.POST.get('pwd')
        cnfm_pwd=request.POST.get('cnfm_pwd')
        if pwd==cnfm_pwd:
            a=register(fname=fname,lname=lname,username=username,email=email,phone=phone,gender=gender,address=address,dob=dob,password=pwd)
            a.save()
            return HttpResponse("Registration Success")
        else:
            return HttpResponse("Password and Confirm Password doesnt match... try Again")
    return render(request,'registration.html')

def loginacc(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        a=register.objects.all()  #[(1,a,123),(2,b.23)]
        for i in a:
            if(i.username==username and i.password==pwd):
                return HttpResponse("Login SuccessFully..")
        else:
            return HttpResponse("Login Failed ....")
    return render(request,'login.html')

def index(request):
   return render(request, 'index.html')

def file_upload(request):
    if request.method=='POST':
        filename=request.POST.get('filename')
        fileupload=request.FILES.get('fileupload')
        desc=request.POST.get('desc')
        b=fileuploadtest(filename=filename,fileupload=fileupload,desc=desc)
        b.save()
        return  HttpResponse("File Upload Success.....")
    return render(request, 'fileupload.html')


def emp(request):
    if request.method=='POST':
        empname=request.POST.get('empname')
        email=request.POST.get('email')
        cmpny_name=request.POST.get('cmpny_name')
        desig=request.POST.get('desig')
        phone=request.POST.get('phone')
        e=employee(empname=empname,email=email,cmpny_name=cmpny_name,desig=desig,phone=phone)
        e.save()
        return HttpResponse("Employee Details Added Successfully")

    return render(request,'employee_add.html')

def product_add(request):
    if request.method=='POST':
        pname=request.POST.get('pname')
        price=request.POST.get('price')
        cmpname = request.POST.get('cmpname')
        qty=request.POST.get('qty')
        expdate=request.POST.get('expdate')
        desc = request.POST.get('desc')
        p=product(pname=pname,price=price,cmpname=cmpname,qty=qty,expdate=expdate,desc=desc)
        p.save()
        return HttpResponse("Product Details Added Successfully")
    return render(request,'product.html')

def emp_search(request):
    if request.method == 'POST':
        empname=request.POST.get('empname')
        phone=request.POST.get('phone')
        desig= request.POST.get('desig')
        e=employee.objects.all()
        for j in e:
            if (j.empname==empname and int(j.phone)==int(phone)):
              return HttpResponse("Employee Found..")
        else:
            return HttpResponse("Failed  To Find Employee....")
    return render(request,'employee_search.html')

def product_search(request):
    if request.method=='POST':
        pname=request.POST.get('pname')
        cmpname=request.POST.get('cmpname')
        p=product.objects.all()
        for i in p:
            if i.pname==pname and i.cmpname==cmpname:
                return HttpResponse("Product  Found..")
        else:
            return HttpResponse("Failed  To Find Product....")

    return render(request, 'product_search.html')

def uploadfiles(request):
    if request.method=='POST':
        audio_name=request.POST.get('audio_name')
        audio_file=request.FILES.get('audio_file')
        video_name = request.POST.get('video_name')
        video_file = request.FILES.get('video_file')
        pdf_name = request.POST.get('pdf_name')
        pdf_file = request.FILES.get('pdf_file')
        f1=uploadall_Files(audio_name=audio_name,audio_file=audio_file,video_name=video_name,video_file=video_file,pdf_name=pdf_name,pdf_file=pdf_file)
        f1.save()
        return  HttpResponse("All Files Uploaded Successfully...!!!!!")
    return render(request,'uploadfile.html')

def select_checkbox(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        state=request.POST.get('state')
        english=request.POST.get('english')
        if english=='on':
            english=True
        else:
            english=False
        malayalam=request.POST.get('malayalam')
        if malayalam == 'on':
            malayalam = True
        else:
            malayalam= False
        hindi=request.POST.get('hindi')
        if hindi == 'on':
            hindi = True
        else:
            hindi= False
        sc=checkbox_select(fullname=fullname,state=state,english=english,malayalam=malayalam,hindi=hindi)
        sc.save()
        return HttpResponse("Saved SuccessFully.......")
    return render(request,'select_checkbox.html')


def display(request):
    a=register.objects.all()
    return render(request,'display.html',{'data':a})

def display_emp(request):
    e=employee.objects.all()
    #b=register.objects.all()
    return render(request,'display_emp.html',{'data':e})
#retuen render(request,'disply',{'data':a,'dat2':b})

#fileuplad image imagename,description

def display_file(request):
    id=[]
    filename=[]
    fileupload=[]
    desc=[]
    f=fileuploadtest.objects.all()
    for i in f:
        id1=i.id
        id.append(id1)
        im=str(i.fileupload).split('/')[-1]
        fileupload.append(im)
        name=i.filename
        filename.append(name)
        descrip=i.desc
        desc.append(descrip)
    mylist=zip(id,filename,fileupload,desc)
        #zip returns list of tuples  [(1,image.jpg,xyz,this is my first),(2,image21.jog,xrhh,this is my second)]

    return render(request,'display_file.html',{'data':mylist})

def display_allfiles(request):
    id=[]
    a_name=[]
    a_file=[]
    v_name=[]
    v_file=[]
    pdf_nm=[]
    pdf_fn=[]
    allfile=uploadall_Files.objects.all()
    for i in allfile:
        id1=i.id
        id.append(id1)
        aname=i.audio_name
        a_name.append(aname)
        af=str(i.audio_file).split('/')[-1]
        a_file.append(af)
        vname=i.video_name
        v_name.append(vname)
        vfile=str(i.video_file).split('/')[-1]
        v_file.append(vfile)
        pname=i.pdf_name
        pdf_nm.append(pname)
        pdffilenm=str(i.pdf_file).split('/')[-1]
        pdf_fn.append(pdffilenm)
    mylist=zip(id,a_name,a_file,v_name,v_file,pdf_nm,pdf_fn)


    return render(request,'displayallfiles.html',{'data':mylist})


def update_data(request,id):
    a=register.objects.get(id=id)
    if request.method=='POST':
      a.fname=request.POST.get('fname')
      a.lname = request.POST.get('lname')
      a.username = request.POST.get('username')
      a.gender = request.POST.get('gender')
      a.address = request.POST.get('address')
      a.phone = request.POST.get('phone')
      # a.dob = request.POST.get('dob')
      if len(str(request.POST.get('dob')))>0:
          a.dob=request.POST.get('dob')
      else:
          a.save()
      if str( request.POST.get('gender'))=='male' or str(request.POST.get('gender'))=='female':
          a.gender = request.POST.get('gender')
      else:
          a.save()
      a.address = request.POST.get('address')
      a.save()
      return redirect(display)

        #redirect is a method that is used to redirect fron from one fn to another fns or urls

    return  render(request,'edit_file.html',{'data':a})


def update_emp(request,id):
    e=employee.objects.get(id=id)
    if request.method=="POST":
        e.empname=request.POST.get('empname')
        e.cmpny_name = request.POST.get('cmpny_name')
        e.email = request.POST.get('email')
        e.desig = request.POST.get('desig')
        e.phone = request.POST.get('phone')
        e.save()
        return redirect(display_emp)
    return render(request,'edit_emp.html',{'data':e})


def update_file(request,id):
    f=fileuploadtest.objects.get(id=id)
    image=str(f.fileupload).split('/')[-1]
    if request.method=="POST":
        f.filename=request.POST.get('filename')
        if len(str(request.FILES.get('fileupload')))>0:
           f.fileupload=request.FILES.get('fileupload')
        else:
            f.save()
        f.desc=request.POST.get('desc')
        f.save()
        return redirect(display_file)
    return render(request,'edit_fileupload.html',{'data':f,'img':image})

def update_allfiles(request,id):
    return render(request,'edit_allfiles.html')



def delete_data(request,id):
    a=register.objects.get(id=id)
    a.delete()
    return redirect(display)

def delete_emp(request,id):
    e=employee.objects.get(id=id)
    e.delete()
    return redirect(display_emp)

def delete_file(request,id):
    f=fileuploadtest.objects.get(id=id)
    f.delete()
    return  redirect(display_file)

def delete_allfiles(request,id):
    fi=uploadall_Files.objects.get(id=id)
    fi.delete()
    return redirect(display_allfiles)

def userregistration(request):
    if request.method=="POST":
        a=userform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['username']
            em=a.cleaned_data['email']
            fname=a.cleaned_data['first_name']
            lname=a.cleaned_data['last_name']
            pwd=a.cleaned_data['password']
            cnfm=a.cleaned_data['cnfm']
            if pwd==cnfm:
              b=User(username=un,email=em,first_name=fname,last_name=lname)
              b.set_password(pwd)
              b.save()
              return HttpResponse("Registered")
            else:
                return HttpResponse("Password not match")

        else:
            return HttpResponse("Failed To ADD User ")
    else:
        form=userform()
        return render(request,'userregister.html',{'form':form})

def custom_login(request):
    if request.method=="POST":
        form=userlogin(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("Logged  in successfully..")
              #replace 'home' with your desired redirect url
            else:
                return HttpResponse("Invalid Username or password")
        else:
            return HttpResponse("Loggin failed..")

    return render(request,'login_auth.html')


class reg_classbase(generic.CreateView):
    form_class = regform
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class login_classbase(generic.View):
    form_class=logform
    template_name='class_login.html'
    def get(self,request):
        form=self.form_class
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        if request.method=="POST":
            a=logform(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                ps=a.cleaned_data['password']
                b=regmodel.objects.all()
                for i in b:
                    if em==i.email and ps==i.password:
                        return HttpResponse("Login Success!")
                else:
                     return HttpResponse("Login Failed")
            return HttpResponse("Invalid Credential..")

def read_response():
    with open(r"C:\Users\user\PycharmProjects\django_project\djangoproject\djangoapp\movie.json","r",encoding="utf8") as f:
        data=json.load(f)
    return data

class mytodos(APIView):
    def get(self,request):
        data=read_response()
        return render(request,'jsonview.html',{'data':data})


def read_hotel():
    with open(r"C:\Users\user\PycharmProjects\django_project\djangoproject\djangoapp\hotelapi.json","r",encoding="utf8") as h:
        data=json.load(h)
    return data

class hotelview(APIView):
    def get(self,request):
        data=read_hotel()
        return render(request,'hoteldisp.html',{'data':data})

