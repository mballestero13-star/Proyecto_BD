# Pruebas y Verificación de la Base de Datos `databaseLeccion5.db`

Este archivo proporciona algunas consultas y pruebas para verificar la integridad, estructura y funcionamiento de la base de datos creada.

---

## 1. Verificar la existencia de las tablas

```sql
-- Listar todas las tablas en la base de datos
SELECT name FROM sqlite_master WHERE type='table';

-- Describir la estructura de la tabla Usuario
PRAGMA table_info(Usuario);

-- Describir la estructura de la tabla Recurso
PRAGMA table_info(Recurso);

-- Describir la estructura de la tabla Prestamo
PRAGMA table_info(Prestamo);

-- Describir la estructura de la tabla Reserva
PRAGMA table_info(Reserva);

-- Mostrar todos los registros de Usuario
SELECT * FROM Usuario;

-- Mostrar todos los registros de Recurso
SELECT * FROM Recurso;

-- Mostrar todos los registros de Prestamo
SELECT * FROM Prestamo;

-- Mostrar todos los registros de Reserva
SELECT * FROM Reserva;

-- Consultar préstamos con usuarios y recursos asociados
SELECT p.PrestamoID, u.Nombre AS Usuario, r.Titulo AS Recurso, p.FechaPrestamo, p.Estado
FROM Prestamo p
JOIN Usuario u ON p.UsuarioID = u.UsuarioID
JOIN Recurso r ON p.RecursoID = r.RecursoID;

-- Consultar reservas con usuarios y recursos asociados
SELECT res.ReservaID, u.Nombre AS Usuario, r.Titulo AS Recurso, res.FechaReserva, res.Estado
FROM Reserva res
JOIN Usuario u ON res.UsuarioID = u.UsuarioID
JOIN Recurso r ON res.RecursoID = r.RecursoID;