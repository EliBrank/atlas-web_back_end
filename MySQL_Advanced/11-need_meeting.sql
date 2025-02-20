-- Create view for students needing meeting
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND (
    last_meeting IS NULL OR (
        last_meeting < DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)
    )
)
