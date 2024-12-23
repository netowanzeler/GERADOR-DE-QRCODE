import qrcode

def generate_qrcode(url, output_file):
    # Cria uma instância de QR Code
    qr = qrcode.QRCode(
        version=1,  # Controla o tamanho do QR Code; números maiores resultam em códigos maiores
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erros
        box_size=10,  # Tamanho de cada quadrado na grade do QR Code
        border=4,  # Espessura da borda (mínimo é 4)
    )

    # Adiciona os dados ao QR Code
    qr.add_data(url)
    qr.make(fit=True)

    # Cria uma imagem do QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Salva a imagem em um arquivo
    img.save(output_file)

# Exibe o nome FIREBALL na saída para branding
print("""
00000   0   00000   00000   0000    00000   0       0
0       0   0   0   0       0   0   0   0   0       0
0000    0   00000   000     00000   00000   0       0
0       0   0  0    0       0   0   0   0   0       0
0       0   0   0   00000   0000    0   0   00000   00000
      
                      TECHNOLOGY
""")

# URL a ser codificada
print("DIGITE A SUA URL: ")
url = input("")
# Nome do arquivo de saída
print("DIGITE O NOME DO ARQUIVO")
output_file = input("")+".png"

# Gera e salva o QR Code
generate_qrcode(url, output_file)

print(f"QR code gerado e salvo como {output_file}")