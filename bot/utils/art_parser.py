import aiohttp
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class JSArtParserAsync:
    def __init__(self, http_client):
        self.url = "https://app.notpx.app/"
        self.js_filename = 'index-DXJ5cfMN.js'
        self.session = http_client
        self.js_content = None

    async def download_html(self):
        try:
            async with self.session.get(self.url) as response:
                response.raise_for_status()
                return await response.text()
        except aiohttp.ClientError as e:
            return None

    def find_js_file(self, html_content):
        pattern = re.compile(r'src=["\'](/assets/index-[A-Za-z0-9]+\.js)["\']')
        match = pattern.search(html_content)
        if match:
            return match.group(1)
        return None

    async def download_js(self, js_url):
        try:
            async with self.session.get(js_url) as response:
                response.raise_for_status()
                self.js_content = await response.text()
        except aiohttp.ClientError as e:
            self.js_content = None

    def parse_image_constants(self, constant_name):
        pattern = rf'{constant_name}\s*=\s*"([^"]+)"'
        match = re.search(pattern, self.js_content)
        if match:
            return urljoin(self.url,  match.group(1))
        else:
            return None

    def calculate_x(self, x):
        pattern = r'(\w+)"\."width"'
        match = re.search(pattern, x)
        if match:
            modified_x = re.sub(pattern, '1000', x)
            operators = re.findall(r'[\+\-\*/]', modified_x)
            numbers = [num.strip('" ') for num in re.split(r'[\+\-\*/]', modified_x)]
            try:
                numbers = [int(num) for num in numbers]
            except ValueError:
                return None
            result = numbers[0]
            for i in range(len(operators)):
                operator = operators[i]
                next_number = numbers[i + 1]
                if operator == '+':
                    result += next_number
                elif operator == '-':
                    result -= next_number
                elif operator == '*':
                    result *= next_number
                elif operator == '/':
                    if next_number != 0:
                        result /= next_number
            return result
        else:
            return None

    def parse_arts_data(self):
        pattern = r"\{[^}]*x\s*:\s*\d+[^}]*y\s*:\s*\d+[^}]*imageSize\s*:\s*\d+[^}]*url\s*:\s*[^,}]+[^}]*type\s*:\s*[^,}]+[^}]*\}"
        matches = re.findall(pattern, self.js_content, re.DOTALL)
        items_list = []

        for match in matches:
            # Регулярні вирази для кожної змінної
            x_pattern = r"x\s*:\s*(\d+)"
            y_pattern = r"y\s*:\s*(\d+)"
            image_size_pattern = r"imageSize\s*:\s*(\d+)"
            url_pattern = r"url\s*:\s*([^,}]+)"
            type_pattern = r"type\s*:\s*([^,}]+)"

            # Витягуємо значення змінних
            x_value = re.search(x_pattern, match).group(1)
            y_value = re.search(y_pattern, match).group(1)
            image_size_value = re.search(image_size_pattern, match).group(1)
            url_value = re.search(url_pattern, match).group(1)
            type_value = re.search(type_pattern, match).group(1)
            item = {"x": int(x_value), "y": int(y_value), "imageSize": int(image_size_value),
                    "url": self.parse_image_constants(url_value), "type": type_value}
            items_list.append(item)
        return items_list

    async def get_all_arts_data(self):
        html_content = await self.download_html()
        if html_content:
            js_url = self.find_js_file(html_content)
            if js_url:
                full_js_url = urljoin(self.url, js_url)
                await self.download_js(full_js_url)
                if self.js_content:
                    results = self.parse_arts_data()
                    return results
