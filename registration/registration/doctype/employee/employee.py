# -*- coding: utf-8 -*-
# Copyright (c) 2021, prakash and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

import re
from frappe import _
from frappe.utils import validate_email_add
from frappe.model.document import Document


class Employee(Document):
	def validate(self):
		validate_email_add(self.email,True)

	def on_submit(self):
		print('on sumbit is called')

