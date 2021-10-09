import statistics
from main import *


def get_accuracy_dct(data):
    for utterance in data:
        unit_nr = re.findall(r'\d', utterance['courseTitle'].split(':')[0])[0]
        items = utterance['items'][0]
        correct = items['correct']
        recognized_raw = items['asrFeedback']['recognized']['raw']
        if recognized_raw == "":
            continue

        if unit_nr not in accuracy_per_lesson:
            accuracy_per_lesson[unit_nr] = list()
        accuracy_per_lesson[unit_nr].append(correct)

        if recognized_raw not in accuracy_per_prompt:
            accuracy_per_prompt[recognized_raw] = list()
        accuracy_per_prompt[recognized_raw].append(correct)

        ###############################################
        # FOR WORD PROBABILITIES                      #
        # words = items['asrFeedback']['words']       #
        # for w in words:                             #
        #     prob = w['confidence']['prob']          #
        #     word = w['label']['raw']                #
        ###############################################


def transform_dct(dct):
    for k, v in dct.items():
        dct[k] = "{:.2f}".format(statistics.mean(v) * 100)
        dct.update()
    return dct


accuracy_per_lesson = dict()
accuracy_per_prompt = dict()
