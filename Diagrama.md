+--------------------+            +--------------------+           +--------------------+
|      Usuario       |            |      Recurso       |           |      Préstamo      |
+--------------------+            +--------------------+           +--------------------+
| PK UsuarioID       |            | PK RecursoID       |           | PK PrestamoID      |
| Nombre             |            | Título             |           | FK UsuarioID       |
| TipoUsuario        |            | Tipo               |           | FK RecursoID       |
+--------------------+            +--------------------+           | FechaPrestamo      |
                                                                  | FechaDevolucion    |
                                                                  | Estado             |
                                                                  +--------------------+
                                                                          |
                                                                          | N
                                                                          |
                                                                          | 1
                                                                  +--------------------+
                                                                  |      Reserva       |
                                                                  +--------------------+
                                                                  | PK ReservaID       |
                                                                  | FK UsuarioID       |
                                                                  | FK RecursoID       |
                                                                  | FechaReserva       |
                                                                  | Estado             |
                                                                  +--------------------+
