from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

# Import this function to get the exit code for a single player
from .exit_codes import aes_encrypt

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    def vars_for_template(self):
        return {'exit_code' : aes_encrypt(self.participant.code.encode())}


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
