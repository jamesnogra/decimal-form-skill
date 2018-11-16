from mycroft import MycroftSkill, intent_file_handler


class DecimalForm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('form.decimal.intent')
    def handle_form_decimal(self, message):
        first_number = message.data.get('first_number')
        second_number = message.data.get('second_number')
        answer_number = ''

        self.speak_dialog('form.decimal', data={
            'second_number': second_number,
            'answer_number': answer_number,
            'first_number': first_number
        })


def create_skill():
    return DecimalForm()

