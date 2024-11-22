// servicios/tareas.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import * as API from '../api/api';
import { TareaBase, Persona, TareaProgramadaNew, PersonaConTareas } from '../api/interfaces';
import { API_ENDPOINTS } from '../api/constants';

@Injectable({
  providedIn: 'root'
})
export class TareasService {
  constructor(private http: HttpClient) {}

  getTareas(): Observable<TareaBase[]> {
    return API.getTareas(this.http);
  }

  createTarea(tarea: Partial<TareaBase>): Observable<TareaBase> {
    return API.createTarea(this.http, tarea);
  }

  updateTarea(tarea: Partial<TareaBase>): Observable<TareaBase> {
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
