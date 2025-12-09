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

Préstamo es la tabla central (fact table).

Usuario y Recurso son dimensiones, conectadas mediante claves foráneas (FK).

Reserva también podría considerarse una tabla de hechos adicional, vinculando las mismas dimensiones.