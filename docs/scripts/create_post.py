#!/home/od/sites/oddsun.github.io/docs/scripts/venv/bin/python3
from jinja2 import Template
import datetime

def gen_template():
    ''' gen templates from cmd line inputs'''
    fp = '../templates/post_template.md'
    with open(fp, 'r') as f:
        template = Template(f.read())
    title = input('title: ')
    now = datetime.datetime.utcnow()
    out_file = f'../_posts/{now.date()}-{title.replace(" ", "_")}.md'
    with open(out_file, 'w') as f:
        f.write(template.render(**{'title': title, 'date_time': now.strftime('%Y-%m-%d %H:%M:%S')}))


if __name__ == '__main__':
    gen_template()
