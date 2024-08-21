# Initial service tickets stored in a nested dictionary
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to open a new service ticket
def open_ticket(ticket_id, customer, issue):
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}

# Function to update the status of an existing ticket
def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
    else:
        print(f"Ticket ID {ticket_id} not found.")

# Function to display all tickets or filter by status
def display_tickets(status=None):
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"Ticket ID: {ticket_id}")
            for key, value in details.items():
                print(f"  {key}: {value}")
            print()

# Sample usage:
# Open a new ticket
open_ticket("Ticket003", "Charlie", "Account locked")

# Update the status of an existing ticket
update_ticket_status("Ticket001", "closed")

# Display all tickets
print("All Tickets:")
display_tickets()

# Display only open tickets
print("Open Tickets:")
display_tickets(status="open")
