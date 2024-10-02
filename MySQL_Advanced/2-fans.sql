-- SQL script ranking countries of origins of bands based on number of fans!

DROP TABLE IF EXISTS ranked_bands;

CREATE TABLE ranked_bands As
SELECT origin AS origin, SUM(fans) as nb_fans
from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
