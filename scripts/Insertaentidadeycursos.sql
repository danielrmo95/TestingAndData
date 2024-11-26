-- Insertar datos de prueba en EntidadesEducativas
INSERT INTO dbo.EntidadesEducativas(nombre, email, contrasena, nombre_representante, telefono_representante, fecha_registro)
VALUES 
    ('Instituto de Tecnología de Medellín', 'contacto@itm.edu.co', 'pass123', 'Carlos Pérez', '3101234567', GETDATE()),
    ('Academia Colombiana de Software', 'info@academiasoftware.com', 'pass456', 'Ana Ramírez', '3157654321', GETDATE()),
    ('Bootcamp Digital Bogotá', 'contacto@bootcampdigital.co', 'pass789', 'Juan González', '3201112233', GETDATE()),
    ('Centro de Idiomas Avanzados', 'info@idiomasavanzados.com', 'pass321', 'María García', '3123344556', GETDATE()),
    ('Diplomados IT Cali', 'contacto@diplomadosit.co', 'pass654', 'Santiago Martínez', '3145566778', GETDATE()),
    ('Smart', 'info@smart.com.co', 'smartpass', 'Lucía Fernández', '3209876543', GETDATE());
go
-- Insertar datos de prueba en Cursos
INSERT INTO dbo.Cursos 
    (nombre_curso, descripcion, instructor, entidad_id)
VALUES
    ('Diplomado en Desarrollo Web', 'Diplomado intensivo sobre desarrollo de aplicaciones web modernas', 'Laura Torres', 1),
    ('Curso de Ciencia de Datos', 'Curso introductorio a la ciencia de datos con Python y SQL', 'Mario López', 1),
    ('Bootcamp en Desarrollo Full Stack', 'Programa intensivo de desarrollo web Full Stack', 'Diana Sánchez', 2),
    ('Curso de Programación en Java', 'Curso práctico para aprender Java desde cero', 'Luis Ramírez', 2),
    ('Curso de Inglés para Tecnología', 'Curso de inglés enfocado en términos y temas de tecnología', 'Andrea Ruiz', 3),
    ('Diplomado en Inteligencia Artificial', 'Diplomado avanzado sobre Inteligencia Artificial y Machine Learning', 'Camilo Gómez', 3),
    ('Curso de Ciberseguridad', 'Curso básico de ciberseguridad y buenas prácticas en IT', 'Sofía Rodríguez', 4),
    ('Diplomado en Gestión de Proyectos IT', 'Diplomado en gestión de proyectos en el sector de tecnología', 'Felipe Álvarez', 4),
    ('Curso Intensivo de Inglés para Programadores', 'Inglés especializado para profesionales en programación y tecnología', 'Miguel Ángel', 5),
    ('Curso de Inglés Básico', 'Curso de inglés para principiantes', 'Daniela Méndez', 6),
    ('Curso de Inglés Intermedio', 'Curso de inglés de nivel intermedio con énfasis en tecnología', 'Julián Pérez', 6),
    ('Curso de Inglés Avanzado para Negocios', 'Curso de inglés avanzado enfocado en vocabulario empresarial y de tecnología', 'Lucía Moreno', 6);
