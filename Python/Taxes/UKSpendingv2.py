from matplotlib import pyplot as plt
from csv import DictReader
import numpy as np
import mplcursors

listOfFiles = "UK_public_spending.csv"
listOfHeaders = ["benefits", "health", "education", "defence", "police", "transport", "housing", "aid"]
listOfXLists = []
listOfYLists = []

def getdata(filename: str) -> list[dict]: #csv.Dictreader
    with open(filename, "r", newline="") as f:
        return list(DictReader(f))

def plot(filename: str, headers: list[str]) -> None:
    ups = getdata(filename)
    label_positions = []

    for h in headers:
        xpoints, ypoints = [], []
        for i in ups:
            x = int(i.get("year", "")[:4])
            y_raw = i.get(h, "")
            y = float(y_raw) if y_raw not in (None, "") else np.nan
            xpoints.append(x)
            ypoints.append(y)
        xpoints, ypoints = np.array(xpoints), np.array(ypoints)

        line, = plt.plot(xpoints, ypoints, label=h)
        label_positions.append((ypoints[-1], h, line.get_color(), xpoints[-1]))

    plt.ylim(bottom=0)
    plt.xlim(left=1955)

    if label_positions: #Fix overlapping labels
        label_positions.sort(key=lambda x: x[0])
        adjusted_positions = []
        y_min, y_max = plt.ylim()
        min_spacing = (y_max - y_min) * 0.03

        for y_pos, label_text, color, x_pos in label_positions:
            adjusted_y = y_pos
            for prev_y in adjusted_positions:
                if abs(adjusted_y - prev_y) < min_spacing:
                    adjusted_y = prev_y + min_spacing
            adjusted_positions.append(adjusted_y)
            plt.text(x_pos, adjusted_y, f'     {label_text}', color=color, va="center", fontsize=9, clip_on=False)

        # Make graph end nearer to last line
        x_data_max = max(pos[3] for pos in label_positions)
        x_min, x_max = plt.xlim()
        plt.xlim(x_min, x_data_max + (x_data_max - x_min) * 0.02)

    plt.xlabel("Financial Year Commencing")
    plt.ylabel("Spending (Billions of GBP)")
    plt.title("UK Public Spending from 1955 to 2023")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.show()


plot(listOfFiles, listOfHeaders) #Plot the graph
