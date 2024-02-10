from transformers import T5ForConditionalGeneration, T5Tokenizer


def split_text(text):
    max_chunk_size = 512
    chunks = []
    current_chunk = ""
    for sentence in text.split("."):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def generate_summary(text):
    input_chunks = split_text(text)
    output_chunks = []
    for chunk in input_chunks:
        inputs = tokenizer.encode(chunk, return_tensors="pt", max_length = 512, truncation = True)
        response = model.generate(inputs, min_length = 40, max_length = 100)
        summary = tokenizer.decode(response[0], skip_special_tokens=True)
        output_chunks.append(summary)
    return " ".join(output_chunks)


# Load the T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained('t5-base')

# Define the input text and the summary length
path = 'D:/NLP Project/Summary-Generator/server/models/test_input.txt'
f = open(path,'r',encoding='utf-8')
text = f.read().replace('\n','')
f.close()

summary_text = generate_summary(text)

print("Summary: ", summary_text)
