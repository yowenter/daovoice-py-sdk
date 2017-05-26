DaoVoice Python Sdk
====================================


Installation
------------------

::

    pip install daovoice-sdk




Basic Usage
-----------------------

.. code:: python

    from daovoice.client import Client

    daovoice_client = Client(token="Your Token Here")



Note that you can find your token  in `http://dashboard.daovoice.io/app/{app_id}/apps/settings/open-api`




Resources
~~~~~~~~~~~~~~~~~~

Resources this API supports:

    https://api.daovoice.io/v1/conversations  

    https://api.daovoice.io/v1/admins

    https://api.daovoice.io/v1/users

    




Examples
~~~~~~~~~~~~~~~~~

Conversations
^^^^^^^^^^^^^

.. code:: python

    # Get Conversation by id
    conversation = daovoice_client.conversations.get(id="conversation_id")
    print conversation.conversation_parts
    print conversation.conversation_message

    # Reply

    daovoice_client.conversations.reply(id="conversation_id",admin_id="***",body="reply msg")



Admins
^^^^^^

.. code:: python

    # list admins
    admins = daovoice_client.admins.all()
    for ad in admins:
        print ad.name

User
^^^^^^

.. code:: python

    # create user
    user = daovoice_client.user.create(user_id="123456",name="example", email="example@daovoice.io")






