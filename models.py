from django.db import models


# Create your models here.

class ProductTag(models.Model):
    title = models.CharField(max_length=100,default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='برچسب'
        verbose_name_plural='برچسب ها'




class ProductCategory(models.Model):
    title = models.CharField(max_length=100,verbose_name='دسته بندی',default=False)
    url_titile=models.CharField(max_length=100,verbose_name='عنوان در آدرس',null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'







class Product(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, verbose_name='عنوان')
    price = models.IntegerField(null=True, verbose_name='قیمت')
    off=models.IntegerField(default=True,verbose_name='تخفیف')
    tags = models.ManyToManyField(ProductTag , verbose_name='برچسب')
    category=models.ForeignKey(ProductCategory,verbose_name='دسته بندی',on_delete=models.CASCADE,null=True)
    create_date = models.DateTimeField(auto_now=True)
    descript = models.TextField(null=True, max_length=1000, verbose_name='توضیحات بیشتر')
    short_descript = models.TextField(null=True, max_length=200, verbose_name='توضیحات مختصر')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/حذف نشده')
    slug=models.SlugField(max_length=100,allow_unicode=True,db_index=True,verbose_name='عنوان در آدرس',null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'