CREATE TABLE documents(
    document_name text unique,
    word_quantity int

);

CREATE TABLE word_in_documents_inverted(
    word text unique,
    document_name text references documents

);



CREATE TABLE word_in_documents(
    document_name text references documents,
    word text references word_in_documents_inverted

);


CREATE TABLE word_position_in_document(
    word text references word_in_documents_inverted,
    document_name text references documents,
    position text unique
);
