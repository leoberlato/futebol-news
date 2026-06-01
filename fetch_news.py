import urllib.request
import json
import os
from datetime import datetime

API_KEY = os.environ.get("GNEWS_API_KEY", "")

CATEGORIAS = [
    {"id": "brasileirao", "query": "Brasileirao 2026", "label": "Brasileirão"},
    {"id": "champions",   "query": "Champions League 2026", "label": "Champions"},
    {"id": "selecao",     "query": "Selecao Brasileira futebol", "label": "Seleção"},
    {"id": "copa",        "query": "Copa do Mundo 2026", "label": "Copa do Mundo"},
    {"id": "geral",       "query": "futebol", "label": "Geral"},
]

def buscar(query, max_resultados=6):
    url = (
        f"https://gnews.io/api/v4/search"
        f"?q={urllib.parse.quote(query)}"
        f"&lang=pt&country=br"
        f"&max={max_resultados}"
        f"&token={API_KEY}"
    )
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            data = json.loads(r.read())
            return data.get("articles", [])
    except Exception as e:
        print(f"Erro ao buscar '{query}': {e}")
        return []

import urllib.parse

todas = {}
for cat in CATEGORIAS:
    print(f"Buscando: {cat['label']}...")
    artigos = buscar(cat["query"])
    todas[cat["id"]] = {
        "label": cat["label"],
        "artigos": [
            {
                "titulo":    a.get("title", ""),
                "descricao": a.get("description", ""),
                "url":       a.get("url", ""),
                "fonte":     a.get("source", {}).get("name", ""),
                "imagem":    a.get("image", ""),
                "publicado": a.get("publishedAt", ""),
            }
            for a in artigos
        ]
    }

resultado = {
    "atualizado_em": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "categorias": todas
}

with open("noticias.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=2)

print(f"noticias.json gerado com sucesso — {datetime.now().strftime('%d/%m/%Y %H:%M')}")
