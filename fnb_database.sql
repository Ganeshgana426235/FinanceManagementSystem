-- drop database fnb;
create database fnb;
use fnb;
CREATE TABLE LOGIN(LOGIN_ID VARCHAR(100) NOT NULL,
						   USER_NAME VARCHAR(100) NOT NULL,
						   LOGIN_PASSWORD VARCHAR (50)NOT NULL);

INSERT INTO LOGIN VALUES(1,"test","test");
CREATE TABLE CUSTOMER_DETAILS (CUST_ID  VARCHAR(25) PRIMARY KEY,
							   CUSTOMER_NAME VARCHAR(50) NOT NULL,
                               CUST_PHOTO     LONGBLOB NULL,
							   FATHER_NAME    VARCHAR(50) NOT NULL,
							   MOTHER_NAME    VARCHAR(50) NOT NULL,
							   ADDRESS        VARCHAR(300) NOT NULL,
							   DATE_OF_BIRTH  DATE NULL,
							   GENDER         CHAR(1) NULL,
							   OCCUPATION     VARCHAR(60) NULL,
							   AADHAR_NUMBER  VARCHAR(24) NOT NULL,
							   PAN_CARD       VARCHAR(15) NULL,
							   EMAIL          VARCHAR(50) NULL,
							   MOBILE         VARCHAR(20) NOT NULL,
							   ALTERNATE_MOBILE_NUMBER VARCHAR(20) NULL,
							   LOAN_STATUS       TINYINT NULL);


CREATE TABLE  GUARANTOR(GUA_ID VARCHAR(25) PRIMARY KEY,
					CUST_ID VARCHAR(25),
				    GUARANTOR_NAME VARCHAR(155) NOT NULL,
					GUARANTOR_MOBILE   VARCHAR(20) NOT NULL,
					GUARANTOR_AADHAR   VARCHAR(20) NOT NULL,
					GUARANTOR_PANCARD  VARCHAR(20) NULL,
					RELATIONSHIP       VARCHAR(60) NOT NULL,
                    FOREIGN KEY(CUST_ID) REFERENCES CUSTOMER_DETAILS(CUST_ID));


CREATE TABLE LOAN_DETAILS(LOAN_ID VARCHAR(25) PRIMARY KEY,
						CUST_ID VARCHAR(25),
                        GUA_ID VARCHAR(25),
                        LOAN_TYPE VARCHAR(10),
                        LOAN_AMOUNT DOUBLE,
                        INTEREST_RATE DOUBLE,
                        LOAN_APPROVED_DATE DATE,
                        TOTAL_NO_OF_INSTALLMENTS INT,  
                        NO_OF_INSTALLMENTS_PAID INT,
                        AMOUNT_PER_INSTALLMENT DOUBLE,
                        ADVANCED_PAYMENT_RECIEVED INT,
                        OVER_DUES INT,                      -- over dues count 
                        NEXT_INSTALLMENT_DATE DATE,			-- next installment date 
                        LOAN_CLOSING_DATE DATE,				-- loan closing date
                        LOAN_STATUS TINYINT,
                        FOREIGN KEY(CUST_ID) REFERENCES CUSTOMER_DETAILS(CUST_ID),
                        FOREIGN KEY(GUA_ID) REFERENCES GUARANTOR(GUA_ID));


CREATE TABLE COLLECTIONS(COLLECTION_ID VARCHAR(40),
						LOAN_ID VARCHAR(25),
                        CUST_ID VARCHAR(25),
                        NO_OF_INSTALLMENTS_PAYING INT,		-- how many installments going to pay, including overdues and adv payments
                        TOTAL_AMOUNT_RECEIVED DOUBLE,			 -- total amount paid for this instalment
						PAYMENT_MODE VARCHAR(10),                -- online / offline
                        PAYMENT_RECEIVED_DATE DATE,
                        TRANSACTION_DETAILS VARCHAR(50),       -- transaction id
                        FOREIGN KEY(LOAN_ID) REFERENCES LOAN_DETAILS(LOAN_ID),
                        FOREIGN KEY(CUST_ID) REFERENCES CUSTOMER_DETAILS(CUST_ID));  



