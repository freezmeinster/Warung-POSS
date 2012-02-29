from django.contrib import admin
from jualan import models

class ProdukAdmin(admin.ModelAdmin):
    class Media:
        js = (
              '/asset/tiny_mce/tiny_mce.js',
              '/asset/textarea.js',)

admin.site.register(models.Produk,ProdukAdmin)
admin.site.register(models.Kategori)
admin.site.register(models.Diskon)
admin.site.register(models.Gambar)
admin.site.register(models.Pelanggan)
admin.site.register(models.KeranjangBelanja)