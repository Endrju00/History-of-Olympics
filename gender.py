import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    athlete_events = pd.read_csv('athlete_events.csv')
    labels = ('Male', 'Female')

    male = athlete_events[athlete_events['Sex'] == 'M']
    female = athlete_events[athlete_events['Sex'] == 'F']

    # All participants
    male_size = male['Sex'].count()
    female_size = female['Sex'].count()
    sizes = [male_size, female_size]
    explode = (0, 0.1)

    # Medals
    male_medals = male[pd.notna(male['Medal'])]['Medal'].count()
    female_medals = female[pd.notna(female['Medal'])]['Medal'].count()
    medal_sizes = [male_medals, female_medals]

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    ax1.set_title(f"Gender of {male_size + female_size} participants",
            fontsize=16)

    ax2.pie(medal_sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax2.axis('equal')
    ax2.set_title(f'Medals of women and men. (Total: {male_medals+female_medals} medals)',
            fontsize=16)

    plt.legend(loc='lower left')
    plt.show()
