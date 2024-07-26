
-- Crear la tabla bands
CREATE TABLE bands (
    band_id INT PRIMARY KEY,
    band_name VARCHAR(100),
    genre VARCHAR(50),
    formation_year INT
);

-- Crear la tabla albums
CREATE TABLE albums (
    album_id INT PRIMARY KEY,
    album_name VARCHAR(100),
    release_year INT,
    band_id INT,
    FOREIGN KEY (band_id) REFERENCES bands(band_id)
);

-- Crear la tabla songs
CREATE TABLE songs (
    song_id INT PRIMARY KEY,
    song_title VARCHAR(100),
    release_year INT,
    band_id INT,
    album_id INT,
    FOREIGN KEY (band_id) REFERENCES bands(band_id),
    FOREIGN KEY (album_id) REFERENCES albums(album_id)
);

-- Insertar registros en la tabla bands
INSERT INTO bands (band_id, band_name, genre, formation_year) VALUES
(1, 'The Beatles', 'Rock', 1960),
(2, 'Led Zeppelin', 'Rock', 1968),
(3, 'Pink Floyd', 'Progressive Rock', 1965),
(4, 'Queen', 'Rock', 1970),
(5, 'The Rolling Stones', 'Rock', 1962),
(6, 'Nirvana', 'Grunge', 1987),
(7, 'Metallica', 'Heavy Metal', 1981),
(8, 'U2', 'Rock', 1976),
(9, 'Radiohead', 'Alternative Rock', 1985),
(10, 'AC/DC', 'Hard Rock', 1973);

-- Insertar registros en la tabla albums
INSERT INTO albums (album_id, album_name, release_year, band_id) VALUES
(1, 'Abbey Road', 1969, 1),
(2, 'Led Zeppelin IV', 1971, 2),
(3, 'The Wall', 1979, 3),
(4, 'A Night at the Opera', 1975, 4),
(5, 'Let It Bleed', 1969, 5),
(6, 'Nevermind', 1991, 6),
(7, 'Metallica (The Black Album)', 1991, 7),
(8, 'The Joshua Tree', 1987, 8),
(9, 'OK Computer', 1997, 9),
(10, 'Back in Black', 1980, 10);

-- Insertar registros en la tabla songs
INSERT INTO songs (song_id, song_title, release_year, band_id, album_id) VALUES
(1, 'Hey Jude', 1968, 1, NULL),
(2, 'Stairway to Heaven', 1971, 2, 2),
(3, 'Comfortably Numb', 1979, 3, 3),
(4, 'Bohemian Rhapsody', 1975, 4, 4),
(5, 'Paint It Black', 1966, 5, NULL),
(6, 'Smells Like Teen Spirit', 1991, 6, 6),
(7, 'Enter Sandman', 1991, 7, 7),
(8, 'With or Without You', 1987, 8, 8),
(9, 'Creep', 1992, 9, NULL),
(10, 'Back in Black', 1980, 10, 10),
(11, 'Let It Be', 1970, 1, NULL),
(12, 'Whole Lotta Love', 1969, 2, NULL),
(13, 'Wish You Were Here', 1975, 3, NULL),
(14, 'We Will Rock You', 1977, 4, NULL),
(15, 'Angie', 1973, 5, NULL),
(16, 'Come As You Are', 1991, 6, 6),
(17, 'Nothing Else Matters', 1992, 7, 7),
(18, 'Sunday Bloody Sunday', 1983, 8, NULL),
(19, 'Karma Police', 1997, 9, 9),
(20, 'Highway to Hell', 1979, 10, NULL);

-- Comprobar que los registros se han insertado correctamente
SELECT * FROM bands;
SELECT * FROM albums;
SELECT * FROM songs;
