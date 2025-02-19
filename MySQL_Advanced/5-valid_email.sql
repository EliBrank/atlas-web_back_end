-- Create trigger to reset valid_email on email change

-- DELIMITER used to stop ';' from ending trigger early
DELIMITER $$

CREATE TRIGGER email_validation
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email
    THEN SET NEW.valid_email = 0;
    END IF;
END $$

DELIMITER ;
