from django.shortcuts import HttpResponse,render

def home(request):
    data={
        'name':'rakesh',
        'age':25
    }
    return render(request,home.html,context={'data':data})
