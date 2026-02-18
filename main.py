user_input = input()

char_to_count = user_input[0]
phrase = user_input[2:]  # Skip the character and the space

count = phrase.count(char_to_count)

if count == 1:
    print(f"{count} {char_to_count}")
else:
    print(f"{count} {char_to_count}'s")
