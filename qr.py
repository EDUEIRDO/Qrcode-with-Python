import qrcode
import os
img = input("Digite o url do site aqui para gerar um qrcode:")
name_format = input("Digite o nome inicial do arquivo:")
img = qrcode.make(img)
type(img)
pasta_save = "qrcode_save"
caminho_completo = os.path.join(pasta_save,f"{name_format}.png")
img.save(caminho_completo)