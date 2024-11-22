import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators, AbstractControl } from '@angular/forms';
import { TareasService } from './tareas.service';
import { TareaBase, Persona, TareaProgramadaNew } from '../api/interfaces';
import { FormsModule } from '@angular/forms';
import { fechaPasadaValidator } from '../shared/validators';


type EstadoTarea = 'Pendiente' | 'Fuera de tiempo';

@Component({
    selector: 'app-tareas',
    standalone: true,
    imports: [CommonModule, ReactiveFormsModule, FormsModule],
    providers: [TareasService],
    templateUrl: './tareas.component.html',
    styleUrls: ['./tareas.component.css']
})
export class TareasComponent implements OnInit {
    tareas: TareaBase[] = [];
    error: string = '';
    mostrarModal = false;
    mostrarModalUpdate = false;
    tareaForm: FormGroup;
    editForm: FormGroup;
    fechaMinima: string;
    tareaEditando: TareaBase | null = null;
    mostrarModalConfirmacion = false;
    tareaAEliminar: number | null = null;
    mostrarModalAsignacion = false;
    tareaAsignar: TareaBase | null = null;
    personas: Persona[] = [];
    personaSeleccionada: number | null = null;
    modalAsignacionAbierto = false;
    intentoAsignar = false;


    estadoToIdCategoria: Record<EstadoTarea, number> = {
        'Pendiente': 2,
        'Fuera de tiempo': 3
    };

    constructor(
        private tareasService: TareasService,
        private fb: FormBuilder
    ) {
        const hoy = new Date();
        this.fechaMinima = hoy.toISOString().split('T')[0];

        this.tareaForm = this.fb.group({
            titulo: ['', [Validators.required, Validators.minLength(3)]],
            descripcion: ['', [Validators.required, Validators.minLength(10)]],
            fecha_vencimiento: ['', [Validators.required, fechaPasadaValidator]]
        });

        this.editForm = this.fb.group({
            titulo: ['', [Validators.required, Validators.minLength(3)]],
            descripcion: ['', [Validators.required, Validators.minLength(10)]],
            fecha_vencimiento: ['', [Validators.required, fechaPasadaValidator]],
            id_categoria: ['',Validators.required]
        });
    }

    ngOnInit() {
        this.cargarTareas();
        this.cargarPersonas();
    }

    abrirModal() {
        this.tareaEditando = null;
        this.mostrarModal = true;
        this.tareaForm.reset();
    }

    cerrarModal() {
        this.mostrarModal = false;
        this.tareaEditando = null;
        this.tareaForm.reset();
    }

    abrirModalUpdate() {
        this.tareaEditando = null;
        this.mostrarModalUpdate = true;
        this.editForm.reset();
    }

    cerrarModalUpdate() {
        this.mostrarModalUpdate = false;
        this.tareaEditando = null;
        this.editForm.reset();
    }

    guardarTarea() {
        if (this.tareaForm.valid) { 
            const formData = this.tareaForm.value;
            const tareaData = {
                titulo: formData.titulo,
                descripcion: formData.descripcion,
                fecha_vencimiento: formData.fecha_vencimiento,
                id_categoria: 2
            };

            this.tareasService.createTarea(tareaData).subscribe({
                next: (response) => {
                    const nuevaTarea: TareaBase = {
                        ...response,
                        categoria_nombre: 'Pendiente'
                    };
                    this.tareas = [...this.tareas, nuevaTarea];
                    this.cerrarModal();
                    this.error = '';
                    this.cargarTareas();
                },
                error: (error) => {
                    console.error('Error al crear tarea:', error);
                    this.error = 'Error al crear la tarea';
                }
            });
        } else {
            this.marcarCamposComoTocados();
        }
    }

    guardarUpdate() {
        if (this.editForm.valid) {            
            const formData = this.editForm.value;
            const tareaActualizada = {
                id_tarea: this.tareaEditando?.id_tarea,
                titulo: formData.titulo,
                descripcion: formData.descripcion,
                fecha_vencimiento: formData.fecha_vencimiento,
                id_categoria: formData.id_categoria
            };

            this.tareasService.updateTarea(tareaActualizada).subscribe({
                next: () => {
                    this.cerrarModalUpdate();
                    this.error = '';
                    this.cargarTareas();
                },
                error: (error) => {
                    console.error('Error al actualizar tarea:', error);
                    this.error = 'Error al actualizar la tarea';
                }
            });
        } else {
            this.marcarCamposComoTocados();
        }
    }
    
    editarTarea(tarea: TareaBase) {
        this.tareaEditando = tarea;
        this.mostrarModalUpdate = true;
        
        this.editForm.patchValue({
            titulo: tarea.titulo,
            descripcion: tarea.descripcion,
            fecha_vencimiento: tarea.fecha_vencimiento,
            id_categoria: tarea.id_categoria
        });
    }

