from fastapi import FastAPI, Form, Cookie, Body

app = FastAPI()


@app.post("/unify_phone_from_json")
def index_page(phone=Body(...)):
    """Преобразование номера телефона к стандартизированному виду"""
    digits = []
    phone = phone.get("phone")
    if phone:
        for char in phone:
            if char.isdecimal():
                digits.append(char)
        if len(digits) == 10 and digits[0] == '9':
            digits.insert(0, '8')
        if len(digits) == 11:
            if digits[0] == '7':
                digits[0] = '8'
            result = f'{digits[0]} ({"".join(digits[1:4])}) {"".join(digits[4:7])}-{digits[7]}{digits[8]}-{digits[9]}{digits[10]}'
        else:
            result = ''.join(digits)
        return Response(result, media_type='text/html')
