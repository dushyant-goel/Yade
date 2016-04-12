#Rainfall will be a box of spheres

RAINFALL_BOX_CENTER = (5,20,0)
RAINFALL_BOX_EDGE1 = (0,15,5)
RAINFALL_BOX_EDGE2 = (10,25,-5)

DROP_MEAN_RADIUS = 0.002 # source:wikipedia
DROP_MEAN_VARIATON = 0.5


sp=pack.SpherePack()
sp.makeCloud(RAINFALL_BOX_EDGE1,RAINFALL_BOX_EDGE2,DROP_MEAN_RADIUS,DROP_MEAN_VARIATION)

sp.toSimulation(material=idWater)

