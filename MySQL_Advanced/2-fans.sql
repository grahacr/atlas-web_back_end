-- SQL script ranking countries of origins of bands based on number of fans!

SELECT origin AS origin, SUM(fans) as nb_fans
from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
