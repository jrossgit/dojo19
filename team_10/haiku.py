import wave
import os
import random
import sys

WORDS = {
    1: [
        'a',
        'and',
        'the',
        'code',
        'get',
        'dance',
        'will',
        'fork',
        'git',
        'snake',
        'plant',
        'trees',
    ],
    2: [
        'python',
        'dojo',
        'dancing',
        'pizza',
        'cocos',
        'Cardiff',
        'London',
        'Pycon',
        'hurry',
        'quickly',
    ],
    3: [
        'meditate',
        'introspect',
        'validate',
        'optimist',
        'realist',
        'happiness',
        'indulgence',
        'decadence',
        'unsponsored',
        'reverted',
    ],
}

def generate_haiku():
    lines = []
    for syl_count in 5, 7, 5:
        this_line = []
        while syl_count > 3:
            this_syl = random.randint(1, 3)
            this_word = random.choice(
                WORDS[this_syl]
            )
            syl_count -= this_syl
            this_line.append(this_word)

        if syl_count > 0:
            this_line.append(random.choice(WORDS[syl_count]))
        lines.append(' '.join(this_line))
    return lines



def main():
    haiku = generate_haiku()
    for line in haiku:
        print(line)

if __name__ == '__main__':
    main()