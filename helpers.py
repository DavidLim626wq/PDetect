from nltk.tokenize import sent_tokenize
# imported sent_tokenize according to walkthrough instructions

def lines(a, b):
    list_a = a.split("\n")
    list_b = b.split("\n")
    intersection = set([line for line in list_a if line in list_b])  # reduce to a set to eliminate duplicates

    return intersection


def sentences(a, b):
    list_a = sent_tokenize(a)
    list_b = sent_tokenize(b)
    intersection = set([sent for sent in list_a if sent in list_b])

    return intersection


def get_substrings(a, n):
    substrings = []
    for i in range(len(a) - n + 1):
        sg = a[i:n+i]
        substrings.append(sg)

    return(substrings)


def substrings(a, b, n):
    list_a = get_substrings(a, n)
    list_b = get_substrings(b, n)
    intersection = set([item for item in list_a if item in list_b])

    # TODO
    return intersection
