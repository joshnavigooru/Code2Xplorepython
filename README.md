Day 05 - Smart Transport Load Balancing

Full Name: joshnavi gooru
L value (letters excluding spaces): 13
PLI value: 1
Applied Rule: Rule B – Remove Very Light items

Problem Statement

The program analyzes package weights before transport loading.
Each weight is classified into Very Light, Normal Load, Heavy Load, Overload, or Invalid entries based on defined ranges.
After classification, a personalized rule (PLI) calculated from the name length modifies the final loading plan and produces a balanced loading report.

Approach / Logic Used

Accept number of weights and read each weight using a loop.

Categorize each weight using conditional statements.

Calculate L (letters in name excluding spaces).

Compute PLI = L % 3.

Apply the rule:

PLI = 0 → Move overload to invalid entries

PLI = 1 → Remove very light items

PLI = 2 → Keep only normal and heavy loads

Count valid weights and affected items.

Display final categorized lists.

Test Case

Input

Number of weights: 7
Weights: 4, 18, 70, -2, 30, 55, 0
Name: joshnavi gooru


Output

Very Light: []
Normal Load: [18]
Heavy Load: [30, 55]
Overload: []
Invalid Entries: [-2]
Total Valid Weights: 3
Affected items due to PLI: 2
