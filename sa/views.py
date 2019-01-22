from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'sa/index.html')

def senti(request):
    return render(request,'senti/index.html')