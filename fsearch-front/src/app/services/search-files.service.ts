import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { ResponseFile } from '../shared/responseFile';
import { ProcessHttpmsgService } from './process-httpmsg.service'
import { catchError, map } from 'rxjs/operators'
import { Observable, of } from 'rxjs';
import { EventEmitter } from 'protractor';
import { Document } from '../shared/doc'

@Injectable({
  providedIn: 'root'
})
export class SearchFilesService {

  private filesURL = "api/files/"
  files: Observable<ResponseFile>

  constructor(
    private http: HttpClient,
    private processHttpmsg: ProcessHttpmsgService
  ) { }

  searchFiles(data: string): Observable<ResponseFile> {
    this.files = this.http.get<ResponseFile>(`${this.filesURL}/?search_words=${data}`)
      .pipe(
        map(files => files[0]),
        catchError(this.processHttpmsg.handleError)
      )
    return this.files
  }

  getIds() {
    return this.files.pipe(
      map(files => files.docs.map(file => file.file_id))
    )
  }

  getFileByid(id: string): Observable<Document> {
    return this.http.get<Document>(`${this.filesURL}/?file_id=${id}`)
      .pipe(
        map(file => file[0]),
        catchError(this.processHttpmsg.handleError)
      )
  }

  // getFileByid(id: string): Observable<Document> {
  //   return this.http.get<Document>(`${this.filesURL}/docs/?file_id=${id}`)
  //     .pipe(
  //       catchError(this.processHttpmsg.handleError)
  //     )x
  // }


}
