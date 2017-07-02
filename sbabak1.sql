--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE categories (
    cg_id integer NOT NULL,
    cg_name character varying(30) NOT NULL
);


ALTER TABLE categories OWNER TO vagrant;

--
-- Name: categories_cg_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE categories_cg_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE categories_cg_id_seq OWNER TO vagrant;

--
-- Name: categories_cg_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE categories_cg_id_seq OWNED BY categories.cg_id;


--
-- Name: category_detail_values; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE category_detail_values (
    cg_detailvalue_id integer NOT NULL,
    cg_detailname_id integer,
    detail_value character varying(30) NOT NULL
);


ALTER TABLE category_detail_values OWNER TO vagrant;

--
-- Name: category_detail_values_cg_detailvalue_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE category_detail_values_cg_detailvalue_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE category_detail_values_cg_detailvalue_id_seq OWNER TO vagrant;

--
-- Name: category_detail_values_cg_detailvalue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE category_detail_values_cg_detailvalue_id_seq OWNED BY category_detail_values.cg_detailvalue_id;


--
-- Name: category_detailname; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE category_detailname (
    cg_detailname_id integer NOT NULL,
    detailname character varying(30) NOT NULL
);


ALTER TABLE category_detailname OWNER TO vagrant;

--
-- Name: category_detailname_cg_detailname_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE category_detailname_cg_detailname_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE category_detailname_cg_detailname_id_seq OWNER TO vagrant;

--
-- Name: category_detailname_cg_detailname_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE category_detailname_cg_detailname_id_seq OWNED BY category_detailname.cg_detailname_id;


--
-- Name: category_details; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE category_details (
    cg_detail_id integer NOT NULL,
    cg_id integer NOT NULL,
    cg_detailname_id integer NOT NULL
);


ALTER TABLE category_details OWNER TO vagrant;

--
-- Name: category_details_cg_detail_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE category_details_cg_detail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE category_details_cg_detail_id_seq OWNER TO vagrant;

--
-- Name: category_details_cg_detail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE category_details_cg_detail_id_seq OWNED BY category_details.cg_detail_id;


