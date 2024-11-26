SELECT en.nombre AS entidad_nombre, cu.nombre_curso, cu.instructor, co.calificacion, co.comentario, co.fecha_comentario
FROM  dbo.Comentarios co 
INNER JOIN dbo.Cursos cu ON cu.curso_id = co.curso_id 
INNER JOIN dbo.EntidadesEducativas en ON en.entidad_id = co.entidad_id
where en.nombre like '%prueba%' or cu.nombre like '%prueba%' or cu.instructor= '%prueba%'


SELECT * FROM  dbo.Cursos co
where co.nombre_curso like '%prueba%'

SELECT * FROM  dbo.EntidadesEducativas en
where en.nombre like '%prueba%' or en.nombre like '%dsa%' 


SELECT * FROM  [dbo].[Comentarios] co
where entidad_id>6



delete from dbo.EntidadesEducativas where entidad_id>6 
delete from dbo.Cursos where curso_id>12 
delete from [dbo].[Comentarios]  where entidad_id>6