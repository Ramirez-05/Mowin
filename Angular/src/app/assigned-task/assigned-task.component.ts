import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AssignedTaskService } from './assigned-task.service';
import { PersonaConTareas } from '../api/interfaces';

@Component({
    selector: 'app-assigned-task',
    standalone: true,
    imports: [CommonModule],
    providers: [AssignedTaskService],
    templateUrl: './assigned-task.component.html',
    styleUrls: ['./assigned-task.component.css']
})
export class AssignedTaskComponent implements OnInit {
    personasConTareas: PersonaConTareas[] = [];
    error: string = '';

    constructor(private assignedTaskService: AssignedTaskService) {}

    ngOnInit() {
        this.cargarPersonasConTareas();
    }

    cargarPersonasConTareas() {
        this.assignedTaskService.getAllPersonasConTareas().subscribe({
            next: (data: PersonaConTareas[]) => {
                this.personasConTareas = data;
            },
            error: (error: any) => {
                console.error('Error:', error);
                this.error = 'Error al cargar personas con tareas';
            }
        });
    }

    getCategoryClass(categoryName: string): string {
        switch (categoryName.toLowerCase()) {
            case 'pendiente':
                return 'pendiente';
            case 'en progreso':
                return 'en-progreso';
            case 'completada':
                return 'completada';
            case 'fuera de tiempo':
                return 'fuera-de-tiempo';
            default:
                return '';
        }
    }

    onCheckboxChange(tarea: any) {
        const updateData = {
            id_tarea: tarea.id_tarea,
            id_categoria: 4  // ID 4 corresponds to "Completada"
        };

        this.assignedTaskService.updateTareaCategoria(updateData).subscribe({
            next: () => {
                this.cargarPersonasConTareas();
            },
            error: (error: any) => {
                console.error('Error al actualizar la tarea:', error);
            }
        });
    }

    onUncheckTask(tarea: any) {
        const updateData = {
            id_tarea: tarea.id_tarea,
            id_categoria: 1  // ID 1 corresponds to "Pendiente"
        };

        this.assignedTaskService.updateTareaCategoria(updateData).subscribe({
            next: () => {
                this.cargarPersonasConTareas();
            },
            error: (error: any) => {
                console.error('Error al actualizar la tarea:', error);
            }
        });
    }
}
