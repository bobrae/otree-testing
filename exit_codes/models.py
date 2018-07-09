from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range, safe_json
)
from .exit_codes import encrypt_and_save_csv, encrypt_and_save_json


author = 'Bodo Brägger'

doc = """
An example app for MTurk exit code generation.
After the creating a session in the app using either the sessions tab or the demo tab
a new file named as 'YEAR-MONTH-DAY_Hour_Minute_Second_SessionCode.csv' will appear
in the project directory
"""
# json_data = ""

class Constants(BaseConstants):
	name_in_url = 'exit_codes'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	def before_session_starts(self):
		# You can change the URL or leave it blank for a simple AccessCode, ExitCode file.
		encrypt_and_save_csv(self.session.participant_set.all(), self.session.code, "")
		# global json_data
		self.session.vars['codes'] = encrypt_and_save_json(self.session.participant_set.all(), self.session.code, "")



	def vars_for_admin_report(self):
		if('codes' not in self.session.vars):
			self.session.vars['codes'] = encrypt_and_save_json(self.session.participant_set.all(), self.session.code, "")
		return {'AccessExit': safe_json(self.session.vars['codes'])}


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	def set_payoff_like_previous_apps(self):
		""" you can call this in 'is_displayed' on a page because it does not alter 
			payoff values and is safe consequently.
		"""
		if self.participant.vars.get('payoff', False):
			self.payoff = self.participant.vars['payoff']
		else:
			print('No payoff saved in participant vars')
