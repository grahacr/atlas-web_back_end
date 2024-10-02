-- SQL script listing bands with Glam Rock as main style ranked by longevity

SELECT band_name, COALESCE(split, YEAR(CURDATE())) - formed as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
