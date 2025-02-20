-- Creates index on names table with name's first char, score
CREATE INDEX idx_name_first_score ON names (name (1), score)
