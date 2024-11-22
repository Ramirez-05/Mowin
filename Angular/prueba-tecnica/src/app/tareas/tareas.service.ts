// servicios/tareas.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import * as API from '../api/api';
import { Tarea, Persona, TareaProgramadaNew } from '../api/interfaces';

@Injectable({
  providedIn: 'root'
})
export class TareasService {
  constructor(private http: HttpClient) {}

  getTareas(): Observable<Tarea[]> {
    return API.getTareas(this.http);
  }

  createTarea(tarea: Partial<Tarea>): Observable<Tarea> {
    return API.createTarea(this.http, tarea);
  }

  updateTarea(tarea: Partial<Tarea>): Observable<Tarea> {
    return API.updateTarea(this.http, tarea);
  }

  deleteTask(id_tarea: number): Observable<any> {
    return API.deleteTask(this.http, id_tarea);
  }

  getAllPersonas(): Observable<Persona[]> {
    return API.getAllPersonas(this.http);
  }

  createTareaProgramada(tarea: TareaProgramadaNew): Observable<TareaProgramadaNew> {
    return API.createTareaProgramada(this.http, tarea);
  }
}
