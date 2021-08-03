from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #django does not produce image url soo we use imageField to get it (from stackoverflow)
    image = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)    
    class Meta:
        model = Product
        fields = ('id','name','description','price','image','category')