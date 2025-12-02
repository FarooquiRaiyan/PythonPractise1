import pandas as pd
import google.generativeai as genai
import os


genai.configure(api_key="YOUR_API_KEY")



models = genai.list_models()

df = pd.read_excel('Book1.xlsx')

# print(df.head())
# print(df.columns)


def df_to_text(df):
    txt=""
    for idx, row in df.iterrows():
        # print("idx =", idx, " row=",row, '\n')
        # print()
        row_text = ", ".join([f"{col}:{row[col]}" for col in df.columns])
        # print("rowtext=", row_text)
        txt +=  f"Row{idx+1}:{row_text}\n"
    return txt
        
excel_knowldege = df_to_text(df)
print("excel knwoledge " ,excel_knowldege)


def ask_excel(question):
    prompt = f"""
    You are a data expert. Answer the question only using this Excel data:
    {excel_knowldege}
    
    Question : {question}
    """ 
    model = genai.GenerativeModel("models/gemini-flash-latest")

    response = model.generate_content(prompt)
    return response.text



# user_question = "What is the total of the Amount column?"
# answer = ask_excel(user_question)
user_inp = input("enter the question")
answer = ask_excel(user_inp)

print("\nAnswer:", answer)