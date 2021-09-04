import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_dual(labels, short, rest, title):
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, short, width, label='Short', color='#e63946')
    rects2 = ax.bar(x + width/2, rest, width, label='The rest', color='#023e8a')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of participants')
    ax.set_title(title, fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=14)
    ax.legend(fontsize=15)

    ax.bar_label(rects1, padding=3, fontsize=15)
    ax.bar_label(rects2, padding=3, fontsize=15)

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    athlete_events = pd.read_csv('athlete_events.csv')

    # Gender
    male = athlete_events[athlete_events['Sex'] == 'M']
    female = athlete_events[athlete_events['Sex'] == 'F']

    # Height
    short_male = male[male["Height"] < 175]
    male = male[male["Height"] >= 175]

    short_female = female[female["Height"] < 165]
    female = female[female["Height"] >= 165]

    # Sports
    sports = athlete_events.drop_duplicates('Sport')['Sport']

    data_male = []
    data_female = []

    for sport in sports:
        # Count short and other male
        short_male_size = short_male[short_male['Sport'] == sport]['Sport'].count()
        male_size = male[male['Sport'] == sport]['Sport'].count()

        # if dominated append
        if short_male_size > male_size:
            data_male.append((sport, short_male_size, male_size))

        # Count short and other female
        short_female_size = short_female[short_female['Sport'] == sport]['Sport'].count()
        female_size = female[female['Sport'] == sport]['Sport'].count()

        # if dominated append
        if short_female_size > female_size:
            data_female.append((sport, short_female_size, female_size))

    # Sort data
    data_male = sorted(data_male, key=lambda x: x[1], reverse=True)
    data_female = sorted(data_female, key=lambda x: x[1], reverse=True)

    # Data for men
    labels_men = [x[0] for x in data_male]
    short_men = [x[1] for x in data_male]
    rest_men = [x[2] for x in data_male]

    # Data for women
    labels_women = [x[0] for x in data_female]
    short_women = [x[1] for x in data_female]
    rest_women = [x[2] for x in data_female]

    # Plot
    plot_dual(labels_men, short_men, rest_men, 'Sports dominated by short men.')
    plot_dual(labels_women, short_women, rest_women, 'Sports dominated by short women.')
