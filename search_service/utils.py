import json
from docx import Document, document


def get_config(path_to_config: str) -> dict:
    with open(path_to_config) as config_file:
        config = json.load(config_file)
    return config


def docx_to_html(doc: document.Document) -> str:
    file_content = \
        """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
        """

    file_content += '<br>'.join([paragraph.text for paragraph in doc.paragraphs])

    file_content += \
        """
            </body>
        </html>"""

    return file_content
