style_buttons_left = str(
    "border-left: 2px solid rgb(0, 171, 179);\n"
    "border-bottom: 2px solid rgb(0, 171, 179);\n"
    "border-top: 2px solid rgb(0, 171, 179);\n"
    "background-color:rgb(30,35,40);\n"
    "border-top-left-radius:15px;\n"
    "border-bottom-left-radius:15px;"
)

dict_combo_items = {
    "tipocontrato": ["Obra", "Fijo", "Indefinido", "Trato"],
    "factura": ["Crédito", "Debito", "Nota de Credito"],
    "afps": ["Capital", "Cuprum", "Habitat", "PlanVital", "ProVida", "Modelo", "Uno"],
    "prevision": [
        "Banmédica",
        "Consalud",
        "Colmena",
        "CruzBlanca",
        "Nueva Masvida",
        "Vida tres",
        "Fonasa",
    ],
    "banco": [
        "Banco de Chile",
        "Scotiabank ",
        "Banco Internacional",
        "BCI",
        "Corpbanca",
        "BICE ",
        "HSBC Bank",
        "Santander",
        "Itaú",
        "The Royal Bank of Scotland ",
        "Security",
        "Falabella",
        "Deutsche Bank",
        "Rabobank",
        "Ripley",
        "Consorcio",
        "Penta",
        "Paris",
    ],
    "tipocuenta": [
        "Vista",
        "Ahorro",
        "Corriente",
        "Valores",
        "Chequera electrónica",
        "Cuenta rut",
    ],
}
# COMBOBOX'S ITEMS

dict_table_widget = {
    "asignacion": ["TRAMO", "MONTO", "REQUISITO_RENTA"],
    "cesantia": [
        "TIPO_CONTRATO",
        "FINANCIAMIENTO_EMPLEADOR",
        "FINANCIAMIENTO_TRABAJADOR",
    ],
    "afp": ["AFP", "TASA_INDEPENDIENTE", "TASA_DEPENDIENTE", "SIS"],
    "proyecto": [
        "ID",
        "NOMBRE_PROYECTO",
        "MANDANTE",
        "RUT_MANDANTE",
        "NOMBRE_CONTACTO",
        "FONO_CONTACTO",
        "CODIGO_OC",
        "NETO",
        "IVA",
        "TOTAL_OC",
    ],
    "trabajador": [
        "ID",
        "APELLIDOS",
        "NOMBRES",
        "FECHA_NACIMIENTO",
        "EDAD",
        "RUT",
        "TIPO_CONTRATO",
        "CARGO",
        "SUELDO_BASE",
        "COLACION",
        "MOVILIZACION",
        "ASIGNACION_FAMILIAR",
        "AFP",
        "PREVISION_SALUD",
        "FECHA_CONTRATO",
        "FECHA_DESVINCULO",
        "BANCO",
        "TIPO_CUENTA",
        "NUMERO_CUENTA",
        "CORREO",
    ],
    "factura": [
        "ID",
        "FOLIO",
        "TIPO_FACTURA",
        "ID_PROYECTO",
        "RUT",
        "MONTO_NETO",
        "MONTO_IVA",
        "MONTO_TOTAL",
    ],
}

# List of every lineedit in rightwidget
