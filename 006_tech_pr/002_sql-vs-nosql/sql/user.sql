CREATE TABLE user (
    username VARCHAR(30) PRIMARY KEY,
    password VARCHAR(255),
    description VARCHAR(300),
    phone_number VARCHAR(30),
    address VARCHAR(300),
    address_detail VARCHAR(300),
    address_post_number VARCHAR(30)
);

CREATE TABLE account (
    username VARCHAR(30) PRIMARY KEY,
    password VARCHAR(255)
);

CREATE TABLE user_info (
    username VARCHAR(30),
    description VARCHAR(300) PRIMARY KEY,
    phone_number VARCHAR(30),
    
    FOREIGN KEY (username) REFERENCES account (username)
);

CREATE TABLE user_address (
    username VARCHAR(30),
    address VARCHAR(300),
    address_detail VARCHAR(300),
    address_post_number VARCHAR(30),
    
    FOREIGN KEY (username) REFERENCES account (username)
);

INSERT INTO account (username, password) VALUES
('A', 'password_string'), ('B', 'password_string'), ('C', 'password_string');
INSERT INTO account (username, password) VALUES
('D', 'password_string');

INSERT INTO user_address (username, address, address_detail, address_post_number) VALUES
('A', 'address', 'address_detail', 'address_post_number'),
('B', 'address', 'address_detail', 'address_post_number'),
('C', 'address', 'address_detail', 'address_post_number');

SELECT * FROM account, user_address;