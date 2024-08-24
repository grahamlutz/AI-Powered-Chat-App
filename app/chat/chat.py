from app.chat.models import ChatArgs
from app.chat.vector_stores.pinecode import built_retriever


def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming boolean flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """
    retriever = built_retriever(chat_args)
