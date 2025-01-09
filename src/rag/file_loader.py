from typing import Union, List, Literal
import glob
from tqdm import tqdm
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def remove_non_utf18_characters(text):
    return "".join(char for char in text if ord(char) < 128)

def load_pdf(pdf_file):
    docs = PyPDFLoader(pdf_file, extract_images=True).load()
    for doc in docs:
        doc.page_content = remove_non_utf18_characters(doc.page_content)
    return docs

class PDFLoader():
    def __init__(self) -> None:
        super().__init__()
    def __call__(self, pdf_files: List[str], **kwargs):
        doc_loaded = []
        total_files = len(pdf_files)
        with tqdm(total=total_files, desc="Loading PDFs", unit="file") as pbar:
            for pdf_file in pdf_files:
                result = load_pdf(pdf_file)
                doc_loaded.extend(result)
                pbar.update(1)
        return doc_loaded
    
class TextSplitter:
    def __init__(self,
                 separator: List[str] = ["\n\n", "\n", "", " "],
                 chunk_size: int = 300,
                 chunk_overlap: int = 0) -> None:
        
        self.splitter = RecursiveCharacterTextSplitter(
            separators=separator,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    
    def __call__(self, documents):
        return self.splitter.split_documents(documents)
    
class Loader:
    def __init__(self,
                 file_type: str = Literal["pdf"],
                 split_kwargs: dict = {
                     "chunk_size": 300,
                     "chunk_overlap": 0
                    } ) -> None:
        
        assert file_type in ["pdf"], "file_type must be 'pdf'"
        self.file_type = file_type
        self.doc_splitter = TextSplitter()
        if file_type == "pdf":
            self.doc_loader = PDFLoader()
        else:
            raise ValueError(f"file_type {file_type} not supported")
    
    def load(self, pdf_files: Union[str, List[str]], workers: int = 1):
        if isinstance(pdf_files, str):
            pdf_files = [pdf_files]
        doc_loaded = self.doc_loader(pdf_files, workers=workers)
        doc_split = self.doc_splitter(doc_loaded)
        return doc_split
    
    def load_dir(self, dir_path: str, workers: int = 1):
        if self.file_type == "pdf":
            files = glob.glob(f"{dir_path}/*.pdf")
            assert len(files) > 0, f"No PDF files found in {dir_path}"
        else:
            raise ValueError(f"file_type {self.file_type} not supported, file_type must be 'pdf'")
        return self.load(files, workers=workers)
        