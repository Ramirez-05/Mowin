import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TareaAsignada, PersonaConTareas } from '../api/interfaces';
import { AssignedTaskService } from './assigned-task.service';

@Component({
    selector: 'app-assigned-task',
    standalone: true,
    imports: [CommonModule],
    templateUrl: './assigned-task.component.html',
    styleUrls: ['./assigned-task.component.css']
})
export class AssignedTaskComponent {
    personasConTareas: PersonaConTareas[] = [];
    error: string = '';
    tareaAsignada: TareaAsignada | null = null;

    constructor(private assignedTaskService: AssignedTaskService) {
        this.cargarPersonasConTareas();
    }

    cargarPersonasConTareas() {
        this.assignedTaskService.getAllPersonasConTareas().subscribe({
            next: (data: PersonaConTareas[]) => {
                this.personasConTareas = data;
            },
            error: (error: any) => {
                console.error('Error al cargar personas con tareas:', error);
                this.error = 'Error al cargar personas con tareas';
            }
        });
    }

    getCategoryClass(categoryName: string): string {
        return categoryName.toLowerCase().replace(/ /g, '-');
    }

    onCheckboxChange(tarea: any) {
        const updateData = {
            id_tarea: tarea.id_tarea,
            id_categoria: 4 
        };

        this.assignedTaskService.updateTareaCategoria(updateData).subscribe({
            next: () => {
                this.cargarPersonasConTareas();
            },
            error: (error) => {
                console.error('Error al actualizar la tarea:', error);
            }
        });
    }

    onUncheckTask(tarea: any) {
        const updateData = {
            id_tarea: tarea.id_tarea,
            id_categoria: 1
        };

        this.assignedTaskService.updateTareaCategoria(updateData).subscribe({
            next: () => {
                this.cargarPersonasConTareas();
            },
            error: (error) => {
                console.error('Error al actualizar la tarea:', error);
            }
        });
    }
}
