import frappe

@frappe.whitelist(allow_guest=False)
def demoApi():
    user = frappe.get_doc('User', frappe.session.user)
    frappe.response["message"] = {
        "message"   : user.name,
        "User type" : user.user_type
    }

