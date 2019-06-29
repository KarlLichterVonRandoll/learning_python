from sstack import SStack

str01 = "]Thanks to {the} [flexibility of Python " \
        "and the [powerful] ecosystem of pac(kages, " \
        "{the Azure (CLI)} supports features such as autoc]ompletion " \
        "(in shells that support it), persistent credentials, JMESPath result parsing," \
        " lazy initialization, network-less unit tests, and more."

str0 = "[hel{lo(}w)orld)}],python{program},(2019)]"

st = SStack()

for i in range(len(str01)):
    if str01[i] in ["{", "}", "[", "]", "(", ")"]:
        if st.is_empty() or str01[i] in ["{", "[", "("]:
            st.push((i, str01[i]))
        else:
            top_elem = st.top()[1]
            if (top_elem == "{" and str01[i] == "}") or (top_elem == "(" and str01[i] == ")") or (top_elem == "[" and str01[i] == "]"):
                st.pop()
            else:
                print(i, str01[i])
print("==================================")
while not st.is_empty():
    re = st.pop()
    print(re[0], re[1])

# for i in range(len(str01)):
#     if str01[i] in ["{", "[", "("]:
#         st.push((i, str01[i]))
#     elif str01[i] in ["}", "]", ")"]:
#         top = st.top()[1]
#         if (top == "{" and str01[i] == "}") or (top == "(" and str01[i] == ")") or (top == "[" and str01[i] == "]"):
#             st.pop()
#         else:
#             print(i, str01[i])
#
# while not st.is_empty():
#     re = st.pop()
#     print(re[0], re[1])
