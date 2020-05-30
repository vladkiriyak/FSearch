import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router'
import { switchMap, tap } from 'rxjs/operators';
import { SearchFilesService } from '../services/search-files.service';
import { ResponseFile } from '../shared/responseFile'
import { Document } from '../shared/doc'
import { Location } from '@angular/common'

@Component({
  selector: 'app-file-detail',
  templateUrl: './file-detail.component.html',
  styleUrls: ['./file-detail.component.scss']
})
export class FileDetailComponent implements OnInit {

  selectedFile: Document
  fileIds
  prev: string
  next: string

  constructor(
    private route: ActivatedRoute,
    private searchFilesService: SearchFilesService,
    private location: Location
  ) { }

  ngOnInit(): void {
    this.searchFilesService.getIds()
      .subscribe(ids => { this.fileIds = ids, console.log(this.fileIds) })

    this.route.params.pipe(switchMap((params: Params) => this.searchFilesService.getFileByid(params['id'])))
      .subscribe(file => { this.selectedFile = file, this.setPrevNext(file.file_id), console.log(this.selectedFile)})

  }

  /**
   * This method turns us back to the previous page
   */

  goBack() {
    this.location.back()
  }

  /**
   * This method sets the rigth indexof the file
   * this is made for swiping files 
   * @param fileId the curent file id
   */
  setPrevNext(fileId: string) {
    const index = this.fileIds.indexOf(fileId)
    this.prev = this.fileIds[(this.fileIds.length + index - 1) % this.fileIds.length];
    this.next = this.fileIds[(this.fileIds.length + index + 1) % this.fileIds.length];

  }

} 
