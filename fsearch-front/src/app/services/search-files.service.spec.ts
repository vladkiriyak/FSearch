import { TestBed } from '@angular/core/testing';

import { SearchFilesService } from './search-files.service';

describe('SearchFilesService', () => {
  let service: SearchFilesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SearchFilesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
