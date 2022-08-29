import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


print("FRESH MEAT!")

try:
    x = int(input("\nEnter the number of messages: "))
    time.sleep(1)
except ValueError:
    print("Incorrect input!")
    x = 1000 # default
print("//The process is running!")

with open('spam.txt', 'r') as file:
    text = file.read() # spam text. make yor own with record.py
  
token = '' # add your token here
group_id = 0 # add ID of your group here

if __name__ == '__main__':
    pudge = vk_api.VkApi(token=token)
    LongPoll = VkBotLongPoll(pudge, group_id=group_id)


for event in LongPoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        peer_id = event.message.peer_id
        from_id = event.message.from_id
        for i in range(x): # limit of messages
            try:
                pudge.method("messages.send", {"peer_id": peer_id, "message": text[:4096],
                                               "random_id": random.randint(0, 100000)})
                print("Сообщений отправлено:", i+1)
            except:
                continue
