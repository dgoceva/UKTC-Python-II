from django.shortcuts import render

# Create your views here.
full_stars = 0
half_stars = 0
empty_stars = 10
rating = 0


def index(request):
    context = {
        'full_stars': range(full_stars),
        'half_stars': range(half_stars),
        'empty_stars': range(empty_stars),
        'rating': rating,
    }
    return render(request, 'rating_app/index.html', context)
