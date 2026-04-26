import random
import math
import copy
import numpy as np
import pandas as pd

def generate_data(n):
    data = []
    for i in range(n):
        entry = {
            "zone": i + 1,
            "metrics": {
                "traffic": random.randint(50, 500),
                "pollution": random.randint(20, 300),
                "energy": random.randint(30, 400)
            },
            "history": [random.randint(10, 200) for _ in range(5)]
        }
        data.append(entry)
    return data

def personalize_data(data, roll):
    if roll % 2 == 0:
        return data[::-1]
    else:
        k = 3
        return data[k:] + data[:k]

def custom_risk_score(t, p, e):
    return math.log(t + p + e) * math.sqrt(t + 1)

def mutate_data(data):
    for entry in data:
        entry["metrics"]["traffic"] += random.randint(1, 10)
        entry["history"].append(random.randint(5, 50))
        entry["risk"] = math.log(entry["metrics"]["traffic"] + entry["metrics"]["pollution"] + entry["metrics"]["energy"])

def dataframe_convert(data):
    rows = []
    for entry in data:
        row = {
            "zone": entry["zone"],
            "traffic": entry["metrics"]["traffic"],
            "pollution": entry["metrics"]["pollution"],
            "energy": entry["metrics"]["energy"],
            "risk": entry["risk"]
        }
        rows.append(row)
    return pd.DataFrame(rows)

def manual_corr(x, y):
    x = np.array(x)
    y = np.array(y)
    xm = np.mean(x)
    ym = np.mean(y)
    num = np.sum((x - xm) * (y - ym))
    den = math.sqrt(np.sum((x - xm) ** 2) * np.sum((y - ym) ** 2))
    return num / den

def anomaly_detection(values):
    mean = np.mean(values)
    std = np.std(values)
    anomalies = [i + 1 for i, v in enumerate(values) if v > mean + std]
    return anomalies, mean, std

def cluster_detection(risky):
    clusters = []
    current = []
    for i in range(len(risky)):
        if i == 0 or risky[i] == risky[i - 1] + 1:
            current.append(risky[i])
        else:
            clusters.append(current)
            current = [risky[i]]
    if current:
        clusters.append(current)
    return clusters

def stability_index_calc(var):
    return 1 / var if var != 0 else 0

def final_decision(stability, corruption):
    if corruption > 8:
        return "Critical Failure"
    elif corruption > 5:
        return "High Corruption Risk"
    elif stability < 0.01:
        return "Moderate Risk"
    else:
        return "System Stable"

roll_number = int(input())

data = generate_data(15)
data = personalize_data(data, roll_number)

assignment_copy = data
shallow_copy = copy.copy(data)
deep_copy = copy.deepcopy(data)

print("BEFORE MUTATION")
print(data)

mutate_data(shallow_copy)

print("AFTER MUTATION")
print("ORIGINAL")
print(data)
print("SHALLOW COPY")
print(shallow_copy)
print("DEEP COPY")
print(deep_copy)

df = dataframe_convert(data)
print(df)

traffic = df["traffic"].values
pollution = df["pollution"].values

corr_value = manual_corr(traffic, pollution)
print("Correlation:", corr_value)

risks = []
for entry in data:
    t = entry["metrics"]["traffic"]
    p = entry["metrics"]["pollution"]
    e = entry["metrics"]["energy"]
    risks.append(custom_risk_score(t, p, e))

anomalies, mean_risk, std_risk = anomaly_detection(risks)
print("Anomaly Zones:", anomalies)

clusters = cluster_detection(anomalies)
print("Risk Clusters:", clusters)

variance = np.var(risks)
stability = stability_index_calc(variance)

max_risk = max(risks)
min_risk = min(risks)

print((max_risk, min_risk, stability))

decision = final_decision(stability, len(anomalies))
print(decision)