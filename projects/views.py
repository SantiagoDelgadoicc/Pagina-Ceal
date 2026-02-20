from django.shortcuts import render

# Create your views here.
def projects_index(request):
    return render(request, 'projects/index.html')