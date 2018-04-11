from django.shortcuts import render, redirect, get_object_or_404
from .models import MainGenre
from .forms import MainGenreForm, SubGenreForm

# Create your views here.
def get_mainpage_index(request): 
    genres = MainGenre.objects.all()
    return render(request, 'new_music/mainpage.html', {'genres': genres})

def new_main_genre(request):
    if request.method == "POST":
        form = MainGenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainpage')
    else:
        form = MainGenreForm()
        
    return render(request, 'new_music/new_genre.html', {'form': form})

def new_sub_genre(request, id):
    main_genre = get_object_or_404(SubGenreForm, pk=id)
    if request.method == "POST":
        form = SubGenreForm(request.POST, request.FILES)
        if form.is_valid():
            sub_genre = form.save(commit=False)
            sub_genre.dom = main_genre.name
            sub_genre.save()
            return redirect('mainpage')
    else:
        form = SubGenreForm()
        
    return render(request, 'new_music/new_genre.html', {'form': form})

def genre_description(request, id):
    genre = get_object_or_404(MainGenre, pk=id)
    subs = MainGenre.objects.all()
    return render(request, "new_music/genre_description.html", {'genre': genre, 'subs': subs})