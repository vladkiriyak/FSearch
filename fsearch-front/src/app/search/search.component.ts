import { Component, OnInit, Output } from '@angular/core';
import { FormBuilder, FormGroup, Validators, Form } from '@angular/forms'
import { ResponseFile } from '../shared/responseFile'
import { SearchFilesService } from '../services/search-files.service';
import { EventEmitter } from 'protractor';
import { EXAMPLE } from '../shared/example'

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  searchForm: FormGroup;
  files: ResponseFile
  file

  formErrors = {
    'searchText': '',

  }

  validationMessages = {
    'searchText': {
      'required': 'Enter at least something!',
      'minlength': 'Search request must be 4 characters at least',
    },
  }

  constructor(
    private fb: FormBuilder,
    private searchFilesService: SearchFilesService
  ) {
    this.createForm()
  }

  ngOnInit(): void {
  }

  /**
   * creating form for word searching
   */
  createForm(): void {
    this.searchForm = this.fb.group({
      searchText: ['', [Validators.required, Validators.minLength(4)]]
    })

    this.searchForm.valueChanges
      .subscribe(data => this.onValueChanged(data))
  }

  /**
   * Filling formsErrors according to the errors while value occured changing
   * @param data form data
   */

  onValueChanged(data?: any) {
    if (!this.searchForm) { return; }
    const form = this.searchForm;
    for (const field in this.formErrors) {
      if (this.formErrors.hasOwnProperty(field)) {
        // clear previous error message (if any)
        this.formErrors[field] = '';
        const control = form.get(field);
        if (control && control.dirty && !control.valid) {
          const messages = this.validationMessages[field];
          for (const key in control.errors) {
            if (control.errors.hasOwnProperty(key)) {
              this.formErrors[field] += messages[key] + ' ';
            }
          }
        }
      }
    }
  }

  /**
   * Submit method
   * submits form and resets it
   */

  onSubmit() {
    const searchText = this.searchForm.value
    console.log(searchText.searchText)

    this.searchFilesService.searchFiles(searchText.searchText)
      .subscribe((response) => { this.files = response})
    

    this.searchForm.reset({
      searchText: ''
    })

  }



}
