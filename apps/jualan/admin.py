from django.contrib import admin
from jualan.models import Produk, Kategori, Diskon, Gambar

class ProdukAdmin(admin.ModelAdmin):
    class Media:
        js = (
              '/asset/tiny_mce/tiny_mce.js',
              '/asset/textarea.js',)

admin.site.register(Produk,ProdukAdmin)
admin.site.register(Kategori)
admin.site.register(Diskon)
admin.site.register(Gambar)