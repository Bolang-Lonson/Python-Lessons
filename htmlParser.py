from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    header_count = {
        'h1': 0,
        'h2': 0,
        'h3': 0,
        'h4': 0,
        'h5': 0,
        'h6': 0,
    }
    anchor_count = 0
    anchor_attr = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # tallying the header count with all 6 header types
        if tag in self.header_count.keys():
            self.header_count[tag] += 1

        # digging into anchor tag attributes to get hrefs
        if tag == 'a':
            self.anchor_count += 1
            for attr in attrs:
                # isolating href attributes
                if attr[0] == 'href':
                    href = attr[1]
                    self.anchor_attr[f'href{self.anchor_count}'] = href



parser = MyHtmlParser()

# html_content = '''
#     <h1>This is a heading</h1>
#     <p>This is a paragraph with some <em>emphasized</em> text.</p>
# '''

# parser.feed(html_content)
doc = open('index.html', 'rt')
html_content = doc.read()  #   reading from html file
doc.close()

parser.feed(html_content)
parser.close()
print(parser.header_count, '\n', parser.anchor_attr,)