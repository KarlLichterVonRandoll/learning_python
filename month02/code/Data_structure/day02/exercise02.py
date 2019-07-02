from sstack import SStack

str01 = "]Thanks to {the} [flexibility of Python " \
        "and the [powerful] ecosys[)]tem of pac(kages, " \
        "{the Azure (CLI)} supports features such as autoc]ompletion " \
        "(in shells that support it), persistent credentials, JMESPath result parsing," \
        " lazy initialization, network-less unit tests, and more."

str0 = "[hel{lo}world],python{program},(]2019)"

# st = SStack()
#
# for i in range(len(str01)):
#     if str01[i] in ["{", "}", "[", "]", "(", ")"]:
#         if st.is_empty() or str01[i] in ["{", "[", "("]:
#             st.push((i, str01[i]))
#         else:
#             # top = st.pop()
#             top_elem = st.top()[1]
#             if (top_elem == "{" and str01[i] == "}") or (top_elem == "(" and str01[i] == ")") or (
#                     top_elem == "[" and str01[i] == "]"):
#                 st.pop()
#             else:
#                 print(i, str01[i])
# print("==================================")
# while not st.is_empty():
#     re = st.pop()
#     print(re[0], re[1])

ss = SStack()

dict01 = {"}": "{", ")": "(", "]": "["}


def travel(text):
    i = 0
    text_len = len(text)

    while True:
        while i < text_len and text[i] not in "{}()[]":
            i += 1

        if i >= text_len:
            return
        else:
            yield text[i], i
            i += 1


def verify(text):
    leap = True
    for pr, i in travel(text):
        if pr in "{([":
            ss.push((pr, i))
        elif ss.is_empty() or ss.pop()[0] != dict01[pr]:
            leap = False
            print(pr, i)
    else:
        while not ss.is_empty():
            print(ss.pop()[0], ss.pop()[1])
    if leap:
        print("no mistake")



verify(str0)
