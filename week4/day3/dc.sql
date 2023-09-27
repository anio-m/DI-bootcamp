-- create table Customer (
-- 	id serial primary key,
-- 	first_name varchar (50),
-- 	last_name varchar not null
-- )

-- insert into Customer(first_name, last_name) values
-- ('john', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive')

-- create table Customer_profile (
-- 	id serial primary key,
-- 	isLoggedIn boolean default(false),
-- 	customer_id integer 
-- )

-- INSERT INTO Customer_profile (isLoggedIn, customer_id)
-- VALUES (
--     true,
--     (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')
-- );

-- INSERT INTO Customer_profile (isLoggedIn, customer_id)
-- VALUES (
--     false,
--     (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu')
-- );

-- select first_name from Customer 
-- inner join Customer_profile on Customer.id = Customer_profile.customer_id
-- where Customer_profile.isLoggedIn = true;

-- SELECT Customer.first_name, COALESCE(Customer_profile.isLoggedIn, false) AS isLoggedIn
-- FROM Customer
-- LEFT JOIN Customer_profile ON Customer.id = Customer_profile.customer_id;



	