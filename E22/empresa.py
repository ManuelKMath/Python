
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

    def buscar_vehiculo(self, placa):
        if not placa.upper() in self.flota:
            return
        return self.flota[placa]

    def actualizar_kilometraje_vehiculo(self, placa, kilometraje_nuevo: float):
            if not self.flota:
                print("No hay vehículos en la flota")
                return
            if self.buscar_vehiculo(placa) is None:
                print("Introduce una placa válida")
                return
            self.buscar_vehiculo(placa).kilometraje = kilometraje_nuevo
            return