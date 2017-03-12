def vyhodnot(pole):

    if "xxx" in pole:
        return "x"
         # vyhral hrac s x - pc
    elif "ooo" in pole:
        return "o"
         #vyhrali kolecka - hrac
    elif "-" not in pole:
        return "!" #remiza
    else:
        return "-"    # nic z toho
