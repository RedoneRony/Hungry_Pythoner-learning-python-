'''
def add_explanation(line):
    return line + '!'
update_line= add_explanation
#when print Updat_line automatically call this function
print(update_line("Hello world"))

#function use as a another functions argument

def beautify(text):
    return text + '!!!'
def make_line(func, words):
    return "Hello" + func(words)

print(make_line(beautify,"world"))
'''

pr=[12,12,12,12,13]
pr[4]=145
print(pr[4])