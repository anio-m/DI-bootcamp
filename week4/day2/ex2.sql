-- select * from  customer 
-- select concat(first_name, ' ', last_name) as full_name from customer
-- select distinct create_date from customer
-- select * from customer order by first_name desc
-- select film_id, title, description, release_year, rental_rate from film order by rental_rate
-- select address, phone from address where district = 'Texas'
-- select * from film  where film_id = 15 or film_id  =150
-- select film_id, title, description, length, rental_rate from film where title = 'The Equalizer' 
-- select film_id, title, description, length, rental_rate from film where title like 'Th%'  
-- select * from film order by rental_rate limit 10
-- select * from film order by rental_rate limit 10 offset 10
-- select c.last_name, c.first_name, p.amount, p.payment_date 
-- from customer as c
-- join payment as p on c.customer_id = p.customer_id
-- order by c.customer_id
-- select f.title 
-- from film as f
-- left join inventory as i on f.film_id = i.film_id
-- where i.film_id is null;
-- select ci.city, co.country
-- from city as ci
-- join country as co on ci.country_id = co.country_id 




