import json
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


f = open('./example.json')
data = json.load(f)

bal = data['bal']
doel = data['doel']

poly_bal = Polygon(bal)
poly_doel = Polygon(doel)

print(poly_bal.intersects(poly_doel))


