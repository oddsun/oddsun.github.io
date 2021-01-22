#!/home/od/sites/oddsun.github.io/docs/scripts/venv/bin/python3
from jinja2 import Template
import datetime
import os

def gen_tag(tag):
    ''' gen templates from cmd line inputs'''
    fp = '../templates/tag_template.md'
    with open(fp, 'r') as f:
        template = Template(f.read())
    now = datetime.datetime.now()
    out_file = f'../tag/{tag}.md'
    if os.path.exists(out_file):
        return
    if not os.path.exists(os.path.dirname(out_file)):
        os.mkdir(os.path.dirname(out_file))
    with open(out_file, 'w') as f:
        f.write(template.render(**{'tag_name': tag}))


def scan_and_gen_tags():
    dir_name = '../_posts'
    tags_set = set()
    for fn in filter(lambda x: not x.endswith('swp'), os.listdir(dir_name)):
        fp = os.path.join(dir_name, fn)
        with open(fp, 'r') as f:
            text = f.read().split('\n')
        line = next(filter(lambda x: x.startswith('tags:'), text))
        tags = line.replace('tags:', '').strip().split(' ')
        tags_set = tags_set.union(set(tags))
    for tag in tags_set:
        gen_tag(tag)

if __name__ == '__main__':
    scan_and_gen_tags()
