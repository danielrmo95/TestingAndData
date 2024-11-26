CREATE TABLE EntidadesEducativas (
    entidad_id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL UNIQUE,
    contrasena NVARCHAR(255) NOT NULL,
    nombre_representante NVARCHAR(100) NOT NULL,
    telefono_representante NVARCHAR(15),
    fecha_registro DATETIME DEFAULT GETDATE()
);
GO

CREATE TABLE Cursos (
    curso_id INT IDENTITY(1,1) PRIMARY KEY,
    nombre_curso NVARCHAR(150) NOT NULL,
    descripcion NVARCHAR(MAX),
    instructor NVARCHAR(100),
    entidad_id INT,  -- Llave foránea que hace referencia a EntidadesEducativas
    CONSTRAINT FK_Cursos_Entidad FOREIGN KEY (entidad_id) REFERENCES EntidadesEducativas(entidad_id)
);
GO

CREATE TABLE Comentarios (
    comentario_id INT IDENTITY(1,1) PRIMARY KEY,
    entidad_id INT NOT NULL,
    curso_id INT NOT NULL,
    calificacion INT CHECK (calificacion BETWEEN 1 AND 5),
    comentario NVARCHAR(MAX),
    fecha_comentario DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (usuario_id) REFERENCES EntidadesEducativas(entidad_id) ON DELETE CASCADE,
    FOREIGN KEY (curso_id) REFERENCES Cursos(curso_id) ON DELETE CASCADE
);
GO