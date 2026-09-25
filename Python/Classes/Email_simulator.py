emails = []

while True:
    print("\n===== Email Simulator =====")
    print("1. Send Email")
    print("2. View Inbox")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sender = input("From: ")
        receiver = input("To: ")
        subject = input("Subject: ")
        message = input("Message: ")

        email = {
            "From": sender,
            "To": receiver,
            "Subject": subject,
            "Message": message
        }

        emails.append(email)
        print("Email Sent!")

    elif choice == "2":
        print("\n===== Inbox =====")

        if not emails:
            print("No emails found.")

        for email in emails:
            print("-" * 30)
            print("From:", email["From"])
            print("To:", email["To"])
            print("Subject:", email["Subject"])
            print("Message:", email["Message"])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")