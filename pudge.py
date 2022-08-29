import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


print("СВЕЖЕЕ МЯСО!!!!")

with open('spam.txt', 'r') as file:
    text = file.read()
token = '969df25fdd94c38a8bd95bf5d7dbf81c48110ac9c2a4a03ec4fcdf92a8ddd0cc956c355fb6c7b0e2d7f04'
group_id = 213450595

if __name__ == '__main__':
    pudge = vk_api.VkApi(token=token)
    LongPoll = VkBotLongPoll(pudge, group_id=group_id)


for event in LongPoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        peer_id = event.message.peer_id
        from_id = event.message.from_id
        for i in range(1000):
            try:
                pudge.method("messages.send", {"peer_id": peer_id, "message": text[:4096],
                                               "random_id": random.randint(0, 100000)})
                print("Сообщений отправлено:", i+1)
            except:
                continue