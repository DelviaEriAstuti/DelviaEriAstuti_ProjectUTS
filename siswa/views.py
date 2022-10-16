from django.shortcuts import render

# Create your views here.
def siswa(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexsiswa.html', konteks)
