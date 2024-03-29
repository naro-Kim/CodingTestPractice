SELECT p.PRODUCT_CODE, SUM(p.PRICE*s.SALES_AMOUNT) as SALES 
from PRODUCT as p, OFFLINE_SALE as s 
where p.PRODUCT_ID = s.PRODUCT_ID
group by p.PRODUCT_CODE
order by SALES desc, p.PRODUCT_CODE asc