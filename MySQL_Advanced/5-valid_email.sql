-- SQL trigger to reset valid_email when email has been changed

DELIMITER //
CREATE TRIGGER reset_validity
BEFORE UPDATE ON users
    if NEW.email != OLD.email
    THEN SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER;