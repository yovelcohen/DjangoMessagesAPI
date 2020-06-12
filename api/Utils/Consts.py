class MessageFields:
    SENDER = 'sender'
    SUBJECT = 'subject'
    CONTENT = 'content'
    SENT_TO = 'sent_to'
    MARK_READ = 'mark_read'
    DATE = 'sent_at'
    ID = 'id'


class UserFields:
    URL = 'url'
    PASSWORD = 'password'
    EMAIL = 'email'
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    USER_NAME = 'username'
    IS_STAFF = 'is_staff'
    IS_SUPERUSER = 'is_superuser'


class SerializerFields:
    READ_ONLY = 'read only'
    WRITE_ONLY = 'write_only'
    ALLOW_NULL = 'allow_null'
    REQUIRED = 'required'
