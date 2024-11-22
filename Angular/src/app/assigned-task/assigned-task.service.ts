import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { API_ENDPOINTS } from '../api/constants';
import { PersonaConTareas, TareaUpdateCategoria } from '../api/interfaces';


@Injectable({
    providedIn: 'root'
})
export class AssignedTaskService {
    constructor(private http: HttpClient) {}

    getAllPersonasConTareas(): Observable<PersonaConTareas[]> {
        return this.http.get<PersonaConTareas[]>(`${API_ENDPOINTS.tareaProgramada.base}/get-tareas-programadas`);
    }

    updateTareaCategoria(data: TareaUpdateCategoria): Observable<any> {
        return this.http.put(`${API_ENDPOINTS.tareas.base}/update_categoria_tareas`, data);
    }
}