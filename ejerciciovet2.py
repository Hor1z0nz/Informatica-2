class Medicamento:
    def __init__(self, nombre, dosis):
        self.nombre = nombre
        self.dosis = dosis

class Mascota:
    def __init__(self, nombre, historia_clinica, tipo, peso, fecha_ingreso, medicamentos=[]):
        self.nombre = nombre
        self.historia_clinica = historia_clinica
        self.tipo = tipo
        self.peso = peso
        self.fecha_ingreso = fecha_ingreso
        self.medicamentos = medicamentos

class ClinicaVeterinaria:
    def __init__(self):
        self.servicio_hospitalizacion = []
        self.max_pacientes = 10

    def ingresar_mascota(self, mascota):
        if len(self.servicio_hospitalizacion) < self.max_pacientes:
            if not self.existe_mascota(mascota.historia_clinica):
                self.servicio_hospitalizacion.append(mascota)
                print("Mascota ingresada correctamente.")
            else:
                print("Error: Ya existe una mascota con la misma historia clínica.")
        else:
            print("Error: El servicio de hospitalización está completo.")

    def ver_fecha_ingreso(self, historia_clinica):
        for mascota in self.servicio_hospitalizacion:
            if mascota.historia_clinica == historia_clinica:
                return mascota.fecha_ingreso
        return "Mascota no encontrada."

    def ver_numero_mascotas(self):
        return len(self.servicio_hospitalizacion)

    def ver_medicamentos(self, historia_clinica):
        for mascota in self.servicio_hospitalizacion:
            if mascota.historia_clinica == historia_clinica:
                return [medicamento.nombre for medicamento in mascota.medicamentos]
        return "Mascota no encontrada."

    def eliminar_mascota(self, historia_clinica):
        for mascota in self.servicio_hospitalizacion:
            if mascota.historia_clinica == historia_clinica:
                self.servicio_hospitalizacion.remove(mascota)
                print("Mascota eliminada del servicio.")
                return
        print("Mascota no encontrada.")

    def existe_mascota(self, historia_clinica):
        for mascota in self.servicio_hospitalizacion:
            if mascota.historia_clinica == historia_clinica:
                return True
        return False

# Función para el menú del programa
def menu():
    clinica = ClinicaVeterinaria()
    
    while True:
        print("\n--- Clínica Veterinaria ---")
        print("1. Ingresar una mascota")
        print("2. Ver fecha de ingreso de una mascota")
        print("3. Ver número de mascotas en el servicio")
        print("4. Ver medicamentos de una mascota")
        print("5. Eliminar una mascota")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la mascota: ")
            historia_clinica = input("Número de historia clínica: ")
            tipo = input("Tipo de mascota (canino o felino): ")
            peso = float(input("Peso de la mascota: "))
            fecha_ingreso = input("Fecha de ingreso: ")
            
            # Ingresar medicamentos
            medicamentos = []
            while True:
                nombre_medicamento = input("Nombre del medicamento (dejar en blanco para finalizar): ")
                if not nombre_medicamento:
                    break
                dosis = input("Dosis del medicamento: ")
                medicamento = Medicamento(nombre_medicamento, dosis)
                medicamentos.append(medicamento)
            
            mascota = Mascota(nombre, historia_clinica, tipo, peso, fecha_ingreso, medicamentos)
            clinica.ingresar_mascota(mascota)
            
        elif opcion == "2":
            historia_clinica = input("Número de historia clínica de la mascota: ")
            fecha = clinica.ver_fecha_ingreso(historia_clinica)
            print(f"Fecha de ingreso de la mascota: {fecha}")
            
        elif opcion == "3":
            num_mascotas = clinica.ver_numero_mascotas()
            print(f"Número de mascotas en el servicio: {num_mascotas}")
            
        elif opcion == "4":
            historia_clinica = input("Número de historia clínica de la mascota: ")
            medicamentos = clinica.ver_medicamentos(historia_clinica)
            if medicamentos != "Mascota no encontrada.":
                print("Medicamentos que se administra la mascota:")
                for medicamento in medicamentos:
                    print(f"- {medicamento}")
            else:
                print("Mascota no encontrada.")
            
        elif opcion == "5":
            historia_clinica = input("Número de historia clínica de la mascota a eliminar: ")
            clinica.eliminar_mascota(historia_clinica)
            
        elif opcion == "6":
            print("Saliendo del programa.")
            break
            
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
