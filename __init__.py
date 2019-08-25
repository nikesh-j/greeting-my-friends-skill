from mycroft import MycroftSkill, intent_file_handler


class GreetingMyFriends(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('friends.my.greeting.intent')
    def handle_friends_my_greeting(self, message):
        self.speak_dialog('friends.my.greeting')


def create_skill():
    return GreetingMyFriends()

