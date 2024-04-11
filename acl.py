aclNum = int(input(" Cual es el numero de la ACL?: "))
if aclNum >= 1 and aclNum <= 99:
    print("ESTA ES UNA ACL ESTANDAR.")
elif aclNum >=100 and aclNum <= 199:
    print("ESTA ES UNA ACL EXTENDIDA.")
else:
    print("Esta ACL IPv4 no es extendida o estandar.")
