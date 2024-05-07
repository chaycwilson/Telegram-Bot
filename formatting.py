import spacy

nlp = spacy.load("en_core_web_sm")

def extract_food_item(text):
    doc = nlp(text)
    nouns = list(doc.noun_chunks)
    quantity = None
    unit = None

    for token in doc:
        if token.pos_ == 'NUM':
            quantity = token.text
            if token.i + 1 < len(doc):
                next_token = doc[token.i + 1]
                if next_token.pos_ in ['NOUN', 'PROPN']:  
                    unit = next_token.text

    # The food item is likely the last noun chunk
    if nouns:
        food = nouns[-1].text
    else:
        food = None

    return food, quantity, unit

# Example usage
question = "How many calories are in 200 grams of steak?"
food, quantity, unit = extract_food_item(question)
print(f"Food: {food}, Quantity: {quantity}, Unit: {unit}")
