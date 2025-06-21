from .conexion import ConexionBD
from tkinter import messagebox

# Metodo para listar el historial de los pacientes registrados
def listarHistorial(idPersona):
    conexion = ConexionBD()
    listaHistoria = []

    sql = ('SELECT h.idHistorialMedica, '
           'p.apellidoPaterno || " " || p.apellidoMaterno AS Apellidos, '
           'h.fechaHistorial, h.motivo, h.examenAuxiliar, '
           'h.tratamiento, h.detalle '
           'FROM historialMedica h '
           'INNER JOIN Persona p ON p.idPersona = h.idPersona '
           'WHERE p.idPersona = ?')

    try:
        conexion.cursor.execute(sql, (idPersona,))
        listaHistoria = conexion.cursor.fetchall()
    except Exception as e:
        messagebox.showerror('Error', f'Error al Listar el Historial Médico: {e}')
    finally:
        conexion.cerrarConexion()

    return listaHistoria

# Metodo para guardar el historial de un paciente
def guardarHistorial(idPersona, fechaHistoria, motivo, examenAuxiar, tratamiento, detalle):
    conexion = ConexionBD()
    sql = f"""INSERT INTO historialMedica (idPersona, fechaHistorial, motivo, examenAuxiliar, tratamiento, detalle) VALUES
          ({idPersona}, '{fechaHistoria}', '{motivo}', '{examenAuxiar}', '{tratamiento}', '{detalle}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        messagebox.showinfo('Registrar Historial', 'Historial Médico Registrado con Éxito')
    except Exception as e:
        messagebox.showerror('Error', f'Error al Registrar el Historial Médico: {e}')

# Metodo para eliminar el registro de un historial de paciente
def eliminarHistorial(idHistorialMedica):
    conexion = ConexionBD()
    sql = f'DELETE FROM historialMedica WHERE idHistorialMedica = {idHistorialMedica}'

    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()
    except Exception as e:
        messagebox.showerror('Error', f'Error al Eliminar el Historial Médico: {e}')
    finally:
        conexion.cerrarConexion()

# Metodo para editar la informacion de un historial de pacientes 
def editarHistorial(fechaHistorial, motivo, examenAuxiliar, tratamiento, detalle, idHistorialMedica):
    conexion = ConexionBD()
    sql_editar = f"""UPDATE historialMedica 
    SET 
        fechaHistorial = '{fechaHistorial}', 
        motivo = '{motivo}', 
        examenAuxiliar = '{examenAuxiliar}', 
        tratamiento = '{tratamiento}', 
        detalle = '{detalle}'
    WHERE 
        idHistorialMedica = '{idHistorialMedica}'"""
    try:
        conexion.cursor.execute(sql_editar)
        conexion.conexion.commit()
    except Exception as e:
        messagebox.showerror('Error', f'Error al Modificar el Historial: {e}')
    finally:
        conexion.cerrarConexion()


# Clase que representa el registro de una historia médica de un paciente
class historiaMedica:
    def __init__(self, idPersona, fechaHistorial, motivo, examenAuxiliar, tratamiento, detalle):
        self.idHitorialMedica = None  
        self.idPersona = idPersona 
        self.fechaHistorial = fechaHistorial  
        self.motivo = motivo 
        self.examenAuxiliar = examenAuxiliar  
        self.tratamiento = tratamiento  
        self.detalle = detalle  


    def __str__(self):
        return f'historialMedica[{self.idPersona}, {self.fechaHistorial}, {self.motivo}, {self.examenAuxiliar}, {self.tratamiento}, {self.detalle}]'