# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:09:03 2020

@author: jrbra
"""
import pyphen
import random

dic = pyphen.Pyphen(lang='en')


def read_word_list():
    with open("word_list.txt", "r") as f  :
        return [i.strip() for i in f.readlines()]
    
    
def syllable_count(word):
    return len(dic.inserted(word).split("-"))


def parse_syllables():
    syl_dict = {}
    for word in read_word_list():
        syl_count = syllable_count(word)
        if not syl_count in syl_dict.keys():
            syl_dict[syl_count] = [word]
        else:
            syl_dict[syl_count].append(word)
    return syl_dict


def subset_sum(numbers, target, partial=[], results=[]):
    s = sum(partial)
    if s == target:
        results.append(partial)
    if s >= target:
        return
    for i in range(len(numbers)):
        n = numbers[i]
        subset_sum(numbers, target, partial + [n], results = results)
    return results

if __name__ == "__main__":
    syl_dictionary = parse_syllables()
    all_5_syl_sums = subset_sum(list(syl_dictionary.keys()), 5, results=[])
    all_7_syl_sums = subset_sum(list(syl_dictionary.keys()), 7, results=[])
    
    first_line_sum = random.choice(all_5_syl_sums)
    sec_line_sum = random.choice(all_7_syl_sums)
    third_line_sum = random.choice(all_5_syl_sums)
    
    first_line = ""
    second_line = ""
    third_line = ""
    
    for i in first_line_sum:
        first_line += random.choice(syl_dictionary[i]) + " "
    for i in sec_line_sum:
        second_line += random.choice(syl_dictionary[i]) + " "
    for i in third_line_sum:
        third_line += random.choice(syl_dictionary[i]) + " "
        
    print(first_line.capitalize() + "\n" + second_line.capitalize() + "\n" + third_line.capitalize())
    input()