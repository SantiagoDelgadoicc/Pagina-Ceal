from django.shortcuts import render

# Create your views here.
def assistance_index(request):
    return render(request, 'assistance/index.html')