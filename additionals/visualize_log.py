import csv
from collections import Counter
import matplotlib.pyplot as plt

def get_classification_counts():
    with open("classification_log.csv", mode="r") as file:
        reader = csv.reader(file)
        waste_types = [row[0] for row in reader]
    return Counter(waste_types)

def plot_classification_counts():
    counts = get_classification_counts()
    waste_types = list(counts.keys())
    frequencies = list(counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(waste_types, frequencies, color="skyblue")
    plt.xlabel("Waste Type")
    plt.ylabel("Frequency")
    plt.title("Frequency of Each Waste Type")
    plt.xticks(rotation=45)
    plt.show()

plot_classification_counts()
