from extensions import mail
from flask_mail import Message


def send_application_registered_msg(name: str, email: str, track_number: str) -> None:
    msg = Message('Ваша заявка принята к рассмотрению', recipients=[email])
    msg.html = f'<h1>Ваша заявка была принята к рассмотрению!</h1><p>{name}, ожидайте звонка.' \
               f' Также Вы можете отследить статус вашей заявки на нашем сайте.</p>' \
               f'<h2>Ваш трек-код:</h2><h3>{track_number}</h3> '
    mail.send(msg)
