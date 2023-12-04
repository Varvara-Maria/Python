def remove_previous_occurrences(text):

    words = text.split();
    result = [];

    for word in words:
        last_letter = word[-1];

        filtered_word = ''.join([char for char in word if char != last_letter]);

        result.append(filtered_word)

    final_text = ' '.join(result)
    return final_text

input_text = "Текст з прикладом програми. Перевірки роботи."
output_text = remove_previous_occurrences(input_text)
print(output_text)