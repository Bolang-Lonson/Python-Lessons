from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    isTitle: bool = False
    login_conditions = {
        'has_pass_field': False,
        'has_submit': False,
        'has_btn': False,
        'has_post_form': False,
        'has_login_button': False
    }
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
                    if input_type == 'password': self.login_conditions['has_pass_field'] = True
                    if input_type == 'submit': self.login_conditions['has_submit'] = True 
                    if input_type == 'button': self.login_conditions['has_btn'] = True 

                # If we have a submit input we can read the value attribute for human language hints
                if attr[0] == 'value' and (self.login_conditions['has_submit'] or self.login_conditions['has_btn']):
                    # using common human language button text for login buttons
                    if attr[1].lower() in ['login', 'log-in', 'log in', 'signin', 'sign-in', 'sign in']: self.login_conditions['has_login_button'] = True

        # getting the form's method
        if tag == 'form':
            for attr in attrs:
                if (attr[0] == 'method' and attr[1].lower() == 'post'): self.login_conditions['has_post_form'] = True 


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
html_content = doc.read().strip()  #   reading from html file
doc.close()

# looking out for <!DOCTYPE html>
if html_content.startswith('<!DOCTYPE html>'):
    print('Document is html:5')
elif html_content.startswith('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"'):
    print('Document is html:4.01')
elif html_content.startswith('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.'):
    print('Document is xhtml:1')
else:
    print('Unknown html version')

parser.feed(html_content)
parser.close()
print(parser.header_count)
print(f'Title: {parser.Title}')
# Seperating the links into internal and external links
external = [url for url in parser.anchor_hrefs if url.startswith('http')]
internal = [url for url in parser.anchor_hrefs if url not in external]
print('External links: ', external)
print('Internal links: ', internal)
# condition to conclude login page
if parser.login_conditions['has_pass_field']:
    if parser.login_conditions['has_login_button'] or parser.login_conditions['has_post_form']:
        print('Probably a login page')