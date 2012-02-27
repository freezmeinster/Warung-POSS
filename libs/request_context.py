from jualan.models import Kategori,Produk

def get_list_kategori(request):
    kategori_barang = []
    kategori_jasa = []
    for barang in Produk.objects.filter(jenis="BR"):
	if barang.kategori in kategori_barang :
	    pass 
	else :
	    kategori_barang.append(barang.kategori)
    
    for jasa in Produk.objects.filter(jenis="JS"):
	if jasa.kategori in kategori_jasa :
	    pass
	else :
	    kategori_jasa.append(jasa.kategori)
	    
    try :
        hot = Produk.objects.get(promote=True)
    except :
        hot = None
    slider = Produk.objects.filter(slider=True,jumlah__gt=0)
    return { 
        'list_kategori_barang' : kategori_barang,
        'list_kategori_jasa' : kategori_jasa,
        'hot' : hot,
        'produk_slider' : slider,
     }