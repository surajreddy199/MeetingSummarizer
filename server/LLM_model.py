import google.generativeai as genai

def model_summarizer(prompt):
    genai.configure(api_key="AIzaSyBxKB_RrpTne5BwzQx0hMgi4ytVE_ZPt0M")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text