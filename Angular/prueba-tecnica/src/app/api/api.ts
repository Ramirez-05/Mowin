// api/api.ts
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { API_ENDPOINTS } from './constants';
import { Tarea, Persona, TareaProgramadaNew } from './interfaces';

export function getTareas(http: HttpClient): Observable<Tarea[]> {
  return http.get<Tarea[]>(`${API_ENDPOINTS.tareas.base}${API_ENDPOINTS.tareas.getTareas}`);
}

export function createTarea(http: HttpClient, tarea: Partial<Tarea>): Observable<Tarea> {
  return http.post<Tarea>(`${API_ENDPOINTS.tareas.base}${API_ENDPOINTS.tareas.createTarea}`, tarea);
}

export function updateTarea(http: HttpClient, tarea: Partial<Tarea>): Observable<Tarea> {
  return http.put<Tarea>(`${API_ENDPOINTS.tareas.base}${API_ENDPOINTS.tareas.updateTarea}`, tarea);
}

export function deleteTask(http: HttpClient, id_tarea: number): Observable<any> {
  return http.delete(`${API_ENDPOINTS.tareas.base}${API_ENDPOINTS.tareas.deleteTarea}`, {
    params: { id_tarea }
  });
}

export function getAllPersonas(http: HttpClient): Observable<Persona[]> {
  return http.get<Persona[]>(`${API_ENDPOINTS.personas.base}${API_ENDPOINTS.personas.getAllPersonas}`);
}

export function createTareaProgramada(http: HttpClient, tarea: TareaProgramadaNew): Observable<TareaProgramadaNew> {
  return http.post<TareaProgramadaNew>(
    `${API_ENDPOINTS.tareaProgramada.base}${API_ENDPOINTS.tareaProgramada.createTareaProgramada}`, tarea);
}
