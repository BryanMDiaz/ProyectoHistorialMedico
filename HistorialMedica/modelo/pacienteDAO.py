from .conexion import ConexionBD
from tkinter import messagebox

# Metodo para registrar un Paciente en la BD
def guardarDatoPaciente(persona):
    conexion = ConexionBD()
    
    # Verificar si el DUI ya existe en la base de datos
    sql_verificar = f"SELECT COUNT(*) FROM Persona WHERE dui = '{persona.dui}'"
    conexion.cursor.execute(sql_verificar)
    resultado = conexion.cursor.fetchone()

    if resultado[0] > 0:
        messagebox.showerror('Error', 'El paciente ya está registrado con este número de DUI')
        conexion.cerrarConexion()
        return
    
    # Si el DUI no existe, proceder con la inserción
    sql_insertar = f"""INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno, dui, fechaNacimiento, edad, antecedentes, correo, telefono, activo) VALUES 
            ('{persona.nombre}', '{persona.apellidoPaterno}', '{persona.apellidoMaterno}', '{persona.dui}', '{persona.fechaNacimiento}', '{persona.edad}', '{persona.antecedentes}', '{persona.correo}', '{persona.telefono}', 1)"""
    try:
        conexion.cursor.execute(sql_insertar)
        conexion.cerrarConexion()
        messagebox.showinfo('Registrar Paciente', 'Paciente Registrado con Éxito')
    except Exception as e:
        messagebox.showerror('Error', f'Error al Registrar el Paciente: {e}')

# Metodo para editar los datos del paciente
def editarDatoPaciente(persona, idPersona):
    conexion = ConexionBD()
    sql_editar = f"""UPDATE Persona 
    SET 
        nombre = '{persona.nombre}', 
        apellidoPaterno = '{persona.apellidoPaterno}', 
        apellidoMaterno = '{persona.apellidoMaterno}', 
        fechaNacimiento = '{persona.fechaNacimiento}', 
        edad = '{persona.edad}', 
        antecedentes = '{persona.antecedentes}', 
        correo = '{persona.correo}', 
        telefono = '{persona.telefono}', 
        activo = 1 
    WHERE 
        dui = '{persona.dui}'"""
    try:
        conexion.cursor.execute(sql_editar)
        conexion.cerrarConexion()
        messagebox.showinfo('Modificar Paciente', 'Paciente Modificado con Éxito')
    except Exception as e:
        messagebox.showerror('Error', f'Error al Modificar el Paciente: {e}')


# Método para listar todos los pacientes registrados en la BD
def listar():
    conexion = ConexionBD()
    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
    except Exception as e:
        messagebox.showerror('Error', f'Error al listar Pacientes: {e}')
    finally:
        conexion.cerrarConexion()
    return listaPersona

# Método para listar con condición personalizada
def listarCondicion(where):
    conexion = ConexionBD()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
    except Exception as e:
        messagebox.showerror('Error', f'Error al listar Pacientes: {e}')
    finally:
        conexion.cerrarConexion()
    return listaPersona

# Metodo para eliminar el paciente 
def eliminarPaciente(idPersona):
    conexion = ConexionBD()
    sql = f"UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"
    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  
        messagebox.showinfo('Eliminar', 'Paciente Eliminado con Éxito')
    except Exception as e:
        messagebox.showwarning('Error', f'Error al Eliminar el Paciente: {e}')
    finally:
        conexion.cerrarConexion()



class Persona: 
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, dui, fechaNacimiento, edad, antecedentes, correo, telefono):
        self.idPersona = None
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.dui = dui
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.correo = correo
        self.telefono = telefono


    def __str__(self):
        return f'Persona[{self.nombre}, {self.apellidoPaterno}, {self.apellidoMaterno},{self.dui}, {self.fechaNacimiento}, {self.edad}, {self.antecedentes}, {self.correo}, {self.telefono}]'