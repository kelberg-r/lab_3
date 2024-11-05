-- отримання Код ресурсу, Назва ресурсу, Дата, Загальна кількість купленого ресурсу на дату, Залишок на дату
SELECT 
    r.resource_id AS 'Код ресурсу',
    r.resource_name AS 'Назва ресурсу',
    o.order_date AS 'Дата',
    SUM(od.quantity_ordered) AS 'Загальна кількість купленого ресурсу на дату',
    SUM(od.quantity_ordered) - COALESCE(SUM(vr.використана_кількість), 0) AS 'Залишок на дату'
FROM 
    Resources r
JOIN 
    OrderDetails od ON r.resource_id = od.resource_id
JOIN 
    Orders o ON od.order_id = o.order_id
LEFT JOIN (
    SELECT 
        tm.resource_id,
        s.sale_date,
        SUM(tm.quantity_required * sd.quantity_sold) AS використана_кількість
    FROM 
        TechMap tm
    JOIN 
        SaleDetails sd ON tm.product_id = sd.product_id
    JOIN 
        Sales s ON sd.sale_id = s.sale_id
    GROUP BY 
        tm.resource_id, s.sale_date
) vr ON r.resource_id = vr.resource_id AND o.order_date = vr.sale_date
GROUP BY 
    r.resource_id, r.resource_name, o.order_date;
