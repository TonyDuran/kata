try:
    from raw_input import input
except ImportError:
    pass


from itertools import count, zip_longest


def lisas_workbook(n, k, a):
    page = count(1)
    return sum([len([1 for probs in zip_longest(*[iter(range(1, num_chpt_probs+1))]*k) if next(page) in probs]) for num_chpt_probs in a])


# def lisas_workbook(n,k,a):
#     '''Return count of "special numbers" -> same problem number as page number.

#     n: total chapters
#     k: max problems per page
#     a[i] total problems in chapter i+1 '''

#     num_special=0
#     cur_page=1

#     for i in range(len(a)):

#         num_probs_in_chapter=a[i]
#         num_full_pages, leftover_probs = divmod(num_probs_in_chapter, k)
#         #print('num_full_pages, leftover_probs', num_full_pages, leftover_probs)

#         total_pages = num_full_pages + ( 1 if leftover_probs else 0 )
#         problems_in_chapter=iter(range(1, a[i]+1))

#         for _ in range(total_pages):
#             probs_on_page = [next(problems_in_chapter, None) for _ in range(k)]
#             if cur_page in probs_on_page:
#                 #print('found %d in %s' % (cur_page, str(probs_on_page)) )
#                 num_special+=1
#     return num_special

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = lisas_workbook(n, k, arr)
    print(result)