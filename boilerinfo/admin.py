# Below import is to facilitate import/export in the admin console
from import_export.admin import ImportExportModelAdmin
#from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields

from django.contrib import admin

# Register your models here.

from .models import Document, Profile, ProductPrice

admin.site.register(Document)
admin.site.register(Profile)
#admin.site.register(PricingFile)
#admin.site.register(ProductPrice)

class ProductPriceResource(resources.ModelResource):
    class Meta:
        model = ProductPrice
        import_id_fields = ('user','product_code',)
        exclude = ('id',)
        skip_unchanged = True
        fields = ('user', 'brand', 'model_name', 'product_code','price',)


@admin.register(ProductPrice)
class ProductPriceAdmin(ImportExportModelAdmin):
    resource_class = ProductPriceResource
    list_display = ('user','brand', 'model_name', 'product_code','price')
    #pass