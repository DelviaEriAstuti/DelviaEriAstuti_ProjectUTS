from django.shortcuts import render

# Create your views here.
def pentutor(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexpentutor.html', konteks)
