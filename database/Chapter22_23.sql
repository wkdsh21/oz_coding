-- 생성 초급 --

-- 1.customers 테이블에 새 고객을 추가하세요.
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES (2, 'abc store', 'Smith', 'John', '40.32.2555', '54, rue Royale', NULL, 'Nantes', NULL, '44000', 'France', 1370, 21000.00);


-- 2.products 테이블에 새 제품을 추가하세요.--
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
VALUES ('S10_16780', '1969 Harley Davidson Ultimate Chopper', 'Classic Cars', '1:10', 'Min Lin Diecast', 'This is a detailed replica of the Harley Davidson Ultimate Chopper.', 7933, 48.81, 95.70);


-- 3.employees 테이블에 새 직원을 추가하세요.--
INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle) 
VALUES 
(1, 'Smith', 'John', 'x1234', 'Smith@classicmodelcars.com', '1', NULL, 'Sales Rep');

-- 4.offices 테이블에 새 사무실을 추가하세요.
INSERT INTO offices (officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory)
VALUES ('8', 'San Francisco', '123-456-7890', '123 Market Street', 'Suite 123', 'CA', 'USA', '12345', 'NA');

-- 5.orders 테이블에 새 주문을 추가하세요.
INSERT INTO orders (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)
VALUES (10099, '2003-01-06', '2003-01-13', '2003-01-10', 'Shipped', NULL, 144);

-- 6.orderdetails 테이블에 주문 상세 정보를 추가하세요.
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
VALUES (10099, 'S10_1678', 30, 95.70, 3);

-- 7.payments 테이블에 지불 정보를 추가하세요.
INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount)
VALUES (103, 'HQ336330', '2004-10-20', 2338.64);

-- 8.productlines 테이블에 제품 라인을 추가하세요.
INSERT INTO productlines (productLine, textDescription, htmlDescription, image)
VALUES ('super Cars', 'High-quality super car.', '<p>super Cars Description</p>', NULL);

-- 9.customers 테이블에 다른 지역의 고객을 추가하세요.
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES (3, 'Atelier graphique', 'Schmitt', 'Carine', '40.32.2555', '54, rue Royale', NULL, 'Nantes', NULL, '44000', 'seoul', 1370, 21000.00);

-- 10.products 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
VALUES ('S10_16781', '1969 Harley Davidson Ultimate Chopper', 'super Cars', '1:10', 'Min Lin Diecast', 'This is a detailed replica of the Harley Davidson Ultimate Chopper.', 7933, 48.81, 95.70);


-- 읽기 초급 --

-- 1.customers 테이블에서 모든 고객 정보를 조회하세요.
select * from customers;

-- 2.products 테이블에서 모든 제품 목록을 조회하세요.
select * from products;

-- 3.employees 테이블에서 모든 직원의 이름과 직급을 조회하세요.
select firstName,jobTitle from employees;

-- 4.offices 테이블에서 모든 사무실의 위치를 조회하세요.
select addressLine1 from offices;
 
-- 5.orders 테이블에서 최근 10개의 주문을 조회하세요.
select * from orders LIMIT 10; 

-- 6.orderdetails 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
select * from orderdetails where orderNumber=10100; 

-- 7.payments 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
select * from payments where customerNumber=103;

-- 8.productlines 테이블에서 각 제품 라인의 설명을 조회하세요.
select textDescription from productlines;

-- 9.customers 테이블에서 특정 지역의 고객을 조회하세요.
select * from customers where city="Nantes";

-- 10.products 테이블에서 특정 가격 범위의 제품을 조회하세요.
select * from products where buyPrice between 30 and 50;


-- 갱신 초급 --

-- 1.customers 테이블에서 특정 고객의 주소를 갱신하세요.
UPDATE customers
SET addressLine1= "149 Spinnaker Dr."
WHERE customerName="abc store";

-- 2.products 테이블에서 특정 제품의 가격을 갱신하세요.
UPDATE products
SET buyPrice = 10
WHERE productName="1996 Moto Guzzi 1100i";

-- 3.employees 테이블에서 특정 직원의 직급을 갱신하세요.
UPDATE employees
SET jobTitle = "VP Marketing"
WHERE employeeNumber=1;

-- 4.offices 테이블에서 특정 사무실의 전화번호를 갱신하세요.
UPDATE offices
SET phone = "+33 14 113 4404"
WHERE officeCode=1;

-- 5.orders 테이블에서 특정 주문의 상태를 갱신하세요.
UPDATE orders
SET status = "Cancelled"
WHERE orderNumber=10162;

-- 6.테이블에서 특정 주문 상세의 수량을 갱신하세요.
UPDATE orderdetails
SET quantityOrdered = 17
WHERE orderNumber=10099 and productCode="S10_1678";

-- 7.payments 테이블에서 특정 지불의 금액을 갱신하세요.
UPDATE payments
SET amount = 1900
WHERE customerNUmber=103 and checkNumber="HQ336330";

-- 8.productlines 테이블에서 특정 제품 라인의 설명을 갱신하세요.
UPDATE productlines
SET textDescription = "High-quality real super car"
WHERE productLine="super cars";

-- 9.customers 테이블에서 특정 고객의 이메일?을 갱신하세요?.



-- 삭제 초급 --

-- 1.customers 테이블에서 특정 고객을 삭제하세요.
DELETE FROM customers WHERE creditLimit=0;

-- 2.products 테이블에서 특정 제품을 삭제하세요.
DELETE FROM products WHERE quantityInStock=0;

-- 3.employees 테이블에서 특정 직원을 삭제하세요.
delete from employees where employeeNumber=1;

-- 4.offices 테이블에서 특정 사무실을 삭제하세요.
DELETE FROM offices WHERE officeCode = 1;

-- 5.orders 테이블에서 특정 주문을 삭제하세요.
DELETE FROM orders WHERE orderNumber = 10102;

-- 6.orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
DELETE FROM orderdetails WHERE orderNumber = 10103 and productCode="S10_1949";

-- 7.payments 테이블에서 특정 지불 내역을 삭제하세요.
DELETE FROM payments WHERE amount<=1900;

-- 8.productlines 테이블에서 특정 제품 라인을 삭제하세요.
DELETE FROM productlines WHERE productLine = 'Classic Cars';

-- 9.customers 테이블에서 특정 지역의 모든 고객을 삭제하세요
DELETE FROM customers WHERE city = 'Paris';

-- 10.products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
DELETE FROM products WHERE productLine = 'super Cars';




