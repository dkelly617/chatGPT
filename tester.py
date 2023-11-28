
import openai

client = openai.api_key = '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'  # this is also the default, it can be omitted

messages = [ {"role": "system", "content": "You are a intelligent assistant."} ] 

while True: 
	message = input("User : ") 
	if message: 
		messages.append({"role": "user", "content": message}) 
		chat = openai.ChatCompletion.create( 
			model="gpt-3.5-turbo", messages=messages 
		) 
	reply = chat.choices[0].message.content 
	print("ChatGPT: {reply}") 
	messages.append({"role": "assistant", "content": reply}) 