"""Penyuntingan akhir berkas .docx: bagian depan bernomor Romawi,
lebar kolom tabel proporsional, dan perapian paragraf di dalam sel."""
import copy
import os
import sys
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCX = os.path.join(ROOT, "Pengantar-Seismologi.docx")

LEBAR_TEKS = 7597          # twips: 176 mm - 24 mm - 18 mm
MIN_KOL = 880              # lebar kolom minimum (twips)


def el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn("w:" + k), str(v))
    return e


def atur_penomoran(sectPr, fmt, start=None):
    for lama in sectPr.findall(qn("w:pgNumType")):
        sectPr.remove(lama)
    p = el("w:pgNumType", fmt=fmt)
    if start is not None:
        p.set(qn("w:start"), str(start))
    # pgNumType harus berada sebelum elemen tertentu; ditaruh setelah pgMar
    ref = sectPr.find(qn("w:cols"))
    if ref is not None:
        ref.addprevious(p)
    else:
        sectPr.append(p)


def pisah_bagian(doc):
    """Sisipkan pemutus bagian sebelum Bab 1."""
    body = doc.element.body
    sect_akhir = body.find(qn("w:sectPr"))
    target = None
    for p in doc.paragraphs:
        if p.style.name == "Heading 1" and p.text.strip().startswith("BAB 1"):
            target = p
            break
    if target is None:
        print("  !! judul Bab 1 tidak ditemukan; pemisahan bagian dilewati")
        return
    depan = copy.deepcopy(sect_akhir)
    # bagian depan: tanpa header berjalan, nomor halaman Romawi kecil,
    # dan halaman judul dibiarkan polos
    for e in depan.findall(qn("w:headerReference")):
        depan.remove(e)
    for lama in depan.findall(qn("w:titlePg")):
        depan.remove(lama)
    ref = depan.find(qn("w:cols"))
    tp = OxmlElement("w:titlePg")
    if ref is not None:
        ref.addnext(tp)
    else:
        depan.append(tp)
    atur_penomoran(depan, "lowerRoman", 1)
    atur_penomoran(sect_akhir, "decimal", 1)

    p_baru = OxmlElement("w:p")
    ppr = OxmlElement("w:pPr")
    ppr.append(depan)
    p_baru.append(ppr)
    target._p.addprevious(p_baru)
    print("  bagian depan (angka Romawi) dipisahkan dari isi utama")


def rapikan_tabel(doc):
    diubah = 0
    for tbl in doc.tables:
        n = len(tbl.columns)
        if n == 0:
            continue
        panjang = []
        for j in range(n):
            tot = 0
            for i, row in enumerate(tbl.rows):
                try:
                    t = row.cells[j].text
                except IndexError:
                    continue
                # baris tajuk diberi bobot lebih kecil
                tot += len(t) * (0.6 if i == 0 else 1.0)
            panjang.append(max(tot / max(len(tbl.rows), 1), 1.0))
        # akar kuadrat meredam perbedaan yang terlalu ekstrem
        bobot = [x ** 0.62 for x in panjang]
        jml = sum(bobot)
        lebar = [max(MIN_KOL, int(LEBAR_TEKS * b / jml)) for b in bobot]
        sisa = LEBAR_TEKS - sum(lebar)
        lebar[bobot.index(max(bobot))] += sisa

        tblPr = tbl._tbl.tblPr
        for lama in tblPr.findall(qn("w:tblLayout")):
            tblPr.remove(lama)
        tblPr.append(el("w:tblLayout", type="fixed"))
        for lama in tblPr.findall(qn("w:tblW")):
            tblPr.remove(lama)
        tblPr.append(el("w:tblW", w=str(LEBAR_TEKS), type="dxa"))
        for lama in tblPr.findall(qn("w:tblCellMar")):
            tblPr.remove(lama)
        mar = OxmlElement("w:tblCellMar")
        for sisi in ("left", "right"):
            mar.append(el("w:" + sisi, w="62", type="dxa"))
        for sisi in ("top", "bottom"):
            mar.append(el("w:" + sisi, w="24", type="dxa"))
        tblPr.append(mar)

        grid = tbl._tbl.find(qn("w:tblGrid"))
        if grid is not None:
            tbl._tbl.remove(grid)
        grid = OxmlElement("w:tblGrid")
        for w in lebar:
            grid.append(el("w:gridCol", w=str(w)))
        tblPr.addnext(grid)

        for row in tbl.rows:
            for j, cell in enumerate(row.cells):
                if j >= len(lebar):
                    continue
                tcPr = cell._tc.get_or_add_tcPr()
                for lama in tcPr.findall(qn("w:tcW")):
                    tcPr.remove(lama)
                tcPr.insert(0, el("w:tcW", w=str(lebar[j]), type="dxa"))
                for par in cell.paragraphs:
                    pf = par.paragraph_format
                    pf.first_line_indent = 0
                    pf.left_indent = 0
                    pf.right_indent = 0
                    pf.space_after = 0
                    for run in par.runs:
                        if run.font.size is None:
                            run.font.size = None
        diubah += 1
    print(f"  lebar kolom disetel untuk {diubah} tabel")


def kecilkan_font_tabel(doc):
    """Ukuran huruf tabel 9 pt (8 pt untuk tabel berkolom banyak)."""
    for tbl in doc.tables:
        ukuran = "16" if len(tbl.columns) >= 8 else "18"
        for row in tbl.rows:
            for cell in row.cells:
                for par in cell.paragraphs:
                    ppr = par._p.get_or_add_pPr()
                    rpr = ppr.find(qn("w:rPr"))
                    if rpr is None:
                        rpr = OxmlElement("w:rPr")
                        ppr.append(rpr)
                    for tag, val in (("w:sz", ukuran), ("w:szCs", ukuran)):
                        for lama in rpr.findall(qn(tag)):
                            rpr.remove(lama)
                        rpr.append(el(tag, val=val))
                    for run in par.runs:
                        run.font.size = None
                        r = run._r.get_or_add_rPr()
                        for tag in ("w:sz", "w:szCs"):
                            for lama in r.findall(qn(tag)):
                                r.remove(lama)
                            r.append(el(tag, val=ukuran))


def jaga_gambar(doc):
    """Setel keepNext pada paragraf bergambar agar keterangannya tidak
    terpisah ke halaman berikutnya."""
    n = 0
    for par in doc.paragraphs:
        if par._p.findall(".//" + qn("w:drawing")):
            ppr = par._p.get_or_add_pPr()
            for tag in ("w:keepNext", "w:keepLines"):
                for lama in ppr.findall(qn(tag)):
                    ppr.remove(lama)
                ppr.insert(0, OxmlElement(tag))
            n += 1
    print(f"  {n} paragraf bergambar dijaga bersama keterangannya")


def main():
    if not os.path.exists(DOCX):
        sys.exit("berkas .docx belum dibuat")
    doc = Document(DOCX)
    pisah_bagian(doc)
    jaga_gambar(doc)
    rapikan_tabel(doc)
    kecilkan_font_tabel(doc)
    doc.save(DOCX)
    print("  -> penyuntingan akhir selesai")


if __name__ == "__main__":
    main()
