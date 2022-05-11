from django.db import models


PLANT_SIZES = [
    ('small', 'small (< 15cm)'),
    ('medium', 'medium (15cm - 30cm)'),
    ('big', '> big (30cm)'),
]

WATER_NEED = [
    ('++', 'Big Drinker'),
    ('--', 'Teetotaler'),
]

LIGHT_NEED = [
    ('++', 'Ginger Tan'),
    ('--', 'European'),
]

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    """ This Model is for the pant category """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Habitat(models.Model):
    """ This Model is for the pant habitat """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    water_need = models.CharField(max_length=254, choices=WATER_NEED, null=True, blank=True)
    light_need = models.CharField(max_length=254, choices=LIGHT_NEED, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ This Model is for the plant products """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=400, choices=PLANT_SIZES, default='medium (15cm - 30cm)', null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    habitat = models.ForeignKey('Habitat', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name