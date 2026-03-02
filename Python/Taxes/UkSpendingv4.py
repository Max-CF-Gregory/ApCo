from matplotlib import pyplot as plt
from csv import DictReader
import numpy as np
import mplcursors
#👆import statements️
def getdata(filename: str) -> list[dict]:
    with open(filename, "r", newline="") as f:
        return list(DictReader(f))

def plot(filename: str, headers: list[str]) -> None:
    ups = getdata(filename)
    label_positions = []
    lines = []

    for h in headers:
        xpoints, ypoints = [], []
        for i in ups:
            x = int(i["year"][:4])
            try:
                y=float(i[h])
            except ValueError:
                y=np.nan
            xpoints.append(x)
            ypoints.append(y)
        xpoints, ypoints = np.array(xpoints), np.array(ypoints)
        line, = plt.plot(xpoints, ypoints, label=h.capitalize())
        lines.append(line)
        #Find last point for label positioning
        if len(ypoints) > 0:
            #Get the x of the last point
            x_label = xpoints[-1]
            #Get the y of the last NaNaN (or is it just number?) point
            valid_mask = ~np.isnan(ypoints)
            if valid_mask.any():
                last_valid_idx = np.where(valid_mask)[0][-1]
                y_label = ypoints[last_valid_idx]
            else:
                y_label = 0  #Default y if all are Nan

            label_positions.append((y_label, h.capitalize(), line.get_color(), x_label))

    plt.ylim(bottom=0) #Bottom starts @ 0
    plt.xlim(left=1955) #Left starts in 1955
    # Fix overlapping that labels
    if label_positions:
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
            plt.text(x_pos, adjusted_y, f'    {label_text}', color=color, va="center", fontsize=9, clip_on=False) #Adjust the number of space before label_text to change it's offset

        x_data_max = max(pos[3] for pos in label_positions)
        x_min, x_max = plt.xlim()
        plt.xlim(x_min, x_data_max + (x_data_max - x_min) * 0.02)

    plt.xlabel("Financial Year Commencing")
    plt.ylabel("Spending (Billions of GBP)")
    plt.title("UK Public Spending from 1955 to 2023")
    plt.grid(alpha=0.25)
    plt.tight_layout()

    # Hover annotations
    cursor = mplcursors.cursor(lines, hover=True)
    @cursor.connect("add")
    def on_add(sel):
        x, y = sel.target
        label = sel.artist.get_label()
        sel.annotation.set_text(f"{label}\nYear: {int(x)}\nSpending: {y:.2f} bn")
        sel.annotation.get_bbox_patch().set(alpha=0.9)
    plt.show()

plot("UK_public_spending.csv", ["benefits", "health", "education", "defence", "police", "transport", "housing", "aid"])
