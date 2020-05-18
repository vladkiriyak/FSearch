import { Injectable } from '@angular/core';
import { InMemoryDbService } from 'angular-in-memory-web-api';
import { ResponseFile } from '../shared/responseFile'

@Injectable({
  providedIn: 'root'
})
export class InMemoryDataService implements InMemoryDbService {
  createDb() {
    const files = [
      {
        "user_id": "abcde1",
        "file_id": "1",
        "file_name": "file.docx",
        "file_content": "Cooooooonetent lalala"
      },
      {
        "user_id": "adfsdvbcde1",
        "file_id": "432rwfsdfdsfasd",
        "file_name": "file1.docx",
        "file_content": "Cooooooonetent lalala"
      },
      {
        "user_id": "abcdsdfse1",
        "file_id": "432rwfsdfdscvsd",
        "file_name": "file2.docx",
        "file_content": "Cooooooonetent lalala oooo"
      },
      {
        "search_words": "hello",
        "docs": [
          {
            "user_id": "abcde1",
            "file_id": "1",
            "file_name": "file.docx",
            "file_content": "Cooooooonetent lalala"
          },
          {
            "user_id": "adfsdvbcde1",
            "file_id": "432rwfsdfdsfasd",
            "file_name": "file1.docx",
            "file_content": "Cooooooonetent lalala"
          },
          {
            "user_id": "abcdsdfse1",
            "file_id": "432rwfsdfdscvsd",
            "file_name": "file2.docx",
            "file_content": "Cooooooonetent lalala oooo"
          }
        ]
      },
      {
        "search_words": "hallo",
        "docs": [
          {
            "user_id": "abcde1",
            "file_id": "432rwfsd",
            "file_name": "file.docx",
            "file_content": "Cooooooonetent lalala"
          },
          {
            "user_id": "adfsdvbcde1",
            "file_id": "432rwfsdfdsfasd",
            "file_name": "file1.docx",
            "file_content": "Cooooooonetent lalala"
          },
          {
            "user_id": "abcdsdfse1",
            "file_id": "432rwfsdfdscvsd",
            "file_name": "file2.docx",
            "file_content": "Cooooooonetent lalala oooo"
          }
        ]
      },
      {
        "search_words": "hullo",
        "docs": [
          {
            "user_id": "abcde1",
            "file_id": "432rwfsd",
            "file_name": "file.docx",
            "file_content": "Cooooooonetent lalala"
          },
          {
            "user_id": "adfsdvbcde1",
            "file_id": "432rwfsdfdsfasd",
            "file_name": "file1.docx",
            "file_content": "Cooooooonetent lalala"
          },
          {
            "user_id": "abcdsdfse1",
            "file_id": "432rwfsdfdscvsd",
            "file_name": "file2.docx",
            "file_content": "Cooooooonetent lalala oooo"
          }
        ]
      }
    ]
    return { files }
  }

  constructor() { }
}
