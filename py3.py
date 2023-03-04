def reverse_string(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

input_str = input("Enter a sentence: ")
output_str = reverse_string(input_str)
print(output_str)