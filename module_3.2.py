def send_email(massege, recipient,*,sender = "university.help@gmail.com"):
    domains = ('.com', '.ru', '.net')
    if not (recipient.endswith(domains) and sender.endswith(domains) and ("@" in recipient and "@" in sender)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('123', 'vasyok1337@gmail.com')
send_email('123', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('123', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')
send_email('123', 'urban.fan@mail.ru', sender ='university1.help@gmail.com')
