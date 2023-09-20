-- create table students(
-- id serial primary key,
-- last_name VARCHAR(50),
-- first_name VARCHAR(50),
-- birth_date date);

-- insert into students (last_name, first_name, birth_date)
-- values
-- -- ('Marc', 'Benichou', '1998/11/02'),
-- ('Yoan', 'Cohen', '03/12/2010'),
-- ('Lea', 'Benichou', '1987/07/27'),
-- ('Amelia', 'Dux', '1996/04/07'),
-- ('David', 'Grez', '2003/06/14'),
-- ('Omer', 'Simpson','03/10/1980');

-- -- select * from students
-- select first_name, last_name from students 
-- select first_name, last_name from students where id = 2;
-- select first_name, last_name from students where last_name = 'Benichou' and first_name = 'Marc'
-- alter table students rename column first_name_old to last_name; 
-- select first_name, last_name from students where first_name = 'Marc' or last_name = 'Benichou'
-- SELECT first_name from students where first_name like '_a%'
-- SELECT first_name from students where first_name ilike 'a%'
-- SELECT first_name from students where first_name like '%a'
-- select * from students where first_name like '%_a_%'
-- select * from students where id in (1, 3)
-- select * from students where birth_date >= '1/01/2000'


