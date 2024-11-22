export interface TareaBase {
    id_tarea: number;
    titulo: string;
    descripcion: string;
    fecha_vencimiento: string;
    id_categoria: number;
    categoria_nombre: string;
}

export interface TareaAsignada {
    id_tarea: number;
    titulo: string;
    descripcion: string;
    fecha_vencimiento: string;
    categoria: Categoria;
}

export interface Categoria {
    id_categoria: number;
    nombre: string;
}

export interface Persona {
    id_persona: number;
    nombre: string;
    email: string;
}

export interface TareaProgramadaNew {
    id_tarea: number;
    id_persona: number;
}

export interface PersonaConTareas {
    cedula: string;
    nombre: string;
    apellido: string;
    id_persona: number;
    tareas_programadas: TareaAsignada[];
}

export interface TareaUpdateCategoria {
    id_tarea: number;
    id_categoria: number;
}
  