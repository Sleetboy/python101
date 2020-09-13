import urllib.request, json, urllib.parse, time

TOKEN = '1397888794:AAFurhhdPRWZMZNE3ElOit26TEbnDSofGJM'

def request(url):
    """지정한 url의 웹 문서를 요청하여, 본문을 반환한다."""
    response = urllib.request.urlopen(url)
    byte_data = response.read()
    text_data = byte_data.decode()
    return text_data

def build_url(method, query):
    """텔레그램 챗봇 웹 API에 요청을 보내기 위한 URL을 만들어 반환한다."""
    return f'https://api.telegram.org/bot{TOKEN}/{method}?{query}'

def request_to_chatbot_api(method, query):
    """메서드(method)와 질의조건(query)을 전달받아 텔레그램 챗봇 웹 API에 요청을 보내고,
        응답 결과를 사전 객체로 해석해 반환한다."""
    url = build_url(method, query)
    response = request(url)
    return json.loads(response)

response = request_to_chatbot_api('getUpdates', 'offset=0')

def simplify_messages(response):
    """텔레그램 챗봇 API의 getUpdate 메서드 요청 결과에서 필요한 정보만 남긴다."""
    result = response['result']
    if not result:
        return None,
    last_update_id = max(item['update_id'] for item in result)
    messages = [item['message'] for item in result]
    simplify_messages = [{'from_id': message['from']['id'],
                            'text': message['text']}
                            for message in messages]
    return last_update_id, simplify_messages

def get_updates(update_id):
    """챗봇 API로 update_id 이후에 수신한 메시지를 조회하여 반환한다."""
    query = f'offset={update_id}'
    response = request_to_chatbot_api(method='getUpdates', query=query)
    return simplify_messages(response)

def send_message(chat_id, text):
    """챗봇 API로 메시지를 chat_id 사용자에게 text 메시지를 발신한다."""
    text = urllib.parse.quote(text)
    query = f'chat_id={chat_id}&text={text}'
    response = request_to_chatbot_api(method='sendMessage', query=query)
    return response

def check_messages_and_response(next_update_id):
    """챗봇으로 메시지를 확인하고, 적절히 응답한다."""
    last_update_id, recieved_messages = get_updates(next_update_id)
    for message in recieved_messages:
        chat_id = message['from_id']
        text = message['text']
        send_text = text + '라고 말씀하셨군요~'
        send_message(chat_id, send_text)
        return last_update_id

if __name__ == "__main__":
    next_update_id = 0
    while True:
        last_update_id = check_messages_and_response(next_update_id)
        if last_update_id


send_message(1289852953, '안녕')

#response = request(build_url('getMe', ''))
#print(json.loads(response))


#response = (build_url('getMe', ''))
#print(request(response))





