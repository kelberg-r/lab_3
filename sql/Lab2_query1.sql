-- отримання загальної кількості закупівлі та залишкової кількості ресурсу
SELECT 
    r.resource_name AS 'Назва ресурсу',
    SUM(od.quantity_ordered) AS 'Загальна кількість закупівлі ресурсу',
    SUM(od.quantity_ordered) - COALESCE(vr.використана_кількість, 0) AS 'Залишкова кількість ресурсу'
FROM 
    Resources r
JOIN 
    OrderDetails od ON r.resource_id = od.resource_id
LEFT JOIN (
    SELECT 
        tm.resource_id,
        SUM(tm.quantity_required * sd.quantity_sold) AS використана_кількість
    FROM 
        TechMap tm
    JOIN 
        SaleDetails sd ON tm.product_id = sd.product_id
    GROUP BY 
        tm.resource_id
) vr ON r.resource_id = vr.resource_id
GROUP BY 
    r.resource_name, r.resource_id;
