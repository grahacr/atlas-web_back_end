-- SQL script creating index on "names" table
-- using first letter of name and a score range
-- enabling us to search for names that start with a certain letter and with certain score values

CREATE INDEX idx_name_first_score ON names (name(1), score);