from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jualan.views',
    url(r'^detil/(?P<produk_id>\d+)', 'detil', name='produk_detil'),
    url(r'^kategori/(?P<kategori_id>\d+)', 'kategori', name='kategori_detil'),
    )
