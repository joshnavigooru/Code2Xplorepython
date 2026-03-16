Smart Campus Energy Analyzer

Register Number Last Digit: 8
Personalization Applied: Balanced Usage Detection

Problem Statement

The program analyzes energy consumption readings collected from different campus buildings.
It classifies each reading as Efficient, Moderate, High Consumption, or Invalid based on predefined ranges.

The program first checks whether the energy readings are valid (non-negative).
Then it calculates the total energy consumption and number of buildings and generates an energy efficiency report.

Based on the analysis, the campus usage is categorized as Efficient Campus, Moderate Usage, or Energy Waste Detected.
Approach / Logic Used

Set reg_last_digit = 8 for personalization.

Accept the number of energy readings from the user.

Store all energy readings in a list.

Classify readings using a dictionary:

e < 0 → Invalid

0 – 50 → Efficient

51 – 150 → Moderate

150 → High Consumption

Use list comprehension to filter valid readings.

Calculate:

Total consumption using sum()

Number of buildings using len()

Store summary information in a tuple.

Apply efficiency analysis logic:

If total consumption > 600 → Energy Waste Detected

If high consumption readings > 3 → Moderate Usage

If efficient and moderate counts are equal → Efficient Campus

Otherwise → Moderate Usage

Finally, generate a structured Energy Category Report.

Test Case
Input
Number of energy readings: 6
Energy readings: 30, 45, 70, 90, 20, 60
Calculations

Total Consumption = 315 units
Number of Buildings = 6

Efficient Readings = [30, 45, 20]
Moderate Readings = [70, 90, 60]
High Consumption = []

Energy Analysis Report

Personalized Balanced Condition: Efficient Count = Moderate Count

Total Consumption: 315 units
Number of Buildings: 6

Category: Efficient Campus

Recommendation: Energy usage is balanced and efficient across buildings.

Learning Outcome

Through this program, I learned:

How to use lists, loops, and conditional statements in Python

How to organize data using dictionaries

How to filter data using list comprehension

How to store summary information using tuples

How to analyze data and generate a structured report using Python logic
