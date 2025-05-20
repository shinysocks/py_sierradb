sql_query = """
    SET search_path = 'sierra_view';
    SELECT
        code AS "Location Code",
        name AS "Location Name"
    FROM location_myuser
    ORDER BY
        "Location Code" DESC
    LIMIT 15
    ;
"""
