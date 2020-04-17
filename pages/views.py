from django.shortcuts import render
from .models import HomePage
# Create your views here.
def index (request):
    homepages=HomePage.objects.all()
    context={
        'homepages':homepages,
    }

    return render(request, 'pages/index.html', context)
