-- Step 3: Create Employee Table
USE ROLE FULL_ACCESS_ROLE;
USE SCHEMA EMP_DB.HR_SCHEMA;

CREATE OR REPLACE TABLE EMPLOYEE (
    EMP_ID INT,
    EMP_NAME STRING,
    EMAIL STRING,
    SALARY NUMBER
);

INSERT INTO EMPLOYEE VALUES 
(1, 'John Doe', 'john.doe@example.com', 75000),
(2, 'Jane Smith', 'jane.smith@example.com', 82000),
(3, 'Bob Lee', 'bob.lee@example.com', 65000);