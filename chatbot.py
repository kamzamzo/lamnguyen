import requests

def generate_response(user_input):
    # Gửi câu hỏi từ người dùng đến chatbot AI
    response = requests.post('http://api.ai.com/chat', data={'question': user_input})

    # Lấy câu trả lời từ chatbot AI
    answer = response.json()['answer']
    
    return answer
