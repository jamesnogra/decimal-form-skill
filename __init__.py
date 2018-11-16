import time

from mycroft import MycroftSkill, intent_file_handler


class DecimalForm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('form.decimal.intent')
    def handle_form_decimal(self, message):
        expression_num = message.data.get('expression_num')
        num, den = expression_num.split( '/' )
        answer_number = str(round((float(num)/float(den)), 2))

        #display result instead of mouth
        self.enclosure.mouth_text(answer_number)
        self.enclosure.deactivate_mouth_events()

        self.speak_dialog('form.decimal', data={
            'expression_num': expression_num.replace('/', ' over '),
            'answer_number': answer_number
        })

        #reset mouth events after 5 seconds
        time.sleep(5)
        self.enclosure.activate_mouth_events()
        self.enclosure.mouth_reset()


def create_skill():
    return DecimalForm()

