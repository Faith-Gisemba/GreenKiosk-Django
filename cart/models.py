from django.db import models
from refund.models import Refund

class Cart(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    image = models.ImageField()
    price = models.IntegerField()
    date = models.DateTimeField()

    refund = models.ForeignKey(Refund, on_delete=models.CASCADE, null=True)
    
    
    def add_product(self, product):
        self.products.add(product)
        self.save()
        return self
    
    def get_total(self):
        products = self.products.all()
        total = 0
        for product in products:
            total+= product.price
            return total
        
        # total = sum([product.price for product in self.products.all()])
        
# class Cart.serializer(models.ModelSerializer):
    # products = ProductSerializer(many = True)
    # serializers.py
    
    
    
    
    
    # views.py
    # class AddToCart(ApiView):
    #     def post(self, request, format = None):
    #         cart_id = request.data["cart_id"]
    #         product_id = request.data["product_id"]
    #         cart = Cart.objects.get(id = cart_id)
    #         product = Product.objects.get(id = product_id)
    #         upload_cart = Cart.add_product(product)
    #         serializer = CartSerializers(updated_cart)
    #         return Response(serializer.data)
    
    
        
    #     urls.py
    #     path("add_to_cart", AddToCartViews-view(), name = "add_to_cart")
        
        
        
        
            
        
        
    
    
    


    
    
    



