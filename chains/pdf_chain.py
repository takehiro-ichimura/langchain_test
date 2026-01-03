from langchain_community.document_loaders import PyPDFLoader


def load_pdf_range(pdf_path: str, start: int, end: int):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    # PyPDFLoaderは0始まり
    return pages[start - 1: end]
