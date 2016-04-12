#Debris Material
idConcrete=O.materials.append(FrictMat(young=30e9,poisson=.2,frictionAngle=.6,label="concrete"))
idSteel=O.materials.append(FrictMat(young=210e9,poisson=.25,frictionAngle=.8,label="steel"))
idWood=O.materials.append(FrictMat(young=13e9,poisson=.4,frictionAngle=.8,label="wood"))

#Rainfall
idWater=O.materials.append(FrictMat(young=2.2e9,poisson=.5,frictionAngle=.1,label="water"))

#Slope
idSoil=O.materials.append(FrictMat(young=80e6,poisson=.4,frictionAngle=.5,label="soil"))
