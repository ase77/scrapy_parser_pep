import datetime as dt
from pathlib import Path

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / 'results'


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = {}

    def process_item(self, item, spider):
        if item['status'] not in self.results:
            self.results[item['status']] = 1
        else:
            self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_format = now.strftime(DATETIME_FORMAT)
        filename = f'status_summary_{now_format}.csv'
        file_path = RESULTS_DIR / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            total = 0
            for key, value in self.results.items():
                total += value
                f.write(f'{key},{value}\n')
            f.write(f'Total,{total}\n')
