-- SQL script creating index on "names" table using first letter of name
-- enabling us to search for names that start with a certain letter

CREATE INDEX idx_name_first ON names (name(1));