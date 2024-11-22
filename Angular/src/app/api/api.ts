// api/api.ts
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { API_ENDPOINTS } from './constants';
import { TareaBase, Persona, TareaProgramadaNew, PersonaConTareas } from './interfaces';

export function getTareas(http: HttpClient): Observable<TareaBase[]> {
  return http.get<TareaBase[]>(`${API_ENDPOINTS.tareas.base}/get_tareas`);
}

export function createTarea(http: HttpClient, tarea: Partial<TareaBase>): Observable<TareaBase> {
  return http.post<TareaBase>(`${API_ENDPOINTS.tareas.base}/create_tarea`, tarea);
}

export function updateTarea(http: HttpClient, tarea: Partial<TareaBase>): Observable<TareaBase> {
  return http.put<TareaBase>(`${API_ENDPOINTS.tareas.base}/update_tarea`, tarea);
}

export function deleteTask(http: HttpClient, id_tarea: number): Observable<any> {
  return http.delete(`${API_ENDPOINTS.tareas.base}/delete_tarea?id_tarea=${id_tarea}`);
}

export function getAllPersonas(http: HttpClient): Observable<Persona[]> {
  return http.get<Persona[]>(`${API_ENDPOINTS.personas.base}/get-all-personas`);
}

export function createTareaProgramada(http: HttpClient, tarea: TareaProgramadaNew): Observable<TareaProgramadaNew> {
  return http.post<TareaProgramadaNew>(
    `${API_ENDPOINTS.tareaProgramada.base}/create_tarea_programada`, tarea);
}

export function getAllAssignedTasks(http: HttpClient): Observable<any> {
  return http.get<any>(`${API_ENDPOINTS.tareaProgramada.base}/get-tareas-programadas`);
}

export function getAllPersonasConTareas(http: HttpClient): Observable<PersonaConTareas[]> {
  return http.get<PersonaConTareas[]>(`${API_ENDPOINTS.personas.base}/get-personas-con-tareas`);
}
