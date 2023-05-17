from seo.analyzer import Analyzer, AnalyzerConfiguration

if __name__ == "__main__":
    url = "https://guiahomens.com.br/saude/saude-mental-5-dicas-para-melhorar/"
    analyzer = Analyzer(url=url, configuration=AnalyzerConfiguration())

    print(analyzer.report())
