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

# class Time(models.Model):
#     MONTH_CHOICES=[
#         (1,"January"),
#         (2,"February"),
#         (3,"March"),
#         (4,"April"),
#         (5,"May"),
#         (6,"June"),
#         (7,"July"),
#         (8,"August"),
#         (9,"September"),
#         (10,"October"),
#         (11,"November"),
#         (12,"December"),
#     ]

#     time_period=models.IntegerField(choices=MONTH_CHOICES)

#     def __str__(self):
#         return self.get_time_period_display()

class Refined_Sighting(models.Model):
    MONTH_CHOICES=[
        (1,"January"),
        (2,"February"),
        (3,"March"),
        (4,"April"),
        (5,"May"),
        (6,"June"),
        (7,"July"),
        (8,"August"),
        (9,"September"),
        (10,"October"),
        (11,"November"),
        (12,"December"),
    ]

    time_period=models.IntegerField(choices=MONTH_CHOICES)

    Location=models.ForeignKey('Location', on_delete=models.CASCADE)

    Species=models.ForeignKey('Species', on_delete=models.CASCADE)

    Count=models.PositiveIntegerField(default=0)

    Number_of_sightings=models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} AT {} IN {}".format(self.Species, self.Location, self.get_time_period_display())






