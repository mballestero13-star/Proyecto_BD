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
+--------------------+       |
|      Préstamo      |-------+
+--------------------+
| PK PrestamoID      |
| FK UsuarioID       |
| FK RecursoID       |
| FechaPrestamo      |
| FechaDevolucion    |
| Estado             |
+--------------------+
                             |
                             | FK
                             |
                    +--------------------+
                    |      Recurso       |
                    +--------------------+
                    | PK RecursoID       |
                    | Título             |
                    | Tipo               |
                    +--------------------+

                    +--------------------+
                    |      Reserva       |
                    +--------------------+
                    | PK ReservaID       |
                    | FK UsuarioID       |
                    | FK RecursoID       |
                    | FechaReserva       |
                    | Estado             |
                    +--------------------+