--
-- Name: customers; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE customers (
    cust_id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    gender_code character varying(8) NOT NULL,
    phone_number character varying(50) NOT NULL,
    email character varying(50) NOT NULL,
    birth_date date NOT NULL,
    address character varying(256) NOT NULL,
    city character varying(30) NOT NULL,
    state character varying(8) NOT NULL,
    zipcode integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE customers OWNER TO vagrant;

--
-- Name: customers_cust_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE customers_cust_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE customers_cust_id_seq OWNER TO vagrant;

--
-- Name: customers_cust_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE customers_cust_id_seq OWNED BY customers.cust_id;


--
-- Name: gender; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE gender (
    gender_code character varying(8) NOT NULL,
    gender_name character varying(8)
);


ALTER TABLE gender OWNER TO vagrant;

--
-- Name: product_details; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE product_details (
    detail_id integer NOT NULL,
    p_id integer,
    cg_detailvalue_id integer
);


ALTER TABLE product_details OWNER TO vagrant;

--
-- Name: product_details_detail_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE product_details_detail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE product_details_detail_id_seq OWNER TO vagrant;

--
-- Name: product_details_detail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE product_details_detail_id_seq OWNED BY product_details.detail_id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE products (
    p_id integer NOT NULL,
    cg_id integer NOT NULL,
    user_id integer NOT NULL,
    purchase_at timestamp without time zone NOT NULL,
    purchase_price double precision NOT NULL,
    cust_id integer,
    sale_price double precision,
    sold_at timestamp without time zone,
    returned_at timestamp without time zone
);


ALTER TABLE products OWNER TO vagrant;

--
-- Name: products_p_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE products_p_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE products_p_id_seq OWNER TO vagrant;

--
-- Name: products_p_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE products_p_id_seq OWNED BY products.p_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE users (
    user_id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(50) NOT NULL,
    password character varying(30) NOT NULL
);


ALTER TABLE users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE users_user_id_seq OWNED BY users.user_id;


--
-- Name: cg_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY categories ALTER COLUMN cg_id SET DEFAULT nextval('categories_cg_id_seq'::regclass);


--
-- Name: cg_detailvalue_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category_detail_values ALTER COLUMN cg_detailvalue_id SET DEFAULT nextval('category_detail_values_cg_detailvalue_id_seq'::regclass);


--
-- Name: cg_detailname_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category_detailname ALTER COLUMN cg_detailname_id SET DEFAULT nextval('category_detailname_cg_detailname_id_seq'::regclass);


--
-- Name: cg_detail_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category_details ALTER COLUMN cg_detail_id SET DEFAULT nextval('category_details_cg_detail_id_seq'::regclass);


--
-- Name: cust_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY customers ALTER COLUMN cust_id SET DEFAULT nextval('customers_cust_id_seq'::regclass);


--
-- Name: detail_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY product_details ALTER COLUMN detail_id SET DEFAULT nextval('product_details_detail_id_seq'::regclass);


--
-- Name: p_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY products ALTER COLUMN p_id SET DEFAULT nextval('products_p_id_seq'::regclass);


--
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY users ALTER COLUMN user_id SET DEFAULT nextval('users_user_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY categories (cg_id, cg_name) FROM stdin;
1	clothing
2	shoes
\.


--
-- Name: categories_cg_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('categories_cg_id_seq', 2, true);


--
-- Data for Name: category_detail_values; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY category_detail_values (cg_detailvalue_id, cg_detailname_id, detail_value) FROM stdin;
1	1	0
2	1	2
3	1	4
4	1	6
5	1	8
6	1	10
7	2	Midnight
8	2	Pink Polish
9	2	Purple Dark
10	2	Red Lipstick
11	2	Black
12	3	Gap
13	4	Silk
14	5	Dress
15	1	5
16	1	5.5
17	1	6
18	1	6.5
19	1	7
20	1	7.5
21	1	8
22	2	Black/Matte
23	2	White/Pure
24	3	Nike
25	5	AIR JORDAN 4 RETRO
\.


--
-- Name: category_detail_values_cg_detailvalue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('category_detail_values_cg_detailvalue_id_seq', 25, true);


--
-- Data for Name: category_detailname; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY category_detailname (cg_detailname_id, detailname) FROM stdin;
1	size
2	color
3	brand
4	material
5	sub_category
\.


--
-- Name: category_detailname_cg_detailname_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('category_detailname_cg_detailname_id_seq', 5, true);


--
-- Data for Name: category_details; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY category_details (cg_detail_id, cg_id, cg_detailname_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	2	1
7	2	2
8	2	3
9	2	5
\.


--
-- Name: category_details_cg_detail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('category_details_cg_detail_id_seq', 9, true);


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY customers (cust_id, first_name, last_name, gender_code, phone_number, email, birth_date, address, city, state, zipcode, user_id) FROM stdin;
1	Edwin	Lucas	M	(907)952-5552x44905	EdwinLucas@gmail.com	2002-05-02	717 Sherri Trace Suite 235	Rochaberg	CA	61583	1
2	Brian	Booth	M	499-361-7168x9962	BrianBooth@gmail.com	1995-04-28	0042 Cross Squares	Troymouth	CA	42749	1
3	Tracy	Garcia	M	226.624.8922	TracyGarcia@gmail.com	1976-06-17	81955 Jeremy Terrace Apt. 561	Feliciamouth	CA	21214	1
4	Jonathan	Klein	M	975-732-5055x8048	JonathanKlein@hotmail.com	1986-05-27	3913 Villa Stravenue	Sylviaborough	CA	15070	1
5	David	Johnson	M	1-189-786-1975	DavidJohnson@gmail.com	1976-05-07	71926 Young Overpass Suite 548	South Darrell	CA	90554	1
6	Patrick	Banks	M	1-374-344-2217	PatrickBanks@gmail.com	2014-12-24	317 Green Springs Apt. 447	Lake Lindseymouth	CA	53847	1
7	Matthew	Ortiz	M	1-260-587-7586x125	MatthewOrtiz@gmail.com	1998-03-19	04771 Huffman Plains	Flemingport	CA	97877	1
8	Gregory	Torres	M	124.032.2266	GregoryTorres@hotmail.com	1996-01-29	578 Morrison Lakes	Jamesburgh	CA	58330	1
9	Jason	Howard	M	782.427.7564x548	JasonHoward@gmail.com	1991-09-28	6743 Tammy Throughway	Port Hannahborough	CA	35426	1
10	Daniel	Thomas	M	(720)783-5302	DanielThomas@hotmail.com	1985-09-13	5447 Lawrence Common	East Jasonshire	CA	32250	1
11	Jeremy	Dennis	M	1-830-194-0922x38927	JeremyDennis@gmail.com	2013-03-18	963 Brian Meadow Apt. 929	North Amanda	CA	11429	1
12	John	Welch	M	(059)497-1143x180	JohnWelch@hotmail.com	1979-06-05	9990 Max Rapid	Lisaview	CA	99720	1
13	Philip	Daniel	M	04208510237	PhilipDaniel@gmail.com	2015-03-30	9585 Tina Summit Suite 371	Crystalhaven	CA	27399	1
14	Ricky	Fritz	M	993.414.1485	RickyFritz@gmail.com	1998-09-21	11121 Lopez Forks	Sarahfurt	CA	25879	1
15	James	Green	M	1-069-770-8340	JamesGreen@hotmail.com	2016-01-12	9826 David Ramp Apt. 802	North Hollychester	CA	83024	1
16	Christopher	Dougherty	M	833-250-6168x06775	ChristopherDougherty@gmail.com	1988-11-21	158 Johnson Station	Ginatown	CA	78313	1
17	Gregory	Blankenship	M	05560925373	GregoryBlankenship@gmail.com	2012-01-15	5247 Brian Greens Apt. 252	Toddton	CA	90644	1
18	Zachary	Delacruz	M	127-913-9838x03773	ZacharyDelacruz@gmail.com	2010-02-11	82989 Lowe Skyway	Lake Ashley	CA	36067	1
19	Howard	Hansen	M	(286)214-3538	HowardHansen@gmail.com	1978-09-15	23878 Warner Burgs Suite 159	West Jason	CA	98634	1
20	Joshua	Bennett	M	150.250.7003	JoshuaBennett@hotmail.com	1987-04-21	5472 Lucas Shoal	Butlerborough	CA	2943	1
21	Gregory	Hopkins	M	1-422-911-1758	GregoryHopkins@gmail.com	1985-08-20	946 Michael Square	West Jeffrey	CA	63503	1
22	John	Torres	M	1-230-011-9669x07703	JohnTorres@hotmail.com	1998-04-05	14080 Paul Village	East Samuel	CA	72551	1
23	Daniel	Davies	M	1-253-336-3572	DanielDavies@gmail.com	2009-10-02	930 Garcia Burgs Apt. 113	Pachecoville	CA	69159	1
24	Justin	Garrison	M	527.248.1727x753	JustinGarrison@hotmail.com	1992-12-27	9302 Barnett Island Apt. 602	North Williamville	CA	78229	1
25	Parker	Barry	M	258.515.3854x587	ParkerBarry@gmail.com	2006-07-15	2437 Reese Meadows	Lake Denise	CA	29096	1
26	Robert	Taylor	M	1-285-258-6701	RobertTaylor@gmail.com	2001-10-21	28777 Craig Spur Suite 734	Ryanport	CA	75438	1
27	Brian	Williams	M	(287)529-3667x2425	BrianWilliams@gmail.com	2002-06-10	5373 James Way Apt. 334	Lake Jennifer	CA	56650	1
28	Kenneth	Mccormick	M	018-895-7139x435	KennethMccormick@hotmail.com	2009-11-14	756 Tanya Forest	Gloriamouth	CA	98548	1
29	Charles	Schwartz	M	1-993-698-3474x00053	CharlesSchwartz@gmail.com	1976-01-02	161 Julie Cliffs Apt. 651	South Michellefort	CA	38014	1
30	John	Wilson	M	278.857.5731	JohnWilson@hotmail.com	1987-02-25	85951 Larry Shoal Suite 550	Taylorstad	CA	61141	1
31	Rick	Cunningham	M	283.824.9586x2099	RickCunningham@hotmail.com	2004-01-04	72524 Golden Flats	Joshuaton	CA	14256	1
32	Jason	Huerta	M	610-911-5459	JasonHuerta@hotmail.com	2004-05-15	41462 Rodney Fall Suite 150	New Michaeltown	CA	51034	1
33	Jonathan	Hunter	M	210-430-1846x70626	JonathanHunter@hotmail.com	2002-12-21	7691 Sutton Villages	Thompsonland	CA	68984	1
34	James	Shaw	M	(088)654-3081x8452	JamesShaw@hotmail.com	2015-05-12	576 Lisa Flat	New Andrewport	CA	15226	1
35	Scott	Allison	M	1-140-208-0554x922	ScottAllison@hotmail.com	2008-04-16	45950 Richard Causeway	Lake Rebeccamouth	CA	67588	1
36	Michael	Cunningham	M	(842)374-3918x2393	MichaelCunningham@hotmail.com	1976-08-24	7929 Jenkins Viaduct Apt. 415	Jamesview	CA	85741	1
37	Mark	Davis	M	820.402.6776	MarkDavis@hotmail.com	2000-09-27	53648 Bentley Forest Suite 355	East Anthony	CA	50720	1
38	Jose	Long	M	176-089-4430x801	JoseLong@hotmail.com	1990-10-09	439 Kenneth Locks	West Stephanie	CA	61903	1
39	Shane	Brown	M	01360214460	ShaneBrown@hotmail.com	2014-07-11	717 Jerry Isle Suite 702	Johnsonshire	CA	86148	1
40	Tyler	Parsons	M	+40(1)8602667933	TylerParsons@hotmail.com	1991-07-28	35374 Robert Drive	East Jamieberg	CA	50426	1
41	Jesus	Caldwell	M	(464)196-0375x53409	JesusCaldwell@hotmail.com	2016-07-30	8390 Pacheco Dale Apt. 785	East Nicholas	CA	68243	1
42	Joshua	Cook	M	+49(8)1564662488	JoshuaCook@hotmail.com	1984-08-23	994 Tucker Pike Suite 624	North Victoria	CA	40808	1
43	Andrew	Thompson	M	1-135-918-1493	AndrewThompson@gmail.com	1976-03-23	103 Lewis Trail Suite 134	Brandonside	CA	68931	1
44	Brad	Knight	FM	(044)490-1902x3409	BradKnight@hotmail.com	1985-05-22	93907 Elizabeth Knoll	Hughesville	CA	83725	1
45	David	Robinson	FM	304-836-0324	DavidRobinson@gmail.com	1971-07-23	547 Allen Mills	Garciaborough	CA	34141	1
46	Joseph	Collins	FM	1-833-622-4124x82123	JosephCollins@gmail.com	2014-03-17	893 Ashley Drives	Elizabethberg	CA	35701	1
47	Donald	Torres	FM	582.961.4426x4759	DonaldTorres@gmail.com	1976-04-16	59242 Finley Rapid	South Diamondville	CA	44601	1
48	Robert	Weber	FM	785.387.8596x050	RobertWeber@gmail.com	1987-07-07	536 Fletcher Mountain Suite 412	Lake Michaelville	CA	10338	1
49	Zachary	Paul	FM	544.644.6179	ZacharyPaul@gmail.com	1981-09-04	936 James Drive Apt. 866	South Lance	CA	41013	1
50	Louis	Knox	FM	746-332-7710	LouisKnox@hotmail.com	1978-01-14	9063 Stanley Prairie Suite 432	North Karen	CA	8589	1
51	Travis	Sparks	FM	588-670-3620x119	TravisSparks@hotmail.com	1976-02-18	7519 Reynolds Wells	Kimberlybury	CA	45599	1
52	Jeffrey	Hart	FM	693.525.1164x7926	JeffreyHart@hotmail.com	2000-10-28	159 Walton Viaduct	Juanberg	CA	13978	1
53	Ryan	Anderson	FM	194-545-0001	RyanAnderson@hotmail.com	1981-06-25	1378 Arias Vista Suite 090	Dianafurt	CA	24328	1
54	Anthony	Anderson	FM	082-657-6306	AnthonyAnderson@gmail.com	1980-08-25	6320 Madeline Ridges Suite 326	East Christophermouth	CA	5937	1
55	Thomas	Jenkins	FM	366-052-1283	ThomasJenkins@hotmail.com	2009-10-16	17402 Melanie Fords Suite 683	New Rodneymouth	CA	37613	1
56	Brian	Adams	FM	850.789.8731x4150	BrianAdams@hotmail.com	2011-04-12	30355 Troy Lakes Apt. 802	Port Devon	CA	11569	1
57	James	Freeman	FM	945-735-1467x380	JamesFreeman@gmail.com	2005-11-16	781 Benjamin Row Suite 872	North Jeffreyland	CA	69204	1
58	Jesse	Rogers	FM	632.012.3156x68810	JesseRogers@hotmail.com	1982-02-05	71538 Dawn Lake Suite 311	West Heather	CA	6066	1
59	Randy	Bishop	FM	1-476-518-6417	RandyBishop@gmail.com	2011-11-02	01939 Heidi Hollow Apt. 101	Rogersland	CA	16211	1
60	Phillip	Banks	FM	1-384-751-0799x136	PhillipBanks@hotmail.com	1976-06-12	58502 Donna Villages	New Samantha	CA	29477	1
61	Gregory	Lewis	FM	036.332.8516x1999	GregoryLewis@gmail.com	1982-10-19	54602 Rodriguez Road	Turnershire	CA	78993	1
62	Andrew	Holmes	FM	1-470-096-4342x996	AndrewHolmes@gmail.com	2000-08-11	232 Stephen Loaf Apt. 251	South Catherine	CA	79474	1
63	Michael	Collins	FM	479-095-8333x583	MichaelCollins@gmail.com	2014-12-29	67962 Jeffery Meadows	Staceytown	CA	3732	1
64	Henry	Stokes	FM	603.138.7056	HenryStokes@gmail.com	1991-01-08	879 Michael Extensions	Martinmouth	CA	1098	1
65	Eric	Lawson	FM	(783)875-5269x4996	EricLawson@hotmail.com	1983-08-26	0742 Katelyn Bypass	New Elizabeth	CA	40793	1
66	Chad	Henry	FM	294.958.0523	ChadHenry@hotmail.com	2008-10-19	689 John Center	Shelleyside	CA	98088	1
67	Joshua	Miller	FM	750.571.4073x0614	JoshuaMiller@hotmail.com	1993-10-13	5645 Lori Island	South Savannah	CA	52792	1
68	James	Moore	FM	1-170-854-7156	JamesMoore@gmail.com	1983-03-15	5148 Parks Court	Gravesburgh	CA	27605	1
69	Tyler	Johnston	FM	1-011-779-9677x024	TylerJohnston@gmail.com	1979-06-04	434 Rodriguez Ranch	Jaystad	CA	34474	1
70	Jared	Moreno	FM	736-104-1410x79150	JaredMoreno@hotmail.com	1977-05-21	38419 Neal Ridge Suite 679	South Sarahtown	CA	89627	1
71	Gary	Warner	FM	08991745382	GaryWarner@hotmail.com	2007-11-26	464 Rachel Crossroad	West Michaelbury	CA	81845	1
72	Lance	Nguyen	FM	994.545.0949x72394	LanceNguyen@hotmail.com	1981-08-07	0524 Parker Ridge	East Shelby	CA	59354	1
73	Austin	Allen	FM	819.806.6491	AustinAllen@hotmail.com	1986-02-05	57261 Nicholas Road Apt. 930	West Jennifermouth	CA	36366	1
74	Frank	Chan	FM	241.446.0763x41628	FrankChan@gmail.com	1992-04-04	767 Tammy Plains	Morrisonborough	CA	26417	1
75	Scott	Brooks	FM	(873)388-8879	ScottBrooks@gmail.com	2014-03-28	33149 Glenn Mount	Port Madisonfurt	CA	26413	1
76	Brian	Boone	FM	+55(6)9187119882	BrianBoone@gmail.com	2002-11-16	13585 Sabrina Rue	North Peterville	CA	11881	1
77	William	Hamilton	FM	+91(1)9006420643	WilliamHamilton@gmail.com	1971-08-23	44263 Steven Spurs Suite 524	East Danielburgh	CA	32150	1
78	Jason	Armstrong	FM	245.555.1293	JasonArmstrong@hotmail.com	2000-04-29	658 Young Union	New Jessefort	CA	95290	1
79	Stanley	Sullivan	FM	863.314.9125x7026	StanleySullivan@hotmail.com	2016-04-07	074 Nelson Place	North Stacy	CA	43106	1
80	Curtis	Potter	FM	(597)535-6651x511	CurtisPotter@gmail.com	2005-03-04	2368 Lopez Turnpike Apt. 026	Gilbertshire	CA	42743	1
81	Reginald	Phillips	FM	+43(5)4995092721	ReginaldPhillips@hotmail.com	1976-08-01	59913 Rivera Land	Christineville	CA	32000	1
82	Daniel	Henderson	FM	380-220-1933	DanielHenderson@gmail.com	1989-04-30	17111 White Island Suite 249	Mariaview	CA	83465	1
83	Robert	Garcia	FM	1-003-435-1355x305	RobertGarcia@hotmail.com	1976-06-28	18664 Gonzalez Mountains Suite 394	East Kimberly	CA	47840	1
84	Steve	Nunez	FM	158-467-4570	SteveNunez@hotmail.com	1984-04-06	786 Macdonald Landing	North Cherylview	CA	63790	1
85	Christopher	Wilson	FM	061.737.6424x136	ChristopherWilson@gmail.com	2003-04-02	499 Victor Hills	Reneeport	CA	71705	1
86	Christopher	Martin	FM	1-559-070-6644	ChristopherMartin@hotmail.com	2007-07-29	71152 Gordon Way	West Ronald	CA	17944	1
87	Brandon	Camacho	FM	895.398.7757x7728	BrandonCamacho@hotmail.com	2004-06-23	701 Johnson Wall Suite 036	East Shelby	CA	26255	1
88	Eugene	Rodriguez	FM	+00(4)3681756245	EugeneRodriguez@hotmail.com	1974-02-01	75595 Wells Field Suite 672	Bowmanstad	CA	29778	1
89	Javier	Ramos	FM	09464689258	JavierRamos@gmail.com	1996-12-28	059 Benjamin Skyway	East Daniellechester	CA	34431	1
90	Barry	Reid	FM	1-997-406-0182x316	BarryReid@gmail.com	1989-06-19	649 Hall Streets Apt. 262	South Donnaborough	CA	14294	1
91	Ricky	Reyes	FM	(905)377-9356x80716	RickyReyes@gmail.com	1978-12-21	4655 Anita Lane Apt. 307	Lake Sharonport	CA	18966	1
92	Matthew	Perez	FM	08404076573	MatthewPerez@gmail.com	2000-06-02	95043 Carrie Plaza	Schmidtstad	CA	92435	1
93	John	Clements	FM	029-506-6849	JohnClements@gmail.com	1993-11-20	83428 Walter Forge	Brooksberg	CA	28263	1
94	Scott	Smith	FM	735-517-9229x606	ScottSmith@gmail.com	1988-06-21	2079 Nicole Street	North Tylermouth	CA	96462	1
95	Travis	Hanson	FM	1-719-044-9489x02358	TravisHanson@gmail.com	1977-08-15	0793 Francis Corner	West James	CA	47734	1
96	Eric	Rodriguez	FM	(185)502-0722x0043	EricRodriguez@hotmail.com	1972-10-28	69041 Allen Place	East Jacob	CA	1054	1
97	Craig	Krueger	FM	962.683.0101	CraigKrueger@hotmail.com	1977-11-12	2978 William Squares	North Robertshire	CA	23373	1
98	Christopher	Pruitt	FM	606.755.4929x1866	ChristopherPruitt@gmail.com	1975-02-22	9947 Richardson Roads Suite 741	New Stephanie	CA	35784	1
99	Eric	Sharp	FM	1-492-538-9660x703	EricSharp@gmail.com	2006-05-29	2686 Deanna Spurs Suite 287	West Margaret	CA	55176	1
100	Leonard	Hutchinson	FM	618.704.6643	LeonardHutchinson@hotmail.com	2013-01-20	6848 Tonya Circles Suite 567	West Mitchellbury	CA	68631	1
\.


--
-- Name: customers_cust_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('customers_cust_id_seq', 100, true);


--
-- Data for Name: gender; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY gender (gender_code, gender_name) FROM stdin;
M	Male
FM	Female
\.


--
-- Data for Name: product_details; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY product_details (detail_id, p_id, cg_detailvalue_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	1	7
8	1	8
9	1	9
10	1	10
11	1	11
12	1	12
13	1	13
14	1	14
15	2	1
16	2	2
17	2	3
18	2	4
19	2	5
20	2	6
21	2	7
22	2	8
23	2	9
24	2	10
25	2	11
26	2	12
27	2	13
28	2	14
29	4	1
30	4	2
31	4	3
32	4	4
33	4	5
34	4	6
35	4	7
36	4	8
37	4	9
38	4	10
39	4	11
40	4	12
41	4	13
42	4	14
43	5	1
44	5	2
45	5	3
46	5	4
47	5	5
48	5	6
49	5	7
50	5	8
51	5	9
52	5	10
53	5	11
54	5	12
55	5	13
56	5	14
57	6	1
58	6	2
59	6	3
60	6	4
61	6	5
62	6	6
63	6	7
64	6	8
65	6	9
66	6	10
67	6	11
68	6	12
69	6	13
70	6	14
71	11	1
72	11	2
73	11	3
74	11	4
75	11	5
76	11	6
77	11	7
78	11	8
79	11	9
80	11	10
81	11	11
82	11	12
83	11	13
84	11	14
85	12	1
86	12	2
87	12	3
88	12	4
89	12	5
90	12	6
91	12	7
92	12	8
93	12	9
94	12	10
95	12	11
96	12	12
97	12	13
98	12	14
99	13	1
100	13	2
101	13	3
102	13	4
103	13	5
104	13	6
105	13	7
106	13	8
107	13	9
108	13	10
109	13	11
110	13	12
111	13	13
112	13	14
113	16	1
114	16	2
115	16	3
116	16	4
117	16	5
118	16	6
119	16	7
120	16	8
121	16	9
122	16	10
123	16	11
124	16	12
125	16	13
126	16	14
127	17	1
128	17	2
129	17	3
130	17	4
131	17	5
132	17	6
133	17	7
134	17	8
135	17	9
136	17	10
137	17	11
138	17	12
139	17	13
140	17	14
141	21	1
142	21	2
143	21	3
144	21	4
145	21	5
146	21	6
147	21	7
148	21	8
149	21	9
150	21	10
151	21	11
152	21	12
153	21	13
154	21	14
155	22	1
156	22	2
157	22	3
158	22	4
159	22	5
160	22	6
161	22	7
162	22	8
163	22	9
164	22	10
165	22	11
166	22	12
167	22	13
168	22	14
169	23	1
170	23	2
171	23	3
172	23	4
173	23	5
174	23	6
175	23	7
176	23	8
177	23	9
178	23	10
179	23	11
180	23	12
181	23	13
182	23	14
183	25	1
184	25	2
185	25	3
186	25	4
187	25	5
188	25	6
189	25	7
190	25	8
191	25	9
192	25	10
193	25	11
194	25	12
195	25	13
196	25	14
197	26	1
198	26	2
199	26	3
200	26	4
201	26	5
202	26	6
203	26	7
204	26	8
205	26	9
206	26	10
207	26	11
208	26	12
209	26	13
210	26	14
211	27	1
212	27	2
213	27	3
214	27	4
215	27	5
216	27	6
217	27	7
218	27	8
219	27	9
220	27	10
221	27	11
222	27	12
223	27	13
224	27	14
225	28	1
226	28	2
227	28	3
228	28	4
229	28	5
230	28	6
231	28	7
232	28	8
233	28	9
234	28	10
235	28	11
236	28	12
237	28	13
238	28	14
239	30	1
240	30	2
241	30	3
242	30	4
243	30	5
244	30	6
245	30	7
246	30	8
247	30	9
248	30	10
249	30	11
250	30	12
251	30	13
252	30	14
253	31	1
254	31	2
255	31	3
256	31	4
257	31	5
258	31	6
259	31	7
260	31	8
261	31	9
262	31	10
263	31	11
264	31	12
265	31	13
266	31	14
267	33	1
268	33	2
269	33	3
270	33	4
271	33	5
272	33	6
273	33	7
274	33	8
275	33	9
276	33	10
277	33	11
278	33	12
279	33	13
280	33	14
281	36	1
282	36	2
283	36	3
284	36	4
285	36	5
286	36	6
287	36	7
288	36	8
289	36	9
290	36	10
291	36	11
292	36	12
293	36	13
294	36	14
295	37	1
296	37	2
297	37	3
298	37	4
299	37	5
300	37	6
301	37	7
302	37	8
303	37	9
304	37	10
305	37	11
306	37	12
307	37	13
308	37	14
309	40	1
310	40	2
311	40	3
312	40	4
313	40	5
314	40	6
315	40	7
316	40	8
317	40	9
318	40	10
319	40	11
320	40	12
321	40	13
322	40	14
323	43	1
324	43	2
325	43	3
326	43	4
327	43	5
328	43	6
329	43	7
330	43	8
331	43	9
332	43	10
333	43	11
334	43	12
335	43	13
336	43	14
337	44	1
338	44	2
339	44	3
340	44	4
341	44	5
342	44	6
343	44	7
344	44	8
345	44	9
346	44	10
347	44	11
348	44	12
349	44	13
350	44	14
351	47	1
352	47	2
353	47	3
354	47	4
355	47	5
356	47	6
357	47	7
358	47	8
359	47	9
360	47	10
361	47	11
362	47	12
363	47	13
364	47	14
365	50	1
366	50	2
367	50	3
368	50	4
369	50	5
370	50	6
371	50	7
372	50	8
373	50	9
374	50	10
375	50	11
376	50	12
377	50	13
378	50	14
379	51	1
380	51	2
381	51	3
382	51	4
383	51	5
384	51	6
385	51	7
386	51	8
387	51	9
388	51	10
389	51	11
390	51	12
391	51	13
392	51	14
393	54	1
394	54	2
395	54	3
396	54	4
397	54	5
398	54	6
399	54	7
400	54	8
401	54	9
402	54	10
403	54	11
404	54	12
405	54	13
406	54	14
407	57	1
408	57	2
409	57	3
410	57	4
411	57	5
412	57	6
413	57	7
414	57	8
415	57	9
416	57	10
417	57	11
418	57	12
419	57	13
420	57	14
421	58	1
422	58	2
423	58	3
424	58	4
425	58	5
426	58	6
427	58	7
428	58	8
429	58	9
430	58	10
431	58	11
432	58	12
433	58	13
434	58	14
435	60	1
436	60	2
437	60	3
438	60	4
439	60	5
440	60	6
441	60	7
442	60	8
443	60	9
444	60	10
445	60	11
446	60	12
447	60	13
448	60	14
449	65	1
450	65	2
451	65	3
452	65	4
453	65	5
454	65	6
455	65	7
456	65	8
457	65	9
458	65	10
459	65	11
460	65	12
461	65	13
462	65	14
463	66	1
464	66	2
465	66	3
466	66	4
467	66	5
468	66	6
469	66	7
470	66	8
471	66	9
472	66	10
473	66	11
474	66	12
475	66	13
476	66	14
477	67	1
478	67	2
479	67	3
480	67	4
481	67	5
482	67	6
483	67	7
484	67	8
485	67	9
486	67	10
487	67	11
488	67	12
489	67	13
490	67	14
491	68	1
492	68	2
493	68	3
494	68	4
495	68	5
496	68	6
497	68	7
498	68	8
499	68	9
500	68	10
501	68	11
502	68	12
503	68	13
504	68	14
505	69	1
506	69	2
507	69	3
508	69	4
509	69	5
510	69	6
511	69	7
512	69	8
513	69	9
514	69	10
515	69	11
516	69	12
517	69	13
518	69	14
519	71	1
520	71	2
521	71	3
522	71	4
523	71	5
524	71	6
525	71	7
526	71	8
527	71	9
528	71	10
529	71	11
530	71	12
531	71	13
532	71	14
533	73	1
534	73	2
535	73	3
536	73	4
537	73	5
538	73	6
539	73	7
540	73	8
541	73	9
542	73	10
543	73	11
544	73	12
545	73	13
546	73	14
547	74	1
548	74	2
549	74	3
550	74	4
551	74	5
552	74	6
553	74	7
554	74	8
555	74	9
556	74	10
557	74	11
558	74	12
559	74	13
560	74	14
561	76	1
562	76	2
563	76	3
564	76	4
565	76	5
566	76	6
567	76	7
568	76	8
569	76	9
570	76	10
571	76	11
572	76	12
573	76	13
574	76	14
575	77	1
576	77	2
577	77	3
578	77	4
579	77	5
580	77	6
581	77	7
582	77	8
583	77	9
584	77	10
585	77	11
586	77	12
587	77	13
588	77	14
589	81	1
590	81	2
591	81	3
592	81	4
593	81	5
594	81	6
595	81	7
596	81	8
597	81	9
598	81	10
599	81	11
600	81	12
601	81	13
602	81	14
603	82	1
604	82	2
605	82	3
606	82	4
607	82	5
608	82	6
609	82	7
610	82	8
611	82	9
612	82	10
613	82	11
614	82	12
615	82	13
616	82	14
617	84	1
618	84	2
619	84	3
620	84	4
621	84	5
622	84	6
623	84	7
624	84	8
625	84	9
626	84	10
627	84	11
628	84	12
629	84	13
630	84	14
631	86	1
632	86	2
633	86	3
634	86	4
635	86	5
636	86	6
637	86	7
638	86	8
639	86	9
640	86	10
641	86	11
642	86	12
643	86	13
644	86	14
645	88	1
646	88	2
647	88	3
648	88	4
649	88	5
650	88	6
651	88	7
652	88	8
653	88	9
654	88	10
655	88	11
656	88	12
657	88	13
658	88	14
659	89	1
660	89	2
661	89	3
662	89	4
663	89	5
664	89	6
665	89	7
666	89	8
667	89	9
668	89	10
669	89	11
670	89	12
671	89	13
672	89	14
673	90	1
674	90	2
675	90	3
676	90	4
677	90	5
678	90	6
679	90	7
680	90	8
681	90	9
682	90	10
683	90	11
684	90	12
685	90	13
686	90	14
687	92	1
688	92	2
689	92	3
690	92	4
691	92	5
692	92	6
693	92	7
694	92	8
695	92	9
696	92	10
697	92	11
698	92	12
699	92	13
700	92	14
701	95	1
702	95	2
703	95	3
704	95	4
705	95	5
706	95	6
707	95	7
708	95	8
709	95	9
710	95	10
711	95	11
712	95	12
713	95	13
714	95	14
715	96	1
716	96	2
717	96	3
718	96	4
719	96	5
720	96	6
721	96	7
722	96	8
723	96	9
724	96	10
725	96	11
726	96	12
727	96	13
728	96	14
729	98	1
730	98	2
731	98	3
732	98	4
733	98	5
734	98	6
735	98	7
736	98	8
737	98	9
738	98	10
739	98	11
740	98	12
741	98	13
742	98	14
743	99	1
744	99	2
745	99	3
746	99	4
747	99	5
748	99	6
749	99	7
750	99	8
751	99	9
752	99	10
753	99	11
754	99	12
755	99	13
756	99	14
757	101	1
758	101	2
759	101	3
760	101	4
761	101	5
762	101	6
763	101	7
764	101	8
765	101	9
766	101	10
767	101	11
768	101	12
769	101	13
770	101	14
771	102	1
772	102	2
773	102	3
774	102	4
775	102	5
776	102	6
777	102	7
778	102	8
779	102	9
780	102	10
781	102	11
782	102	12
783	102	13
784	102	14
785	103	1
786	103	2
787	103	3
788	103	4
789	103	5
790	103	6
791	103	7
792	103	8
793	103	9
794	103	10
795	103	11
796	103	12
797	103	13
798	103	14
799	104	1
800	104	2
801	104	3
802	104	4
803	104	5
804	104	6
805	104	7
806	104	8
807	104	9
808	104	10
809	104	11
810	104	12
811	104	13
812	104	14
813	106	1
814	106	2
815	106	3
816	106	4
817	106	5
818	106	6
819	106	7
820	106	8
821	106	9
822	106	10
823	106	11
824	106	12
825	106	13
826	106	14
827	107	1
828	107	2
829	107	3
830	107	4
831	107	5
832	107	6
833	107	7
834	107	8
835	107	9
836	107	10
837	107	11
838	107	12
839	107	13
840	107	14
841	110	1
842	110	2
843	110	3
844	110	4
845	110	5
846	110	6
847	110	7
848	110	8
849	110	9
850	110	10
851	110	11
852	110	12
853	110	13
854	110	14
855	114	1
856	114	2
857	114	3
858	114	4
859	114	5
860	114	6
861	114	7
862	114	8
863	114	9
864	114	10
865	114	11
866	114	12
867	114	13
868	114	14
869	115	1
870	115	2
871	115	3
872	115	4
873	115	5
874	115	6
875	115	7
876	115	8
877	115	9
878	115	10
879	115	11
880	115	12
881	115	13
882	115	14
883	117	1
884	117	2
885	117	3
886	117	4
887	117	5
888	117	6
889	117	7
890	117	8
891	117	9
892	117	10
893	117	11
894	117	12
895	117	13
896	117	14
897	119	1
898	119	2
899	119	3
900	119	4
901	119	5
902	119	6
903	119	7
904	119	8
905	119	9
906	119	10
907	119	11
908	119	12
909	119	13
910	119	14
911	120	1
912	120	2
913	120	3
914	120	4
915	120	5
916	120	6
917	120	7
918	120	8
919	120	9
920	120	10
921	120	11
922	120	12
923	120	13
924	120	14
925	122	1
926	122	2
927	122	3
928	122	4
929	122	5
930	122	6
931	122	7
932	122	8
933	122	9
934	122	10
935	122	11
936	122	12
937	122	13
938	122	14
939	123	1
940	123	2
941	123	3
942	123	4
943	123	5
944	123	6
945	123	7
946	123	8
947	123	9
948	123	10
949	123	11
950	123	12
951	123	13
952	123	14
953	127	1
954	127	2
955	127	3
956	127	4
957	127	5
958	127	6
959	127	7
960	127	8
961	127	9
962	127	10
963	127	11
964	127	12
965	127	13
966	127	14
967	131	1
968	131	2
969	131	3
970	131	4
971	131	5
972	131	6
973	131	7
974	131	8
975	131	9
976	131	10
977	131	11
978	131	12
979	131	13
980	131	14
981	134	1
982	134	2
983	134	3
984	134	4
985	134	5
986	134	6
987	134	7
988	134	8
989	134	9
990	134	10
991	134	11
992	134	12
993	134	13
994	134	14
995	135	1
996	135	2
997	135	3
998	135	4
999	135	5
1000	135	6
1001	135	7
1002	135	8
1003	135	9
1004	135	10
1005	135	11
1006	135	12
1007	135	13
1008	135	14
1009	140	1
1010	140	2
1011	140	3
1012	140	4
1013	140	5
1014	140	6
1015	140	7
1016	140	8
1017	140	9
1018	140	10
1019	140	11
1020	140	12
1021	140	13
1022	140	14
1023	141	1
1024	141	2
1025	141	3
1026	141	4
1027	141	5
1028	141	6
1029	141	7
1030	141	8
1031	141	9
1032	141	10
1033	141	11
1034	141	12
1035	141	13
1036	141	14
1037	142	1
1038	142	2
1039	142	3
1040	142	4
1041	142	5
1042	142	6
1043	142	7
1044	142	8
1045	142	9
1046	142	10
1047	142	11
1048	142	12
1049	142	13
1050	142	14
1051	143	1
1052	143	2
1053	143	3
1054	143	4
1055	143	5
1056	143	6
1057	143	7
1058	143	8
1059	143	9
1060	143	10
1061	143	11
1062	143	12
1063	143	13
1064	143	14
1065	146	1
1066	146	2
1067	146	3
1068	146	4
1069	146	5
1070	146	6
1071	146	7
1072	146	8
1073	146	9
1074	146	10
1075	146	11
1076	146	12
1077	146	13
1078	146	14
1079	149	1
1080	149	2
1081	149	3
1082	149	4
1083	149	5
1084	149	6
1085	149	7
1086	149	8
1087	149	9
1088	149	10
1089	149	11
1090	149	12
1091	149	13
1092	149	14
1093	150	1
1094	150	2
1095	150	3
1096	150	4
1097	150	5
1098	150	6
1099	150	7
1100	150	8
1101	150	9
1102	150	10
1103	150	11
1104	150	12
1105	150	13
1106	150	14
1107	157	1
1108	157	2
1109	157	3
1110	157	4
1111	157	5
1112	157	6
1113	157	7
1114	157	8
1115	157	9
1116	157	10
1117	157	11
1118	157	12
1119	157	13
1120	157	14
1121	159	1
1122	159	2
1123	159	3
1124	159	4
1125	159	5
1126	159	6
1127	159	7
1128	159	8
1129	159	9
1130	159	10
1131	159	11
1132	159	12
1133	159	13
1134	159	14
1135	160	1
1136	160	2
1137	160	3
1138	160	4
1139	160	5
1140	160	6
1141	160	7
1142	160	8
1143	160	9
1144	160	10
1145	160	11
1146	160	12
1147	160	13
1148	160	14
1149	161	1
1150	161	2
1151	161	3
1152	161	4
1153	161	5
1154	161	6
1155	161	7
1156	161	8
1157	161	9
1158	161	10
1159	161	11
1160	161	12
1161	161	13
1162	161	14
1163	162	1
1164	162	2
1165	162	3
1166	162	4
1167	162	5
1168	162	6
1169	162	7
1170	162	8
1171	162	9
1172	162	10
1173	162	11
1174	162	12
1175	162	13
1176	162	14
1177	163	1
1178	163	2
1179	163	3
1180	163	4
1181	163	5
1182	163	6
1183	163	7
1184	163	8
1185	163	9
1186	163	10
1187	163	11
1188	163	12
1189	163	13
1190	163	14
1191	164	1
1192	164	2
1193	164	3
1194	164	4
1195	164	5
1196	164	6
1197	164	7
1198	164	8
1199	164	9
1200	164	10
1201	164	11
1202	164	12
1203	164	13
1204	164	14
1205	165	1
1206	165	2
1207	165	3
1208	165	4
1209	165	5
1210	165	6
1211	165	7
1212	165	8
1213	165	9
1214	165	10
1215	165	11
1216	165	12
1217	165	13
1218	165	14
1219	167	1
1220	167	2
1221	167	3
1222	167	4
1223	167	5
1224	167	6
1225	167	7
1226	167	8
1227	167	9
1228	167	10
1229	167	11
1230	167	12
1231	167	13
1232	167	14
1233	170	1
1234	170	2
1235	170	3
1236	170	4
1237	170	5
1238	170	6
1239	170	7
1240	170	8
1241	170	9
1242	170	10
1243	170	11
1244	170	12
1245	170	13
1246	170	14
1247	172	1
1248	172	2
1249	172	3
1250	172	4
1251	172	5
1252	172	6
1253	172	7
1254	172	8
1255	172	9
1256	172	10
1257	172	11
1258	172	12
1259	172	13
1260	172	14
1261	3	15
1262	3	16
1263	3	17
1264	3	18
1265	3	19
1266	3	20
1267	3	21
1268	3	22
1269	3	23
1270	3	24
1271	3	25
1272	7	15
1273	7	16
1274	7	17
1275	7	18
1276	7	19
1277	7	20
1278	7	21
1279	7	22
1280	7	23
1281	7	24
1282	7	25
1283	8	15
1284	8	16
1285	8	17
1286	8	18
1287	8	19
1288	8	20
1289	8	21
1290	8	22
1291	8	23
1292	8	24
1293	8	25
1294	9	15
1295	9	16
1296	9	17
1297	9	18
1298	9	19
1299	9	20
1300	9	21
1301	9	22
1302	9	23
1303	9	24
1304	9	25
1305	10	15
1306	10	16
1307	10	17
1308	10	18
1309	10	19
1310	10	20
1311	10	21
1312	10	22
1313	10	23
1314	10	24
1315	10	25
1316	14	15
1317	14	16
1318	14	17
1319	14	18
1320	14	19
1321	14	20
1322	14	21
1323	14	22
1324	14	23
1325	14	24
1326	14	25
1327	15	15
1328	15	16
1329	15	17
1330	15	18
1331	15	19
1332	15	20
1333	15	21
1334	15	22
1335	15	23
1336	15	24
1337	15	25
1338	18	15
1339	18	16
1340	18	17
1341	18	18
1342	18	19
1343	18	20
1344	18	21
1345	18	22
1346	18	23
1347	18	24
1348	18	25
1349	19	15
1350	19	16
1351	19	17
1352	19	18
1353	19	19
1354	19	20
1355	19	21
1356	19	22
1357	19	23
1358	19	24
1359	19	25
1360	20	15
1361	20	16
1362	20	17
1363	20	18
1364	20	19
1365	20	20
1366	20	21
1367	20	22
1368	20	23
1369	20	24
1370	20	25
1371	24	15
1372	24	16
1373	24	17
1374	24	18
1375	24	19
1376	24	20
1377	24	21
1378	24	22
1379	24	23
1380	24	24
1381	24	25
1382	29	15
1383	29	16
1384	29	17
1385	29	18
1386	29	19
1387	29	20
1388	29	21
1389	29	22
1390	29	23
1391	29	24
1392	29	25
1393	32	15
1394	32	16
1395	32	17
1396	32	18
1397	32	19
1398	32	20
1399	32	21
1400	32	22
1401	32	23
1402	32	24
1403	32	25
1404	34	15
1405	34	16
1406	34	17
1407	34	18
1408	34	19
1409	34	20
1410	34	21
1411	34	22
1412	34	23
1413	34	24
1414	34	25
1415	35	15
1416	35	16
1417	35	17
1418	35	18
1419	35	19
1420	35	20
1421	35	21
1422	35	22
1423	35	23
1424	35	24
1425	35	25
1426	38	15
1427	38	16
1428	38	17
1429	38	18
1430	38	19
1431	38	20
1432	38	21
1433	38	22
1434	38	23
1435	38	24
1436	38	25
1437	39	15
1438	39	16
1439	39	17
1440	39	18
1441	39	19
1442	39	20
1443	39	21
1444	39	22
1445	39	23
1446	39	24
1447	39	25
1448	41	15
1449	41	16
1450	41	17
1451	41	18
1452	41	19
1453	41	20
1454	41	21
1455	41	22
1456	41	23
1457	41	24
1458	41	25
1459	42	15
1460	42	16
1461	42	17
1462	42	18
1463	42	19
1464	42	20
1465	42	21
1466	42	22
1467	42	23
1468	42	24
1469	42	25
1470	45	15
1471	45	16
1472	45	17
1473	45	18
1474	45	19
1475	45	20
1476	45	21
1477	45	22
1478	45	23
1479	45	24
1480	45	25
1481	46	15
1482	46	16
1483	46	17
1484	46	18
1485	46	19
1486	46	20
1487	46	21
1488	46	22
1489	46	23
1490	46	24
1491	46	25
1492	48	15
1493	48	16
1494	48	17
1495	48	18
1496	48	19
1497	48	20
1498	48	21
1499	48	22
1500	48	23
1501	48	24
1502	48	25
1503	49	15
1504	49	16
1505	49	17
1506	49	18
1507	49	19
1508	49	20
1509	49	21
1510	49	22
1511	49	23
1512	49	24
1513	49	25
1514	52	15
1515	52	16
1516	52	17
1517	52	18
1518	52	19
1519	52	20
1520	52	21
1521	52	22
1522	52	23
1523	52	24
1524	52	25
1525	53	15
1526	53	16
1527	53	17
1528	53	18
1529	53	19
1530	53	20
1531	53	21
1532	53	22
1533	53	23
1534	53	24
1535	53	25
1536	55	15
1537	55	16
1538	55	17
1539	55	18
1540	55	19
1541	55	20
1542	55	21
1543	55	22
1544	55	23
1545	55	24
1546	55	25
1547	56	15
1548	56	16
1549	56	17
1550	56	18
1551	56	19
1552	56	20
1553	56	21
1554	56	22
1555	56	23
1556	56	24
1557	56	25
1558	59	15
1559	59	16
1560	59	17
1561	59	18
1562	59	19
1563	59	20
1564	59	21
1565	59	22
1566	59	23
1567	59	24
1568	59	25
1569	61	15
1570	61	16
1571	61	17
1572	61	18
1573	61	19
1574	61	20
1575	61	21
1576	61	22
1577	61	23
1578	61	24
1579	61	25
1580	62	15
1581	62	16
1582	62	17
1583	62	18
1584	62	19
1585	62	20
1586	62	21
1587	62	22
1588	62	23
1589	62	24
1590	62	25
1591	63	15
1592	63	16
1593	63	17
1594	63	18
1595	63	19
1596	63	20
1597	63	21
1598	63	22
1599	63	23
1600	63	24
1601	63	25
1602	64	15
1603	64	16
1604	64	17
1605	64	18
1606	64	19
1607	64	20
1608	64	21
1609	64	22
1610	64	23
1611	64	24
1612	64	25
1613	70	15
1614	70	16
1615	70	17
1616	70	18
1617	70	19
1618	70	20
1619	70	21
1620	70	22
1621	70	23
1622	70	24
1623	70	25
1624	72	15
1625	72	16
1626	72	17
1627	72	18
1628	72	19
1629	72	20
1630	72	21
1631	72	22
1632	72	23
1633	72	24
1634	72	25
1635	75	15
1636	75	16
1637	75	17
1638	75	18
1639	75	19
1640	75	20
1641	75	21
1642	75	22
1643	75	23
1644	75	24
1645	75	25
1646	78	15
1647	78	16
1648	78	17
1649	78	18
1650	78	19
1651	78	20
1652	78	21
1653	78	22
1654	78	23
1655	78	24
1656	78	25
1657	79	15
1658	79	16
1659	79	17
1660	79	18
1661	79	19
1662	79	20
1663	79	21
1664	79	22
1665	79	23
1666	79	24
1667	79	25
1668	80	15
1669	80	16
1670	80	17
1671	80	18
1672	80	19
1673	80	20
1674	80	21
1675	80	22
1676	80	23
1677	80	24
1678	80	25
1679	83	15
1680	83	16
1681	83	17
1682	83	18
1683	83	19
1684	83	20
1685	83	21
1686	83	22
1687	83	23
1688	83	24
1689	83	25
1690	85	15
1691	85	16
1692	85	17
1693	85	18
1694	85	19
1695	85	20
1696	85	21
1697	85	22
1698	85	23
1699	85	24
1700	85	25
1701	87	15
1702	87	16
1703	87	17
1704	87	18
1705	87	19
1706	87	20
1707	87	21
1708	87	22
1709	87	23
1710	87	24
1711	87	25
1712	91	15
1713	91	16
1714	91	17
1715	91	18
1716	91	19
1717	91	20
1718	91	21
1719	91	22
1720	91	23
1721	91	24
1722	91	25
1723	93	15
1724	93	16
1725	93	17
1726	93	18
1727	93	19
1728	93	20
1729	93	21
1730	93	22
1731	93	23
1732	93	24
1733	93	25
1734	94	15
1735	94	16
1736	94	17
1737	94	18
1738	94	19
1739	94	20
1740	94	21
1741	94	22
1742	94	23
1743	94	24
1744	94	25
1745	97	15
1746	97	16
1747	97	17
1748	97	18
1749	97	19
1750	97	20
1751	97	21
1752	97	22
1753	97	23
1754	97	24
1755	97	25
1756	100	15
1757	100	16
1758	100	17
1759	100	18
1760	100	19
1761	100	20
1762	100	21
1763	100	22
1764	100	23
1765	100	24
1766	100	25
1767	105	15
1768	105	16
1769	105	17
1770	105	18
1771	105	19
1772	105	20
1773	105	21
1774	105	22
1775	105	23
1776	105	24
1777	105	25
1778	108	15
1779	108	16
1780	108	17
1781	108	18
1782	108	19
1783	108	20
1784	108	21
1785	108	22
1786	108	23
1787	108	24
1788	108	25
1789	109	15
1790	109	16
1791	109	17
1792	109	18
1793	109	19
1794	109	20
1795	109	21
1796	109	22
1797	109	23
1798	109	24
1799	109	25
1800	111	15
1801	111	16
1802	111	17
1803	111	18
1804	111	19
1805	111	20
1806	111	21
1807	111	22
1808	111	23
1809	111	24
1810	111	25
1811	112	15
1812	112	16
1813	112	17
1814	112	18
1815	112	19
1816	112	20
1817	112	21
1818	112	22
1819	112	23
1820	112	24
1821	112	25
1822	113	15
1823	113	16
1824	113	17
1825	113	18
1826	113	19
1827	113	20
1828	113	21
1829	113	22
1830	113	23
1831	113	24
1832	113	25
1833	116	15
1834	116	16
1835	116	17
1836	116	18
1837	116	19
1838	116	20
1839	116	21
1840	116	22
1841	116	23
1842	116	24
1843	116	25
1844	118	15
1845	118	16
1846	118	17
1847	118	18
1848	118	19
1849	118	20
1850	118	21
1851	118	22
1852	118	23
1853	118	24
1854	118	25
1855	121	15
1856	121	16
1857	121	17
1858	121	18
1859	121	19
1860	121	20
1861	121	21
1862	121	22
1863	121	23
1864	121	24
1865	121	25
1866	124	15
1867	124	16
1868	124	17
1869	124	18
1870	124	19
1871	124	20
1872	124	21
1873	124	22
1874	124	23
1875	124	24
1876	124	25
1877	125	15
1878	125	16
1879	125	17
1880	125	18
1881	125	19
1882	125	20
1883	125	21
1884	125	22
1885	125	23
1886	125	24
1887	125	25
1888	126	15
1889	126	16
1890	126	17
1891	126	18
1892	126	19
1893	126	20
1894	126	21
1895	126	22
1896	126	23
1897	126	24
1898	126	25
1899	128	15
1900	128	16
1901	128	17
1902	128	18
1903	128	19
1904	128	20
1905	128	21
1906	128	22
1907	128	23
1908	128	24
1909	128	25
1910	129	15
1911	129	16
1912	129	17
1913	129	18
1914	129	19
1915	129	20
1916	129	21
1917	129	22
1918	129	23
1919	129	24
1920	129	25
1921	130	15
1922	130	16
1923	130	17
1924	130	18
1925	130	19
1926	130	20
1927	130	21
1928	130	22
1929	130	23
1930	130	24
1931	130	25
1932	132	15
1933	132	16
1934	132	17
1935	132	18
1936	132	19
1937	132	20
1938	132	21
1939	132	22
1940	132	23
1941	132	24
1942	132	25
1943	133	15
1944	133	16
1945	133	17
1946	133	18
1947	133	19
1948	133	20
1949	133	21
1950	133	22
1951	133	23
1952	133	24
1953	133	25
1954	136	15
1955	136	16
1956	136	17
1957	136	18
1958	136	19
1959	136	20
1960	136	21
1961	136	22
1962	136	23
1963	136	24
1964	136	25
1965	137	15
1966	137	16
1967	137	17
1968	137	18
1969	137	19
1970	137	20
1971	137	21
1972	137	22
1973	137	23
1974	137	24
1975	137	25
1976	138	15
1977	138	16
1978	138	17
1979	138	18
1980	138	19
1981	138	20
1982	138	21
1983	138	22
1984	138	23
1985	138	24
1986	138	25
1987	139	15
1988	139	16
1989	139	17
1990	139	18
1991	139	19
1992	139	20
1993	139	21
1994	139	22
1995	139	23
1996	139	24
1997	139	25
1998	144	15
1999	144	16
2000	144	17
2001	144	18
2002	144	19
2003	144	20
2004	144	21
2005	144	22
2006	144	23
2007	144	24
2008	144	25
2009	145	15
2010	145	16
2011	145	17
2012	145	18
2013	145	19
2014	145	20
2015	145	21
2016	145	22
2017	145	23
2018	145	24
2019	145	25
2020	147	15
2021	147	16
2022	147	17
2023	147	18
2024	147	19
2025	147	20
2026	147	21
2027	147	22
2028	147	23
2029	147	24
2030	147	25
2031	148	15
2032	148	16
2033	148	17
2034	148	18
2035	148	19
2036	148	20
2037	148	21
2038	148	22
2039	148	23
2040	148	24
2041	148	25
2042	151	15
2043	151	16
2044	151	17
2045	151	18
2046	151	19
2047	151	20
2048	151	21
2049	151	22
2050	151	23
2051	151	24
2052	151	25
2053	152	15
2054	152	16
2055	152	17
2056	152	18
2057	152	19
2058	152	20
2059	152	21
2060	152	22
2061	152	23
2062	152	24
2063	152	25
2064	153	15
2065	153	16
2066	153	17
2067	153	18
2068	153	19
2069	153	20
2070	153	21
2071	153	22
2072	153	23
2073	153	24
2074	153	25
2075	154	15
2076	154	16
2077	154	17
2078	154	18
2079	154	19
2080	154	20
2081	154	21
2082	154	22
2083	154	23
2084	154	24
2085	154	25
2086	155	15
2087	155	16
2088	155	17
2089	155	18
2090	155	19
2091	155	20
2092	155	21
2093	155	22
2094	155	23
2095	155	24
2096	155	25
2097	156	15
2098	156	16
2099	156	17
2100	156	18
2101	156	19
2102	156	20
2103	156	21
2104	156	22
2105	156	23
2106	156	24
2107	156	25
2108	158	15
2109	158	16
2110	158	17
2111	158	18
2112	158	19
2113	158	20
2114	158	21
2115	158	22
2116	158	23
2117	158	24
2118	158	25
2119	166	15
2120	166	16
2121	166	17
2122	166	18
2123	166	19
2124	166	20
2125	166	21
2126	166	22
2127	166	23
2128	166	24
2129	166	25
2130	168	15
2131	168	16
2132	168	17
2133	168	18
2134	168	19
2135	168	20
2136	168	21
2137	168	22
2138	168	23
2139	168	24
2140	168	25
2141	169	15
2142	169	16
2143	169	17
2144	169	18
2145	169	19
2146	169	20
2147	169	21
2148	169	22
2149	169	23
2150	169	24
2151	169	25
2152	171	15
2153	171	16
2154	171	17
2155	171	18
2156	171	19
2157	171	20
2158	171	21
2159	171	22
2160	171	23
2161	171	24
2162	171	25
2163	173	15
2164	173	16
2165	173	17
2166	173	18
2167	173	19
2168	173	20
2169	173	21
2170	173	22
2171	173	23
2172	173	24
2173	173	25
\.


--
-- Name: product_details_detail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('product_details_detail_id_seq', 2173, true);


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY products (p_id, cg_id, user_id, purchase_at, purchase_price, cust_id, sale_price, sold_at, returned_at) FROM stdin;
1	1	1	2017-02-26 16:48:39	60	54	157	2017-03-19 16:48:39	\N
2	1	1	2016-08-24 06:52:44	44	94	137	2016-10-13 06:52:44	\N
3	2	1	2016-09-18 23:23:49	20	41	56	2016-11-05 23:23:49	\N
4	1	1	2016-07-04 16:33:58	61	61	135	2016-08-16 16:33:58	\N
5	1	1	2017-02-21 21:18:45	41	11	110	2017-03-06 21:18:45	\N
6	1	1	2016-07-10 11:37:48	20	80	78	2016-07-26 11:37:48	\N
7	2	1	2016-12-19 11:22:03	81	52	113	2016-12-22 11:22:03	\N
8	2	1	2016-11-24 14:28:24	95	81	190	2017-01-11 14:28:24	\N
9	2	1	2016-07-31 21:46:27	26	64	58	2016-09-05 21:46:27	\N
10	2	1	2016-07-23 05:30:57	65	84	95	2016-07-25 05:30:57	\N
11	1	1	2017-01-25 22:06:31	63	33	135	2017-03-10 22:06:31	\N
12	1	1	2017-03-06 10:08:43	53	74	150	2017-03-07 10:08:43	\N
13	1	1	2016-09-13 21:17:52	23	23	89	2016-11-11 21:17:52	\N
14	2	1	2017-06-14 05:50:55	56	82	130	2017-07-08 05:50:55	\N
15	2	1	2016-07-23 18:59:19	57	9	99	2016-09-17 18:59:19	\N
16	1	1	2017-01-27 07:42:50	46	53	89	2017-02-11 07:42:50	\N
17	1	1	2017-04-29 19:17:21	77	94	115	2017-06-28 19:17:21	\N
18	2	1	2017-04-05 19:42:35	63	18	156	2017-04-12 19:42:35	\N
19	2	1	2016-10-21 14:34:27	80	56	170	2016-11-24 14:34:27	\N
20	2	1	2017-03-06 13:04:07	48	6	133	2017-05-06 13:04:07	\N
21	1	1	2017-03-16 09:44:17	22	77	106	2017-05-12 09:44:17	\N
22	1	1	2016-07-29 22:41:09	90	67	169	2016-09-19 22:41:09	\N
23	1	1	2016-07-21 10:52:47	54	28	140	2016-09-03 10:52:47	\N
24	2	1	2017-01-10 12:18:29	81	33	128	2017-03-05 12:18:29	\N
25	1	1	2017-01-12 13:42:35	97	43	128	2017-03-05 13:42:35	\N
26	1	1	2016-07-11 04:14:54	36	56	110	2016-07-24 04:14:54	\N
27	1	1	2017-03-12 14:41:58	96	91	132	2017-04-20 14:41:58	\N
28	1	1	2017-02-01 00:12:04	70	70	114	2017-03-09 00:12:04	\N
29	2	1	2016-08-17 16:35:46	47	38	84	2016-10-14 16:35:46	\N
30	1	1	2016-12-12 12:51:05	87	96	159	2016-12-15 12:51:05	\N
31	1	1	2016-10-15 19:49:03	99	36	181	2016-12-01 19:49:03	\N
32	2	1	2017-04-25 08:01:42	63	63	138	2017-06-13 08:01:42	\N
33	1	1	2016-07-09 14:07:26	69	26	101	2016-07-23 14:07:26	\N
34	2	1	2016-09-04 00:37:11	94	54	170	2016-10-19 00:37:11	\N
35	2	1	2017-01-05 14:27:12	70	11	141	2017-01-18 14:27:12	\N
36	1	1	2017-05-31 03:32:09	48	10	129	2017-07-20 03:32:09	\N
37	1	1	2016-09-22 08:16:55	51	38	137	2016-10-14 08:16:55	\N
38	2	1	2017-05-03 00:57:51	15	81	74	2017-07-01 00:57:51	\N
39	2	1	2016-12-19 23:25:46	17	66	76	2016-12-29 23:25:46	\N
40	1	1	2016-06-29 03:28:18	98	77	184	2016-08-26 03:28:18	\N
41	2	1	2016-10-24 12:18:38	64	39	144	2016-12-24 12:18:38	\N
42	2	1	2017-03-03 06:27:20	62	8	134	2017-03-05 06:27:20	\N
43	1	1	2017-06-01 21:09:22	39	39	114	2017-06-14 21:09:22	\N
44	1	1	2016-08-27 02:02:38	20	72	87	2016-09-01 02:02:38	\N
45	2	1	2017-04-11 08:16:35	24	78	65	2017-05-13 08:16:35	\N
46	2	1	2017-05-18 21:08:55	81	29	133	2017-07-16 21:08:55	\N
47	1	1	2017-01-12 17:48:00	74	77	133	2017-03-13 17:48:00	\N
48	2	1	2017-02-15 09:06:39	33	80	133	2017-04-14 09:06:39	\N
49	2	1	2016-12-10 14:27:34	31	19	129	2017-01-17 14:27:34	\N
50	1	1	2017-06-17 12:18:20	91	1	191	2017-07-21 12:18:20	\N
51	1	1	2017-06-12 10:17:46	84	75	153	2017-06-13 10:17:46	\N
52	2	1	2016-10-08 14:21:20	61	62	102	2016-12-08 14:21:20	\N
53	2	1	2017-02-22 04:25:58	65	23	144	2017-04-19 04:25:58	\N
54	1	1	2017-04-24 15:34:26	36	65	97	2017-05-14 15:34:26	\N
55	2	1	2016-12-03 02:20:39	93	58	132	2017-01-04 02:20:39	\N
56	2	1	2017-03-31 14:28:24	36	68	96	2017-04-20 14:28:24	\N
57	1	1	2017-03-28 18:49:30	44	68	111	2017-04-13 18:49:30	\N
58	1	1	2016-08-26 10:53:23	26	55	117	2016-09-19 10:53:23	\N
59	2	1	2017-05-28 09:30:08	97	4	177	2017-07-07 09:30:08	\N
60	1	1	2017-04-30 01:44:23	27	45	80	2017-06-26 01:44:23	\N
61	2	1	2016-12-02 00:57:00	19	92	59	2017-01-31 00:57:00	\N
62	2	1	2016-09-12 14:04:02	22	38	61	2016-10-21 14:04:02	\N
63	2	1	2017-02-17 19:35:33	93	12	145	2017-03-01 19:35:33	\N
64	2	1	2016-08-22 00:20:10	85	56	167	2016-09-26 00:20:10	\N
65	1	1	2016-12-03 23:59:42	85	31	171	2017-01-24 23:59:42	\N
66	1	1	2017-04-20 06:08:13	28	53	95	2017-05-09 06:08:13	\N
67	1	1	2016-08-11 00:03:03	99	93	138	2016-08-13 00:03:03	\N
68	1	1	2016-10-05 03:57:12	48	12	80	2016-10-21 03:57:12	\N
69	1	1	2016-08-14 15:34:16	46	54	132	2016-10-03 15:34:16	\N
70	2	1	2017-04-16 23:13:57	47	80	115	2017-05-09 23:13:57	\N
71	1	1	2017-03-22 08:36:45	100	13	177	2017-05-10 08:36:45	\N
72	2	1	2016-09-18 10:56:16	41	74	74	2016-09-22 10:56:16	\N
73	1	1	2016-12-09 19:46:00	96	18	190	2017-01-23 19:46:00	\N
74	1	1	2016-09-23 15:22:18	86	10	172	2016-10-05 15:22:18	\N
75	2	1	2017-03-12 16:28:56	48	30	102	2017-04-28 16:28:56	\N
76	1	1	2016-11-07 14:06:38	65	89	107	2016-11-18 14:06:38	\N
77	1	1	2016-09-09 22:09:50	26	9	109	2016-10-15 22:09:50	\N
78	2	1	2016-11-15 04:28:12	36	9	72	2016-12-02 04:28:12	\N
79	2	1	2017-04-23 16:48:34	31	76	116	2017-06-23 16:48:34	\N
80	2	1	2017-04-25 11:50:29	55	16	130	2017-05-06 11:50:29	\N
81	1	1	2017-01-28 09:08:01	37	73	116	2017-03-17 09:08:01	\N
82	1	1	2017-02-18 15:38:37	24	52	87	2017-03-22 15:38:37	\N
83	2	1	2017-04-07 23:28:11	75	38	134	2017-06-02 23:28:11	\N
84	1	1	2017-06-21 00:35:49	50	97	116	2017-08-05 00:35:49	\N
85	2	1	2017-05-20 15:24:04	70	3	109	2017-06-12 15:24:04	\N
86	1	1	2017-06-12 05:11:05	88	23	179	2017-07-26 05:11:05	\N
87	2	1	2017-06-17 07:01:57	76	81	156	2017-07-07 07:01:57	\N
88	1	1	2017-01-01 16:23:36	65	21	137	2017-01-17 16:23:36	\N
89	1	1	2016-09-08 12:08:31	83	40	178	2016-10-28 12:08:31	\N
90	1	1	2016-12-02 19:33:18	100	52	191	2016-12-15 19:33:18	\N
91	2	1	2016-10-10 04:48:48	67	18	128	2016-12-04 04:48:48	\N
92	1	1	2017-01-27 23:26:33	57	6	154	2017-03-13 23:26:33	\N
93	2	1	2017-04-19 12:58:22	15	2	94	2017-06-08 12:58:22	\N
94	2	1	2017-02-19 05:50:13	49	74	141	2017-02-22 05:50:13	\N
95	1	1	2017-01-16 20:50:14	57	15	157	2017-02-11 20:50:14	\N
96	1	1	2017-06-14 03:49:39	23	61	84	2017-07-19 03:49:39	\N
97	2	1	2016-10-25 00:01:52	90	6	180	2016-11-17 00:01:52	\N
98	1	1	2016-11-20 19:17:49	83	51	117	2017-01-19 19:17:49	\N
99	1	1	2016-09-13 17:03:06	53	62	124	2016-10-14 17:03:06	\N
100	2	1	2016-07-03 12:45:40	80	36	179	2016-07-04 12:45:40	\N
101	1	1	2017-01-07 08:29:25	37	70	112	2017-03-06 08:29:25	\N
102	1	1	2016-09-16 07:42:00	100	32	158	2016-10-13 07:42:00	\N
103	1	1	2017-02-13 15:39:20	88	14	171	2017-03-03 15:39:20	\N
104	1	1	2016-10-28 15:53:09	73	55	150	2016-11-24 15:53:09	\N
105	2	1	2017-05-12 11:55:27	50	2	109	2017-06-02 11:55:27	\N
106	1	1	2016-09-10 03:34:34	29	19	65	2016-09-18 03:34:34	\N
107	1	1	2016-11-03 08:26:49	91	80	162	2016-12-07 08:26:49	\N
108	2	1	2016-07-29 17:33:41	36	64	108	2016-09-01 17:33:41	\N
109	2	1	2016-07-05 21:33:28	15	61	78	2016-07-14 21:33:28	\N
110	1	1	2017-02-23 05:35:04	68	33	126	2017-04-23 05:35:04	\N
111	2	1	2017-01-14 03:59:09	52	23	85	2017-01-31 03:59:09	\N
112	2	1	2016-10-25 19:56:18	38	28	70	2016-12-21 19:56:18	\N
113	2	1	2017-02-15 02:58:09	58	94	96	2017-04-16 02:58:09	\N
114	1	1	2017-06-20 04:20:49	51	58	141	2017-07-31 04:20:49	\N
115	1	1	2016-10-18 00:38:38	84	83	121	2016-10-30 00:38:38	\N
116	2	1	2017-01-17 15:01:29	78	49	171	2017-02-26 15:01:29	\N
117	1	1	2016-07-25 02:01:55	88	18	162	2016-08-13 02:01:55	\N
118	2	1	2016-07-06 16:43:07	35	50	129	2016-09-04 16:43:07	\N
119	1	1	2017-06-25 01:12:52	68	39	99	2017-08-22 01:12:52	\N
120	1	1	2016-12-14 19:19:27	86	80	170	2017-01-22 19:19:27	\N
121	2	1	2017-04-07 06:00:36	15	71	92	2017-04-25 06:00:36	\N
122	1	1	2017-05-06 10:02:03	97	79	179	2017-06-09 10:02:03	\N
123	1	1	2016-09-07 21:44:42	80	18	141	2016-10-14 21:44:42	\N
124	2	1	2016-08-25 07:13:53	51	91	\N	\N	\N
125	2	1	2017-01-18 20:18:37	68	48	\N	\N	\N
126	2	1	2016-09-13 22:52:54	46	14	\N	\N	\N
127	1	1	2017-05-17 16:35:32	94	52	\N	\N	\N
128	2	1	2016-10-11 16:02:20	37	50	\N	\N	\N
129	2	1	2016-12-03 11:32:11	57	64	\N	\N	\N
130	2	1	2016-09-18 22:10:34	48	75	\N	\N	\N
131	1	1	2016-09-22 03:01:06	26	65	\N	\N	\N
132	2	1	2017-02-08 14:51:18	28	100	\N	\N	\N
133	2	1	2016-07-09 05:02:13	16	42	\N	\N	\N
134	1	1	2016-11-19 23:46:27	80	90	\N	\N	\N
135	1	1	2017-01-29 09:27:12	94	31	\N	\N	\N
136	2	1	2016-09-21 09:15:18	100	14	\N	\N	\N
137	2	1	2017-05-25 19:57:12	46	76	\N	\N	\N
138	2	1	2017-06-21 00:46:54	55	54	\N	\N	\N
139	2	1	2016-12-30 01:53:01	60	25	\N	\N	\N
140	1	1	2017-02-11 17:09:32	30	84	\N	\N	\N
141	1	1	2016-08-21 01:11:39	22	73	\N	\N	\N
142	1	1	2017-06-17 02:14:38	46	55	\N	\N	\N
143	1	1	2017-02-23 08:19:43	81	6	\N	\N	\N
144	2	1	2017-06-04 07:03:43	50	61	\N	\N	\N
145	2	1	2017-04-14 09:55:56	70	95	\N	\N	\N
146	1	1	2016-09-11 05:25:02	21	50	\N	\N	\N
147	2	1	2017-04-15 01:18:48	29	86	\N	\N	\N
148	2	1	2016-08-10 22:46:42	80	56	\N	\N	\N
149	1	1	2017-02-07 12:11:57	92	26	\N	\N	\N
150	1	1	2017-04-18 04:07:10	63	48	\N	\N	\N
151	2	1	2017-03-17 05:32:26	67	9	\N	\N	\N
152	2	1	2017-05-11 02:04:31	26	81	\N	\N	\N
153	2	1	2016-09-13 01:35:25	61	83	\N	\N	\N
154	2	1	2016-12-24 11:21:14	61	38	\N	\N	\N
155	2	1	2016-11-01 05:29:02	89	10	\N	\N	\N
156	2	1	2017-04-20 16:59:48	92	42	\N	\N	\N
157	1	1	2016-08-27 20:58:11	31	42	\N	\N	\N
158	2	1	2017-04-18 19:06:19	68	77	\N	\N	\N
159	1	1	2016-08-01 20:30:51	79	15	\N	\N	\N
160	1	1	2017-02-15 01:50:25	93	66	\N	\N	\N
161	1	1	2016-07-28 02:45:55	48	55	\N	\N	\N
162	1	1	2017-06-16 03:10:54	51	13	\N	\N	\N
163	1	1	2016-12-26 07:50:26	74	55	\N	\N	\N
164	1	1	2016-09-01 15:49:04	62	49	\N	\N	\N
165	1	1	2016-10-14 06:36:39	82	78	\N	\N	\N
166	2	1	2016-07-03 05:27:10	70	68	\N	\N	\N
167	1	1	2017-03-12 00:16:37	26	43	\N	\N	\N
168	2	1	2016-10-20 03:44:15	22	86	\N	\N	\N
169	2	1	2016-09-12 18:02:08	51	40	\N	\N	\N
170	1	1	2016-07-17 05:15:37	91	37	\N	\N	\N
171	2	1	2017-05-08 12:58:49	74	64	\N	\N	\N
172	1	1	2016-10-14 11:12:24	66	95	\N	\N	\N
173	2	1	2017-06-20 15:31:48	34	42	\N	\N	\N
\.


--
-- Name: products_p_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('products_p_id_seq', 173, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY users (user_id, first_name, last_name, email, password) FROM stdin;
1	sisi	wang	wangss.wuhan@gmail.com	1111
2	sisi1	wang	wangss.wuhan1@gmail.com	1111
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('users_user_id_seq', 2, true);


--
-- Name: categories_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (cg_id);


--
-- Name: category_detail_values_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category_detail_values
    ADD CONSTRAINT category_detail_values_pkey PRIMARY KEY (cg_detailvalue_id);


--
-- Name: category_detailname_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category_detailname
    ADD CONSTRAINT category_detailname_pkey PRIMARY KEY (cg_detailname_id);


--
-- Name: category_details_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category_details
    ADD CONSTRAINT category_details_pkey PRIMARY KEY (cg_detail_id);


--
-- Name: customers_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (cust_id);


--
-- Name: gender_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY gender
    ADD CONSTRAINT gender_pkey PRIMARY KEY (gender_code);


--
-- Name: product_details_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY product_details
    ADD CONSTRAINT product_details_pkey PRIMARY KEY (detail_id);


--
-- Name: products_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY products
    ADD CONSTRAINT products_pkey PRIMARY KEY (p_id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: category_detail_values_cg_detailname_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category_detail_values
    ADD CONSTRAINT category_detail_values_cg_detailname_id_fkey FOREIGN KEY (cg_detailname_id) REFERENCES category_detailname(cg_detailname_id);


--
-- Name: category_details_cg_detailname_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category_details
    ADD CONSTRAINT category_details_cg_detailname_id_fkey FOREIGN KEY (cg_detailname_id) REFERENCES category_detailname(cg_detailname_id);


--
-- Name: category_details_cg_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category_details
    ADD CONSTRAINT category_details_cg_id_fkey FOREIGN KEY (cg_id) REFERENCES categories(cg_id);


--
-- Name: customers_gender_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY customers
    ADD CONSTRAINT customers_gender_code_fkey FOREIGN KEY (gender_code) REFERENCES gender(gender_code);


--
-- Name: customers_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY customers
    ADD CONSTRAINT customers_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: product_details_cg_detailvalue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY product_details
    ADD CONSTRAINT product_details_cg_detailvalue_id_fkey FOREIGN KEY (cg_detailvalue_id) REFERENCES category_detail_values(cg_detailvalue_id);


--
-- Name: product_details_p_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY product_details
    ADD CONSTRAINT product_details_p_id_fkey FOREIGN KEY (p_id) REFERENCES products(p_id);


--
-- Name: products_cg_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY products
    ADD CONSTRAINT products_cg_id_fkey FOREIGN KEY (cg_id) REFERENCES categories(cg_id);


--
-- Name: products_cust_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY products
    ADD CONSTRAINT products_cust_id_fkey FOREIGN KEY (cust_id) REFERENCES customers(cust_id);


--
-- Name: products_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY products
    ADD CONSTRAINT products_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

