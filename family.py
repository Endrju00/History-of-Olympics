import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    athlete_events = pd.read_csv('athlete_events.csv')
    participants = athlete_events.drop_duplicates('ID')['Name'] # to count gender the objects have to be unique

    # Prepare data
    d = {'Firstname': [], 'Surname':[]}
    for person in participants:
        data = person.split()
        d['Firstname'].append(data[0])
        d['Surname'].append(data[-1]) # get the last part of the surname

    df = pd.DataFrame(data=d)

    top_10 = df['Surname'].value_counts()[1:11] # first is .Jr
    labels = [x for x in top_10.keys()]
    values = [top_10[x] for x in top_10.keys()]

    # Plot
    plt.style.use('ggplot')
    fig, ax1 = plt.subplots(1, 1)
    rects = ax1.bar(labels, values, color=['#03045e', '#032174', '#023E8A', '#015BA0', '#0077B6', '#0096C7', '#00A5D0', '#00B4D8', '#48CAE4', '#6CD5EA'])

    ax1.bar_label(rects, padding=3, fontsize=15)
    ax1.set_title("Most popular surnames.", fontsize=16)
    plt.xlabel("Surnames", fontsize=15)
    plt.ylabel("Number of occurrences of the surname", fontsize=15)
    plt.show()
