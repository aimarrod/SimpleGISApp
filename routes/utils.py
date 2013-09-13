from django.contrib.gis.geos import Point, LineString, MultiLineString
from lxml import etree
from simplegisapp.models import Route
import datetime

def parse_gpx(f, name):    
        route = None
        point = None
        sections = None
        points = None
        
        context = etree.iterparse(f, events=('start', 'end'))
                
        for event, element in context:
            
            if element.tag[-3:] == 'trk' and event == 'start':
                route = Route(name=name, creation_date=datetime.datetime.now())
                sections = []                
                
            if element.tag[-3:] == 'trk' and event == 'end':
                route.representation = MultiLineString(sections)
                route.save()
                sections = None
                
            if element.tag[-6:] == 'trkseg' and event == 'start':
                points = []
                
            if element.tag[-6:] == 'trkseg' and event == 'end':
                sections.append(LineString(points))
                points = None
                        
            if element.tag[-3:] == 'ele' and event == 'end' and point is not None:
                point.z = float(element.text)
            
            if element.tag[-5:] == 'trkpt' and event == 'start' and points is not None:
                point = Point(x=float(element.get('lon')), y=float(element.get('lat')), z=0)
                print point.x, point.y
                    
            if element.tag[-5:] == 'trkpt' and event == 'end' and point is not None:
                points.append(point)
                point = None
        
        return route