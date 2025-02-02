import frappe

@frappe.whitelist()
def set_default_company():
    user = frappe.session.user
    company = frappe.db.get_value(
        "User Permission",
        {"user": user, "allow": "Company", "is_default": 1},
        "for_value"
    )

    if company:
        frappe.defaults.set_user_default("Company", company)
        frappe.defaults.set_user_default("company", company)
        return {"company": company}
    else:
        frappe.throw("No default company assigned to your account. Please contact the administrator.")
