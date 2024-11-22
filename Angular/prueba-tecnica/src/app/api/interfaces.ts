export interface Tarea {
    id_tarea: number;
    titulo: string;
    descripcion: string;
    fecha_vencimiento: string;
    categoria_nombre: string;
    id_categoria?: number;
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