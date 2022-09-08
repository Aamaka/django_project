from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    context = [1, 4, 6, 7]
    text = "Amaka is a girl unf jnrkdnd jendn jenknd nekni jikni"
    return render(request, 'my_app/index.html', context={'abc': context, 'name': "Amaka", 'is_major': True, 'text': text})


def about(request):
    return render(request, 'my_app/about.html')


def redirect(request):
    print(reverse('my_app:redirect_to_about'))
    return HttpResponseRedirect(reverse('my_app:redirect_to_about'))
