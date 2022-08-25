import PyPDF2

outputFolder = 'temp\\' #出力先フォルダ
f = 'test.pdf' #分割したいPDF
page_sep = 2 #何ページごとに分割したいか

#pdfのページ数を把握する
reader = PyPDF2.PdfFileReader(f)
page_num = reader.getNumPages()

#ページの抽出とファイル名に使う数字を派生させforで回す
for page in range(0, page_num, page_sep):
    merger = PyPDF2.PdfFileMerger()
    start = page
    end = start + page_sep
    merger.append(f, pages=(start,end))
    file_name =  outputFolder + str(start) + '.pdf'
    merger.write(file_name)
    merger.close

print('終わり')