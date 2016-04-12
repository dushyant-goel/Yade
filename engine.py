O.engines=[
   ForceResetter(),
   InsertionSortCollider([Bo1_Sphere_Aabb(),Bo1_Facet_Aabb()]),
   InteractionLoop(
      # handle sphere+sphere and facet+sphere collisions
      [Ig2_Sphere_Sphere_L3Geom(),Ig2_Facet_Sphere_L3Geom()],
      [Ip2_FrictMat_FrictMat_FrictPhys()],
      [Law2_L3Geom_FrictPhys_ElPerfPl()]
   ),
   NewtonIntegrator(gravity=(0,0,-9.81),damping=0.4),
   # call the checkUnbalanced function (defined below) every 2 seconds
   PyRunner(command='checkUnbalanced()',realPeriod=2),
   # call the addPlotData function every 200 steps
   PyRunner(command='addPlotData()',iterPeriod=100)
]
O.dt=.5*PWaveTimeStep()
