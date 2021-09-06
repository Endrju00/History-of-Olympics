import pandas as pd
import matplotlib.pyplot as plt

def count_medals(medals, countries):
    """Return sorted array with tuples including NOC and number of medals"""
    data = []
    for country in countries:
        data.append((country, medals[medals['NOC']==country]['Medal'].count()))

    return sorted(data, key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    athlete_events = pd.read_csv('athlete_events.csv')
    country_definitions = pd.read_csv('country_definitions.csv')

    # Get people with medals
    medals = athlete_events[pd.notna(athlete_events['Medal'])]
    medals_after_2000 = medals[medals['Year'] >= 2000]
    medals_after_2011 = medals[medals['Year'] >= 2011]

    countries = country_definitions['NOC'] # get all countires NOC

    # Count medals
    timespan = count_medals(medals, countries)
    years_20 = count_medals(medals_after_2000, countries)
    years_10 = count_medals(medals_after_2011, countries)

    # Get top4
    top_4_timespan = timespan[:4]
    top_4_20 = years_20[:4]
    top_4_10 = years_10[:4]

    # Plot
    plt.style.use('seaborn-darkgrid')
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

    colors = ['#023e8a', '#0077b6', '#00b4d8', '#48cae4']
    rects1 = ax1.bar([x[0] for x in top_4_timespan], [x[1] for x in top_4_timespan],
            color=colors)
    rects2 = ax2.bar([y[0] for y in top_4_20], [y[1] for y in top_4_20],
            color=colors)
    rects3 = ax3.bar([z[0] for z in top_4_10], [z[1] for z in top_4_10],
            color=colors)

    ax1.set_xlabel("Countries", fontsize=15)
    ax1.set_ylabel("Number of medals won", fontsize=15)
    ax1.set_title("Top four medal winners of all time.", fontsize=15)
    ax2.set_xlabel("Countries", fontsize=15)
    ax2.set_ylabel("Number of medals won", fontsize=15)
    ax2.set_title("Top four medal winners of the past 20 years.", fontsize=15)
    ax3.set_xlabel("Countries", fontsize=15)
    ax3.set_ylabel("Number of medals won", fontsize=15)
    ax3.set_title("Top four medal winners of the past 10 years.", fontsize=15)

    ax1.bar_label(rects1, padding=3, fontsize=15)
    ax2.bar_label(rects2, padding=3, fontsize=15)
    ax3.bar_label(rects3, padding=3, fontsize=15)

    plt.show()
