-- Write your query below
select u.name ,sum(CASE WHEN u.id in (select distinct user_id from rides) THEN r.distance ELSE 0 END) travelled_distance 
from users u
left join rides r 
on r.user_id = u.id
group by u.name
order by travelled_distance desc;