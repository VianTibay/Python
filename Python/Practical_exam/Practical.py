exclude_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}

text = input("Enter a string statement:\n")

words = ["".join(char for char in word if char.isalpha()) for word in text.split()]


filtered_words = [word for word in words if word.lower() not in exclude_words and word]


word_counts = {}
for word in filtered_words:
    word_counts[word] = word_counts.get(word, 0) + 1

lower_words = sorted([word for word in word_counts if word.islower()], key=str.lower)
upper_words = sorted([word for word in word_counts if word[0].isupper()], key=str.lower)

print("\nFiltered words (sorted):\n")
for word in lower_words + upper_words:
    print(f"{word:<10} - {word_counts[word]}")

print(f"\nTotal words filtered: {sum(word_counts.values())}")
