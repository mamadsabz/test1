from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def home (request):
    return render(request,'home.html',{

    })



def headr_render_partial(request):
    return render (request, 'header.html',{

    })


def footer_render_partial(request):
    return render(request, 'foter.html', {

    })