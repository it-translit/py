mapping = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'з': 'z',
    'и': 'i',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',

    'е': 'e',
    'ё': 'yo',
    'ж': 'zh',
    'й': 'j',
    'х': 'h',
    'сх':'skh',
    'кс':'x',
    'ц': 'cz',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shh',
    'шх':'shkh',
    'ъ': "''",
    'ы': 'y',
    'ь': "'",
    'э': "e'",
    'ю': 'yu',
    'я': 'ya',

    'ыа': 'yaw',
    'ыу': 'yuw',
    'ыо': 'yow',
    'еь': "e'w",
    'ьь': "'w",
    'ьъ': "'ww",
    'еъ': 'eww',
    'зх': 'zkh',
    'зкх':'zkhw',
    'скх':'skhw',
    'шкх':'shkhw',
}

def get_mappings(items):
    mappings = [{} for _ in range(max(len(fr) for fr, to in items))]
    for fr, to in items:
        mappings[len(fr) - 1][fr] = to
    return mappings

mappings_wo_q = get_mappings(mapping.items())
mappings_with_q = get_mappings([(fr, to.replace("'", 'q')) for fr, to in mapping.items()])

mappings_reverse_items = []
for fr, to in mapping.items():
    mappings_reverse_items.append((to, fr))
    if "'" in to:
        mappings_reverse_items.append((to.replace("'", 'q'), fr))
mappings_reverse = get_mappings(mappings_reverse_items)

def trans(source, use_q = False):
    mappings = mappings_with_q if use_q else mappings_wo_q
    source_lower = source.lower()
    res = ''
    i = 0
    while i < len(source):
        for n in range(len(mappings), 0, -1):
            sl = source_lower[i:i+n]
            to = mappings[n-1].get(sl)
            if to is not None:
                #if not source[i:i+n].islower() and source[i:i+n].isalpha():
                if source[i:i+n] != sl:
                    if len(to) == 1:
                        if sl == 'кс':
                            if source[i:i+n] == 'кС':
                                to = 'kS'
                            elif source[i:i+n] == 'КС' and not (source[i+2:i+3].isupper() or (i > 0 and source[i-1].isupper())):
                                to = 'KS'
                            elif source[i:i+n] == 'Кс' and not source[i+2:i+3].islower():
                                to = 'Ks'
                            else:
                                to = to.upper()
                        else:
                            to = to.upper()
                    else:
                        if n == 1:
                            if source[i+1:i+2].isupper() or (i > 0 and source[i-1].isupper()):
                                to = to.upper()
                            else:
                                to = to.capitalize()
                        else:
                            to = to.upper()
                res += to
                i += n
                break
        else:
            res += source[i]
            i += 1
    return res

def reverse(source):
    source_lower = source.lower()
    res = ''
    i = 0
    while i < len(source):
        for n in range(len(mappings_reverse), 0, -1):
            sl = source_lower[i:i+n]
            to = mappings_reverse[n-1].get(sl)
            if to is not None:
                if source[i:i+n] != sl:
                    if len(to) == 1:
                        to = to.upper()
                    else:
                        if n == 1:
                            if source[i+1:i+2].isupper() or (i > 0 and source[i-1].isupper()):
                                to = to.upper()
                            else:
                                to = to.capitalize()
                        else:
                            to = to.upper()
                elif source[i] == "'":
                    if i > 0 and source[i-1].isupper():
                        to = to.upper()
                res += to
                i += n
                break
        else:
            res += source[i]
            i += 1
    return res
