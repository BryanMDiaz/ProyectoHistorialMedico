import re
import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel, LabelFrame
from tkinter import messagebox
from modelo.pacienteDAO import Persona, editarDatoPaciente, guardarDatoPaciente, listar, listarCondicion, eliminarPaciente
from modelo.historiaMedicaDAO import eliminarHistorial, historiaMedica, guardarHistorial, listarHistorial
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date

# Clase de inicializacion predeterminada
class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.idPersona = None
        self.camposPacientes() 
        self.idPersona = None
        self.idPersonaHistoria = None
        self.idHistoriaMedica = None 
        self.deshabilitar()
        self.tablaPaciente()

    def camposPacientes(self): 

        # Diseño de los label
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblApellidoPaterno = tk.Label(self, text='Apellidos Paterno:')
        self.lblApellidoPaterno.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblApellidoPaterno.grid(column=0, row=1, padx=10, pady=5)

        self.lblApellidoMaterno = tk.Label(self, text='Apellidos Materno:')
        self.lblApellidoMaterno.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblApellidoMaterno.grid(column=0, row=2, padx=10, pady=5)

        self.lblDui = tk.Label(self, text='DUI:')
        self.lblDui.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblDui.grid(column=0, row=3, padx=10, pady=5)

        self.lblFechaNac = tk.Label(self, text='Fecha de Nacimiento:')
        self.lblFechaNac.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblFechaNac.grid(column=0, row=4, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad:')
        self.lblEdad.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblEdad.grid(column=0, row=5, padx=10, pady=5)

        self.lblAntecedentes = tk.Label(self, text='Antecedentes:')
        self.lblAntecedentes.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblAntecedentes.grid(column=0, row=6, padx=10, pady=5)

        self.lblCorreo = tk.Label(self, text='Correo Electronico:')
        self.lblCorreo.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblCorreo.grid(column=0, row=7, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Nº Telefono:')
        self.lblTelefono.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0, row=8, padx=10, pady=5)

        # Diseño de las entradas de texto (Entry)

        self.svNombre = tk.StringVar()
        self.txtNombre = tk.Entry(self, textvariable=self.svNombre)
        self.txtNombre.config(width=50, font=('ARIAL', 15))
        self.txtNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApellidoPaterno = tk.StringVar()
        self.txtApellidoPaterno = tk.Entry(self, textvariable=self.svApellidoPaterno)
        self.txtApellidoPaterno.config(width=50, font=('Arial', 15))
        self.txtApellidoPaterno.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svApellidoMaterno = tk.StringVar()
        self.txtApellidoMaterno = tk.Entry(self, textvariable=self.svApellidoMaterno)
        self.txtApellidoMaterno.config(width=50, font=('Arial', 15))
        self.txtApellidoMaterno.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svDui = tk.StringVar()
        self.txtDui = tk.Entry(self, textvariable=self.svDui)
        self.txtDui.config(width=50, font=('Arial', 15))
        self.txtDui.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svFechaNacimiento = tk.StringVar()
        self.txtFechaNac = tk.Entry(self, textvariable=self.svFechaNacimiento)
        self.txtFechaNac.config(width=50, font=('Arial', 15))
        self.txtFechaNac.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.txtEdad = tk.Entry(self, textvariable=self.svEdad)
        self.txtEdad.config(width=50, font=('Arial', 15))
        self.txtEdad.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svAntecedentes = tk.StringVar()
        self.txtAntecedenetes = tk.Entry(self, textvariable=self.svAntecedentes)
        self.txtAntecedenetes.config(width=50, font=('Arial', 15))
        self.txtAntecedenetes.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.txtCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.txtCorreo.config(width=50, font=('Arial', 15))
        self.txtCorreo.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.txtTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.txtTelefono.config(width=50, font=('Arial', 15))
        self.txtTelefono.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        # Botones
        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#158645',
                             cursor='hand2', activebackground='#35BD6F')
        self.btnNuevo.grid(column=0, row=9, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000',
                               cursor='hand2', activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1, row=9, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#B00000',
                                cursor='hand2', activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=9, padx=10, pady=5)

        # BUSCAR PACIENTE YA SEA CON EL DUI O APELLIDO
        self.lblBuscarDUI = tk.Label(self, text='Buscar por DUI: ')
        self.lblBuscarDUI.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblBuscarDUI.grid(column=3, row=0, padx=10, pady=5)
        
        self.lblbuscarApellido = tk.Label(self, text='Buscar por Apellido: ')
        self.lblbuscarApellido.config(font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblbuscarApellido.grid(column=3, row=1, padx=10, pady=5)

        # Texbox del buscador
        self.svBuscarDui = tk.StringVar()
        self.txtBuscarDui = tk.Entry(self, textvariable=self.svBuscarDui)
        self.txtBuscarDui.config(width=15, font=('ARIAL', 15))
        self.txtBuscarDui.grid(column=4, row=0, padx=10, pady=5, columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.txtBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido) 
        self.txtBuscarApellido.config(width=10, font=('ARIAL', 15))
        self.txtBuscarApellido.grid(column=4, row=1, padx=10, pady=5, columnspan=2)

        # Boton de busqueda 
        self.btnBuscarCondicion = tk.Button(self, text='Buscar', command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=12, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#00396F',
                                cursor='hand2', activebackground='#5B8DBD')
        self.btnBuscarCondicion.grid(column=3, row=2, padx=10, pady=5, columnspan=1)

        # Boton de limpiar busqueda 
        self.btnLimpiar = tk.Button(self, text='Calendario', command=self.limpiarBuscador)
        self.btnLimpiar.config(width=12, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#120061',
                                cursor='hand2', activebackground='#7C6DC1')
        self.btnLimpiar.grid(column=4, row=2, padx=10, pady=5, columnspan=1)

        # Boton de Calendario
        self.btnCalendario = tk.Button(self, text='Calendario', command=self.vistaCalendario )
        self.btnCalendario.config(width=12, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#53005B',
                                cursor='hand2', activebackground='#C774CF')
        self.btnCalendario.grid(column=3, row=4, padx=10, pady=5, columnspan=1)

# Funcion de vista de calendario usando el boton 
    def vistaCalendario(self):
        # Creando la ventana secundaria del calendario
        self.calendario = Toplevel(self)
        self.calendario.title("FECHA DE NACIMIENTO")
        self.calendario.resizable(0, 0)
        self.calendario.config(bg='#CDD8FF')

        # Creando el calendario
        self.calendar = tc.Calendar(
            self.calendario,
            selectmode='day',
            year=1990,
            month=1,
            day=1,
            locale='es_US',
            background='#777777',
            foreground='#FFFFFF',
            headersbackground='#B6DDFE',
            cursor='hand2',
            date_pattern='dd-mm-Y'
        )
        self.calendar.grid(row=0, column=0, padx=20, pady=20)

        # Enlace directo al evento de clic sobre la fecha
        self.calendar.bind("<<CalendarSelected>>", self.seleccionar_fecha)

# Enviar fecha seleccionada desde la ventana de calendario al textbox de fecha de nacimiento
    def seleccionar_fecha(self, event):
        # Obtener fecha seleccionada
        fecha_str = self.calendar.get_date()
        self.svFechaNacimiento.set(fecha_str)

        # Calcular edad inmediatamente
        self.calcularEdad(fecha_str)

        # Cerrar la ventana del calendario
        self.calendario.destroy()

# Calculando la edad por medio de la fecha seleccionada
    def calcularEdad(self, fecha_str):
        try:
            fecha_nacimiento = datetime.strptime(fecha_str, "%d-%m-%Y").date()
            fecha_actual = date.today()
            edad = fecha_actual.year - fecha_nacimiento.year - (
                (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
            )
            self.svEdad.set(str(edad))
        except ValueError:
            self.svEdad.set("Error")

# Funcion para buscar al paciente por medio del Apellido Paterno o DUI
    def buscarCondicion(self):
        condiciones = []

        # Captura de valores y limpieza de espacios
        dui = self.svBuscarDui.get().strip()
        apellido = self.svBuscarApellido.get().strip()

        # Validación de campos vacíos
        if not dui and not apellido:
            messagebox.showwarning("Campos vacíos", "Por favor ingrese el DUI o el Apellido para realizar la búsqueda.")
            return  # Detiene la ejecución si no hay datos

        # Construcción de la condición WHERE
        if dui:
            condiciones.append(f"dui = '{dui}'")
        if apellido:
            condiciones.append(f"apellidoPaterno LIKE '{apellido}%'")

        where = "WHERE " + " AND ".join(condiciones) + " AND activo = 1"

        # Obtener resultados
        self.listarPersona = listarCondicion(where)

        # Validación de resultados vacíos
        if not self.listarPersona:
            messagebox.showinfo("Sin resultados", "No se encontró ningún paciente con los datos proporcionados.")
            
            # Limpia la tabla si se desea eliminar resultados anteriores
            if hasattr(self, 'tabla'):
                for item in self.tabla.get_children():
                    self.tabla.delete(item)
            return

        # Mostrar los resultados en la tabla
        self.tablaPaciente(where)

# Funcion para limpiar los textbox de busqueda 
    def limpiarBuscador(self):
        self.svBuscarDui.set('')
        self.svBuscarApellido.set('')

        # Mostrar los resultados en la tabla
        self.tablaPaciente()

# Funcion para guardar Paciente llamada de PacienteDAO
    def guardarPaciente(self):
        # Captura de datos desde la interfaz
        nombre = self.svNombre.get().strip()
        apellido_paterno = self.svApellidoPaterno.get().strip()
        apellido_materno = self.svApellidoMaterno.get().strip()
        dui = self.svDui.get().strip()
        fecha_nacimiento = self.svFechaNacimiento.get().strip()
        edad = self.svEdad.get().strip()
        antecedentes = self.svAntecedentes.get().strip()
        correo = self.svCorreo.get().strip()
        telefono = self.svTelefono.get().strip()

        # -------------------------------
        # Validaciones
        # -------------------------------

        if not nombre or not apellido_paterno or not apellido_materno:
            messagebox.showwarning("Validación", "Nombre y apellidos son obligatorios.")
            return

        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
            return

        if not re.match(r'^[0-9]{8}-[0-9]$', dui):
            messagebox.showerror("Error", "El formato del DUI debe ser ########-#.")
            return

        if not fecha_nacimiento:
            messagebox.showwarning("Validación", "La fecha de nacimiento es obligatoria.")
            return

        if not edad:
            messagebox.showwarning("Validación", "El campo de edad no puede estar vacío.")
            return

        if correo and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            messagebox.showerror("Error", "Correo electrónico inválido.")
            return

        if not re.match(r'^[267]{1}[0-9]{3}-?[0-9]{4}$', telefono):
            messagebox.showerror("Error", "Número de teléfono inválido. Debe tener 8 dígitos y puede incluir un guion (####-####), comenzando con 2, 6 o 7.")
            return

        # Creación del objeto y almacenamiento
        persona = Persona(
            nombre,
            apellido_paterno,
            apellido_materno,
            dui,
            fecha_nacimiento,
            edad,
            antecedentes,
            correo,
            telefono
        )

        if self.idPersona is None:
            guardarDatoPaciente(persona)
            messagebox.showinfo("Éxito", "Paciente guardado exitosamente.")
        else:
            editarDatoPaciente(persona, self.idPersona)
            messagebox.showinfo("Éxito", "Paciente actualizado exitosamente.")

        self.deshabilitar()
        self.tablaPaciente()

# Deabilita la los textbox y los botones
    def deshabilitar(self):
        self.idPersona = None
        self.svNombre.set('')
        self.svApellidoPaterno.set('')
        self.svApellidoMaterno.set('')
        self.svDui.set('')
        self.svFechaNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')

        self.txtNombre.config(state='disabled')
        self.txtApellidoPaterno.config(state='disabled')
        self.txtApellidoMaterno.config(state='disabled')
        self.txtDui.config(state='disabled')
        self.txtFechaNac.config(state='disabled')
        self.txtEdad.config(state='disabled')
        self.txtAntecedenetes.config(state='disabled')
        self.txtCorreo.config(state='disabled')
        self.txtTelefono.config(state='disabled')

        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnCalendario.config(state='disabled')

# Habilita los textbox y botones
    def habilitar(self):
        #self.idPersona = None
        self.svNombre.set('')
        self.svApellidoPaterno.set('')
        self.svApellidoMaterno.set('')
        self.svDui.set('')
        self.svFechaNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')

        self.txtNombre.config(state='normal')
        self.txtApellidoPaterno.config(state='normal')
        self.txtApellidoMaterno.config(state='normal')
        self.txtDui.config(state='normal')
        self.txtFechaNac.config(state='normal')
        self.txtEdad.config(state='normal')
        self.txtAntecedenetes.config(state='normal')
        self.txtCorreo.config(state='normal')
        self.txtTelefono.config(state='normal')

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')

# Diseño de la tabla para muestra de datos
    def tablaPaciente(self, where=""):
        # Obtener los datos
        self.listarPersona = listarCondicion(where) if where else listar()

        # Crear tabla si no existe
        if not hasattr(self, 'tabla'):
            self.tabla = ttk.Treeview(self, column=('Nombre', 'Ape Paterno', 'Ape Materno', 'Dui', 'Fecha Nacim', 'Edad', 'Antecedentes', 'Correo', 'Telefono'))
            self.tabla.grid(column=0, row=10, columnspan=10, sticky='nsew')
            self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
            self.scroll.grid(row=10, column=11, sticky='nse')
            self.tabla.configure(yscrollcommand=self.scroll.set)
            self.tabla.tag_configure('evenrow', background='#C5EAFE')
            self.tabla.heading('#0', text='ID')
            self.tabla.heading('#1', text='Nombre')
            self.tabla.heading('#2', text='AP. Paterno')
            self.tabla.heading('#3', text='AP. Materno')
            self.tabla.heading('#4', text='DUI')
            self.tabla.heading('#5', text='F. Nacimiento')
            self.tabla.heading('#6', text='Edad')
            self.tabla.heading('#7', text='Antecedentes')
            self.tabla.heading('#8', text='Correo')
            self.tabla.heading('#9', text='Telefono')
            self.tabla.column("#0", anchor=W, width=50)
            self.tabla.column("#1", anchor=W, width=110)
            self.tabla.column("#2", anchor=W, width=110)
            self.tabla.column("#3", anchor=W, width=110)
            self.tabla.column("#4", anchor=W, width=80)
            self.tabla.column("#5", anchor=W, width=90)
            self.tabla.column("#6", anchor=W, width=50)
            self.tabla.column("#7", anchor=W, width=150)
            self.tabla.column("#8", anchor=W, width=150)
            self.tabla.column("#9", anchor=W, width=85)

        # Eliminar todos los registros previos
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar nuevos registros
        for p in self.listarPersona:
            self.tabla.insert('', 'end', text=p[0], values=(p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]), tags=('evenrow'))

                
            self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
            self.btnEditarPaciente.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#1E0075', activebackground='#9379E0', cursor='hand2')
            self.btnEditarPaciente.grid(row=11, column=0, padx=10, pady=5)

            self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command=self.eliminarDatoPaciente)
            self.btnEliminarPaciente.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
            self.btnEliminarPaciente.grid(row=11, column=1, padx=10, pady=5)

            self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente', command=self.historialMedica)
            self.btnHistorialPaciente.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
            self.btnHistorialPaciente.grid(row=11, column=2, padx=10, pady=5)

            self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
            self.btnSalir.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')
            self.btnSalir.grid(row=11, column=4, padx=10, pady=5)


