# Gera index.html (documento completo para a Vercel) a partir de arqora-home.html (fonte do artifact).
# Rode depois de cada alteração: python build-index.py
s = open("arqora-home.html", encoding="utf-8").read()
s = s.replace('<meta charset="utf-8">\n', "")
s = s.replace("<title>Àrqora Home</title>", "<title>Àrqora Imóveis | Imóveis de Alto Padrão</title>")
head_end = s.index("</style>") + len("</style>")

doc = (
    '<!doctype html>\n<html lang="pt-BR">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="description" content="Àrqora seleciona imóveis de alto padrão com valor real em localização, arquitetura, exclusividade e potencial patrimonial.">\n'
    '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
    + s[:head_end]
    + "\n</head>\n<body>\n"
    + s[head_end:]
    + "\n</body>\n</html>\n"
)
open("index.html", "w", encoding="utf-8", newline="\n").write(doc)
