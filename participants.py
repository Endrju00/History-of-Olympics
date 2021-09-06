import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    athlete_events = pd.read_csv('athlete_events.csv')

    data = []
    for year in range(1896, 2017):
        participants = athlete_events[athlete_events['Year'] == year]
        participants = participants.drop_duplicates("ID", keep=False) # Get unique participants from year
        data.append((year, participants['Name'].count()))

    # Plot
    plt.style.use('seaborn-darkgrid')
    fig, ax1 = plt.subplots(1, 1)
    ax1.bar([x[0] for x in data], [x[1] for x in data], color='#023e8a')

    ax1.set_title("Participants 1896-2016.", fontsize=16)
    plt.xlabel("Years", fontsize= 15)
    plt.ylabel("Number of participants", fontsize= 15)
    plt.show()
