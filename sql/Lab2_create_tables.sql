-- Створення таблиці ресурсів
create table Resources (
	resource_id INT PRIMARY KEY,
    resource_name VARCHAR(50)
);

-- Створення таблиці продукції
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50)
);

-- Створення технологічної карти
CREATE TABLE TechMap (
    product_id INT,
    resource_id INT,
    quantity_required INT,
    PRIMARY KEY (product_id, resource_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (resource_id) REFERENCES Resources(resource_id)
);

-- Створення таблиці замовлень ресурсів
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    order_date DATE
);

-- Створення таблиці вмісту замовлень
CREATE TABLE OrderDetails (
    order_id INT,
    resource_id INT,
    quantity_ordered INT,
    PRIMARY KEY (order_id, resource_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (resource_id) REFERENCES Resources(resource_id)
);

-- Створення таблиці реалізації продукції
CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    sale_date DATE
);

-- Створення таблиці вмісту реалізації продукції
CREATE TABLE SaleDetails (
    sale_id INT,
    product_id INT,
    quantity_sold INT,
    PRIMARY KEY (sale_id, product_id),
    FOREIGN KEY (sale_id) REFERENCES Sales(sale_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

show tables
    