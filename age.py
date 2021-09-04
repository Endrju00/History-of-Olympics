import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    athlete_events = pd.read_csv('athlete_events.csv')

    data = []
    for age in range(10, 88):
        ppl = athlete_events[athlete_events['Age'] == age]
        ppl = ppl[pd.notna(athlete_events['Medal'])]
        data.append((age, ppl['ID'].count()))

    # Plot
    plt.style.use('seaborn-darkgrid')
    fig, ax1 = plt.subplots(1, 1)
    ax1.bar([x[0] for x in data], [x[1] for x in data])

    ax1.set_title("Age and number of medals won comparision.", fontsize=16)
    plt.xlabel("Age", fontsize= 15)
    plt.ylabel("Number of medals won", fontsize= 15)
    plt.show()
