from main import *


def get_nr_dct(data):
    for utterance in data:
        unit_nr = re.findall(r'\d', utterance['courseTitle'].split(':')[0])[0]
        items = utterance['items'][0]
        recognized_raw = items['asrFeedback']['recognized']['raw']
        if recognized_raw == "":
            continue

        if unit_nr not in utt_per_unit:
            utt_per_unit[unit_nr] = 0
        utt_per_unit[unit_nr] += 1

        if recognized_raw not in most_frequent_prompts:
            most_frequent_prompts[recognized_raw] = 0
        most_frequent_prompts[recognized_raw] += 1


most_frequent_prompts = dict()
utt_per_unit = dict()
