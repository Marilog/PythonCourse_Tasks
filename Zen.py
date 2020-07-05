Zen_Python = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


#print(Zen_Python)

cnt_better=Zen_Python.count("better")
cnt_is=Zen_Python.count("is")
cnt_never=Zen_Python.count("never")
print("The count of BETTER is ", cnt_better,  "The count of IS is", cnt_is, "The count of NEVER is", cnt_never)

upper_register_function=Zen_Python.upper()
print(upper_register_function)

replace_function=Zen_Python.replace("i", "&")
print(replace_function)