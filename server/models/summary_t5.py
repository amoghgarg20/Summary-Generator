# Import necessary modules
import transformers
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained('t5-base')

# Define the input text and the summary length

path = 'D:/NLP Project/Summary-Generator/server/models/test_input.txt'
f = open(path,'r',encoding='utf-8')
text = f.read().replace('\n','')
f.close()

inputs = tokenizer.encode(text, return_tensors="pt", max_length = 512, truncation = True)

output = model.generate(inputs, min_length = 40, max_length = 300, length_penalty = 1.0, num_beams = 4, early_stopping = True)

summary_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Summary: ", summary_text)
