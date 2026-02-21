Smart Playlist Intelligence System

Register Number Last Digit: 8
Personalization Applied: Dynamic Threshold Adjustment

Problem Statement

The program analyzes song durations in a playlist and categorizes it as Too Short, Too Long, Repetitive, Balanced, or Irregular.

It first validates that all durations are greater than zero.
Then it applies personalized duration limits based on the last digit of the register number to generate a customized playlist report.

Approach / Logic Used

Set reg_last_digit = 8 for personalization.

Compute personalized limits:

Minimum limit = 250 + (8 × 5) = 290

Maximum limit = 3200 + (8 × 50) = 3600

Variation limit = 700 + (8 × 20) = 860

Accept number of songs and store durations in a list.

Validate input:

If any duration ≤ 0 → Invalid Playlist

Calculate:

Total duration using sum()

Number of songs using len()

Apply classification logic:

Total < min_limit → Too Short

Total > max_limit → Too Long

Duplicate durations → Repetitive

Duration variation ≤ variation_limit → Balanced

Otherwise → Irregular
Test Case:
Input

Number of songs: 4
Durations: 180, 200, 220, 210

Calculations

Total Duration = 810 seconds
Number of Songs = 4
Variation = 220 − 180 = 40

Personalized Limits:

Min Limit = 290

Max Limit = 3600

Variation Limit = 860

Playlist Analysis Report 
Personalized Short Limit: 290
Personalized Long Limit: 3600
Total Duration: 810 seconds
Songs: 4
Category: Balanced Playlist
Recommendation: Good listening session.

Learning Outcome

Through this program, I learned:

How to implement personalization logic

How to use Python built-in functions (sum(), len(), set(), min(), max())

How to validate user input

How to apply conditional logic for classification

How to design structured output reports
