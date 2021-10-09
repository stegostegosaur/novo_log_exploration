import json

from getUserBehaviourStats import *
from getDescriptiveStats import *
from getNumberData import *
from getAccuracyData import *

descriptive_csv_rows = list()
descriptive_csv_header = ["Participant", "Non-empty utterances",
                          "Ratio correct utterances", "Nr words",
                          "Ratio correct words", "Ratio correct phones"]

behaviour_csv_rows = list()
behaviour_csv_headers = ['Participant', 'First day', 'Last day', 'Total duration (days)',
                         'Active days', 'Nr total utterances', 'Nr unique utterances']


for file in get_current_directory(path):
    if not file.endswith('.json'):
        continue
    if file.split('.')[0] in excluded_users:
        continue
    with open(file) as f:
        if check_empty_file(f):
            continue
        data = json.load(f)
        get_nr_dct(data)
        get_accuracy_dct(data)

        descriptive_columns = extract_binary_correctness_ratios(data)
        descriptive_csv_rows.append(get_csv_rows(file, descriptive_columns))

        behaviour_columns = get_timewise_data(file, data)
        behaviour_csv_rows.append(get_csv_rows(file, behaviour_columns))


write_csv_file(input_file=descriptive_csv_rows,
               title="Descriptive analysis",
               header=descriptive_csv_header)

write_csv_file(input_file=behaviour_csv_rows,
               title="User behaviour analysis",
               header=behaviour_csv_headers)

write_csv_file(input_file=transform_dct(accuracy_per_lesson),
               sort_by='x',
               header=['Lesson', 'Mean'],
               title='Accuracy_per_lesson')

write_csv_file(input_file=transform_dct(accuracy_per_prompt),
               sort_by='y',
               header=['Prompt', 'Mean'],
               title='Accuracy_per_prompt')

plotting_function(utt_per_participant_plot,
                  sort_by='y',
                  bar_type='bar',
                  ticks_to_digits='user',
                  x_label="Participants",
                  y_label="Nr total inputs")

plotting_function(utt_per_day_plot,
                  sort_by='x',
                  bar_type='bar',
                  ticks_to_digits='days',
                  x_label='Days of experiment',
                  y_label='Nr of total inputs')

plotting_function(unique_per_participant_plot,
                  sort_by='y',
                  bar_type='bar',
                  ticks_to_digits='user',
                  x_label="Participants",
                  y_label="Nr unique prompts")

plotting_function(active_per_participant,
                  sort_by='y',
                  bar_type='bar',
                  x_label="Participants",
                  y_label='Days spent with active practice')

plotting_function(most_frequent_prompts,
                  sort_by='y',
                  x_label='Nr practiced',
                  y_label='Prompt',
                  bar_type='barh',
                  top_list=10)

plotting_function(utt_per_unit,
                  sort_by='x',
                  x_label='Unit numbers',
                  y_label='Nr total inputs',
                  bar_type='bar')
