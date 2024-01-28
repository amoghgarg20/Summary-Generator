from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch


model_name = 'google/pegasus-xsum'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

path = 'D:/NLP Project/Summary-Generator/server/models/test_input.txt'
f = open(path,'r',encoding='utf-8')
src_text = f.read().replace('\n','')
f.close()


batch = tokenizer.prepare_seq2seq_batch(src_text, truncation=True,return_tensors='pt')
translated = model.generate(**batch, min_length = 40, max_length = 1000)
tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

print(tgt_text)

