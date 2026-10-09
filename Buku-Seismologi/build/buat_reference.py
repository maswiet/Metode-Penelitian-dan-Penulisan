"""Membuat reference.docx untuk pandoc: ukuran B5, gaya, header, dan footer."""
import copy
import subprocess
import os
from docx import Document
from docx.shared import Mm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn, nsmap
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, "reference.docx")
BASE = os.path.join(HERE, "_pandoc-default.docx")

# 1. ambil reference bawaan pandoc sebagai basis (agar semua gaya pandoc ada)
with open(BASE, "wb") as f:
    f.write(subprocess.run(
        ["pandoc", "--print-default-data-file", "reference.docx"],
        capture_output=True, check=True).stdout)

doc = Document(BASE)
S = {st.name: st for st in doc.styles}

# ---------------------------------------------------------------- halaman B5
sec = doc.sections[0]
sec.page_width = Mm(176)
sec.page_height = Mm(250)
sec.top_margin = Mm(22)
sec.bottom_margin = Mm(20)
sec.left_margin = Mm(24)      # tepi dalam (gutter)
sec.right_margin = Mm(18)     # tepi luar
sec.header_distance = Mm(12)
sec.footer_distance = Mm(11)

sectPr = sec._sectPr
# cetak bolak-balik: margin cermin
mirror = OxmlElement("w:mirrorMargins")
doc.settings.element.append(mirror)
even = OxmlElement("w:evenAndOddHeaders")
doc.settings.element.append(even)


def _set(el, tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn("w:" + k), str(v))
    el.append(e)
    return e


# ----------------------------------------------------------------- font dasar
normal = S["Normal"]
normal.font.name = "Cambria"
normal.font.size = Pt(10.5)
rpr = normal.element.get_or_add_rPr()
rf = rpr.find(qn("w:rFonts"))
if rf is None:
    rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
for a in ("ascii", "hAnsi", "cs", "eastAsia"):
    rf.set(qn("w:" + a), "Cambria")
pf = normal.paragraph_format
pf.space_after = Pt(0)
pf.space_before = Pt(0)
pf.line_spacing = 1.16
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# jarak antarparagraf: pandoc memakai "First Paragraph" + "Body Text"
for nm, first_indent in (("Body Text", Mm(5)), ("First Paragraph", 0)):
    st = S.get(nm)
    if st is None:
        continue
    st.paragraph_format.first_line_indent = first_indent
    st.paragraph_format.space_after = Pt(0)
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# ------------------------------------------------------------------- judul bab
h1 = S["Heading 1"]
h1.font.name = "Cambria"
h1.font.size = Pt(19)
h1.font.bold = True
h1.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
h1.paragraph_format.space_before = Pt(0)
h1.paragraph_format.space_after = Pt(16)
h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h1.paragraph_format.keep_with_next = True
# bab selalu mulai di halaman baru
ppr = h1.element.get_or_add_pPr()
_set(ppr, "w:pageBreakBefore", val="true")
pbdr = OxmlElement("w:pBdr")
_set(pbdr, "w:bottom", val="single", sz="12", space="8", color="111111")
ppr.append(pbdr)

h2 = S["Heading 2"]
h2.font.size = Pt(13); h2.font.bold = True; h2.font.name = "Cambria"
h2.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
h2.paragraph_format.space_before = Pt(15)
h2.paragraph_format.space_after = Pt(5)
h2.paragraph_format.keep_with_next = True

h3 = S["Heading 3"]
h3.font.size = Pt(11); h3.font.bold = True; h3.font.italic = False
h3.font.name = "Cambria"
h3.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
h3.paragraph_format.space_before = Pt(11)
h3.paragraph_format.space_after = Pt(3)
h3.paragraph_format.keep_with_next = True


# ------------------------------------------------------------- gaya tambahan
def tambah(nama, size=10.5, bold=False, italic=False, align=None,
           space_before=0, space_after=0, indent=None, kotak=False,
           shade=None, font=None, color=None, line=1.16, keep=False):
    st = S.get(nama)
    if st is None:
        st = doc.styles.add_style(nama, WD_STYLE_TYPE.PARAGRAPH)
        st.base_style = S["Normal"]
        S[nama] = st
    st.font.size = Pt(size)
    st.font.bold = bold
    st.font.italic = italic
    st.font.name = font or "Cambria"
    if color:
        st.font.color.rgb = RGBColor.from_string(color)
    r = st.element.get_or_add_rPr()
    rfe = r.find(qn("w:rFonts"))
    if rfe is None:
        rfe = OxmlElement("w:rFonts"); r.insert(0, rfe)
    for a in ("ascii", "hAnsi", "cs"):
        rfe.set(qn("w:" + a), font or "Cambria")
    p = st.paragraph_format
    p.space_before = Pt(space_before)
    p.space_after = Pt(space_after)
    p.line_spacing = line
    p.keep_with_next = keep
    if align is not None:
        p.alignment = align
    if indent is not None:
        p.left_indent = Mm(indent)
        p.right_indent = Mm(indent)
    ppr_ = st.element.get_or_add_pPr()
    if kotak:
        b = OxmlElement("w:pBdr")
        for side in ("top", "left", "bottom", "right"):
            _set(b, "w:" + side, val="single", sz="6", space="8",
                 color="8A8A8A")
        ppr_.append(b)
    if shade:
        sh = OxmlElement("w:shd")
        sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto")
        sh.set(qn("w:fill"), shade)
        ppr_.append(sh)
    return st


