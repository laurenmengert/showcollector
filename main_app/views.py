from django.shortcuts import render

class Show:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, num_seasons, description, imdb_rating):
    self.name = name
    self.num_seasons = num_seasons
    self.description = description
    self.imdb_rating = imdb_rating



shows = [
    Show('Schitts Creek', 5, 'Funny!', 8.4)
]

# Create your views here.

def home(request):
    return HttpResponse('<h1>HELLO</h1>')

def about(request):
    return render(request, 'about.html')

def shows_index(request):
    return render(request, 'shows/index.html', {'shows': shows})