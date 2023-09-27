-- select * from language
-- select f.title, f.description, l.name
-- from film as f
-- join language as l on f.language_id = l.language_id 
-- select f.title, f.description,l.name
-- from language as l
-- join film as f on l.language_id = f.language_id 
-- create table new_film (
-- new_film_id serial primary key, 
-- new_film_name varchar (50)
-- )
-- insert into new_film (new_film_name)
-- values 
-- ('The Equalizer'),
-- ('Mudbound');

-- create table customer_review(
-- review_id serial primary key,
-- film_id integer ,
-- language_id integer,
-- title varchar(50),
-- score integer check (score between 1 and 10),
-- review_text varchar(50),
-- last_update date,
	
-- foreign key (film_id) references new_film(new_film_id),
-- foreign key (language_id) references language(language_id)
-- );

-- alter table customer_review alter column review_text type text;

-- insert into customer_review(film_id, language_id, title, score, review_text, last_update)
-- values
-- (
-- 	(select new_film_id from new_film where new_film_name = 'The Equalizer'),
-- 	(select language_id from language where name = 'English'),
-- 	'The Equalizer review',
-- 	10,
-- 	'Robert McCall is a former special service commando who faked his own death in hopes of living out a quiet life.
-- 	Instead, he comes out of his self-imposed retirement to save a young girl, and finds his desire for justice reawakened after coming face-to-face with members of a brutal Russian gang.
-- 	McCall becomes the go-to man when the helpless require the kind of vengeance they would never find without his skills.',
-- 	'2023-01-01'
-- ),
-- (
-- 	(select new_film_id from new_film where new_film_name = 'Mudbound'),
-- 	(select language_id from language where name = 'English'),
-- 	'The Mudbound review',
-- 	9,
-- 	'In the aftermath of WWII, somewhere in the muddy Mississippi Delta,
-- 	two families--one black, the Jacksons, and the other white,
-- 	the McAllans--are forced to share the same patch of land,
-- 	keeping a frail race-based peace with each other.',
-- 	'2017-07-18'
-- )

-- update language 
-- set name = 'French'
-- where language_id = 6

-- select inventory_id from rental

-- select title,rental_rate
-- from film
-- order by rental_rate 
-- desc limit 30;

-- select first_name, last_name from actor where first_name like 'Penelope%' and last_name like 'Monroe%'
-- select name from category where name like 'documentary%' and
-- select length from film where length < 60;
-- select rating from film where rating ='R';
-- select first_name, last_name from customer where first_name like 'Matthew%' and last_name like 'Mahan%' and
-- select rental_rate from film where rental_rate >4 and
-- select rental_date from rental where rental_date between '2005-07-28' and '2005-08-01' and
-- select length from film where length < 60 and
-- select rating from film where rating ='R'; 
-- select title, description from film where title like 'boat' and description or 'boat' and
-- select max(replacement_cost) from film 