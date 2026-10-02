SELECT seller.seller_name 
FROM seller
WHERE seller.seller_id NOT IN (SELECT orders.seller_id 
    FROM orders
    WHERE EXTRACT(YEAR FROM orders.sale_date) = 2020)
ORDER BY seller.seller_name