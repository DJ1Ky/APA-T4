
"""

NOMBRE: Juan Camilo De Los Ríos 

PRÁCTICA 4: GENERACIÓN DE NÚMEROS ALEATORIOS:

    Clase Aleat() ----> implementa el generador de números aleatorios LGC.

"""

class Aleat:

    def __init__(self):
        """
            Inicializa los valores de m, a, c y la semilla.
        """
        self.m = 2**48
        self.a = 25214903917
        self.c = 11
        self.semilla = 1212121
        return none


    # Método que genera el siguiente número aleatorio, y hace iterable la clase Aleat


   	def __next__(self):
   		self.semilla = (self.a * self.semilla + self.c) % self.m
    	return self.semilla 


  # Método que sobrecarga la llamada a función, es decir, el uso del objeto como si fuera una función

    def __call__(self, semilla):  
        self.semilla = semilla


    def aleat (m = pow(48, 2), a = 25214903917, c = 11, semilla = 1212121):
       
	"""
        ESTRUCTURA DE CÓDIGO PARA LA GENERACIÓN DE NÚMEROS ALEATORIOS 

        >>> rand = aleat(m=64, a=5, c=46, x0=36)
        >>> for _ in range(4):
        ...     print(next(rand))
        ...
        34
        24
        38
        44
        >>> rand.send(24)
        38
        >>> for _ in range(4):
        ...     print(next(rand))
        ...
        44
        10
        32
        14
        """
        x = semilla
		while True:
    		x = (a * x + c) % m
    		nextt = yield x
        	if nextt:
            x = nextt
   		 return None
    		

	import doctest
	doctest.testmod()  


# Tests unitarios

rand = Aleat(m=32, a=9, c=13, x0=11)
for _ in range(4):
	print(next(rand))


rand(29)
for _ in range(4):
	print(next(rand))


rand = aleat(m=64, a=5, c=46, x0=36)
for _ in range(4):
	print(next(rand))


rand.send(24)
for _ in range(4):
	print(next(rand))
