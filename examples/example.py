import os
from daovoice.client import Client

# init client 

client = Client(token=os.getenv('TOKEN', ''))

# get conversation

conversation = client.conversations.get(id="11678500-4f3f-4ca3-a322-c5ced27d77f3")

print conversation.conversation_parts
print conversation.conversation_message

# list admins

admins = client.admins.all()

print admins
for ad in admins:
    print ad.name

subscriptions = client.subscriptions.all()

for sub in subscriptions:
    print sub.subscription_id

# reply conversation 
client.conversations.reply(id="11678500-4f3f-4ca3-a322-c5ced27d77f3", admin_id=admins[0].admin_id, body="hello")

# create user 
print client.user.create(user_id="test_134", name="example", email="example@daovoice.io")
