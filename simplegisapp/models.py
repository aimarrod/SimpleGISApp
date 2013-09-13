from django.contrib.gis.db import models
import sys

class Route(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField()
    representation = models.MultiLineStringField(dim=3)
    objects = models.GeoManager()
    
    def length(self):
        return self.representation.length
    
    def nearest(self):
        minDist = sys.maxint
        rt = self
        for route in Route.objects.exclude(pk=self.pk):
            dist = self.representation.distance(route.representation)
            if dist < minDist:
                minDist = dist
                rt = route
        return rt
    
    def geoJSON(self):
        return self.representation.json