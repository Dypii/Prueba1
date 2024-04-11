def determinar_switch_y_native_vlan(vlan):
    if vlan in [10, 20, 30]:
        return "SW1", 99
    elif vlan in [40, 50, 60]:
        return "SW2", 200
    else:
        return "No se pudo determinar el switch y la VLAN nativa para la VLAN ingresada."

def main():
    vlan_ingresada = int(input("Ingrese el número de VLAN: "))
    switch, native_vlan = determinar_switch_y_native_vlan(vlan_ingresada)
    print(f"La VLAN {vlan_ingresada} corresponde a {switch} y la VLAN nativa es {native_vlan}.")

if __name__ == "__main__":
    main()

