import scrapy

class ShipbuildingSpider(scrapy.Spider):
    name = "shipbuilding"
    allowed_domains = ["worldmetrics.org"]
    start_urls = ["https://worldmetrics.org/supply-chain-in-the-shipbuilding-industry-statistics"]

    def parse(self, response):
        # Ubica la sección "Key Findings" y extrae los <li>
        findings = response.xpath('//h2[contains(text(),"Key Findings")]/following-sibling::ul[1]/li//text()').getall()
        for f in findings:
            text = f.strip()
            if text:
                yield {"key_finding": text}

         # Paginación: seguir enlace "Next"
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
