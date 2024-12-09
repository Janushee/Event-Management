SELECT
    e.id,
    e.name,
    e.date,
    e.total_tickets,
    e.tickets_sold
FROM
    eventmanagement.event_event e
ORDER BY
    e.tickets_sold DESC
LIMIT 3;


--These is the query to get the tickets sold. It can be optimised in different ways like,
--1. Index on tickets_sold
--2. Limiting data entry with specific interval
--3. Partitioning by date
--4. Creating Materialized Views