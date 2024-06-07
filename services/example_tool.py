import pronouncing


#Task: Make this method a tool
def find_rhymes(word) -> str:
    rhymes = pronouncing.rhymes(word)
    if rhymes:
        return f"Words that rhyme with {word}: {', '.join(rhymes[:5])}"
    else:
        return f"No rhymes found for {word}."
