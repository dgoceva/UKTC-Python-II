from django.shortcuts import redirect, render

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


def draw_rating(request):
    global rating
    rating = int(request.GET['rating'])
    return calc_rating()


def calc_rating():
    global rating, full_stars, half_stars, empty_stars
    full_stars = rating*10//100
    empty_stars = (100-rating)*10//100
    half_stars = 10 - full_stars-empty_stars
    return redirect('/')
