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
    return chunks[-1]


def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    texts = ""
    for doc in docs:
        texts = texts + doc.page_content + "\n"
    textSplitter = RecursiveCharacterTextSplitter(separators=["   第 .* 章.*\n", "第 \\d* 條\n", "第 \\d*-\\d* 條\n"],
                                                  chunk_size=12,
                                                  chunk_overlap=0,
                                                  is_separator_regex=True)
    chunks = textSplitter.split_text(texts)
    return len(chunks)

# if __name__ == "__main__":
#     response = hw02_2(q2_pdf)
#     print ("lenth:", len(response))
#     for element in response:
#         print("--")
#         print(element)
#         print("--")
#         print()
