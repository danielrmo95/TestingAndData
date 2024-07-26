select * from dbo.table_1

update dbo.table_1 set nombre = 'Daniel' where  nombre = 'daniel';
update dbo.table_1 set nombre = 'Jerson' where  nombre = 'El viejo Jerson';
update dbo.table_1 set nombre = 'Paula' where  nombre = 'Paula';
update dbo.table_1 set nombre = 'Karina' where  nombre = 'kARINA'



Delete from dbo.table_1 where id =2


select ba.*, al.album_name  from dbo.bands ba
inner join dbo.albums al on al.band_id = ba.band_id
where ba.band_id = 1



SELECT b.band_name, COUNT(a.album_id) AS number_of_albums
FROM dbo.bands b
JOIN dbo.albums a ON b.band_id = a.band_id
GROUP BY b.band_name
HAVING COUNT(a.album_id) > 0;


