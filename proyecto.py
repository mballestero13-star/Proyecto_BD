import sqlite3

# Conexión a SQLite (se crea el archivo si no existe)
conn = sqlite3.connect("databaseLeccion5.db")
cursor = conn.cursor()

sql_script = """
-- Crear tabla Usuario
CREATE TABLE IF NOT EXISTS Usuario (
    UsuarioID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    TipoUsuario TEXT NOT NULL
);

-- Crear tabla Recurso
CREATE TABLE IF NOT EXISTS Recurso (
    RecursoID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    Tipo TEXT NOT NULL
);

-- Crear tabla Prestamo
CREATE TABLE IF NOT EXISTS Prestamo (
    PrestamoID INTEGER PRIMARY KEY AUTOINCREMENT,
    UsuarioID INTEGER NOT NULL,
    RecursoID INTEGER NOT NULL,
    FechaPrestamo TEXT NOT NULL,
    FechaDevolucion TEXT,
    Estado TEXT NOT NULL,
    FOREIGN KEY (UsuarioID) REFERENCES Usuario(UsuarioID),
    FOREIGN KEY (RecursoID) REFERENCES Recurso(RecursoID)
);

-- Crear tabla Reserva
CREATE TABLE IF NOT EXISTS Reserva (
    ReservaID INTEGER PRIMARY KEY AUTOINCREMENT,
    UsuarioID INTEGER NOT NULL,
    RecursoID INTEGER NOT NULL,
    FechaReserva TEXT NOT NULL,
    Estado TEXT NOT NULL,
    FOREIGN KEY (UsuarioID) REFERENCES Usuario(UsuarioID),
    FOREIGN KEY (RecursoID) REFERENCES Recurso(RecursoID)
);

-- Inserciones de ejemplo en Usuario
INSERT INTO Usuario (Nombre, TipoUsuario) VALUES ('Juan Perez', 'Estudiante');
INSERT INTO Usuario (Nombre, TipoUsuario) VALUES ('Maria Lopez', 'Profesor');

-- Inserciones de ejemplo en Recurso
INSERT INTO Recurso (Titulo, Tipo) VALUES ('Libro de Matemáticas', 'Libro');
INSERT INTO Recurso (Titulo, Tipo) VALUES ('Revista Científica', 'Revista');

-- Inserciones de ejemplo en Prestamo
INSERT INTO Prestamo (UsuarioID, RecursoID, FechaPrestamo, FechaDevolucion, Estado)
VALUES (1, 1, '2024-04-25', '2024-05-05', 'Prestado');

-- Inserciones de ejemplo en Reserva
INSERT INTO Reserva (UsuarioID, RecursoID, FechaReserva, Estado)
VALUES (2, 2, '2024-04-20', 'Activa');
"""

# Ejecutar el script completo
cursor.executescript(sql_script)

conn.commit()
conn.close()

print("✅ Base de datos creada con éxito: databaseLeccion5.db")