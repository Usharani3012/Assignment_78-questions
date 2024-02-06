u=int(input('units:'))
if u<=50:
    c=u*0.50
    e=c*0.2
    print(c+e)
elif u<=100:
    # 50*0.5=25
    c=25+(u-50)*0.75
    e=c*0.2
    print(c+e)
elif u>100:
    if u<=250:
    # 50*0.5+150*0.75
     c=100+(u-100)*1.20
    e=c*0.2
    print(c+e)
elif u>250:
    # 50*0.5+
    c=200+(u-250)*1.50
    e=c*0.2
    print(c+e)