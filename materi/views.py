from django.shortcuts import render

# Create your views here.
def materi(request):
    judul = ["Materi Kelas 1", "Materi Kelas 2", "Materi Kelas 3", "Materi Kelas 4", "Materi Kelas 5", "Materi Kelas 6", "Materi Kelas 7", "Materi Kelas 8", "Materi Kelas 9", "Materi Kelas 10", "Materi Kelas 11", "Materi Kelas 12"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexmateri.html', konteks)
