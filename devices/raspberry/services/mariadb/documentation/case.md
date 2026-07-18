SELECT 
    l.Date,
    CASE 
        WHEN s.Running = 1 THEN 'Running'
        WHEN s.Gym = 1 THEN 'Gym'
        WHEN s.Swim = 1 THEN 'Swim'
        WHEN s.Karate = 1 THEN 'Karate'
        WHEN s.Badminton = 1 THEN 'Badminton'
        WHEN s.Squash = 1 THEN 'Squash'
        WHEN s.Walk = 1 THEN 'Walk'
        ELSE 'Unknown'
    END as SportType
FROM lifestyle l
JOIN sport s ON l.Date = s.Date
WHERE l.Sport = 1
ORDER BY l.Date;
