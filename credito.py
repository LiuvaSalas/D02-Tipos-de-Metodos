from solicitud_credito import (
    SolicitudCreditoDeConsumo,
    SolicitudCreditoComercial,
    SolicitudCreditoHipotecario,
)

print("¡Gracias por solicitar un crédito con nuestro Banco!")
tipo = int(
    input(
        "\nIngrese el Tipo de Crédito a solicitar:\n"
        "1. Crédito de consumo\n"
        "2. Crédito Comercial\n"
        "3. Crédito Hipotecario\n"
    )
)
monto = int(input("\nIngrese el monto que desea solicitar:\n"))
correo = input("\nIngrese su correo de contacto:\n")

credito = None
if tipo == 1:
    credito = SolicitudCreditoDeConsumo(monto, correo)
elif tipo == 2:
    credito = SolicitudCreditoComercial(monto, correo)
elif tipo == 3:
    credito = SolicitudCreditoHipotecario(monto, correo)
