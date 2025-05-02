CREATE TABLE IF NOT EXISTS accounts (
    user_id VARCHAR(255) PRIMARY KEY,
    balance DECIMAL(10, 2) DEFAULT 0.00
);

CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255),
    amount DECIMAL(10, 2),
    type ENUM('deposit', 'withdraw'),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES accounts(user_id)
);
