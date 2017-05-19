from daovoice.client import Client

client = Client(base_url="http://api.daovoice.co/v1/",
                token="EF802AE9611FD09B0F8B3BBFA13703A6061E20A9D5D68A36689845108D7D71C3")

conversation = client.conversations.get(id="0204274f-0e61-4c15-a794-9e950aca0eb0")

print conversation.conversation_parts
print conversation.conversation_message
