from django.core.mail import send_mail

send_mail(
    'Subject here',         # 제목
    'Here is the message.', # 내용
    '',     # 보내는 이메일  (settings에 설정해서 작성안해도 됨)
    ['2044smile@naver.com'],     # 받는 이메일 리스트
    fail_silently=False,
)

print('성공?실패?')