C = WD_ALIGN_PARAGRAPH.CENTER
J = WD_ALIGN_PARAGRAPH.JUSTIFY

tambah("JudulBuku", size=30, bold=True, align=C, space_before=90,
       space_after=8, line=1.0)
tambah("SubjudulBuku", size=13.5, italic=True, align=C, space_after=60,
       line=1.15)
tambah("PenulisBuku", size=13, align=C, space_after=6)
tambah("AfiliasiBuku", size=10, align=C, space_before=40, line=1.25)
tambah("Persembahan", size=11, italic=True, align=C, space_before=18,
       space_after=18, indent=14, line=1.35)
tambah("TandaTangan", size=10.5, align=WD_ALIGN_PARAGRAPH.RIGHT,
       space_before=16, line=1.25)
tambah("Kotak", size=9.5, align=J, indent=3, space_before=7, space_after=7,
       kotak=True, shade="F2F2F2", line=1.12)
tambah("Tujuan", size=9.5, align=J, indent=3, space_before=6, space_after=10,
       kotak=True, shade="EDEDED", line=1.12)
tambah("Ringkasan", size=9.8, align=J, indent=3, space_before=10,
       space_after=8, kotak=True, shade="F7F7F7", line=1.14)
tambah("Soal", size=9.8, align=J, indent=0, space_before=8, space_after=6,
       line=1.14)
tambah("Bacaan", size=9.3, align=J, indent=0, space_before=8, space_after=6,
       line=1.10)
tambah("ImageCaption", size=8.8, align=C, space_before=4, space_after=12,
       indent=6, line=1.10)
tambah("Image Caption", size=8.8, align=C, space_before=4, space_after=12,
       indent=6, line=1.10)
tambah("Table Caption", size=8.8, align=WD_ALIGN_PARAGRAPH.LEFT,
       space_before=10, space_after=3, line=1.10, keep=True)
tambah("Compact", size=10.5, align=J, space_after=0)
tambah("Author", size=11, align=C)
tambah("Source Code", size=8.6, font="Consolas", align=WD_ALIGN_PARAGRAPH.LEFT,
       space_before=2, space_after=2, indent=3, line=1.05, shade="F4F4F4")

for nm in ("Verbatim Char", "SourceCode"):
    st = S.get(nm)
    if st is not None:
        st.font.name = "Consolas"
        st.font.size = Pt(8.6)

# gambar ditengahkan
for nm in ("Figure", "Captioned Figure"):
    st = S.get(nm)
    if st is not None:
        st.paragraph_format.alignment = C
        st.paragraph_format.space_before = Pt(10)
        st.paragraph_format.space_after = Pt(2)

# ----------------------------------------------------------- header & footer
def isi_hf(par, teks, right=False, field=None, size=8.5, italic=True):
    par.alignment = (WD_ALIGN_PARAGRAPH.RIGHT if right
                     else WD_ALIGN_PARAGRAPH.LEFT)
    if teks:
        run = par.add_run(teks)
        run.font.size = Pt(size)
        run.font.italic = italic
        run.font.name = "Cambria"
    if field:
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), field)
        r = OxmlElement("w:r")
        rp = OxmlElement("w:rPr")
        sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2)))
        rp.append(sz)
        r.append(rp)
        t = OxmlElement("w:t"); t.text = "1"
        r.append(t)
        fld.append(r)
        par._p.append(fld)


sec.different_first_page_header_footer = False
hdr_odd = sec.header.paragraphs[0]
isi_hf(hdr_odd, None, right=True, field=' STYLEREF 1 \\* MERGEFORMAT ')
hdr_even = sec.even_page_header.paragraphs[0]
isi_hf(hdr_even, "Pengantar Seismologi", right=False)

ftr_odd = sec.footer.paragraphs[0]
isi_hf(ftr_odd, None, right=True, field=" PAGE ", italic=False)
ftr_even = sec.even_page_footer.paragraphs[0]
isi_hf(ftr_even, None, right=False, field=" PAGE ", italic=False)

# garis tipis di bawah header
for p in (hdr_odd, hdr_even):
    pp = p._p.get_or_add_pPr()
    b = OxmlElement("w:pBdr")
    _set(b, "w:bottom", val="single", sz="4", space="4", color="B0B0B0")
    pp.append(b)

# buang isi contoh dari reference bawaan
for p in list(doc.paragraphs):
    if p.text.strip() and p.style.name not in ("Header", "Footer"):
        pass

doc.save(REF)
print("reference.docx tersimpan:", REF)
