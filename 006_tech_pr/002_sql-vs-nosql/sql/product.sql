CREATE TABLE product (
    name VARCHAR(100) PRIMARY KEY,
    price INTEGER,
    quantity INTEGER,
    size VARCHAR(100),
    short_info VARCHAR(100),
    long_info VARCHAR(3000)
);

CREATE TABLE product (
    name VARCHAR(100) PRIMARY KEY,
    price INTEGER
);
CREATE TABLE stock (
    stock_id SERIAL,
    name VARCHAR(100) REFERENCES product (name),
    size VARCHAR(100),
    quantity INTEGER
);
CREATE TABLE product_info (
    product_info_id SERIAL,
    product_name VARCHAR(100) REFERENCES product (name),
    short_info VARCHAR(100),
    long_info VARCHAR(3000)
);