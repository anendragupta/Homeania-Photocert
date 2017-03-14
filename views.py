from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.generic import View
from .form import UserForm,ImageForm
import os


def index(request):
    return render(request,'home/base.html')

def level(request):
    return render(request,'home/level_page.html')

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
            print user
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('home:index')

        return render(request,self.template_name,{'form':form})

def image_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = ImageForm()
    return render(request,'home/Image_upload_form.html', {'form':form})





