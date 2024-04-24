from pypdf import PdfReader

def getTextFromPdf(pdfFile):
#    creating object of pdf reader
     pdf_reader = PdfReader(pdfFile)

    #  getting the number of pages in pdf 
     num_pages = len(pdf_reader.pages)
     print(num_pages)
     #getting the text of each page
     page = pdf_reader.pages[4]
     text = page.extract_text()
     print(text)

     
   





# main
getTextFromPdf('abc.pdf')

