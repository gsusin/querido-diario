import datetime

from gazette.spiders.base.dosp import DospGazetteSpider


class SpGuaracaiSpider(DospGazetteSpider):
    TERRITORY_ID = "3517802"
    name = "sp_guaracai"

    code = 4853
    start_date = datetime.date(2018, 9, 27)
