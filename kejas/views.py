from django.shortcuts import render
from . models import MyKeja
from . forms import NewKeja
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, redirect
from PIL import Image
from django.core.paginator import Paginator
from django.http import HttpResponse

def index(request):
    kejas = MyKeja.objects.order_by('published_date')
    paginator = Paginator(kejas, 6) #show three startup per page 
    page = request.GET.get('page')
    kejas = paginator.get_page(page)
    template_name = 'kejas/index.html'
    context = {'kejas': kejas }
    return render(request, template_name, context)

def addkeja(request):
    """ add a new keja """
    if request.method != 'POST':
        "no data has been submitted, create a blank form "
        form = NewKeja()
    else:
        "data has been submitted, time to process it"
        form = NewKeja(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {"form": form}
    template_name = 'kejas/new_keja.html'
    return render(request, template_name, context)

def success(request):

    return HttpResponse('keja successfully uploaded. thanks for partnering with us')

def detail(request, keja_id):
    """ detail for every keja """
    keja = MyKeja.objects.get(pk=keja_id)
    template_name = 'kejas/keja_detail.html'
    context = {'keja': keja}
    return render(request, template_name, context)

