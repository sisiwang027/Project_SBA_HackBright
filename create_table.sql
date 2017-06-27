--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: gender; Type: TABLE; Schema: public;
--

CREATE TABLE gender (
    gender_code VARCHAR(8) PRIMARY KEY,
    gender_name VARCHAR(8) NOT NULL
);


--
-- Name: user; Type: TABLE; Schema: public;
--

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);


--
-- Name: customer; Type: TABLE; Schema: public;
--

CREATE TABLE customers (
    cust_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    gender_code VARCHAR(8) REFERENCES gender,
    phone_number VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL, 
    address VARCHAR(256) NOT NULL,
    city VARCHAR(30) NOT NULL,
    state VARCHAR(8) NOT NULL,
    zipcode INTEGER NOT NULL,
    user_id INTEGER REFERENCES users
);

--
-- Name: product_details; Type: TABLE; Schema: public;
--

CREATE TABLE product_details (
    product_type_id SERIAL PRIMARY KEY,
    brand_code VARCHAR(30) NOT NULL,
    type_name VARCHAR(30) NOT NULL,
    product_detail varchar(256) NOT NULL,
    descriptoin VARCHAR(256)
);

--
-- Name: product; Type: TABLE; Schema: public;
--

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_type_id INTEGER NOT NULL REFERENCES product_details,
    user_id INTEGER REFERENCES users,
    purchase_at TIMESTAMP NOT NULL,
    purchase_price FLOAT NOT NULL,
    cust_id INTEGER REFERENCES customers,
    sale_price FLOAT,
    sold_at TIMESTAMP,
    returned_at TIMESTAMP
);






