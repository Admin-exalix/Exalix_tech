import frappe

@frappe.whitelist(allow_guest=True)
def submit_lead(lead_name, email_id=None, company_name=None, description=None, phone=None):
    """
    Create a Lead in ERPNext from guest submission
    """
    try:
        lead = frappe.get_doc({
            "doctype": "Lead",
            "lead_name": lead_name,
            "email_id": email_id,
            "company_name": company_name,
            "description": description,
            "phone": phone  # <-- added
        })
        lead.insert(ignore_permissions=True)
        frappe.db.commit()
        return {"status": "success", "message": "Lead created successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# custom_app/custom_app/api.py
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def login(usr, pwd):
    """Custom login for AJAX"""
    from frappe.auth import LoginManager
    try:
        lm = LoginManager()
        lm.authenticate(user=usr, pwd=pwd)
        lm.login()
        frappe.db.commit()
        return {"message": "Logged in"}
    except frappe.AuthenticationError:
        frappe.throw(_("Invalid login credentials"))
