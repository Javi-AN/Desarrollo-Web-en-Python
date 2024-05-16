class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas, start=1):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{i}. {tarea.descripcion} ({estado})")

    def marcar_completada_por_posicion(self, posicion):
        if 1 <= posicion <= len(self.tareas):
            self.tareas[posicion - 1].marcar_completada()
        else:
            print("Posición inválida. Introduce un número válido.")

    def eliminar_tarea_por_posicion(self, posicion):
        if 1 <= posicion <= len(self.tareas):
            del self.tareas[posicion - 1]
        else:
            print("Posición inválida. Introduce un número válido.")

# Ejemplo de uso
lista = ListaTareas()
lista.agregar_tarea("Hacer la compra")
lista.agregar_tarea("Estudiar para el examen")
lista.tareas[0].marcar_completada()

print("Lista de tareas:")
lista.mostrar_tareas()

# Marcar como completada la segunda tarea
lista.marcar_completada_por_posicion(2)
print("\nLista de tareas actualizada:")
lista.mostrar_tareas()

# Eliminar la primera tarea
lista.eliminar_tarea_por_posicion(1)
print("\nLista de tareas después de eliminar:")
lista.mostrar_tareas()