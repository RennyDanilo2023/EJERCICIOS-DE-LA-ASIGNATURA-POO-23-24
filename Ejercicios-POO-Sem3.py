# Abstracción: Clase Base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        # Atributos que representan características esenciales de un vehículo
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def descripcion(self):
        # Método que proporciona una descripción básica del vehículo
        return f"{self.marca} {self.modelo}, Velocidad Máxima: {self.velocidad_maxima} km/h"

    # Encapsulación: Método Privado para Actualizar Velocidad
    def __actualizar_velocidad(self, nueva_velocidad):
        # Método privado para cambiar la velocidad (no accesible desde fuera de la clase)
        if 0 <= nueva_velocidad <= self.velocidad_maxima:
            print(f"Velocidad actualizada a {nueva_velocidad} km/h")
        else:
            print("Velocidad fuera de rango")

    def acelerar(self, incremento):
        # Método público que utiliza el método privado __actualizar_velocidad
        self.__actualizar_velocidad(self.velocidad_maxima + incremento)

# Herencia: Subclase Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, num_puertas):
        # Inicialización de la superclase Vehiculo
        super().__init__(marca, modelo, velocidad_maxima)
        self.num_puertas = num_puertas  # Atributo específico de Automovil

    # Polimorfismo: Método Sobreescrito 'descripcion'
    def descripcion(self):
        # Método extendido para incluir información adicional específica de Automovil
        return super().descripcion() + f", Número de puertas: {self.num_puertas}"

# Herencia: Subclase Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, tipo):
        # Inicialización de la superclase Vehiculo
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo = tipo  # Atributo específico de Motocicleta

    # Polimorfismo: Método Sobreescrito 'descripcion'
    def descripcion(self):
        # Método extendido para incluir información adicional específica de Motocicleta
        return super().descripcion() + f", Tipo: {self.tipo}"

# Demostración
auto = Automovil("Toyota", "Corolla", 180, 4)
moto = Motocicleta("Yamaha", "YZF-R1", 299, "Deportiva")

print(auto.descripcion())
print(moto.descripcion())
