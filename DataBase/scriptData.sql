-- Crear la base de datos
CREATE DATABASE prueba_tecnica;

-- Usar la base de datos recién creada
USE prueba_tecnica;

-- Crear la tabla categoria
CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT
);

-- Insertar datos en la tabla categoria
INSERT INTO categoria (nombre, descripcion) 
VALUES
    ('En progreso', 'Tareas que están en proceso de ejecución.'),
    ('Incompleta', 'Tareas que no se han terminado.'),
    ('Fuera de tiempo', 'Tareas que han pasado su fecha de vencimiento.'),
    ('Completada', 'Tareas que han sido terminadas correctamente.');

-- Crear la tabla persona
CREATE TABLE persona (
    id_persona INT AUTO_INCREMENT PRIMARY KEY,
    cedula VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100)
);

-- Insertar datos en la tabla persona
INSERT INTO persona (cedula, nombre, apellido) 
VALUES
    ('123456789', 'Juan', 'Pérez'),
    ('987654321', 'Ana', 'Gómez'),
    ('112233445', 'Carlos', 'López'),
    ('556677889', 'Laura', 'Martínez'),
    ('667788990', 'Sofía', 'Torres'),
    ('445566778', 'Diego', 'Ramírez');

-- Crear la tabla tareas
CREATE TABLE tareas (
    id_tarea INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_vencimiento DATE,
    id_categoria INT, 
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Insertar datos en la tabla tareas
INSERT INTO tareas (titulo, descripcion, fecha_vencimiento, id_categoria) 
VALUES
    ('Tarea 1', 'Descripción de la tarea 1', '2024-11-30', 1), -- En progreso
    ('Tarea 2', 'Descripción de la tarea 2', '2024-11-25', 2), -- Incompleta
    ('Tarea 3', 'Descripción de la tarea 3', '2024-11-15', 3), -- Fuera de tiempo
    ('Tarea 4', 'Descripción de la tarea 4', '2024-11-10', 4), -- Completada
    ('Tarea 5', 'Descripción de la tarea 5', '2024-12-01', 1), -- En progreso
    ('Tarea 6', 'Descripción de la tarea 6', '2024-11-28', 2); -- Incompleta

-- Crear la tabla tarea_programada
CREATE TABLE tarea_programada (
    id_tarea_p INT AUTO_INCREMENT PRIMARY KEY,
    id_persona INT, 
    id_tarea INT,
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_tarea) REFERENCES tareas(id_tarea)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Insertar datos en la tabla tarea_programada
INSERT INTO tarea_programada (id_persona, id_tarea) 
VALUES
    (1, 1), -- Juan Pérez con Tarea 1
    (2, 2), -- Ana Gómez con Tarea 2
    (3, 3), -- Carlos López con Tarea 3
    (4, 4), -- Laura Martínez con Tarea 4
    (5, 5), -- Sofía Torres con Tarea 5
    (6, 6); -- Diego Ramírez con Tarea 6
