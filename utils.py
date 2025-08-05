import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import os

def get_countries():
    return ["Country1", "Country2", "Country3"]


def get_index_year():
    return {
        "Country1": {"ind1": 5, "ind2": 10, "ind3": 7},
        "Country2": {"t1": 2000, "t2": 2005, "t3": 2010}
    }

def generate_chart(data):
    STATIC_FOLDER = "static"
    plt.figure(figsize=(5, 4))
    plt.bar(data.keys(), data.values(), color='skyblue')
    plt.title(f"Chart 1 - Country vs index")
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig(os.path.join(STATIC_FOLDER, "chart1.png"))
    plt.close()
