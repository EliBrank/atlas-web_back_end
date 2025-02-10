-- Lists Glam Rock bands by longevity
SELECT
    band_name,
    -- (COALESCE(split, YEAR(CURDATE())) - formed) AS lifespan
    (COALESCE(split, 2024) - formed) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
