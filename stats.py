def wordcounter(booktext):
    return len(booktext.split())

def char_counter(booktext):

    lower_text = booktext.lower()
    char_dict = {}   
    for char in lower_text:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_dict(dict):

    li = []
    for char, num in dict.items():
      #  if char.isalpha():
        chardict = {"char":char,"num":num}
        li.append(chardict)
    li.sort(reverse=True, key=sort_on)

    return li
    

