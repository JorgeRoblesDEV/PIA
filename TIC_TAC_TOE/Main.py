import gi
gi.require_version('Gtk', '3.0')

from VentanaGrid import VentanaGrid
from gi.repository import Gtk

def main():
    ventana = VentanaGrid(tamanio_texto=100)

    ventana.set_position(Gtk.WindowPosition.CENTER)

    ventana.mostrar_dialogo_inicio()

    ventana.juego()

    # Iniciar el bucle principal de Gtk para manejar eventos y actualizar la interfaz de usuario
    Gtk.main()

if __name__ == "__main__":
    main()


# Crear los botones y el grid a Mano
# button1 = Gtk.Button(label="Button 1")
# button2 = Gtk.Button(label="Button 2")
# button3 = Gtk.Button(label="Button 3")
# button4 = Gtk.Button(label="Button 4")
# button5 = Gtk.Button(label="Button 5")
# button6 = Gtk.Button(label="Button 6")
# button7 = Gtk.Button(label="Button 7")
# button8 = Gtk.Button(label="Button 8")
# button9 = Gtk.Button(label="Button 9")

# grid = Gtk.Grid()
# grid.add(button1)
# grid.attach(button2, 1, 0, 1, 1)
# grid.attach(button3, 2, 0, 1, 1)
# grid.attach_next_to(button4, button1, Gtk.PositionType.BOTTOM, 1, 1)
# grid.attach(button5, 1, 1, 1, 1)
# grid.attach(button6, 2, 1, 1, 1)
# grid.attach_next_to(button7, button4, Gtk.PositionType.BOTTOM, 1, 1)
# grid.attach(button8, 1, 2, 1, 1)
# grid.attach(button9, 2, 2, 1, 1)