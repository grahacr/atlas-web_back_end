-- SQL Script creates stored procedure that computes and stores average score for given student
-- written for external sql tables:
-- corrections, users, projects

DELIMITER //
CREATE procedure ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;

END //
DELIMITER ;
