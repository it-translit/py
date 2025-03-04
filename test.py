import it_translit, sys, itertools

ok = True
def t(s, d, use_q = False):
    global ok
    if it_translit.trans(s, use_q = use_q) != d:
        sys.stderr.write(f"{s} -> {it_translit.trans(s, use_q = use_q)}\n")
        ok = False
        return
    if it_translit.reverse(d) != s:
        sys.stderr.write(f"{s} -> {d} -> {it_translit.reverse(d)}\n")
        ok = False

t('яндекс', 'yandex')
t('Яндекс', 'Yandex')
t('ЯНДЕКС', 'YANDEX')
t('МЯ', 'MYA')
t('Мя', 'Mya')
t('мя', 'mya')
t('хабр', 'habr')

t('только', "tol'ko")
t('только', 'tolqko', use_q = True)
t('Только', "Tol'ko")
t('Только', 'Tolqko', use_q = True)
t('ТОЛЬКО', "TOL'KO")
t('ТОЛЬКО', 'TOLQKO', use_q = True)
t('тольько', "tol'wko")
t('ТОЛЬЬКО', "TOL'WKO")

for rep in range(1, 5):
    for tup in itertools.product([chr(ord('а') + i) for i in range(32)] + ['ё'], repeat = rep):
        if it_translit.reverse(it_translit.trans(''.join(tup))) != ''.join(tup):
            sys.stderr.write(f"{''.join(tup)} -> {it_translit.trans(''.join(tup))} -> {it_translit.reverse(it_translit.trans(''.join(tup)))}\n")
            ok = False

if ok:
    print('ok')
else:
    sys.exit('!ok')
