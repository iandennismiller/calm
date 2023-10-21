import os
import re
import logging
from hashlib import sha256
from typing import Dict, List

import chromadb
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings
from chromadb.utils import embedding_functions


class ContextStorage(object):
    """
    Knowledge is represented as a vectore store.
    A KnowledgeBase is a specific collection of knowledge.
    The KnowledgeBase could represent a set of documents or other information that a language model might use to generate output.
    """

    def __init__(self, chroma_persist_dir=None, host=None, port=7999):
        logging.getLogger('chromadb').setLevel(logging.ERROR)

        if chroma_persist_dir is None:
            chroma_persist_dir = os.path.expanduser("~/.local/share/calm")

        # Create Chroma collection
        if host is not None and len(host) > 0:
            chroma_client = chromadb.HttpClient(host=host, port=port)
        else:
            chroma_client = chromadb.PersistentClient(
                path=chroma_persist_dir,
            )

        # ~/.cache/torch/sentence_transformers/sentence-transformers_all-mpnet-base-v2
        embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-mpnet-base-v2"
        )

        self.collection = chroma_client.get_or_create_collection(
            name="calm",
            metadata={"hnsw:space": "cosine"},
            embedding_function=embedding_function,
        )

    def add(self, content: str, metadata: Dict={}):
        # Check if the entry already exists
        checksum = sha256(content.encode('utf-8')).hexdigest()
        if len(self.collection.get(ids=[checksum])["ids"]) > 0:
            logging.getLogger("calm").debug(f"Entry {checksum} already exists")
        else:
            if metadata == {}:
                metadata = None
            self.collection.add(
                ids=checksum,
                documents=content,
                metadatas=metadata,
            )
            logging.getLogger("calm").info(f"Calculate embeddings for {checksum}")
        return checksum

    def query(self, query:str, top_num:int=50) -> List[dict]:
        entries = self.collection.query(
            query_texts=[query],
            n_results=top_num,
            include=["documents"]
        )
        return [doc for doc in entries["documents"][0]]


def context_to_string(context_list, per_item_limit=128, context_size=2048):
    "Format a list of context items into a string suitable for an LLM prompt"

    if not context_list:
        return

    result = ""
    for idx, item in enumerate(context_list):
        # compress whitespace
        item = re.sub(r"\s+", " ", item)
        item = re.sub(r"\n+", " ", item)

        # replace elipses with periods
        item = re.sub(r"\s*\.\.\.\s*", ".", item)

        # replace list items with semicolon
        item = re.sub(r"^- \[ \] ", "; ", item)
        item = re.sub(r"^- ", "; ", item)
        item = re.sub(r" - ", "; ", item)

        # replace fillers with nothing
        item = re.sub(r"^Okay.\s+", "", item)
        item = re.sub(r"^So\s", "", item)

        # iterate items to build result, truncating if necessary
        if len(item) > per_item_limit:
            truncated = ""
            for token in item.split(" "):
                if len(truncated) + len(token) < per_item_limit:
                    truncated += token + " "
                else:
                    break
            if len(truncated) > 0:
                item = truncated + "..."
            else:
                item = item[:per_item_limit] + "..."

        if len(result) + len(item) < context_size:
            # items += f'{i+1}. {item}\n'
            # items += f'{item}\n\n'
            result += f'- {item}\n'
        else:
            break

    return result
