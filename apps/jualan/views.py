from django.shortcuts import render_to_response
from jualan.models import Produk, Kategori
from django.template import RequestContext

def home(request):
    produk = Produk.objects.all()
    return render_to_response("jualan/index.html",{
            'list_produk' : produk,
        },context_instance=RequestContext(request))

def detil(request,produk_id):
    produk = Produk.objects.get(id=produk_id)
    return render_to_response("jualan/detil.html",{
            'produk' : produk,
        },context_instance=RequestContext(request))

def kategori(request,kategori_id):
    produk = Produk.objects.filter(kategori=kategori_id)
    kategori = Kategori.objects.get(id=kategori_id)
    return render_to_response("jualan/kategori.html",{
            'kategori' : kategori,
            'list_produk' : produk,
        },context_instance=RequestContext(request))