// app.routes.ts
import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { TareasComponent } from './tareas/tareas.component';
import { AssignedTaskComponent } from './assigned-task/assigned-task.component';

export const routes: Routes = [
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: 'home', component: HomeComponent },
    { path: 'tareas', component: TareasComponent },
    { path: 'tareas-asignadas', component: AssignedTaskComponent },
    { path: '**', redirectTo: 'home' }
];