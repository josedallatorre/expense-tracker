CREATE SCHEMA expense;

CREATE TABLE CLIENT (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE TRANSACTION (
    transaction_id SERIAL PRIMARY KEY,
    date DATE,
    value NUMERIC NOT NULL,
    description VARCHAR(50),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES CLIENT (user_id)
);

INSERT INTO CLIENT(user_id,username) VALUES (1,'test');