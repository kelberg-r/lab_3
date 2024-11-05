-- обчислює мінімальну кількість продукції, яку можна виготовити на основі наявної кількості кожного ресурсу.
SELECT 
    p.product_name AS 'Назва продукції',
    MIN(FLOOR(od.quantity_ordered / tm.quantity_required)) AS 'Можлива кількість виготовлення'
FROM 
    Products p
JOIN 
    TechMap tm ON p.product_id = tm.product_id
JOIN 
    OrderDetails od ON tm.resource_id = od.resource_id
GROUP BY 
    p.product_name;
