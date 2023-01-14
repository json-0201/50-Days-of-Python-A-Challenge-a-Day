# Save Emails

def save_emails():
    """Saves emails in csv format per user input."""
    import csv
    
    emails = []
    print("Enter \"done\" to exit.")
    while True:
        email = input("Enter email: ")
        if email.lower() == "done":
            break
        emails.append(email)
    with open("./emails.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        for email in emails:
            writer.writerow([email])
    return

save_emails()
