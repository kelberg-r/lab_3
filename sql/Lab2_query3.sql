-- отримання швидкості витрачання ресурсів по днях
SELECT 
    s.sale_date AS 'Дата',
    r.resource_name AS 'Назва ресурсу',
    SUM(tm.quantity_required * sd.quantity_sold) AS 'Витрачено ресурсу за день'
FROM 
    TechMap tm
JOIN 
    SaleDetails sd ON tm.product_id = sd.product_id
JOIN 
    Sales s ON sd.sale_id = s.sale_id
JOIN 
    Resources r ON tm.resource_id = r.resource_id
GROUP BY 
    s.sale_date, r.resource_name;
