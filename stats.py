def get_num_words(text):
        return len(text.split())
def get_char_count(text):
        char_counts = {}
        for char in text.lower():
                if char in char_counts:
                        char_counts[char] += 1
                else:
                        char_counts[char] = 1
        return char_counts   
def chars_dict_to_sorted_list(char_counts):
        chars_list = []
        for char, count in char_counts.items():
                chars_list.append({"char": char, "count": count})

        def sort_on(dict):
                return dict["count"]

        chars_list.sort(reverse=True, key=sort_on)

        return chars_list
