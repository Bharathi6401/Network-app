from Demos.win32ts_logoff_disconnected import username
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .registerform import *

from.models import *


from django.contrib.auth import authenticate,login,logout



def index(request):
    return render(request,"home.html")


#def register(request):
    #context={
       # 'register_form':Register_form()
    #}
   # if request.method=='POST':
        #print(request.POST)
       # reg_form=Register_form(request.POST,request.FILES)

       # if reg_form.is_valid():
            #reg_form.save()

    #return render(request,'registerationform.html',context)
#
# from django.shortcuts import render, redirect
# from django.contrib import messages
# # from .forms import Register_form  # Ensure Register_form is imported properly
#
# def register(request):
#     if request.method == 'POST':
#         # Include request.FILES for file uploads
#         reg_form = Register_form(request.POST, request.FILES)
#
#         if reg_form.is_valid():
#             reg_form.save()
#             # Display success message
#             messages.success(request, "Registration successful!")
#             return redirect('success_page')  # Replace 'success_page' with your URL name
#         else:
#             # Display error message
#             messages.error(request, "Please correct the errors below.")
#
#     else:
#         reg_form = Register_form()  # Empty form for GET requests
#
#     # Pass the form instance (valid or invalid) to the template
#     context = {'register_form': reg_form}
#     return render(request, 'registerationform.html', context)
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        reg_form = Register_form(request.POST, request.FILES)
        if reg_form.is_valid():
            company=reg_form.save()
            #return redirect('home')  # Replace 'success_page' with the name of your success URL or view.
            company.created_by=request.user

            company.save()
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        reg_form = Register_form()

    context = {
        'register_form': reg_form
    }
    return render(request, 'registerationform.html', context)





def event(request):
    if request.method=='POST':
        event_form=Event_form(request.POST,request.FILES)
        if event_form.is_valid():
            event_form.save()
    else:
        event_form=Event_form()

    return render(request,'event.html',{'event':event_form})


def news(request):
    if request.method=='POST':
        news_form=News_form(request.POST,request.FILES)
        if news_form.is_valid():
            news_form.save()
    else:
        news_form=News_form()

    return render(request,'news.html',{'news':news_form})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        #print(request.POST)

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)

        if user is not None:
            login(request, user)  # This now correctly refers to Django's login function
            return redirect('landing')# Use a URL name instead of a template filename


            #messages.error(request, "Invalid username or password.") # Add feedback for invalid credentials
        else:
            return render(request, 'login.html', {"error":"invalid username or password"})

    return render(request, 'login.html')


def landing(request):
        return render(request,'admin_landing.html')



def partners1(request):
    companies=Reg.objects.filter(status='approved')

    for comp in companies:
        print(f"Company Name: {comp.company_name}, Status: {comp.status}")

    return render(request,'partners.html',context={'companies':companies})


