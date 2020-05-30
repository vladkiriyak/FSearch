import { Injectable } from '@angular/core';
import { throwError } from 'rxjs'
import { HttpErrorResponse }  from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class ProcessHttpmsgService {

  constructor() { }

  /**
   * Handling errors method
   * @param error occurred error
   */
  public handleError(error: HttpErrorResponse | any) {
    let errMsg: string

    if (error.error instanceof ErrorEvent) {
      errMsg = error.error.message
    } 
    else{
      errMsg = `${error.status} -- ${error.statusText || ''} ${error.error} `
    }

    return throwError(errMsg)
  } 
  
}
