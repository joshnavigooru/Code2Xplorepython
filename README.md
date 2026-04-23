Autonomous Smart City Data Intelligence System

Register Number: AP24110011598

Personalization Applied: Controlled Data Sorting & Adaptive Risk Analysis

Problem Statement

The program simulates and analyzes smart city data such as traffic, air quality (AQI), and energy consumption. It classifies zones into High Risk, Energy Critical, Safe Zone, or Moderate and predicts the overall city condition.

Approach / Logic Used
Generate data for multiple zones using random
Store data in a list of dictionaries
Classify zones using conditions
Convert data into Pandas DataFrame
Calculate custom risk score and apply transformation
Use NumPy for mean and variance
Identify Top 3 high-risk zones
Detect patterns (multi-factor risk, stability, clusters)
Generate final decision
 
 Personalization Applied
24110011598 % 3 = 1 → Custom sorting applied
Data sorted using manual logic (traffic-based)
Risk formula modified using name-based factor

Custom Risk Formula
risk_score = traffic * (0.3 + personal_factor*0.01) 
           + air_quality * (0.4 + personal_factor*0.01) 
           + energy * 0.2


Output
DataFrame with risk scores
Categorized zones
Top 3 risk zones
Risk tuple (max, avg, min)

Final decision
Learning Outcome

Learned how to use Python, Pandas, and NumPy for data analysis, apply custom logic, and build a smart system.
