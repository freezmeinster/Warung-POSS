import os
from glob import glob
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response,redirect
from jualan.models import Produk, Kategori
from django.template import RequestContext

def home(request):
    produk = Produk.objects.filter(jumlah__gt=0)
    paginator = Paginator(produk, 12) # Show 25 contacts per page

    page = request.GET.get('page')
    if not page  :
       page = 1
       
    try:
        produks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        produks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        produks = paginator.page(paginator.num_pages)
    return render_to_response("jualan/index.html",{
            'list_produk' : produks,
        },context_instance=RequestContext(request))

def detil(request,produk_id):
    produk = Produk.objects.get(id=produk_id)
    return render_to_response("jualan/detil.html",{
            'produk' : produk,
        },context_instance=RequestContext(request))

def kategori(request,kategori_id):
    produk = Produk.objects.filter(
        kategori=kategori_id,
        jumlah__gt=0
        )
    kategori = Kategori.objects.get(id=kategori_id)
    paginator = Paginator(produk, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    if not page  :
       page = 1
       
    try:
        produks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        produks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        produks = paginator.page(paginator.num_pages)
    return render_to_response("jualan/kategori.html",{
            'kategori' : kategori,
            'list_produk' : produks,
        },context_instance=RequestContext(request))

def static(request,slug):
    loc = os.path.join(settings.TEMPLATE_DIRS[0],"static/"+slug+".html")
    if glob(loc):
	return render_to_response("static/"+slug+".html",{
	},context_instance=RequestContext(request))
    else :
	return redirect("/")