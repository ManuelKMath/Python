
class EmpresaLogistica:
    def __init__(self):
        # flota = {placa (str): vehiculo (obj)}
        self.flota = {}

    def registrar_vehiculo(self, vehiculo):
        if vehiculo.placa in self.flota:
            print(f"El vehículo con placa: {vehiculo.placa} ya está registrado en la flota.")
            return
        self.flota[vehiculo.placa] = vehiculo
        print(f"Se ha registrado exitosamente el vehículo con placa: {vehiculo.placa}")
        return