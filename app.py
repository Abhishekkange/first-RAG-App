from pypdf import PdfReader 
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA 
import os

os.environ['GOOGLE_API_KEY'] = 'AIzaSyANqyvxOpFeKyVjDI_fbkTGp2aaKYu_MS4'



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

    print("generating embedding")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key = "AIzaSyANqyvxOpFeKyVjDI_fbkTGp2aaKYu_MS4")
    db = Chroma.from_texts(chunkedText, embeddings)
    print("eembeddings generated")
    return db

def create_model():
    llm = genai.GenerativeModel(model_name="gemini-pro")
    return llm




   


    
        

        


# main
allText = getTextFromPdf('abc.pdf')
chunked_text = split_text(allText)
embeddings = generateEmbeddings(chunked_text)
result = embeddings.similarity_search('In Rich Dad Poor Dad Robert Kiyosaki mentions his first business venture, which involved selling "Crushed Surfers," wallets made out of Velcro and nylon. He created these wallets with the help of his best friend Mike and started selling them to his classmates in high school.')
print(result[0].page_content)
# model = create_model()
# qa_chain = RetrievalQA.from_chain_type(model,retriever=embeddings,return_source_documents = True)

# question = "what did rich dad told to author?"
# result = qa_chain({"query":question})
# print(result)





