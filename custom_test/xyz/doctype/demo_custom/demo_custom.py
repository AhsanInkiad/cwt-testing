# Copyright (c) 2024, Akib and contributors
# For license information, please see license.txt

import frappe
import pandas as pd
from frappe.model.document import Document

class democustom(Document):
    def on_update(self):
        frappe.msgprint("On Update Triggered")

        # Example: Using Pandas
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [24, 27, 22]
        }
        df = pd.DataFrame(data)
        frappe.msgprint(f"DataFrame:\n{df.to_string(index=False)}")

    def after_insert(self):
        frappe.msgprint("After Insert Triggered")
	

	