

UPDATE albums 
SET release_year = 1982
WHERE id = 1;

SELECT * FROM albums
WHERE release_year < 2000;


SELECT * FROM albums
WHERE name LIKE '%er%' OR band_id = 2;

UPDATE albums
SET release_year = 1950 
WHERE id = 1;

SELECT * FROM albums
UPDATE albums
SET release_year = 1950 
WHERE id = 5;

SELECT * FROM albums
WHERE release_year BETWEEN 1950 AND 2000;

DELETE FROM albums WHERE id = 5;
SELECT * FROM albums;


SELECT * FROM bands
JOIN albums ON bands.id = albums.band_id;

SELECT * FROM albums 
RIGHT JOIN bands ON bands.id = albums.id;


SELECT AVG(release_year) FROM albums
