SELECT a.AUTHOR_ID, 
       a.AUTHOR_NAME, 
       b.CATEGORY, 
       SUM(b.PRICE * bs.SALES) as TOTAL_SALES
FROM BOOK b
    INNER JOIN BOOK_SALES bs ON b.BOOK_ID = bs.BOOK_ID 
    INNER JOIN AUTHOR a ON b.AUTHOR_ID = a.AUTHOR_ID
WHERE bs.SALES_DATE LIKE '2022-01%'
GROUP BY a.AUTHOR_ID, b.CATEGORY
ORDER BY a.AUTHOR_ID asc, b.CATEGORY desc