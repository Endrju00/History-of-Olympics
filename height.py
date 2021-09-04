import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    athlete_events = pd.read_csv('athlete_events.csv')

    male = athlete_events[athlete_events['Sex'] == 'M']
    female = athlete_events[athlete_events['Sex'] == 'F']

    avg_man_height = round(male['Height'].mean(), 0)
    avg_woman_height = round(female['Height'].mean(), 0)
    print(f'AVG MAN HEIGHT: {avg_man_height}, AVG WOMAN HEIGHT: {avg_woman_height}')

    # MEN
    tall_men = male[athlete_events["Height"] >= 180]
    short_men = male[athlete_events["Height"] < 180]

    # with medals
    tall_men = tall_men[pd.notna(tall_men['Medal'])]['Medal'].count()
    short_men = short_men[pd.notna(short_men['Medal'])]['Medal'].count()

    # WOMEN
    tall_women = female[athlete_events["Height"] >= 170]
    short_women = female[athlete_events["Height"] < 170]

    # with medals
    tall_women = tall_women[pd.notna(tall_women['Medal'])]['Medal'].count()
    short_women = short_women[pd.notna(short_women['Medal'])]['Medal'].count()

    # Plot
    plt.style.use('seaborn-darkgrid')
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.bar(['Women (height < 170)', 'Tall women (height >= 170)'],
            [short_women, tall_women,],
            color=['#e63946', '#023e8a'])
    ax1.set_title("Height and number of medals won by women comparision.",
            fontsize=16)
    ax1.set_xlabel("Height")
    ax1.set_ylabel("Number of medals won")

    ax2.bar(['Men (height < 180)', 'Tall men (height >= 180)'],
            [short_men, tall_men],
            color=['#e63946', '#023e8a'])


    ax1.set_title("Height and number of medals won by men comparision.",
            fontsize=16)
    ax1.set_xlabel("Height")
    ax1.set_ylabel("Number of medals won")

    ax2.set_title("Height and number of medals won by women comparision.",
            fontsize=16)
    ax2.set_xlabel("Height")
    ax2.set_ylabel("Number of medals won")

    plt.show()
