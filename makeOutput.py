import matplotlib.pyplot as plt
import csv
from main import *

new_dir = 'Result of Analysis'
create_new_folder(new_dir)
output_dir = path + '/' + new_dir + '/'


def plotting_function(dct, sort_by=None, bar_type='bar', ticks_to_digits=None, x_label=None,
                      y_label=None, top_list=None):

    fig, ax = plt.subplots()
    ax.set_xlabel(' ' if x_label is None else x_label)
    ax.set_ylabel(' ' if y_label is None else y_label)
    plt.xticks(fontsize=5, rotation=315)
    plt.yticks(fontsize=8)

    if sort_by == 'x':
        dct = dict(sorted(dct.items(), key=lambda x: x[0], reverse=False)[:top_list])
    else:
        dct = dict(sorted(dct.items(), key=lambda x: x[1], reverse=True)[:top_list])

    if bar_type == 'bar':
        plt.bar(dct.keys(), dct.values())
    if bar_type == 'barh':
        plt.barh(list(dct.keys()), list(dct.values()))

    if ticks_to_digits == 'user':
        ax.set_xticklabels([get_digit(i) for i in dct.keys()])
    if ticks_to_digits == 'days':
        ax.set_xticklabels([i + 1 for i in range(len(dct))])

    if top_list:
        plt.tight_layout()
        plt.gca().invert_yaxis()
        plt.tick_params(axis='y', labelsize=8)

    output = output_dir + x_label + '-' + y_label
    plt.savefig(output + '.png', dpi=300)


def get_csv_rows(participant, columns):
    csv_row = list()
    csv_row.append(participant.split('.')[0])
    for c in columns:
        csv_row.append("{:.2f}".format(c) if isinstance(c, float) else c)

    return csv_row


def write_csv_file(input_file=[dict, list], title=str, sort_by=None, header=None):
    with open(output_dir + title + ".csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        if isinstance(input_file, dict):
            if sort_by == 'x':
                input_file = dict(sorted(input_file.items(), key=lambda x: x[0], reverse=False))
            if sort_by == 'y':
                input_file = dict(sorted(input_file.items(), key=lambda x: x[1], reverse=True))
            for k, v in input_file.items():
                writer.writerow([k, v])
        if isinstance(input_file, list):
            for i in input_file:
                writer.writerow(i)
