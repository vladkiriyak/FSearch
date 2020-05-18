import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchedFilesComponent } from './searched-files.component';

describe('SearchedFilesComponent', () => {
  let component: SearchedFilesComponent;
  let fixture: ComponentFixture<SearchedFilesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchedFilesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchedFilesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
