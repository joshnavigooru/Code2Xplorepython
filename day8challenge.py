import random
import pandas as pd
import numpy as np
import math

name = input("Enter your name: ")
roll = int(input("Enter your Roll Number: "))

personal_factor = len(name) % 5 + 1

def generate_data(n=18):
    data = []
    for i in range(1, n+1):
        zone = {
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        data.append(zone)

    # test cases
    data.append({"zone": n+1, "traffic": 0, "air_quality": 50, "energy": 100})
    data.append({"zone": n+2, "traffic": 95, "air_quality": 280, "energy": 480})
    data.append({"zone": n+3, "traffic": 60, "air_quality": 120, "energy": 499})

    return data

def classify(data):
    categories = {}
    for d in data:
        if d["air_quality"] > 200 or d["traffic"] > 80:
            categories[d["zone"]] = "High Risk"
        elif d["energy"] > 400:
            categories[d["zone"]] = "Energy Critical"
        elif d["traffic"] < 30 and d["air_quality"] < 100:
            categories[d["zone"]] = "Safe Zone"
        else:
            categories[d["zone"]] = "Moderate"
    return categories


def custom_sort(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]["traffic"] > data[j]["traffic"]:
                data[i], data[j] = data[j], data[i]
    return data

def analyze(df):
    df["risk_score"] = (
        df["traffic"] * (0.3 + personal_factor * 0.01) +
        df["air_quality"] * (0.4 + personal_factor * 0.01) +
        df["energy"] * 0.2
    )

    df["sqrt_risk"] = df["risk_score"].apply(math.sqrt)

    mean_values = np.mean(df[["traffic", "air_quality", "energy"]])

    return df, mean_values

def top3_zones(data):
    sorted_data = sorted(data, key=lambda x: x["risk_score"], reverse=True)
    return sorted_data[:3]

def detect_patterns(df):
    threshold = df["risk_score"].mean()

    df["aqi_rising"] = df["air_quality"].diff() > 0

    multi_factor = df[(df["risk_score"] > threshold) & (df["aqi_rising"])]

    variance = np.var(df["traffic"])
    stability = "Stable" if variance < 500 else "Unstable"

    clusters = []
    temp = []

    for i in range(len(df)):
        if df.loc[i, "risk_score"] > threshold:
            temp.append(df.loc[i, "zone"])
        else:
            if len(temp) >= 2:
                clusters.append(temp)
            temp = []

    return multi_factor, stability, clusters

def decision(df):
    max_risk = df["risk_score"].max()
    avg_risk = df["risk_score"].mean()
    min_risk = df["risk_score"].min()

    if avg_risk < 100:
        final = "City Stable"
    elif avg_risk < 180:
        final = "Moderate Risk"
    elif avg_risk < 250:
        final = "High Alert"
    else:
        final = "Critical Emergency"

    return (max_risk, avg_risk, min_risk), final


data = generate_data()

if roll % 3 == 0:
    random.shuffle(data)
    manipulation = "Data shuffled (Dynamic Behavior)"
else:
    data = custom_sort(data)
    manipulation = "Data sorted by Traffic (Controlled Behavior)"

categories = classify(data)

df = pd.DataFrame(data)

df, means = analyze(df)

updated_data = df.to_dict("records")

top3 = top3_zones(updated_data)

multi_factor, stability, clusters = detect_patterns(df)

risk_tuple, final_decision = decision(df)

unique_categories = set(categories.values())

print("\nSMART CITY SYSTEM ")
print(f"Student: {name}")
print(f"Roll No: {roll}")
print(f"Personal Factor: {personal_factor}")
print(manipulation)

print("\nDataFrame")
print(df)

print("\nCategories ")
print(categories)

print("\nUnique Categories (Set) ")
print(unique_categories)

print("\nTop 3 Risk Zones")
for z in top3:
    print(z)

print("\nRisk Tuple ")
print(risk_tuple)

print("\n Multi-Factor Risk Zones")
print(multi_factor[["zone", "risk_score"]])

print("\nStability")
print(stability)

print("\n Critical Clusters")
print(clusters)

print("\nFINAL DECISION ")
print(final_decision)

print("\nSMART CITY INSIGHT ")
print("A smart city uses data intelligence to predict risks, optimize resources, and ensure sustainability.")
