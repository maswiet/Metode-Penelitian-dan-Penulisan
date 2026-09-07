"""Merakit seluruh naskah menjadi satu berkas .docx siap cetak."""
import os
import re
import subprocess
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "src")
FIGS = os.path.join(ROOT, "figs")
OUT = os.path.join(ROOT, "Pengantar-Seismologi.docx")
GAB = os.path.join(HERE, "_gabungan.md")

LEBAR_TEKS_IN = 5.28          # B5 176 mm - margin 24 + 18 mm

PAGEBREAK = """
```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```
"""

TOC = """
```{=openxml}
<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
<w:r><w:t>Daftar Isi</w:t></w:r></w:p>
<w:p><w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="7370"/></w:tabs></w:pPr>
<w:fldSimple w:instr=" TOC \\o &quot;1-2&quot; \\h \\z \\u ">
<w:r><w:rPr><w:i/><w:sz w:val="18"/></w:rPr>
<w:t xml:space="preserve">Daftar isi otomatis. Di dalam Microsoft Word tekan Ctrl+A lalu F9, pilih "perbarui seluruh daftar", untuk memunculkan judul bab beserta nomor halamannya.</w:t>
</w:r></w:fldSimple></w:p>
```
"""

URUTAN = [
    "00-depan.md", "01-bab01.md", "02-bab02.md", "03-bab03.md",
    "04-bab04.md", "05-bab05.md", "06-bab06.md", "07-bab07.md",
    "08-bab08.md", "09-bab09.md", "10-bab10.md", "11-bab11.md",
    "12-bab12.md", "13-bab13.md", "14-bab14.md", "90-lampiran.md",
    "95-pustaka.md",
]


def lebar_gambar(nama):
    """Persentase lebar kolom teks untuk sebuah gambar."""
    path = os.path.join(FIGS, nama)
    if not os.path.exists(path):
        return None
    with Image.open(path) as im:
        w_px = im.size[0]
        dpi = im.info.get("dpi", (300, 300))[0] or 300
    lebar_in = w_px / dpi
    target = min(lebar_in, LEBAR_TEKS_IN)
    return max(28, min(100, round(target / LEBAR_TEKS_IN * 100)))


def olah(teks):
    teks = teks.replace("\\newpage", PAGEBREAK)

    def _img(m):
        nama = os.path.basename(m.group(1))
        pct = lebar_gambar(nama)
        if pct is None:
            print("  !! gambar hilang:", nama, file=sys.stderr)
            return m.group(0)
        return f"![]({m.group(1)}){{width={pct}%}}"

    teks = re.sub(r"!\[\]\(([^)]+)\)", _img, teks)
    return teks


def daftar(isi_semua):
    gbr = re.findall(r"\*\*(Gambar\s+[\d.]+)\.\*\*\s+(.+?)(?:\n\n|\n:::)",
                     isi_semua, re.S)
    tbl = re.findall(r"\*\*(Tabel\s+[\d.]+)\.\*\*\s+(.+?)(?:\n\n|\n\|)",
                     isi_semua, re.S)

    def rapikan(t):
        t = " ".join(t.split())
        t = re.sub(r"\s*\*([^*]+)\*", r" \1", t)
        potong = re.split(r"(?<=[a-z0-9\)])\.\s+(?=[A-Z])", t, maxsplit=1)
        t = potong[0]
        if len(t) > 118:
            t = t[:115].rsplit(" ", 1)[0] + " …"
        return t.rstrip(". ") + "."

    out = ["# Daftar Gambar {.unnumbered}", ""]
    for nomor, judul in gbr:
        out.append(f"**{nomor}.** {rapikan(judul)}\n")
    out += [PAGEBREAK, "# Daftar Tabel {.unnumbered}", ""]
    for nomor, judul in tbl:
        out.append(f"**{nomor}.** {rapikan(judul)}\n")
    out.append(PAGEBREAK)
    return "\n".join(out), len(gbr), len(tbl)


def main():
    bagian = {}
    for nama in URUTAN:
        with open(os.path.join(SRC, nama), encoding="utf-8") as f:
            bagian[nama] = f.read()

    isi_semua = "\n\n".join(bagian[n] for n in URUTAN)
    dgt, n_g, n_t = daftar(isi_semua)
    print(f"  daftar gambar: {n_g} entri, daftar tabel: {n_t} entri")

    potongan = [olah(bagian["00-depan.md"]), TOC, PAGEBREAK, olah(dgt)]
    for nama in URUTAN[1:]:
        potongan.append(olah(bagian[nama]))

    with open(GAB, "w", encoding="utf-8") as f:
        f.write("\n\n".join(potongan))

    cmd = [
        "pandoc", GAB, "-o", OUT,
        "--from", "markdown+pipe_tables+definition_lists+raw_attribute"
                  "+fenced_divs+tex_math_dollars+implicit_figures",
        "--reference-doc", os.path.join(HERE, "reference.docx"),
        "--resource-path", f"{SRC}{os.pathsep}{ROOT}{os.pathsep}{FIGS}",
        "--metadata", "lang=id",
        "--dpi", "300",
        "--wrap", "none",
    ]
    subprocess.run(cmd, check=True)
    kb = os.path.getsize(OUT) / 1024
    print(f"  -> {OUT} ({kb:.0f} KB)")


if __name__ == "__main__":
    main()
