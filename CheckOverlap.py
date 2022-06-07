import json
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


f = open('./example.json')
data = json.load(f)

bal = data['bal']
doel = data['doel']

x = bal['x']
y = float(bal['y'])
width = float(bal['width'])
height = float(bal['height'])

b = [
    [x, y], 
    [x + width, y], 
    [x, y + height], 
    [x + width, y + height]
]

print(b)
poly_bal = Polygon(b)
poly_doel = Polygon(doel)

print(poly_bal.intersects(poly_doel))


