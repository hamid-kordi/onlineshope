from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterForm
# Create your views here.


class UserRegisterView(View):
    form_class = UserRegisterForm
    templateـname = 'accounts/register.html'
    def get(self,request):
        form = self.form_class
        return render(request,'accounts/register.html',{'form':form})
        

    def post(self,request):
        pass