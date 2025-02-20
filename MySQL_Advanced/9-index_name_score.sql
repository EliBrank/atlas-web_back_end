-- Creates index on names table with name's first char, score
CREATE INDEX idx_score_first ON names (name (1), score)
