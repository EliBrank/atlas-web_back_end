-- Creates trigger to reduce item quantity with order insert

-- DELIMITER used to stop ';' from ending trigger early
DELIMITER $$

CREATE TRIGGER stock_deplete
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END $$

DELIMITER ;
