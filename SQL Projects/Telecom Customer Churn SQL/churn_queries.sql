--Total Customers

SELECT COUNT(*) AS total_Customers
From Churn_Clean;


--Churn Rate 
SELECT
ROUND(
100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS Churn_Rate
FROM Churn_Clean;


--Retention Rate
SELECT
ROUND(
100.0 * SUM(CASE WHEN Churn='No' THEN 1 ELSE 0 END)
/ COUNT(*),
2
)
AS Retention_Rate
FROM Churn_Clean;


--Monthly Revenue
SELECT
ROUND(SUM(MonthlyCharges),2)
AS Monthly_Revenue
FROM Churn_Clean;


--contract with highest churned customers
SELECT contract,
COUNT(*) AS Churned_Customers
FROM Churn_Clean
WHERE churn= 'Yes'
GROUP BY contract
ORDER BY Churned_Customers DESC;


--churn by Gender
SELECT
gender,
COUNT(*) AS Churned_Customers
FROM Churn_Clean
WHERE Churn='Yes'
GROUP BY gender;

--churn by senior citizen Status
SELECT seniorcitizen, COUNT(*) As Churned_Customers 
From Churn_Clean
Where Churn= 'Yes'

GROUP BY seniorcitizen;


--Avg monthly charges by churn Status

SELECT
Churn,
ROUND(AVG(MonthlyCharges),2)
AS Avg_Monthly_Charges
FROM Churn_Clean
GROUP BY Churn;

--Churn by tenure Band
SELECT
Churn,
ROUND(AVG(MonthlyCharges),2)
AS Avg_Monthly_Charges
FROM Churn_Clean
GROUP BY Churn;

--Churn by internet service
SELECT
InternetService,
COUNT(*) AS Churned_Customers
FROM Churn_Clean
WHERE Churn='Yes'
GROUP BY InternetService;

--churned Customers
SELECT 
COUNT(*) AS Churned_Customers
FROM Churn_Clean
WHERE churn= 'Yes'
;

--Churn Rate by tenure
SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END AS Tenure_Group,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 
        2
    ) AS Churn_Rate_Percent
FROM Churn_Clean
GROUP BY Tenure_Group
ORDER BY 
    CASE 
        WHEN Tenure_Group = '0-12 Months' THEN 1
        WHEN Tenure_Group = '13-24 Months' THEN 2
        WHEN Tenure_Group = '25-48 Months' THEN 3
        ELSE 4
    END;





