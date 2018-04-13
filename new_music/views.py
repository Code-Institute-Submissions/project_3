from django.shortcuts import render, redirect, get_object_or_404
from .models import MainGenre, SubGenre, Artists
from .forms import MainGenreForm, SubGenreForm, ArtistForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_mainpage_index(request): 
    genres = MainGenre.objects.all()
    subs = SubGenre.objects.all()
    artists = Artists.objects.all()
    return render(request, 'new_music/mainpage.html', {'genres': genres, 'subs': subs, 'artists': artists})

@login_required
def new_main_genre(request):
    if request.method == "POST":
        form = MainGenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainpage')
    else:
        form = MainGenreForm()
        
    return render(request, 'new_music/new_genre.html', {'form': form})

@login_required
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

@login_required
def new_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainpage')
    else:
        form = ArtistForm()
        
    return render(request, 'new_music/new_artist.html', {'form': form})

def genre_description(request, id):
    genre = get_object_or_404(MainGenre, pk=id)
    subs = genre.subgenres.all()
    artists = genre.artists.all()
    return render(request, "new_music/genre_description.html", {'genre': genre, 'subs': subs, 'artists': artists})

def subgenre_description(request, id):
    subgenre = get_object_or_404(SubGenre, pk=id)
    artists = subgenre.artists.all()
    return render(request, "new_music/subgenre_description.html", {'subgenre': subgenre, 'artists': artists})

def artist_description(request, id):
    artist = get_object_or_404(Artists, pk=id)
    subs = artist.subgenre.all()
    genres = artist.genre.all()
    return render(request, "new_music/artist_description.html", {'genres': genres, 'subs': subs, 'artist': artist})