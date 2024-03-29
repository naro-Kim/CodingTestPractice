SELECT b.CATEGORY, SUM(bs.SALES) as BOOK_SALES
FROM BOOK as b, BOOK_SALES as bs
WHERE b.BOOK_ID = bs.BOOK_ID and DATE_FORMAT(bs.SALES_DATE, "%Y-%m") = '2022-01'
GROUP BY CATEGORY
ORDER BY CATEGORY asc