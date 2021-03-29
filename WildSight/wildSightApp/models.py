from django.db import models

# Create your models here.


class Location(models.Model):
    x_coordinate_start=models.DecimalField(max_digits=9, decimal_places=6)
    x_coordinate_end=models.DecimalField(max_digits=9, decimal_places=6)
    y_coordinate_start=models.DecimalField(max_digits=9, decimal_places=6)
    y_coordinate_end=models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return "Location centred at: {}, {}".format((self.x_coordinate_start+self.x_coordinate_end)/2, (self.y_coordinate_start+self.y_coordinate_end)/2 )


class Species(models.Model):
    
    class Meta:
        verbose_name_plural="Species"

    common_name=models.CharField(max_length=50)
    scientific_name=models.CharField(max_length=50)

    def __str__(self):
        return self.common_name

