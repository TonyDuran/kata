try:
    from raw_input import input
except ImportError:
    pass

def acmTeam(topic):

    lower_index = sum = 0

    upper_index = 1
    final_result = list()

    while lower_index != len(topic)-2:

        if upper_index > len(topic)-1:
            lower_index += 1
            upper_index = lower_index+1

        result = bin(int(topic[lower_index], 2) | int(topic[upper_index], 2))

        temp_count = result.count(str(1))
        upper_index += 1

        if temp_count >= sum:

            sum = temp_count
            final_result.append(sum)

    print(sum)
    print(final_result.count(sum))

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = list()

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    acmTeam(topic)
