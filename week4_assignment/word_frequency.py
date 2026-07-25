# Word Frequency Counter
text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""


# function to count words
def word_frequency(text):
    # initializing empty dictionary
    tracker = {}
    # splitting the text and converting them in lowercase
    # also removing the punctuation
    splitted_text = text.replace(".", "").lower().split()

    # splitted_text is a list, iterating through the list
    for texts in splitted_text:
        # if the splitted text is in dictionary
        if texts in tracker:
            tracker[texts] += 1  # increase count
        # if the splitted text is not in dictionary
        else:
            tracker[texts] = 1  # initialize the count to 1

    # finding top 3 wordsm sorted by values
    sorted_by_values = sorted(tracker.items(), key=lambda x: x[1], reverse=True)

    # Print top 3
    print("Top 3 words:")
    # printing the top 3 words
    for word, count in sorted_by_values[:3]:
        print(f"{word} - {count} times")


word_frequency(text)  # calling the function
