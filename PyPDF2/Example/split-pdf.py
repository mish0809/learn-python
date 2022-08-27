import PyPDF2
import os
from tkinter import filedialog

typ = [('PDFファイル','*.pdf')] 
dir = 'C:\\'
fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir) #分割したいPDF(ファイルダイアログで指定)

basename_without_ext  = os.path.splitext(os.path.basename(fle))[0]
print(fle)
print(basename_without_ext)

outputFolder = 'temp\\' #出力先フォルダ
page_sep = 2 #何ページごとに分割したいか

#pdfのページ数を把握する
reader = PyPDF2.PdfFileReader(fle)
page_num = reader.getNumPages()

#ページの抽出とファイル名に使う数字を派生させforで回す
for page in range(0, page_num, page_sep):
    merger = PyPDF2.PdfFileMerger()
    start = page
    end = start + page_sep
    merger.append(fle, pages=(start,end))
    file_name =  outputFolder + basename_without_ext + str(start) + '.pdf'
    print(file_name)
    merger.write(file_name)
    merger.close

print('終わり')

# 参考
# [【Python】ファイルダイアログを表示する(tkinter.filedialog) | 鎖プログラム](https://pg-chain.com/python-filedialog)
# [Pythonでパス文字列からファイル名・フォルダ名・拡張子を取得、結合 | note.nkmk.me](https://note.nkmk.me/python-os-basename-dirname-split-splitext/)