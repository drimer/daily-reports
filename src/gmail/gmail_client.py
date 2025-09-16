import datetime
import imaplib


def infer_bin_directory_name(mail: imaplib.IMAP4_SSL) -> str:
    _, *directory_tags = mail.list()[1]

    known_bin_names = ("[Gmail]/Trash", "[Gmail]/Bin")

    for tag in directory_tags:
        for known_bin_name in known_bin_names:
            if known_bin_name in tag.decode():
                return known_bin_name

    return None


def delete_old_emails(older_than_days, email, password):
    print(f"Deleting emails older than {older_than_days} days...")

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email, password)

    bin_directory = infer_bin_directory_name(mail)
    if bin_directory:
        print(f"Inferred bin directory: {bin_directory}")
    else:
        raise Exception("Could not infer bin directory name.")

    mail.select('"[Gmail]/All Mail"')
    before_date = datetime.datetime.now() - datetime.timedelta(
        days=int(older_than_days)
    )
    _, data = mail.uid("search", f'BEFORE "{before_date.strftime("%d-%b-%Y")}"')

    if data[0]:
        for uid in data[0].split():
            subject = (
                mail.uid("fetch", uid, "(BODY[HEADER.FIELDS (SUBJECT)])")[1][0][1]
                .decode()
                .strip()
            )
            date_time = (
                mail.uid("fetch", uid, "(BODY[HEADER.FIELDS (DATE)])")[1][0][1]
                .decode()
                .strip()
            )

            print(f"Deleting email with date: {date_time} subject: {subject}")
            mail.uid("move", uid, bin_directory)

    mail.close()
    mail.logout()
