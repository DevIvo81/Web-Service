import os

import matplotlib.pyplot as plt

os.system("cls")

plt.style.use("seaborn-v0_8-dark")


def file_list_and_dict(route):

    data_files = []

    for root, dirs, files in os.walk(route):

        for file in files:
            if len(data_files) < 1000:
                data_files.append(file.lower())
            else:
                data_files.sort()
                break

    occur_dct = {}

    for name in data_files:
        if name[0] not in occur_dct.keys():
            occur_dct[name[0]] = 1
        else:
            occur_dct[name[0]] += 1

    return data_files, occur_dct


def bar_plot(route):

    route = "d:\\000_PyProjects\\ZPro\\App-003-Selectorlib\\"

    file_list, occ = file_list_and_dict(route)

    folder = list(os.listdir(route))

    for file in folder:
        print(file)
        print(type(occ.keys()))

    fig, ax = plt.subplots(figsize=(8, 6))

    x = list(occ.keys())
    height = list(occ.values())
    width = 0.75
    color = "darkorange"

    ax.bar(
        x=x,
        height=height,
        width=width,
        color=color,
        align="center"
    )

    for i, v in enumerate(height):
        ax.text(x = i-0.25,
                y = v + 3, 
                s = str(v),
                c = "green",
                rotation=90)

    plt.savefig(os.path.join(os.getcwd(), "File_Statistics.png"), dpi=300, format="png", bbox_inches="tight")

    plt.show()