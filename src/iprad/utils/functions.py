def get_flag(country_code: str):
    #Get glag from country code
    if not country_code or len(country_code) != 2:
        return ""
    
    return "".join(chr(127397 + ord(c)) for c in country_code.upper())