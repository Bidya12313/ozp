import os


def upload_documents(docs: list):
    uploaded_docs = []
    if docs[0]:
        for document in docs:
            docname = os.path.join('uploads', document.filename)
            document.save(docname)
            uploaded_docs.append(document.filename)
        return ', '.join(uploaded_docs)
    return ''