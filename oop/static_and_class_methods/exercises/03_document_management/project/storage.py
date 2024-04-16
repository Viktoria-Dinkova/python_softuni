from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def find_category(self, _id: int) -> Category:
        return next(filter(lambda c: c.id == _id, self.categories))

    def find_topic(self, _id: int) -> Topic:
        return next(filter(lambda t: t.id == _id, self.topics))

    def find_document(self, _id: int) -> Document:
        return next(filter(lambda d: d.id == _id, self.documents))

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = self.find_category(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = self.find_topic(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        doc = self.find_document(document_id)
        doc.edit(new_file_name)

    def delete_category(self, category_id: int) -> None:
        category = self.find_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int) -> None:
        topic = self.find_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id: int) -> None:
        document = self.find_document(document_id)
        self.documents.remove(document)

    def get_document(self, document_id: int) -> str:
        doc = self.find_document(document_id)
        return doc.__repr__()

    def __repr__(self) -> str:
        return '\n'.join(str(d) for d in self.documents)
