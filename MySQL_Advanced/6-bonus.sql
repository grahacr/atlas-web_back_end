-- create stored procedure that adds new correction for student

DELIMITER //
CREATE procedure AddBonus
    @user_id INT,
    @project_name VARCHAR(255),
    @score INT
AS
BEGIN
    DECLARE project_id INT;
    IF NOT EXISTS (
        SELECT id FROM projects WHERE name = @project_name
    )
    BEGIN
        INSERT INTO projects (name)
        VALUES (@project_name)
        SET @project_id = SCOPE_IDENTITY();
    END
    ELSE
    BEGIN
        SELECT @project_id = id FROM projects WHERE name = @project_name;
    END
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (@user_id, @project_id, @score);
END
DELIMITER;