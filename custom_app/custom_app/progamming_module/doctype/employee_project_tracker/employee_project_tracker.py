import frappe
from frappe.utils import now_datetime, add_days
from datetime import datetime, timedelta

def send_project_summary_email():
    # Query completed projects from the Employee Project Tracker DocType
    completed_projects = frappe.get_list("Employee Project Tracker",
                                         fields=["name", "Project Name", "Start Date", "End Date"],
                                         filters={"Status": "Completed"})

    if completed_projects:
        # Prepare email content
        email_content = "<h2>Completed Projects Summary:</h2>"
        email_content += "<table border='1'><tr><th>Project Name</th><th>Start Date</th><th>End Date</th></tr>"
        for project in completed_projects:
            email_content += f"<tr><td>{project['Project Name']}</td><td>{project['Start Date']}</td><td>{project['End Date']}</td></tr>"
        email_content += "</table>"

        # Send email
        frappe.sendmail(
            recipients=["recipient@example.com"],
            subject="Weekly Completed Projects Summary",
            content=email_content
        )
    else:
        print("No completed projects found for this week.")

# Run the function to send the summary email
send_project_summary_email()
