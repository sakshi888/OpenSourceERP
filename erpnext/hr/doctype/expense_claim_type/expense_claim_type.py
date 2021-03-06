# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class ExpenseClaimType(Document):
	def validate(self):
		self.validate_accounts()
		self.validate_repeating_companies()

	def validate_repeating_companies(self):
		"""Error when Same Company is entered multiple times in accounts"""
		accounts_list = []
		for entry in self.accounts:
			accounts_list.append(entry.company)

		if len(accounts_list)!= len(set(accounts_list)):
			frappe.throw(_("Same Company is entered more than once"))
