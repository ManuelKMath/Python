from clases import Vehiculo, Camion, Auto, Moto

Vehiculo("1", 0, 10)

"""---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[5], line 1
----> 1 Vehiculo("1", 0, 10)

TypeError: Can't instantiate abstract class Vehiculo without an implementation for abstract method 'calcular_impuesto'"""


Moto("2", 0.0, 100.0, 200.0)

"""TypeError                                 Traceback (most recent call last)
Cell In[7], line 1
----> 1 Moto("2", 0.0, 100.0, 200.0)

TypeError: Can't instantiate abstract class Moto without an implementation for abstract method 'calcular_impuesto'"""