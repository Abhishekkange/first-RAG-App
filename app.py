from pypdf import PdfReader 
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain import PromptTemplate
from langchain_community.vectorstores import Chroma


def getTextFromPdf(pdfFile):
#    creating object of pdf reader
     pdf_reader = PdfReader(pdfFile)

    #getting the number of pages in pdf 
     num_pages = len(pdf_reader.pages)
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
    return chunked_text

def generateEmbeddings(chunkedText):

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key = "RAIzaSyANqyvxOpFeKyVjDI_fbkTGp2aaKYu_MS4Z")
    db = Chroma.from_texts(chunkedText, embeddings)



   


    
        

        


# main
allText = getTextFromPdf('abc.pdf')
chunked_text = split_text(allText)
generateEmbeddings(chunked_text)



