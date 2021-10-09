import statistics
from makeOutput import *


# returns a row of csv vars
def extract_binary_correctness_ratios(data):
    # creating variables to be used in the csv
    utterance_list = list()
    word_list = list()

    total_nr_phones = 0
    correctly_pronounced_phones = 0

    # extract binary correctness labels of utterances into a list
    for utterance in data:
        items = utterance['items'][0]
        recognized_raw = items['asrFeedback']['recognized']['raw']

        # skipping empty utterances that were not interacted with by the participant
        if recognized_raw == "":
            continue

        utterance_list.append(items['correct'])

        # extract binary correctness labels of words into a list
        words = items['asrFeedback']['words']
        for w in words:
            word_list.append(w['hasErrors'])

            gold_label_phones = w["minDistCorrectPronunciation"]["phones"]

            # extract total number of phones and correctly pronounced phones
            phone_recognized_list = list()
            for i in range(len(gold_label_phones)):
                total_nr_phones += 1

            phones = w["phones"]
            for p in phones:
                phone_recognized = p['recognized']['label']
                phone_recognized_list.append(phone_recognized)

            # compare phones labels: user input is correct if it matches the closest accepted phone label
            for a, b in zip(phone_recognized_list, gold_label_phones):
                if truncate_digit(a) == truncate_digit(b):
                    correctly_pronounced_phones += 1

    return [len(utterance_list), statistics.mean(utterance_list) * 100,
            len(word_list), 100 - statistics.mean(word_list) * 100,
            total_nr_phones, correctly_pronounced_phones / total_nr_phones * 100]
