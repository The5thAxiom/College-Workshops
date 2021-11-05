import numpy as np
import pandas as pd
from lingualytics.preprocessing import remove_lessthan, remove_punctuation, remove_stopwords
from lingualytics.stopwords import hi_stopwords,en_stopwords
from texthero.preprocessing import remove_digits
from sentence_transformers import SentenceTransformer
import torch

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
cos_fn = torch.nn.CosineSimilarity(dim = 1, eps = 1e-6)

DATASET_PATH = "faq.csv"
df = pd.read_csv(DATASET_PATH, encoding_errors = "ignore")

df["clean_Q"] = df["Q"].pipe(remove_digits)\
    .pipe(remove_punctuation)\
    .pipe(remove_lessthan,length=3)\
    .pipe(remove_stopwords,stopwords = en_stopwords.union(hi_stopwords))

q_embs = model.encode(df["clean_Q"], convert_to_tensor = True)

def pred_answer(user_q, q_embs):
    df_q = pd.DataFrame([user_q], columns = ["user_query"])
    user_q_emb = model.encode(df_q["user_query"], convert_to_tensor=True)
    cos_fn(user_q_emb, q_embs)
    return(df["A"][np.argmax(cos_fn(user_q_emb, q_embs)).item()])

if __name__ == "__main__":
    while True:
        user_query = input("{}\nAsk query: ".format("=" * 10))
        if user_query == "exit":
            print("Thank you")
            break
        else:
            print(pred_answer(user_query, q_embs))