from django.db import models


# --------------------------------------- API Model -------------------------------------------------------------
# class Advertisable(models.Model):
#     is_adv = models.BooleanField(default=False)
#     def __bool__(self):
#          return self.is_adv

class Brand(models.Model):
    name = models.CharField(max_length=50,)
    def __str__(self):
         return self.name


# class Corona_Prod(models.Model):
#     is_corona_prod = models.BooleanField(default=False)
#     def __str__(self):
#          return self.is_corona_prod


class Compositions(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
         return self.name


class Prod_Age_Cat(models.Model):
    cat = models.CharField(max_length=50)
    def __str__(self):
         return self.cat

class Prod_Type(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
         return self.type




class Product_Information(models.Model):
    is_adv = models.BooleanField(default=False)
    availability = models.IntegerField(null=True)
    name = models.CharField(max_length=50) 
    exp_date = models.DateTimeField()
    price = models.IntegerField()
    Strip_contain = models.IntegerField(null=True, blank=True)
    usage = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    is_corona_prod = models.BooleanField(default=False)
    #image = models.ImageField(null=True, blank=True)
    

    

    #advertisable = models.ForeignKey(Advertisable, on_delete=models.SET_DEFAULT, default=False, related_name="adv_related")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="brand_related")
    #corona_prod = models.ForeignKey(Corona_Prod, on_delete=models.SET_DEFAULT, default=False, related_name="corona_related")
    prod_age_cat = models.ManyToManyField(Prod_Age_Cat, related_name="prod_age_related")
    prod_type = models.ForeignKey(Prod_Type, on_delete=models.SET_NULL, null=True, related_name="prod_type_related")
    compositions = models.ManyToManyField(Compositions, related_name="comp_related")


    def __str__(self):
         return self.name

