SELECT YEAR(SALES_DATE) as YEAR,
    MONTH(SALES_DATE) as MONTH,
    GENDER, 
    COUNT(distinct UI.USER_ID) as USERS
FROM USER_INFO as UI, 
    ONLINE_SALE as OS
WHERE UI.USER_ID = OS.USER_ID 
AND GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR asc, MONTH asc, GENDER asc