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

-- Crear la tabla persona
CREATE TABLE persona (
    id_persona INT AUTO_INCREMENT PRIMARY KEY,
    cedula VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100)
);

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
