import nltk
grammer = nltk.CFG.fromstring("""
S -> NP VP
NP -> PROPERN | DET NOM | PRON
VP -> ADVP V NP PP | V VP | V NP | ADVP V NP | V NP NP | V PP
ADVP -> ADV
PP -> P NP
DET -> Q | CD |
ADJP -> ADJ | ADVP ADJ | ADJ ADVP
NOM -> N | N N ADJP | UN N
PROPERN -> 'Nam' | 'Lan'
PRON -> 'Nó'
V -> 'đọc' | 'thích' | 'có' | 'mua' | 'tặng' | 'ở'
P -> 'ở'
N -> 'sách' | 'thư_viện' | 'cuốn'
UN -> 'cuốn'
Q -> 'nhiều'
ADV -> 'rất' | 'mới' | 'đang' | 'hay' | 'mua'
ADJ -> 'hay' | 'mới' | 'nhiều'
CD -> 'một' | 'hai'
""")
nltk.app.rdparser()
nltk.app.srparser()
file1 = open('Cau.txt', 'r', encoding="utf8")
Lines = file1.readlines()
for line in Lines:
    sentence = line.split()
    print(sentence)
    def parse(sent):
        a = []
        parser = new_func()
        for tree in parser.parse(sent):
            a.append(tree)
        return(a[0])

    def new_func():
        parser = nltk.ChartParser(grammer)
        return parser
    parse(sentence).draw()