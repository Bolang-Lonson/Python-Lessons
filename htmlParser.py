from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    isTitle: bool = False
    header_count: dict[str: int] = {
        'h1': 0,
        'h2': 0,
        'h3': 0,
        'h4': 0,
        'h5': 0,
        'h6': 0,
    }
    anchor_count: int = 0
    anchor_hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # tallying the header count with all 6 header types
        if tag in self.header_count.keys():
            self.header_count[tag] += 1

        # digging into anchor tag attributes to get hrefs
        if tag == 'a':
            self.anchor_count += 1
            for attr in attrs:  #   tuple
                # isolating href attributes
                if attr[0] == 'href':
                    href = attr[1]
                    self.anchor_hrefs.append(href)

        # intercepting the title
        if tag == 'title':
            self.isTitle = True

        # Reading self-closing input tags
        if tag == 'input':
            # getting the type (eg. 'text', 'email', 'password')
            for attr in attrs:
                if attr[0] == 'type':
                    input_type = attr[1] 
                    self.has_pass_field = True if input_type == 'password' else False
                    self.has_submit = True if input_type == 'submit' else False
                    self.has_btn = True if input_type == 'button' else False

                # If we have a submit input we can read the value attribute for human language hints
                if attr[0] == 'value' and (self.has_submit or self.has_btn):
                    # using common human language button text for login buttons
                    self.has_login_button = True if attr[1].lower() in ['login', 'log-in', 'log in', 'signin', 'sign-in', 'sign in'] else False
                else:
                    self.has_login_button = False

        # getting the form's method
        if tag == 'form':
            for attr in attrs:
                self.has_post_form = True if (attr[0] == 'method' and attr[1].lower() == 'post') else False


    def handle_data(self, data: str) -> None:
        if self.isTitle:
            self.Title = data.strip()


    def handle_endtag(self, tag: str) -> None:
        # setting it to false to stop reading the title data after reading title closing tag
        if tag == 'title':
            self.isTitle = False



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
print(parser.header_count)
print(f'Title: {parser.Title}')
# Seperating the links into internal and external links
external = [url for url in parser.anchor_hrefs if url.startswith('http')]
internal = [url for url in parser.anchor_hrefs if url not in external]
print('External links: ', external)
print('Internal links: ', internal)
print(f'Has password input: {parser.has_pass_field}')
print(f'Has submit button: {parser.has_submit}. Is login? {parser.has_login_button}')