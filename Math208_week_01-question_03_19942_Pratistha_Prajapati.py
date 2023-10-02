import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

given_data = pd.DataFrame({"Cause of Death": ["Alzheimer's", "Chronic Respiratory Disease", "Diabetes", "Heart Disease", "Influenza/Pneumonia", "Malignant Neoplasms", "Accidents", "Nephritis/Nephrosis", "Septicemia", "Stroke"],
    "Number (x 10,000)": [7.2, 12.5, 7.2, 63.2, 5.6, 56.0, 12.2, 4.5, 3.4, 13.7]})

total_numbers_of_death = given_data["Number (x 10,000)"].sum()


given_data["data_cumulative_percentage"] = (given_data["Number (x 10,000)"].cumsum() / total_numbers_of_death) * 100


given_data = given_data.sort_values(by="data_cumulative_percentage", ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(given_data["Cause of Death"], given_data["Number (x 10,000)"], color="blue")
plt.plot(given_data["Cause of Death"], given_data["data_cumulative_percentage"], color="green", linestyle="--")
plt.xlabel("Cause of Death")
plt.ylabel("Number of Deaths (x 10,000)")
plt.title("Pareto Chart of the 10 Leading Causes of Death in the US in 2006")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
