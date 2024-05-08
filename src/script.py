from pypinyin import lazy_pinyin, Style
from pypinyin.style import register

htmlstart = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no"/>
</head>
<body>
<body>
<a href="1.html">1</a>
<a href="2.html">2</a>
<a href="3.html">3</a>
<a href="4.html">4</a>
<a href="5.html">5</a>
<a href="6.html">6</a>
<a href="7.html">7</a>
<a href="8.html">8</a>
<a href="9.html">9</a>
<a href="10.html">10</a>
<a href="11.html">11</a>
<a href="12.html">12</a>
<a href="13.html">13</a>
<a href="14.html">14</a>
<a href="15.html">15</a>
<a href="16.html">16</a>
<a href="17.html">17</a>
<a href="18.html">18</a>
<a href="19.html">19</a>
<a href="20.html">20</a>
<a href="21.html">21</a>
<a href="22.html">22</a>
<a href="23.html">23</a>
<table style="display:block;">
"""
htmlend = """</table>
</body>
<a href="1.html">1</a>
<a href="2.html">2</a>
<a href="3.html">3</a>
<a href="4.html">4</a>
<a href="5.html">5</a>
<a href="6.html">6</a>
<a href="7.html">7</a>
<a href="8.html">8</a>
<a href="9.html">9</a>
<a href="10.html">10</a>
<a href="11.html">11</a>
<a href="12.html">12</a>
<a href="13.html">13</a>
<a href="14.html">14</a>
<a href="15.html">15</a>
<a href="16.html">16</a>
<a href="17.html">17</a>
<a href="18.html">18</a>
<a href="19.html">19</a>
<a href="20.html">20</a>
<a href="21.html">21</a>
<a href="22.html">22</a>
<a href="23.html">23</a>
<script>
function annotate(element) {
    const annotationid = element.id.toString() + "py"
    const visibility = document.getElementById(annotationid).style.visibility;
    document.getElementById(annotationid).style.visibility = visibility == "hidden" ? "visible" : "hidden";
}
</script>
</html>
"""

def parse_book(book):
    pass

def get_book(i):
    ans = ''
    with open(f'old/{i}.html') as fp:
        for line in fp:
            if len(line) > 1500:
                ans = line
                break
    return ans

def build_html(py, cn):
    assert(len(py) == len(cn))

    html = []
    i = 0
    for j in range(len(cn)):
        assert(len(py[j]) == len(cn[j]))
        row = []

        row.append('<tr scope="row">')

        for k in range(len(py[j])):
            py_cell = build_py_cell(i, py[j][k])
            cn_cell = build_cn_cell(i, cn[j][k])
            cell = build_word_cell(py_cell, cn_cell)
            row.append(cell)
            i += 1

        row.append('</tr>')

        html.extend(row)

    return '\n'.join(html)

def build_word_cell(py, cn):
    return f'<td style="display:inline-block;"><table><tr>{py}</tr><tr>{cn}</tr></table></td>'

def build_py_cell(i, py):
    return f'<td id="w{i}py" style="visibility:hidden;text-align:center;">{py}</td>'

def build_cn_cell(i, cn):
    return f'<td id="w{i}" style="text-align:center;" onclick="annotate(this)">{cn}</td>'

def write_html(i, html):
    with open(f'new/{i}.html', 'x') as fp:
        fp.writelines(htmlstart)
        fp.writelines(html)
        fp.writelines(htmlend)

    return


if __name__ == '__main__':
    for i in range(1, 24):
        book = get_book(i)
        book = book.split('<br/>')
        book = filter(lambda l : 'div' not in str(l), book)
        book = filter(lambda l : '\\u' not in str(l), book)
        book = list(book)
        cn = []
        py = []
        for l in book:
            py.append(lazy_pinyin(l, style=Style.TONE, errors=lambda x: [c for c in x]))
        html = build_html(py, book)
        write_html(i, html)
