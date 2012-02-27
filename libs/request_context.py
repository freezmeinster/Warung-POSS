from jualan.models import Kategori,Produk

def get_list_kategori(request):
    kategori = Kategori.objects.all()
    try :
        hot = Produk.objects.get(promote=True)
    except :
        hot = None
    slider = Produk.objects.filter(slider=True)
    return { 
        'list_kategori' : kategori,
        'hot' : hot,
        'produk_slider' : slider,
     }