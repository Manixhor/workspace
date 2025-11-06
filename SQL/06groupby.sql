
CREATE TABLE working(
	id INT,
    name VARCHAR(100)
    
    );
INSERT INTO working(id,name)
VALUES(1,'Alice');

ALTER TABLE working
ADD COLUMN hours INT;

INSERT INTO working(id,name,hours)
VALUES (1,'Mani',22);

INSERT INTO working(id,name,hours)
VALUES (1,'Manfnkji',12);

SELECT * FROM working;

SELECT SUM(hours) * 1.0 / COUNT(hours) AS avg
FROM working;

SELECT hours, SUM(hours) AS total
FROM working
GROUP BY hours;

SELECT * FROM working
ORDER BY hours DESC;