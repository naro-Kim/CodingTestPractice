SELECT MEMBER_NAME, rr.REVIEW_TEXT, DATE_FORMAT(rr.REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
FROM MEMBER_PROFILE mp
INNER JOIN(
    SELECT rr.MEMBER_ID, rr.REVIEW_TEXT, rr.REVIEW_DATE
    FROM REST_REVIEW rr
    WHERE rr.MEMBER_ID = (
        SELECT r.MEMBER_ID
        FROM (
            SELECT MEMBER_ID
            FROM REST_REVIEW
            GROUP BY MEMBER_ID
            ORDER BY COUNT(*) desc
            LIMIT 1
        ) r
    )
) rr
ON mp.MEMBER_ID = rr.MEMBER_ID
ORDER BY REVIEW_DATE asc, rr.REVIEW_TEXT asc
