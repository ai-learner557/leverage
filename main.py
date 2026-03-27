import requests
from config import API_KEY

API_URL="https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
headers={"Authorization":f"bearer{API_KEY}"}

def summarised_text(text):
    payload={
        "inputs":text,
        "parameters":{
            'min_length':30,
            'max_lenght':100,
            'do_sampel':False

        }
    }

    try:
        response=requests.post(API_URL,headers=headers,json=payload)
        if response.status_code==200:
            return response.json()[0]['summary_text']
        else:
            return f"Error: {response.status_code}-{response.text}"
    except Exception as e:
        return f"Error,Request Failed:{str(e)}"
def main():
    print("---summarise you text---")
    print("Type your text,then press enter to summarise\nType 'quit' to exit")
    
    while True:
        user_input=input(">>Paste or type text here:").strip()
        if user_input.lower()=='quit':
            break
        if not user_input:
            print("Please enter some text")
            continue
        print("Summarising....")
        summary=summarised_text(user_input)

        print(f"\n---SUMMARY---\n{summary}\n")

if __name__=="__main__":
    main()