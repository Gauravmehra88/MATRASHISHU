import google.generativeai as genai

genai.configure(api_key="AIzaSyBue5KqNeZoqOD9L8r2d0oQPEtSd3qYGM8")

# Use a valid model name
model = genai.GenerativeModel("gemini-1.5-pro-latest")

response = model.generate_content("Hello, how can I help you?")
print(response.text)

