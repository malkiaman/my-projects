import PyPDF2 # pip install PyPDF2
# import pdf file
# pdfile stores the pdf names you want to merge
Pdfiles=['file1.pdf','file2.pdf','file3.pdf'] 
merger=PyPDF2.PdfMerger()
for filename in Pdfiles:
    pdfFile=open(filename,'rb')  # r stands for reading while b stands for binary formate
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("merged.pdf")