import os
import re

directory = r'c:\Users\PCX\Desktop\eduCentro'
files = [
    'kanada-master.html',
    'kanada-uni.html',
    'kanada-lise.html',
    'kanada-vize.html',
    'kanada-sss.html',
    'kanadadilokullari.html',
    'kanadayazokullari.html',
    'neden-kanada.html',
    'kanada-meslek-egitim.html'
]

# The standardized menu structure (Vocational Training removed)
def get_menu_html(current_file):
    items = [
        ('neden-kanada.html', 'Neden Kanada’da Eğitim?'),
        ('kanadadilokullari.html', 'Kanada Dil Okulları'),
        ('kanadayazokullari.html', 'Kanada Yaz Okulları'),
        ('kanada-lise.html', 'Kanada’da Lise'),
        ('kanada-uni.html', 'Kanada’da Üniversite'),
        ('kanada-master.html', 'Kanada’da Mastır'),
        # ('kanada-meslek-egitim.html', 'Kanada’da Meslek Eğitimi'), # Removed as per user request
        ('kanada-vize.html', 'Kanada’da Eğitim Vize'),
        ('kanada-sss.html', 'Kanada’da Eğitim Sıkça Sorulan Sorular')
    ]
    
    html = '<ul class="menu" id="menu-kanadada-egitim">\n'
    for href, text in items:
        is_active = href == current_file
        li_class = "menu-item menu-item-type-post_type menu-item-object-page"
        if is_active:
            li_class += " current-menu-item page_item current_page_item active"
        
        html += f'                                                    <li class="{li_class}"><a href="{href}">{text}</a></li>\n'
    html += '                                                </ul>'
    return html

# Regex to find the <ul> and everything inside it
menu_regex = re.compile(r'<ul\s+class="menu"\s+id="menu-kanadada-egitim">.*?</ul>', re.DOTALL)

for filename in files:
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        print(f"File not found: {filename}")
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_menu = get_menu_html(filename)
    new_content = menu_regex.sub(new_menu, content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filename}")
    else:
        print(f"No changes needed: {filename}")

print("All sidebars updated (Vocational link removed).")
