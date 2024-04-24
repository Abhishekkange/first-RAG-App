from pypdf import PdfReader

def getTextFromPdf(pdfFile):
#    creating object of pdf reader
     pdf_reader = PdfReader(pdfFile)

    #getting the number of pages in pdf 
     num_pages = len(pdf_reader.pages)
     print(num_pages)
     #getting the text of each page
     allText = ""
     for page_no in range(num_pages):
        
        page = pdf_reader.pages[page_no]
        text = page.extract_text()
        allText = allText+text
        # print(allText)

     return allText
     
def split_text(text):

    chunked_text = text.split('\n\n')

    #adding each chunk in list
    for i in chunked_text:
        

        


# main
allText = getTextFromPdf('abc.pdf')
print(len(allText))