    marcarCamposComoTocados() {
        if (this.mostrarModal) {
            Object.keys(this.tareaForm.controls).forEach(key => {
                this.tareaForm.get(key)?.markAsTouched();
            });
        }
        if (this.mostrarModalUpdate) {
            Object.keys(this.editForm.controls).forEach(key => {
                this.editForm.get(key)?.markAsTouched();
            });
        }
    }

    // Getters para el formulario de creación
    get tituloInvalido() {
        return this.mostrarModal ? 
            (this.tareaForm.get('titulo')?.invalid && this.tareaForm.get('titulo')?.touched) :
            (this.editForm.get('titulo')?.invalid && this.editForm.get('titulo')?.touched);
    }

    get descripcionInvalida() {
        return this.mostrarModal ?
            (this.tareaForm.get('descripcion')?.invalid && this.tareaForm.get('descripcion')?.touched) :
            (this.editForm.get('descripcion')?.invalid && this.editForm.get('descripcion')?.touched);
    }

    get fechaInvalida() {
        return this.mostrarModal ?
            (this.tareaForm.get('fecha_vencimiento')?.invalid && this.tareaForm.get('fecha_vencimiento')?.touched) :
            (this.editForm.get('fecha_vencimiento')?.invalid && this.editForm.get('fecha_vencimiento')?.touched);
    }

    get fechaPasadaError() {
        return this.mostrarModal ?
            (this.tareaForm.get('fecha_vencimiento')?.errors?.['fechaPasada'] && this.tareaForm.get('fecha_vencimiento')?.touched) :
            (this.editForm.get('fecha_vencimiento')?.errors?.['fechaPasada'] && this.editForm.get('fecha_vencimiento')?.touched);
    }

    get estadoInvalido() {
        return this.tareaForm.get('estado')?.invalid && this.tareaForm.get('estado')?.touched;
    }

    get categoriaInvalida() {
        return this.editForm.get('id_categoria')?.invalid && 
               this.editForm.get('id_categoria')?.touched;
    }

    cargarTareas() {
        this.tareasService.getTareas().subscribe({
            next: (tareas) => {
                this.tareas = tareas;
            },
            error: (error) => {
                this.error = 'Error al cargar las tareas';
                if (error.status === 503) {
                    this.error = 'El servidor no está disponible en este momento';
                }
                console.error('Error:', error);
            }
        });
    }


    eliminarTarea(id_tarea: number) {
        this.tareaAEliminar = id_tarea;
        this.mostrarModalConfirmacion = true;
    }

    cancelarEliminacion() {
        this.mostrarModalConfirmacion = false;
        this.tareaAEliminar = null;
    }

    confirmarEliminacion() {
        if (this.tareaAEliminar) {
            this.tareasService.deleteTask(this.tareaAEliminar).subscribe({
                next: () => {
                    this.mostrarModalConfirmacion = false;
                    this.tareaAEliminar = null;
                    this.error = '';
                    this.cargarTareas();
                },
                error: (error) => {
                    console.error('Error al eliminar tarea:', error);
                    this.error = 'Error al eliminar la tarea';
                    this.mostrarModalConfirmacion = false;
                    this.tareaAEliminar = null;
                }
            });
        }
    }

    abrirModalAsignacion(tarea: TareaBase) {
        this.tareaAsignar = tarea;
        this.mostrarModalAsignacion = true;
        this.personaSeleccionada = null;
        this.modalAsignacionAbierto = true;
        this.intentoAsignar = false;
    }

    cerrarModalAsignacion() {
        this.mostrarModalAsignacion = false;
        this.tareaAsignar = null;
        this.personaSeleccionada = null;
        this.modalAsignacionAbierto = false;
    }

    confirmarAsignacion() {
        this.intentoAsignar = true;
        if (!this.personaSeleccionada) {
            this.error = 'Debes seleccionar una persona para asignar la tarea';
            return;
        }

        if (this.tareaAsignar) {
            const tareaProgramada: TareaProgramadaNew = {
                id_tarea: this.tareaAsignar.id_tarea,
                id_persona: this.personaSeleccionada,
            };
            this.tareasService.createTareaProgramada(tareaProgramada).subscribe({
                next: (tarea) => {
                    console.log('Tarea programada creada:', tarea);
                    this.cerrarModalAsignacion();
                    this.cargarTareas();
                },
                error: (error) => {
                    console.error('Error al crear tarea programada:', error);
                    this.error = 'Error al asignar la tarea';
                }
            });
        }
    }

    cargarPersonas() {
        this.tareasService.getAllPersonas().subscribe({
            next: (personas) => {
                this.personas = personas;
            },
            error: (error) => {
                console.error('Error al cargar las personas:', error);
                this.error = 'Error al cargar las personas';
            }
        });
    }
}