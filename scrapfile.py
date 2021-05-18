

import scrapy

class QuoteSpider(scrapy.Spider):
    name='quotes'
    start_urls =['https://prefeitura.pbh.gov.br/saude/licitacao/pregao-eletronico-151-2020']



def parse(self, response):
    publication_date = response.css('.lbl-licitacao:nth-child(1) font::text').extract()
    object = response.css('.lbl-licitacao:nth-child(4) font::text').extract()
    bidding_date = response.css('.lbl-licitacao:nth-child(19)::text').extract()

    yield {'datetext':publication_date}
    yield {'objecttext':object}
    yield {'biddingdatetext':bidding_date}

    

