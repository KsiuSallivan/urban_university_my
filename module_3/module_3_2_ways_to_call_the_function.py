list_of_ends = ['.com', '.ru', '.net']


def valid_domain(email):
    valid = False
    for i in list_of_ends:
        if email.endswith(i):
            valid = True
    return valid


def valid_at(email):
    if '@' in email:
        return True
    else:
        return False


default_sender = 'university.help@gmail.com'


def send_email(message, recipient, sender = default_sender):
    if not valid_domain(recipient) or not valid_domain(sender) or not valid_at(recipient) or not valid_at(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return

    if recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
        return

    if sender == default_sender:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


