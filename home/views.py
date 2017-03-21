from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Practical_test,Second_level,First_level,Third_level
from django.views.generic import View
from .form import UserForm,ImageForm
import os


def index(request):
    return render(request,'home/base.html')

@login_required(login_url='/login/')
def level(request):
    return render(request,'home/level_page.html')

@login_required(login_url='/login/')
def pdf_download(request, filename):
  path = os.expanduser('~/media/pdf/')
  wrapper = FileWrapper(file(filename,'rb'))
  response = HttpResponse(wrapper, content_type=mimetypes.guess_type(filename)[0])
  response['Content-Disposition'] = "attachment; filename=" + filename
  return response

def first_level(request):
    return render(request,'home/first_level.html')

def second_level(request):
    return render(request,'home/second_level.html')

def third_level(request):
    return render(request,'home/third_level.html')

def logout_view(request):
    logout(request)
    return render(request,'registration/logout.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'Registration/registration_form.html'

    #Display Blank Form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    #process form Data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return user objects if credentials are correct
            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('home:level')

        return render(request,self.template_name,{'form':form})

@login_required(login_url='/login/')
def image_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = ImageForm()
    return render(request,'home/Image_upload_form.html', {'form':form})

@login_required(login_url='/login/')
def quiz_question(request,level_id):
    id= level_id.__str__()
    if id == '1':
        context = First_level.objects.all()
        return render(request, 'home/quiz.html', {'context': context})
    if id == '2':
        context = Second_level.objects.all()
        return render(request, 'home/quiz.html', {'context': context})
    if id == '3':
        context = Third_level.objects.all()
        return render(request, 'home/quiz.html', {'context': context})

def save(request):
    for x in range(1,10):
        print ">>>>>"
        print 'q'+x.__str__()
        p=request.POST.get("q", None)
        if p in ['a','b','c','d']:
            print "Matchhhhh"
        print p
    return redirect('home:index')

