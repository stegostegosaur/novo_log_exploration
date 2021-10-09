from datetime import datetime
from main import *


def initialize_dct_and_lst(file, data):
    utt_per_day_csv = dict()
    prompt_list_csv = list()

    for utterance in data:
        items = utterance['items'][0]
        recognized_raw = items['asrFeedback']['recognized']['raw']
        if recognized_raw == "":
            continue
        prompt_list_csv.append(recognized_raw)
        received = items['asrFeedback']['receivedAt'].split('T')[0]

        if received not in utt_per_day_csv:
            utt_per_day_csv[received] = 0
        utt_per_day_csv[received] += 1

        if received not in utt_per_day_plot:
            utt_per_day_plot[received] = 0
        utt_per_day_plot[received] += 1

        if file.split('.')[0] not in utt_per_participant_plot:
            utt_per_participant_plot[file.split('.')[0]] = 0
        utt_per_participant_plot[file.split('.')[0]] += 1

        if file.split('.')[0] not in unique_per_participant_plot:
            unique_per_participant_plot[file.split('.')[0]] = 0
        unique_per_participant_plot[file.split('.')[0]] = len(set(prompt_list_csv))

    return utt_per_day_csv, prompt_list_csv


def get_timewise_data(file, data):
    dct, lst = initialize_dct_and_lst(file, data)
    date_format = "%Y-%m-%d"
    first_day = list(dct.keys())[0]
    last_day = list(dct.keys())[-1]
    a = datetime.strptime(list(dct.keys())[0], date_format)
    b = datetime.strptime(list(dct.keys())[-1], date_format)
    delta = b - a
    if delta.days != 0:
        total_days = delta.days
    else:
        total_days = 1

    active_days = len(dct)
    values = dct.values()
    total_utterances = sum(values)
    unique_utterances = len(set(lst))

    if get_digit(file) not in active_per_participant:
        active_per_participant[get_digit(file)] = 0
    active_per_participant[get_digit(file)] = active_days

    return [first_day, last_day, total_days, active_days, total_utterances, unique_utterances]


utt_per_participant_plot = dict()
unique_per_participant_plot = dict()
utt_per_day_plot = dict()
active_per_participant = dict()
