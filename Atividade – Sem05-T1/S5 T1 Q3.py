def segs_p_HHMMSS(segs):
    hh = (segs//60)//60
    mm = (segs//60)%60
    ss = ((segs%60)%60)%60
    if hh < 10: hh = '0' + str(hh)
    if mm < 10: mm = '0' + str(mm)
    if ss < 10: ss = '0' + str(ss)
    print(f'{hh}:{mm}:{ss}')

segundos = int(input().strip())
segs_p_HHMMSS(segundos)