# Funcion para editar y seleccinar paciente de la tabla de muestra de datos llamado de PacienteDAO
    def editarPaciente(self):
        try:
            seleccion = self.tabla.selection()

            # Validación de selección
            if not seleccion:
                messagebox.showwarning('Advertencia', 'Por favor, seleccione un paciente para editar.')
                return

            # Obtener ID y datos del paciente seleccionado
            self.idPersona = self.tabla.item(seleccion)['text']
            self.nombrePaciente = self.tabla.item(seleccion)['values'][0]
            self.apellidoPaternoPaciente = self.tabla.item(seleccion)['values'][1]
            self.apellidoMaternoPaciente = self.tabla.item(seleccion)['values'][2]
            self.duiPaciente = self.tabla.item(seleccion)['values'][3]
            self.fechaNacimientoPaciente = self.tabla.item(seleccion)['values'][4]
            self.edadPaciente = self.tabla.item(seleccion)['values'][5]
            self.antecedentesPaciente = self.tabla.item(seleccion)['values'][6]
            self.correoPaciente = self.tabla.item(seleccion)['values'][7]
            self.telefonoPaciente = self.tabla.item(seleccion)['values'][8]

            self.habilitar()

            self.txtNombre.insert(0, self.nombrePaciente)
            self.txtApellidoPaterno.insert(0, self.apellidoPaternoPaciente)
            self.txtApellidoMaterno.insert(0, self.apellidoMaternoPaciente)
            self.txtDui.insert(0, self.duiPaciente)
            self.txtFechaNac.insert(0, self.fechaNacimientoPaciente)
            self.txtEdad.insert(0, self.edadPaciente)
            self.txtAntecedenetes.insert(0, self.antecedentesPaciente)
            self.txtCorreo.insert(0, self.correoPaciente)
            self.txtTelefono.insert(0, self.telefonoPaciente)

        except Exception as e:
            messagebox.showerror('Error', f'Error al editar el paciente: {e}')

