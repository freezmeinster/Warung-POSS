from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    
    class Meta : 
        verbose_name_plural = "Daftar Kategori"
    
    def __unicode__(self):
        return self.nama
        
class Gambar(models.Model):
    nama = models.CharField(max_length=255,null=True,blank=True)
    gambar = models.ImageField(upload_to="media")
    
    class Meta : 
        verbose_name_plural = "Daftar Gambar"
    
    def __unicode__(self):
        return self.nama

class Diskon(models.Model):
    nama = models.CharField(max_length=255)
    nominal = models.IntegerField()
    class Meta : 
        verbose_name_plural = "Daftar Diskon"
    
    def __unicode__(self):
        return self.nama

class Produk(models.Model):
    JNS_PRODUK = (
        ("BR","Barang"),
        ("JS", "Jasa"),
    )
    
    nama = models.CharField(max_length=255)
    kode = models.CharField(max_length=12)
    keterangan = models.TextField(null=True,blank=True)
    kategori = models.ForeignKey(Kategori)
    jenis = models.CharField(max_length=2,choices=JNS_PRODUK)
    harga = models.IntegerField()
    jumlah = models.IntegerField()
    satuan = models.CharField(max_length=255)
    diskon = models.ForeignKey(Diskon,null=True,blank=True)
    slider = models.BooleanField(default=False)
    promote = models.BooleanField(default=False)
    gambar = models.ForeignKey(Gambar,null=True,blank=True)
    berat = models.FloatField()
    
    class Meta : 
        verbose_name_plural = "Daftar Produk"
    
    def __unicode__(self):
        return self.nama
    
    def get_diskon(self):
	harga_potong = (self.harga * self.diskon.nominal) / 100
	return self.harga - harga_potong

class Pelanggan(models.Model):
    nama = models.CharField(max_length=255)
    keranjangbelanja = models.ForeignKey("KeranjangBelanja")
    
    class Meta : 
        verbose_name_plural = "Daftar Pelanggan"
    
    def __unicode__(self):
        return self.nama
        
        
class KeranjangBelanja(models.Model):
    nama = models.CharField(max_length=255)
    produk = models.ManyToManyField(Produk)
    
    class Meta : 
        verbose_name_plural = "Daftar Karanjang Belanja"
    
    def __unicode__(self):
        return self.nama
