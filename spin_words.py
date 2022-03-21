def spin_words(sentence):
    n1 = (" ")
    st1 = sentence.split(' ')
    st2 = []
    for elem in st1:
        if len(elem) > 5:
            st2.append(elem[::-1])
        else:
            st2.append(elem)
    sentence = n1.join(st2)
    return sentence



n = ("Hey fellow warriors")
n1 = spin_words(n)
print(n1)
# n1 = (" ")
# st1 = n.split(' ')
# st2 = []
# for elem in st1:
#     if len(elem) > 5:
#         st2.append(elem[::-1])
#     else:
#         st2.append(elem)

# print(n1.join(st2))
# print(st2)