# Funcion de eliminar datos de paciente llamado de PacienteDAO
    def eliminarDatoPaciente(self):
        try:
            seleccion = self.tabla.selection()

            # Validar si se ha seleccionado un registro
            if not seleccion:
                messagebox.showwarning('Advertencia', 'Por favor, seleccione un paciente para eliminar.')
                return

            # Obtener el ID del paciente desde el ítem seleccionado
            self.idPersona = self.tabla.item(seleccion[0])['text']

            # Confirmación de eliminación (opcional pero recomendable)
            confirmar = messagebox.askyesno('Confirmar', '¿Está seguro que desea eliminar este paciente?')
            if confirmar:
                eliminarPaciente(self.idPersona)
                self.tablaPaciente()  # Actualizar tabla
                self.idPersona = None
                messagebox.showinfo('Éxito', 'Paciente eliminado correctamente.')
        except Exception as e:
            messagebox.showerror('Error', f'Error al eliminar el paciente: {e}')

# Función de abrir la ventana del historial del paciente
    def historialMedica(self):
        try:
            # Reiniciar ID para evitar usar uno previo
            self.idPersona = None

            # Obtener la selección del paciente desde la tabla principal
            seleccion = self.tabla.selection()
            if seleccion:
                self.idPersona = self.tabla.item(seleccion)['text']
                self.idPersonaHistoria = self.idPersona
            else:
                messagebox.showwarning("Advertencia", "Debe seleccionar un paciente para ver su historial.")
                return

            # Validar que el ID del paciente sea numérico y positivo
            try:
                idPersona = int(self.idPersona)
                if idPersona <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "El ID del paciente no es válido.")
                return

            # Crear una nueva ventana para mostrar el historial médico
            self.topHistorialMedica = Toplevel()
            self.topHistorialMedica.title('HISTORIAL MÉDICO')
            self.topHistorialMedica.resizable(0, 0)
            self.topHistorialMedica.config(bg='#CDD8FF')

            # Obtener los datos del historial médico desde la base de datos
            self.listarHistorial = listarHistorial(idPersona)

            # Crear el Treeview para mostrar los datos
            self.tablaHistorial = ttk.Treeview(
                self.topHistorialMedica,
                columns=('Apellido', 'Fecha Historia', 'Motivo', 'Examen Auxiliar', 'Tratamiento', 'Detalle')
            )
            self.tablaHistorial.grid(column=0, row=0, columnspan=7, sticky='nse')

            # Scrollbar vertical
            self.scrollHistoria = ttk.Scrollbar(
                self.topHistorialMedica,
                orient='vertical',
                command=self.tablaHistorial.yview
            )
            self.scrollHistoria.grid(row=0, column=8, sticky='nse')
            self.tablaHistorial.configure(yscrollcommand=self.scrollHistoria.set)

            # Configurar encabezados
            self.tablaHistorial.heading('#0', text='ID')
            self.tablaHistorial.heading('#1', text='Apellidos')
            self.tablaHistorial.heading('#2', text='Fecha y Hora')
            self.tablaHistorial.heading('#3', text='Motivo')
            self.tablaHistorial.heading('#4', text='Examen Auxiliar')
            self.tablaHistorial.heading('#5', text='Tratamiento')
            self.tablaHistorial.heading('#6', text='Detalle')

            # Configurar columnas
            self.tablaHistorial.column('#0', anchor=W, width=50)
            self.tablaHistorial.column('#1', anchor=W, width=100)
            self.tablaHistorial.column('#2', anchor=W, width=100)
            self.tablaHistorial.column('#3', anchor=W, width=120)
            self.tablaHistorial.column('#4', anchor=W, width=250)
            self.tablaHistorial.column('#5', anchor=W, width=200)
            self.tablaHistorial.column('#6', anchor=W, width=200)

            # Limpiar cualquier fila previa en el Treeview
            for item in self.tablaHistorial.get_children():
                self.tablaHistorial.delete(item)

            # Insertar los datos del historial en el Treeview
            for p in self.listarHistorial:
                self.tablaHistorial.insert('', 'end', text=p[0], values=(p[1], p[2], p[3], p[4], p[5], p[6]))

            # Botón: Agregar Historial
            self.btnGuardarHistorial = tk.Button(
                self.topHistorialMedica,
                text='Agregar Historial',
                command=self.topAgregarHistoria
            )
            self.btnGuardarHistorial.config(
                width=20, font=('ARIAL', 12, 'bold'),
                fg='#DAD5D6', bg='#002771',
                cursor='hand2', activebackground='#7198E0'
            )
            self.btnGuardarHistorial.grid(row=2, column=0, padx=10, pady=5)

            # Botón: Editar Historial
            self.btnEditarHistorial = tk.Button(
                self.topHistorialMedica,
                text='Editar Historial',
                command=self.editarHistorial
            )
            self.btnEditarHistorial.config(
                width=20, font=('ARIAL', 12, 'bold'),
                fg='#DAD5D6', bg='#3A005D',
                cursor='hand2', activebackground='#B47CD6'
            )
            self.btnEditarHistorial.grid(row=2, column=1, padx=10, pady=5)

            # Botón: Eliminar Historial
            self.btnEliminarHistorial = tk.Button(
                self.topHistorialMedica,
                text='Eliminar Historial',
                command=self.eliminarHistorialMedico
            )
            self.btnEliminarHistorial.config(
                width=20, font=('ARIAL', 12, 'bold'),
                fg='#DAD5D6', bg='#890011',
                cursor='hand2', activebackground='#DB939C'
            )
            self.btnEliminarHistorial.grid(row=2, column=2, padx=10, pady=5)

            # Botón: Salir del Historial
            self.btnSalirHistorial = tk.Button(
                self.topHistorialMedica,
                text='Salir del Historial',
                command=self.salirTop
            )
            self.btnSalirHistorial.config(
                width=20, font=('ARIAL', 12, 'bold'),
                fg='#DAD5D6', bg='#000000',
                cursor='hand2', activebackground='#6F6F6F'
            )
            self.btnSalirHistorial.grid(row=2, column=3, padx=10, pady=5)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")


