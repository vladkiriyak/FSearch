import { Component, OnInit, ViewChild, Input } from '@angular/core';
import { SearchFilesService } from '../services/search-files.service';
import { SearchComponent } from '../search/search.component';
import { Observable } from 'rxjs';
import { ResponseFile } from '../shared/responseFile'
import { Document } from '../shared/doc'

@Component({
  selector: 'app-searched-files',
  templateUrl: './searched-files.component.html',
  styleUrls: ['./searched-files.component.scss']
})
export class SearchedFilesComponent implements OnInit {
  files: Document[]


  constructor(
    private searchFilesService: SearchFilesService
  ) {
  }

  ngOnInit(): void {
    this.searchFilesService.files
      .subscribe(files => { this.files = files.docs})

  }


}
