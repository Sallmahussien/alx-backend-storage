-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
DELIMITER //

CREATE TRIGGER `reset_email`
BEFORE UPDATE
ON `users` FOR EACH ROW
BEGIN
    DECLARE valid_email_new BOOLEAN;

    IF NEW.`email` != OLD.`email` THEN
        IF NEW.`valid_email` = 0 THEN
            SET valid_email_new = 1;
        ELSE
            SET valid_email_new = 0;
        END IF;

        SET NEW.`valid_email` = valid_email_new;
    END IF;
END//

DELIMITER ;
