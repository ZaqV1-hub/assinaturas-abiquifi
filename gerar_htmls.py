from pathlib import Path

PASTA_JPGS = "assinaturas-bio-2026-jpgs"
PASTA_HTMLS = "assinaturas-bio-2026-htmls"
USUARIO = "ZaqV1-hub"
REPO = "assinaturas-abiquifi"
BRANCH = "main"

pasta_jpgs = Path(PASTA_JPGS)
pasta_htmls = Path(PASTA_HTMLS)

pasta_htmls.mkdir(exist_ok=True)

arquivos = list(pasta_jpgs.glob("*.jpg")) + list(pasta_jpgs.glob("*.jpeg"))

for arquivo in arquivos:
    nome_arquivo = arquivo.name
    nome_base = arquivo.stem

    html = f'''<table cellpadding="0" cellspacing="0">
  <tr>
    <td>
      <img
        src="https://raw.githubusercontent.com/{USUARIO}/{REPO}/{BRANCH}/{PASTA_JPGS}/{nome_arquivo}"
        alt="{nome_base}"
        style="display:block; max-width:100%;"
      />
    </td>
  </tr>
</table>
'''

    saida = pasta_htmls / f"{nome_base}.html"
    saida.write_text(html, encoding="utf-8")

print("HTMLs gerados com sucesso.")