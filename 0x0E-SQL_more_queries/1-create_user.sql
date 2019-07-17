-- Create new user with full privileges
-- Create User
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'user_0d_1_pwd';
-- grant full privileges
GRANT ALL ON *.* TO user_0d_1@localhost;
