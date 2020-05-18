import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SearchComponent } from './search/search.component';
import { SearchedFilesComponent } from './searched-files/searched-files.component';
import { FileDetailComponent } from './file-detail/file-detail.component';


const routes: Routes = [
  {path: 'search', component: SearchComponent},
  {path: 'files', component: SearchedFilesComponent},
  {path: 'files/:id', component: FileDetailComponent},
  {path: '', redirectTo: '/search', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
