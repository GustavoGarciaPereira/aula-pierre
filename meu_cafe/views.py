from django.shortcuts import render

# Create your views here.
def boas_vindas(request):
    return render(request,'boas_vindas.html')