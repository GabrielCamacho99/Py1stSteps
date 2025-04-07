def format_phone (phonenum) :
    area_code = "(" + phonenum [:3] + ")"
    exchange = phonenum [3:6]
    line = phonenum [-4:]
    return area_code + " " + exchange + "-" + line
print (.join(format_phone ("2025551212")) , "USA")