from django.shortcuts import render
from API import api
# Create your views here.
data = []

    
def index(request):
    global data
    data = api.discover_movies()
    
    context = {"img":data["results"][0]["backdrop_path"]}
    return render(request, "index.html", context)

def get_all(request):
    
    global data
    # print(data)
    context = {"img":data["results"][9]["backdrop_path"], "results": data["results"]}
    return render(request, "BrowseMovies.html", context)

def review(request):
     return render(request, "Review.html")

def favorites(request):
    return render(request, "Favorites.html")


def search_movie(request):
    movie_name = request.POST.get('movie_name', '') 

    results = api.search(movie_name)['results']
    if len(results) > 0:
        context = {"img":results[0]["backdrop_path"], "results": results, "movie_name": movie_name}
    else:
        context = {"not_found": True}
    return render(request, "Movies.html", context)

    # results = api.search(movie_name)['results']
    # results
    # context = {"img":results[0]["backdrop_path"], "results": results, "movie_name": movie_name}
    # return render(request, "Movies.html", context)

def movie_item(request, id, link=""):
    print(id)
    movieItem = api.findMovie(id)
    videos = movieItem['videos']['results']
    trailers = []

    # if request.method == "POST":
    print(videos)
    for i in videos:
        # print(i['type'])
        if i['type'] == 'Trailer' or i['type'] == 'Teaser':
            trailers.append(i)
    trailer = videos[0]['key']
    if len(link) > 0:
        trailer = link
    context = {"movie_item": movieItem, "trailers": trailers[:5], "defaultTrailer": trailer}
    return render(request, "MovieItem.html", context)