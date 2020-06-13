class DocsDescriptions:
    RETRIEVE_MSG_URL = "Get api/messages/{pk}/"
    RETRIEVE_MSG = "Get a message by it's id and change mark read to true."
    DELETE_MSG = "Delete a message by it's id"
    UPDATE_MSG = "Update a message instance (PUT)"
    LIST_MESSAGES = "Get all messages of the messages associated with the user. "
    RETRIEVE_USER = "Get a user's data."
    LIST_USERS = "Get all of the users in the system"
    NEWEST_MSG_DESCRIPTION = "Get/Delete/Update the latest message received by the user."
    LAST_50_MESSAGES_DESCRIPTION = "Get the last 50 messages received by the user."
    UNREAD_MESSAGES_DESCRIPTION = "Get all the unread messages by the user."
    LAST_50_MESSAGES = "GET api/messages/1/last_50_messages"
    SENT_MESSAGES = "GET api/messages/1/sent_messages"
    NEWEST_MSG = "GET/DELETE/PUT/PATCH api/messages/newest_msg"
    UNREAD_MESSAGES = "GET api/messages/1/unread_messages"
    SENT_MESSAGES_DESCRIPTION = "Get all the messages sent by the user"


class METHODS:
    DESTROY = 'destroy'
    LIST = 'list'
    UPDATE = 'update'
    PUT = 'put'
    DELETE = 'delete'
    GET = 'get'
    PATCH = 'patch'
