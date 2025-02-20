-- Creates index on names table with first character of each name
CREATE INDEX idx_name_first ON names (name (1))
