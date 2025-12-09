# Diagrama ER - Biblioteca Universitaria

```text
+--------------------+
|      Usuario       |
+--------------------+
| PK UsuarioID       |
| Nombre             |
| TipoUsuario        |
+--------------------+
         |
         | FK
         |
+--------------------+       +--------------------+       +--------------------+
|      Préstamo      |-------|      Recurso       |
+--------------------+       +--------------------+
| PK PrestamoID      |       | PK RecursoID       |
| FK UsuarioID       |       | Título             |
| FK RecursoID       |       | Tipo               |
| FechaPrestamo      |       +--------------------+
| FechaDevolucion    |
| Estado             |
+--------------------+
         |
         | FK
         |
+--------------------+
|      Reserva       |
+--------------------+
| PK ReservaID       |
| FK UsuarioID       |
| FK RecursoID       |
| FechaReserva       |
| Estado             |
+--------------------+
