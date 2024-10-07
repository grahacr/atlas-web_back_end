-- create SQL trigger to decrease quantity of item after adding new order

DELIMITER //
CREATE TRIGGER update_inventory
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    set quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER;