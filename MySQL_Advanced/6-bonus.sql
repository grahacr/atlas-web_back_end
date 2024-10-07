-- create stored procedure that adds new correction for student

DELIMITER //
CREATE procedure AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;
    IF NOT EXISTS (
        SELECT id FROM projects WHERE name = project_name
    ) THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    ELSE
        SELECT id INTO project_id FROM projects WHERE name = project_name;
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END //
DELIMITER ;
