Python Code2Xplore – Day 9 & Day 10 Challenges
Department of Computer Science and Engineering
SRM University-AP
 1. Problem Understanding
 Day 9 – Data Replication & Integrity
This task simulates a cloud system where improper copying (especially shallow copy) leads to data inconsistency and leakage. The goal is to replicate data, apply modifications, and detect corruption.
Day 10 – Data Corruption & Risk Prediction
This extends the system into a large-scale analytics pipeline where corrupted data affects predictions. The goal is to analyze data using NumPy, Pandas, and mathematical models to detect anomalies and predict risks.
2. Objectives
Understand assignment vs shallow vs deep copy
Detect data corruption & leakage
Perform multi-level data modifications
Apply data science techniques (NumPy, Pandas)
Predict system risk using mathematical transformations
3. Data Structures
Day 9 Format
Python
users = [
    {
        "id": 1,
        "data": {"files": ["a.txt", "b.txt"], "usage": 500}
    }
]
Day 10 Format
Python
{
    "zone": int,
    "metrics": {
        "traffic": int,
        "pollution": int,
        "energy": int
    },
    "history": [values]
}
4. Approach / Logic
Day 9 Flow
Step 1: Function Design
generate_data()
replicate_data()
modify_data()
check_integrity()
Step 2: Copy Mechanism
Assignment copy
Shallow copy
Deep copy
Step 3: Multi-Level Modification
Add/remove files
Change usage values
Step 4: Integrity Analysis
Data Leakage → original changed unexpectedly
 Consistency → deep copy safe
 Overlap Detection → using sets
 Mutation Depth → inner vs outer change
 Day 10 Flow
Step 1: Data Simulation
Generate 15 zones with nested structures
Step 2: Copy Mechanism
Assignment, shallow, deep copies
Step 3: Mutation
Modify nested values
Append history
Apply risk formula
Step 4: Analysis
NumPy → mean, variance
Pandas → DataFrame
Manual correlation
Step 5: Pattern Detection
Anomalies
Hidden corruption
Risk clusters
Stability index
 5. Custom Logic
 Personalized Rule
EVEN roll → add/reverse
ODD roll → delete/rotate
    ustom Risk Function (Day 10)
Pyhon
def custom_risk_score(t, p, e):
    return math.log(t + p + e + 1)
 Custom Integrity Rule (Day 9)
Data corruption is defined as:
Any unintended change in the original dataset caused by operations on copied data.
 6. Core Concept Explanation
Why Shallow Copy Causes Corruption?
Shallow copy duplicates only the outer structure.
Inner objects (lists/dictionaries) are still shared references
So:
Python
shallow[0]["data"]["files"].append("x.txt")
This affects original data also Deep Copy
Creates fully independent memory → no corruption
 7. Output Demonstration
 Must Show
BEFORE vs AFTER
Original data
Assignment copy
Shallow copy
Deep copy
Integrity Report (Day 9)
Leakage count
Safe count
Overlap count
Data Analysis (Day 10)
DataFrame
Anomaly zones
Risk scores
Final Tuple Output

(leakage_count, safe_count, overlap_count)
(max_risk, min_risk, stability_index)
 8. Key Observations
Shallow copy leads to hidden corruption
Deep copy ensures data safety
Nested structures are high-risk for bugs
Mathematical models help in predicting failures
 9. Technologies Used
Python
NumPy
Pandas
math
random
10. Conclusion
This project highlights the importance of correct data replication techniques.
Improper copying (like shallow copy) can silently corrupt systems, while deep copy ensures integrity.
By combining Python internals + data science, we can detect corruption, analyze patterns, and predict system failures effectively.
11. Mandatory Proof Checklist
✔ Functions used (≥4/5)
✔ Nested structures
✔ Shallow & Deep copy
✔ BEFORE–AFTER comparison
✔ Integrity explanation
✔ Custom logic applied
✔ NumPy & Pandas (Day 10)
✔ Manual correlation
