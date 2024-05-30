from kavenegar import *


def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('75335459556E5265314678567A3638564656664F4C7977504165377A3761614D5A644855446F72465259673D')
        params = {
        'sender': '',
        'receptor': phone_number,
        'message': f'{code}ببین داداش گلم این کد ثبت نام شماست.تا ۱۲۰ ثانیه دیگه استفاده کردی کردی نکردی دیگه ببین نمیدونم ندیدمو حواسم نبود اینا نداریم پیامک مجدد نداریم وسلام علیکم ',
    } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)
    pass