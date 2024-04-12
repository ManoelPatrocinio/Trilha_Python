from django.db import models


class Categoria (models.Model):

    cat_name = models.CharField(max_length=15)

    def __str__ (self):
        return self.cat_name
 
class Produto (models.Model):
    
    prod_name = models.CharField(max_length=200)
    prod_imgUrl = models.CharField(max_length=200)
    prod_price = models.DecimalField(max_digits = 6, decimal_places=2)
    prod_description = models.TextField()
    prod_categoria =  models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
    createdAt = models.DateTimeField(auto_now_add=False)
    
    
    def __str__ (self):
        return self.prod_name

   

class Influencer (models.Model):
    inf_name = models.CharField(max_length=200)
    inf_at = models.CharField(max_length=70)
    inf_store_name = models.CharField(max_length=200)
    produtos = models.ManyToManyField(Produto)
    createdAt = models.DateTimeField(auto_now_add=False)

    def __str__ (self):
        return self.inf_name

class Venda (models.Model):
    
    vend_total = models.DecimalField(max_digits = 6, decimal_places=2)
    # vend_cliente = 
    createdAt = models.DateTimeField(auto_now_add=False)

    def __str__ (self):
        return self.vend_total
  
   
class ProdutosVenda(models.Model):
    product = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    influencers =  models.ForeignKey(Influencer,on_delete=models.CASCADE,null=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.product.prod_name} - {self.influencer.inf_name}"

    
# class ProdutoInfluencer(models.Model):
#     product = models.ForeignKey(Produto, on_delete=models.CASCADE)
#     influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.product.prod_name} - {self.influencer.inf_name}"
