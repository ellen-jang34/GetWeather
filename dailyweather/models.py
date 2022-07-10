from django.db import models
from pyowm.utils.geo import Polygon

# Create your models here.
class GPSPosition(models.Model):
    id = models.IntegerField(primary_key=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    weather = models.CharField(max_length=20)
    data_pub = models.DateField()
    
#display map 
class Map(models.Model):
    map_name = models.CharField(max_length=256)    
    description = models.TextField()
    picture = models.ImageField()
    geom = Polygon() #PolygonField()

@property
def picture_url(self):
    return self.picture.url

def __unicode__(self):
    return self.title