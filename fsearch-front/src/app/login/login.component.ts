import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material/dialog'
import { FormBuilder, FormGroup, Validators, } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup

  formErrors = {
    'username': '',
    'password': ''
  }

  validationMessages = {
    'username': {
      'required': 'Enter at least something',
      'minlength': 'Username should be 4 characters at least'
    },
    'password': {
      'required': 'Please, enter your password',
      'minlength': 'Password should be 6 characters at least'
    }
  }

  constructor(
    private fb: FormBuilder
  ) { }

  ngOnInit(): void {
    this.createForm()
  }

  /**
   * Method for creating form
   * setting validators and watching if login form values change
   */
  createForm() {
    this.loginForm = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(3)]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    })

    this.loginForm.valueChanges
      .subscribe(data => this.onValueChanged(data))
  }

  /**
   * Filling formsErrors according to the errors while value occured changing
   * @param data form data
   */

  onValueChanged(data?: any) {
    if (!this.loginForm) { return; }
    const form = this.loginForm;
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

}
