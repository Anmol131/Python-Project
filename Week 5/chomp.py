# 4
def chomp(s):
    return s[:-1] if len(s) > 1 else s

for s in ['cheesey', '123456', 'Ni', 'spam', '', 'A']:
    print(f'"{s}" -> "{chomp(s)}"')