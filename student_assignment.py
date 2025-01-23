from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    textSplitter = CharacterTextSplitter(chunk_overlap=0)
    chunks = textSplitter.split_documents(docs)
    return  chunks[-1]


def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    textSplitter = RecursiveCharacterTextSplitter(separators=["第 "], chunk_size=30 ,chunk_overlap=0)
    chunks = textSplitter.split_documents(docs)
    return len(chunks)


if __name__ == "__main__":
    pass
    # response = hw02_2(q2_pdf)
    # for element in response:
    #     print(element.metadata)
    #     print(element.page_content)
    #     print()