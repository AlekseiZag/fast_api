def unify_phone(phone: str = None):
    """Преобразование номера телефона к стандартизированному виду"""
    digits = []
    if phone:
        for char in phone:
            if char.isdecimal():
                digits.append(char)
        if len(digits) == 10 and digits[0] == '9':
            digits.insert(0, '8')
        if len(digits) == 11:
            if digits[0] == '7':
                digits[0] = '8'
            return f'{digits[0]} ({"".join(digits[1:4])}) {"".join(digits[4:7])}-{digits[7]}{digits[8]}-{digits[9]}{digits[10]}'
        return ''.join(digits)
