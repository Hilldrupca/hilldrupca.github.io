from os import path
import sys

def load_html(path: str) -> str:
    '''
    Returns the html file as a string.
    '''
    
    with open(path, 'r') as f:
        lines = f.readlines()
        lines[-1] = lines[-1].rstrip()
        html = ''.join(lines)
        
    return html
    
def merge_base_body(body_name: str, base_name: str = 'base.html') -> None:
        
    #root = path.splitext(body_path)[0]
    title = body_name.split('.')[0]
    
    with open(title + '.html', 'w') as f:
        body = load_html('./templates/' + body_name)
        base = load_html('./templates/' + base_name)
        f.write(base.format(title, body))
                
if __name__ == '__main__':
    for html in sys.argv[1:]:
        merge_base_body(html)