# Función para cerrar la ventana del historial
    def salirTop(self):
        self.topHistorialMedica.destroy()

# Funcion para agregar un nuevo historial al paciente 
    def topAgregarHistoria(self):
        self.topAHistoria = Toplevel()
        self.topAHistoria.title('AGREGAR HISTORIAL')
        self.topAHistoria.resizable(0, 0)
        self.topAHistoria.config(bg='#CDD8FF')

        self.frameDatosHistorial = tk.LabelFrame(self.topAHistoria, text='Datos del Historial', font=('ARIAL', 14, 'bold'), bg='#CDD8FF')
        self.frameDatosHistorial.pack(fill="both", expand="yes", pady=20, padx=20)

        self.lblMotivoHistoria = tk.Label(self.frameDatosHistorial, text='Motivo de la Historia:', font=('ARIAL', 13, 'bold'), bg='#CDD8FF')
        self.lblMotivoHistoria.grid(row=0, column=0, padx=10, pady=8, sticky="e")

        self.lblExamenAuxiliar = tk.Label(self.frameDatosHistorial, text='Examen Auxiliar:', font=('ARIAL', 13, 'bold'), bg='#CDD8FF')
        self.lblExamenAuxiliar.grid(row=1, column=0, padx=10, pady=8, sticky="e")

        self.lblTratamiento = tk.Label(self.frameDatosHistorial, text='Tratamiento:', font=('ARIAL', 13, 'bold'), bg='#CDD8FF')
        self.lblTratamiento.grid(row=2, column=0, padx=10, pady=8, sticky="e")

        self.lblDetalleHistoria = tk.Label(self.frameDatosHistorial, text='Detalle del Historial:', font=('ARIAL', 13, 'bold'), bg='#CDD8FF')
        self.lblDetalleHistoria.grid(row=3, column=0, padx=10, pady=8, sticky="ne")

        self.svMotivoHistorial = tk.StringVar()
        self.entryMotivoHistoria = tk.Entry(self.frameDatosHistorial, textvariable=self.svMotivoHistorial, font=('ARIAL', 13), width=40)
        self.entryMotivoHistoria.grid(row=0, column=1, padx=10, pady=8)

        self.svExamenAuxiliar = tk.StringVar()
        self.entryExamenAuxiliar = tk.Entry(self.frameDatosHistorial, textvariable=self.svExamenAuxiliar, font=('ARIAL', 13), width=40)
        self.entryExamenAuxiliar.grid(row=1, column=1, padx=10, pady=8)

        self.svTratamiento = tk.StringVar()
        self.entryTratamiento = tk.Entry(self.frameDatosHistorial, textvariable=self.svTratamiento, font=('ARIAL', 13), width=40)
        self.entryTratamiento.grid(row=2, column=1, padx=10, pady=8)

        self.entryDetalleHistoria = tk.Text(self.frameDatosHistorial, font=('ARIAL', 13), width=38, height=5)
        self.entryDetalleHistoria.grid(row=3, column=1, padx=10, pady=8)

        # Frame para fecha
        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria, bg='#CDD8FF')
        self.frameFechaHistoria.pack(fill="both", expand="yes", padx=20, pady=10)

        self.lblFechaHistoria  = tk.Label(self.frameFechaHistoria, text='Fecha y Hora', width=20, font=('ARIAL', 12), bg='#CDD8FF')
        self.lblFechaHistoria.grid(row=0, column=0, padx=5, pady=3)

        self.svFechaHistoria = tk.StringVar()
        self.entryFechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria)
        self.entryFechaHistoria.config(width=25, font=('ARIAL', 15))
        self.entryFechaHistoria.grid(row=0, column=1, padx=5, pady=3)

        self.svFechaHistoria.set(datetime.today().strftime('%d-%m-%y %H:%M'))

        self.btnAgregarHistoria = tk.Button(self.frameDatosHistorial, text='Agregar Historial', command=self.agregarHistorialMedico)
        self.btnAgregarHistoria.config(font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2', activebackground='#4E56C6')
        self.btnAgregarHistoria.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.btnSalirHistoria = tk.Button(self.frameDatosHistorial, text='Salir', command=self.topAHistoria.destroy)
        self.btnSalirHistoria.config(font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#646464')
        self.btnSalirHistoria.grid(row=4, column=1, padx=10, pady=5, sticky="w")


# Funcion para agregar una historial a la base de datos
    def agregarHistorialMedico(self):
        try:
            # Obtener y limpiar los datos ingresados
            fecha = self.svFechaHistoria.get().strip()
            motivo = self.svMotivoHistorial.get().strip()
            examen_auxiliar = self.svExamenAuxiliar.get().strip()
            tratamiento = self.svTratamiento.get().strip()
            detalle_historia = self.entryDetalleHistoria.get("1.0", "end-1c").strip()

            # Validar que todos los campos estén completos
            if not all([fecha, motivo, examen_auxiliar, tratamiento, detalle_historia]):
                messagebox.showwarning(
                    "Campos incompletos",
                    "Todos los campos son requeridos. Por favor, complete todos los campos antes de continuar."
                )
                return  # Detener ejecución si hay campos vacíos

            # Guardar historial si aún no existe
            if self.idHistoriaMedica is None:
                guardarHistorial(
                    self.idPersonaHistoria,
                    fecha,
                    motivo,
                    examen_auxiliar,
                    tratamiento,
                    detalle_historia
                )

            # Cerrar ventanas después de guardar
            self.topAHistoria.destroy()
            self.topHistorialMedica.destroy()

        except Exception as e:
            messagebox.showerror("Error inesperado", f"Ocurrió un error al guardar el historial médico: {e}")
    
    # Funcion de eliminar datos de un historial
    def eliminarHistorialMedico(self):
        try:
            seleccion = self.tablaHistorial.selection()  

            if not seleccion:
                messagebox.showwarning('Advertencia', 'Por favor, seleccione un historial para eliminar.')
                return

            self.idHistoriaMedica = self.tablaHistorial.item(seleccion[0])['text']  # Obtener ID del historial

            confirmar = messagebox.askyesno('Confirmar', '¿Está seguro que desea eliminar este Historial?')
            if confirmar:
                eliminarHistorial(self.idHistoriaMedica)  # Llamada a DAO
                self.idHistoriaMedica = None
                messagebox.showinfo('Éxito', 'Historial eliminado correctamente.')
        except Exception as e:
            messagebox.showerror('Error', f'Error al eliminar el Historial: {e}')

# Funcion de editar los datos de un historial
    def editarHistorial(self):
        try:
            seleccion = self.tablaHistorial.selection()

            if not seleccion:
                messagebox.showwarning('Advertencia', 'Por favor, seleccione un historial para editar.')
                return

            # Obtener datos seleccionados
            self.idHistoriaMedica = self.tablaHistorial.item(seleccion)['text']
            fecha = self.tablaHistorial.item(seleccion)['values'][1]
            motivo = self.tablaHistorial.item(seleccion)['values'][2]
            examen = self.tablaHistorial.item(seleccion)['values'][3]
            tratamiento = self.tablaHistorial.item(seleccion)['values'][4]
            detalle = self.tablaHistorial.item(seleccion)['values'][5]

            self.topEditarHistorial = Toplevel()
            self.topEditarHistorial.title('EDITAR HISTORIAL')
            self.topEditarHistorial.resizable(0, 0)
            self.topEditarHistorial.config(bg='#CDD8FF')

            # FRAME DE DATOS
            self.frameEditarHistorial = tk.LabelFrame(self.topEditarHistorial, text='Editar Datos del Historial',
                                                    font=('ARIAL', 14, 'bold'), bg='#CDD8FF')
            self.frameEditarHistorial.pack(fill="both", expand="yes", pady=20, padx=20)

            # MOTIVO
            tk.Label(self.frameEditarHistorial, text='Motivo de la Historia:', font=('ARIAL', 13, 'bold'), bg='#CDD8FF')\
                .grid(row=0, column=0, padx=10, pady=8, sticky="e")
            self.varMotivoEditar = tk.StringVar(value=motivo)
            tk.Entry(self.frameEditarHistorial, textvariable=self.varMotivoEditar, font=('ARIAL', 13), width=40)\
                .grid(row=0, column=1, padx=10, pady=8)

            # EXAMEN AUXILIAR
            tk.Label(self.frameEditarHistorial, text='Examen Auxiliar:', font=('ARIAL', 13, 'bold'), bg='#CDD8FF')\
                .grid(row=1, column=0, padx=10, pady=8, sticky="e")
            self.varExamenEditar = tk.StringVar(value=examen)
            tk.Entry(self.frameEditarHistorial, textvariable=self.varExamenEditar, font=('ARIAL', 13), width=40)\
                .grid(row=1, column=1, padx=10, pady=8)

            # TRATAMIENTO
            tk.Label(self.frameEditarHistorial, text='Tratamiento:', font=('ARIAL', 13, 'bold'), bg='#CDD8FF')\
                .grid(row=2, column=0, padx=10, pady=8, sticky="e")
            self.varTratamientoEditar = tk.StringVar(value=tratamiento)
            tk.Entry(self.frameEditarHistorial, textvariable=self.varTratamientoEditar, font=('ARIAL', 13), width=40)\
                .grid(row=2, column=1, padx=10, pady=8)

            # DETALLE
            tk.Label(self.frameEditarHistorial, text='Detalle del Historial:', font=('ARIAL', 13, 'bold'), bg='#CDD8FF')\
                .grid(row=3, column=0, padx=10, pady=8, sticky="ne")
            self.txtDetalleEditar = tk.Text(self.frameEditarHistorial, font=('ARIAL', 13), width=38, height=5)
            self.txtDetalleEditar.grid(row=3, column=1, padx=10, pady=8)
            self.txtDetalleEditar.insert('1.0', detalle)

            # FECHA
            self.frameFechaEditar = tk.LabelFrame(self.topEditarHistorial, bg='#CDD8FF')
            self.frameFechaEditar.pack(fill="both", expand="yes", padx=20, pady=10)

            tk.Label(self.frameFechaEditar, text='Fecha y Hora:', font=('ARIAL', 12), bg='#CDD8FF')\
                .grid(row=0, column=0, padx=5, pady=3)
            self.varFechaEditar = tk.StringVar(value=fecha)
            tk.Entry(self.frameFechaEditar, textvariable=self.varFechaEditar, font=('ARIAL', 15), width=25)\
                .grid(row=0, column=1, padx=5, pady=3)

            # BOTONES
            tk.Button(self.frameEditarHistorial, text='Guardar Cambios',
                    font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2', activebackground='#4E56C6')\
                .grid(row=4, column=0, padx=10, pady=5, sticky="e")

            tk.Button(self.frameEditarHistorial, text='Salir', command=self.topEditarHistorial.destroy,
                    font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#646464')\
                .grid(row=4, column=1, padx=10, pady=5, sticky="w")

        except Exception as e:
            messagebox.showerror('Error', f'Error al editar la Historia: {e}')
