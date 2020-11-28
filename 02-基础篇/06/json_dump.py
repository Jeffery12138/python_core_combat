import re
import json


def parse(fin):
    # 生成单词和词频的字典
    word_cnt = {}

    for f in fin:

        text_line = f

        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text_line)

        # 转为小写
        text = text.lower()

        # 生成所有单词的列表
        word_list = text.split(' ')

        # 去除空白单词
        word_list = filter(None, word_list)

        # 只保留英文单字
        word_list = [word for word in word_list if word[0] <= 'z']

        # 生成单词和词频的字典
        for word in word_list:
            if word not in word_cnt:
                word_cnt[word] = 0
            word_cnt[word] += 1

    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_word_cnt


with open('in.txt', 'r') as fin:
    word_and_freq = parse(fin)

word_and_freq_dict = {}

for word, freq in word_and_freq:
    word_and_freq_dict[word] = freq

with open('out.json', 'w') as fout:
    json.dump(word_and_freq_dict, fout)
