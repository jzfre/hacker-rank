#!/bin/python3

import sys

# bruteforces
def acmTeam(topic):
    # Convert the binary string to integers first
    topic_ints = [int(member, 2) for member in topic]
    top_topics = 0
    top_teams = 0

    for idx in range(len(topic_ints)):
        for jdx in range(idx + 1, len(topic_ints)):
            count_ones = bin(topic_ints[idx] | topic_ints[jdx]).count('1')
            
            if count_ones > top_topics:
                top_topics = count_ones
                top_teams = 1
            elif count_ones == top_topics:
                top_teams += 1

    return [top_topics, top_teams]

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()