# backend/document_processor/core.py
from pathlib import Path
from unstructured.partition.pdf import partition_pdf

class PDFProcessor:
    def __init__(self, chunk_size=1000):
        self.chunk_size = chunk_size
        
    def process(self, pdf_path: Path):
        elements = partition_pdf(filename=pdf_path, strategy="auto")
        return self._chunk_elements(elements)
    
    def _chunk_elements(self, elements):
        # Custom chunking logic without LangChain dependencies
        chunks = []
        current_chunk = []
        current_length = 0
        
        for element in elements:
            text = element.text
            if current_length + len(text) > self.chunk_size:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                current_length = 0
            current_chunk.append(text)
            current_length += len(text)
            
        if current_chunk:
            chunks.append(" ".join(current_chunk))
            
        return chunks
