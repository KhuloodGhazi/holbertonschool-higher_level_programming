-- Create table and insert multiple registers
-- Execute: cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "Khulood", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Faris", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Nujood", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "Abdulmajeed", 8);
