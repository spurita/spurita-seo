from seo.url import Url

if __name__ == "__main__":
    url = Url("https://guiahomens.com.br/saude/saude-mental-5-dicas-para-melhorar/")

    print(f"is_valid: {url.is_valid()}")
    print(f"is_https: {url.is_https()}")
    print(f"is_www: {url.is_www()}")
