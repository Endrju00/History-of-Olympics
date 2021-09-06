import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    athlete_events = pd.read_csv('athlete_events.csv')
    with_medals = athlete_events[pd.notna(athlete_events['Medal'])] # Get participants with medals
    counted = with_medals['Age'].value_counts().sort_index() # Count and sort by age

    # Plot
    plt.style.use('seaborn-darkgrid')
    fig, ax1 = plt.subplots(1, 1)
    ax1.bar([age for age in counted.keys()], [counted[age] for age in counted.keys()], color='#023e8a')

    ax1.set_title("Number of medals won at a certain age.", fontsize=16)
    plt.xlabel("Age", fontsize= 15)
    plt.ylabel("Number of medals won", fontsize= 15)
    plt.show()
