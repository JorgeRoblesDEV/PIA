from gi.repository import Gtk

import random

class VentanaGrid(Gtk.Window):
    def __init__(self, tamanio_botones = 300, tamanio_texto = 36):
        # Llamar al constructor de la clase padre (Gtk.Window)
        super().__init__(title="Tic - Tac - Toe")

        self.tamanio_botones = tamanio_botones
        self.tamanio_texto = tamanio_texto

        # Objeto que representa la cuadrícula del juego
        self.grid = Gtk.Grid()

        self.empieza = self.turno_empieza()

        self.turno_actual = self.empieza

        self.soluciones = self.inicializar_soluciones()

        self.victorias_X = 0
        self.victorias_O = 0

        # Almacena el resultado de la partida anterior (Ganador, Empate, None)
        self.resultado_anterior = None

        # Crear la cuadrícula y los botones
        self.crear_grid()

        # Conectar la señal "destroy" a la función Gtk.main_quit para cerrar la aplicación al cerrar la ventana
        self.connect("destroy", Gtk.main_quit)

    def juego(self):
        self.add(self.grid)

        self.show_all()

    def inicializar_soluciones(self):
        soluciones = []
        for i in range(3):
            fila = [None] * 3
            soluciones.append(fila)
        return soluciones

    def crear_grid(self):
        self.botones = []
        for i in range(3):
            fila_botones = []
            for j in range(3):
                etiqueta_boton = ""
                boton = Gtk.Button(label=etiqueta_boton)

                fila_botones.append(boton)
                boton.set_size_request(self.tamanio_botones, self.tamanio_botones)
                boton.connect("clicked", self.al_hacer_click, i, j)
            self.botones.append(fila_botones)

        for i, fila in enumerate(self.botones):
            for j, boton in enumerate(fila):
                self.grid.attach(boton, j, i, 1, 1)

    def al_hacer_click(self, boton, fila, columna):
        if boton.get_label() == "":

            nuevo_texto = self.turno_actual
            boton.set_label(nuevo_texto)
            self.soluciones[fila][columna] = nuevo_texto

            # Obtener el widget de la etiqueta del botón
            label_widget = boton.get_child()

            # Cambiar el tamaño del texto utilizando set_markup
            label_widget.set_markup('<span size="{}pt">{}</span>'.format(self.tamanio_texto, nuevo_texto))

            if self.isWinner(nuevo_texto):
                self.resultado_anterior = "Ganador: " + nuevo_texto
                if nuevo_texto == 'X':
                    self.victorias_X += 1
                else:
                    self.victorias_O += 1
                self.mostrar_dialogo_fin_partida(self.resultado_anterior)
                self.mostrar_dialogo_victorias()
            elif self.isBoardFull():
                self.resultado_anterior = "Empate"
                self.mostrar_dialogo_fin_partida(self.resultado_anterior)
                self.mostrar_dialogo_victorias()
            else:
                self.cambiar_turno()

    def turno_empieza(self):
        if random.randint(0, 1) == 0:
            return 'X'
        else:
            return 'O'


    def cambiar_turno(self):
        if self.turno_actual == 'X':
            self.turno_actual = 'O'
        else:
            self.turno_actual = 'X'

    def isWinner(self, jugador):
        for i in range(3):
            # Filas y Columnas
            if (
                (self.soluciones[i][0] == self.soluciones[i][1] == self.soluciones[i][2] == jugador) or
                (self.soluciones[0][i] == self.soluciones[1][i] == self.soluciones[2][i] == jugador)
            ):
                return True

        # Diagonales
        if (
            (self.soluciones[0][0] == self.soluciones[1][1] == self.soluciones[2][2] == jugador) or
            (self.soluciones[0][2] == self.soluciones[1][1] == self.soluciones[2][0] == jugador)
        ):
            return True

        return False

    def reiniciar_partida(self):
        self.soluciones = self.inicializar_soluciones()
        self.numero_turnos = 0
        self.resultado_anterior = ""
        self.empieza = self.turno_empieza()
        self.mostrar_dialogo_inicio()
        self.turno_actual = self.empieza

        for fila in self.botones:
            for boton in fila:
                boton.set_label("")

    def isBoardFull(self):
        for fila in self.soluciones:
            for elemento in fila:
                if elemento is None:
                    return False
        return True

    def mostrar_dialogo_fin_partida(self, mensaje):
        dialogo = Gtk.MessageDialog(
            parent=self,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
        )
        dialogo.format_secondary_text(mensaje)
        dialogo.run()
        dialogo.destroy()

    def mostrar_dialogo_victorias(self):
        mensaje = "Victorias de X: " + str(self.victorias_X) + "\nVictorias de O: " + str(self.victorias_O)
        dialogo = Gtk.MessageDialog(
            parent=self,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
        )
        dialogo.format_secondary_text(mensaje)
        dialogo.run()
        dialogo.destroy()

        dialogo = Gtk.MessageDialog(
            parent=self,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text="¿Desea jugar otra partida?"
        )

        respuesta = dialogo.run()
        dialogo.destroy()

        if respuesta == Gtk.ResponseType.YES:
            self.reiniciar_partida()
        else:
            self.destroy()

    def mostrar_dialogo_inicio(self):
        mensaje_inicial = "Empieza el/la: " + str(self.empieza)
        dialogo_inicial = Gtk.MessageDialog(
            parent=self,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
        )
        dialogo_inicial.format_secondary_text(mensaje_inicial)
        dialogo_inicial.run()
        dialogo_inicial.destroy()
