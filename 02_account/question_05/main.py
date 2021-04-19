from person import Pessoa
from photography import Fotografia

image = "https://welitonsousa.vercel.app/static/media/weliton-profile.b688a162.jpg"
fotografo = Pessoa("Anne Geddes", "123.123.123-12", "Casa dela", "(89) 9 8888-8888")
proprietario = Pessoa("Weliton Sousa", "312.312.312-32", "Casa dela", "(89) 9 9999-9999")

foto = Fotografia(image, fotografo, proprietario)

foto.mostrar_fotografia()
print(foto.propriedade_fotografia())