// api/api-endpoints.ts
export const API_ENDPOINTS = {
    tareas: {
      base: 'http://localhost:8000/tarea',
      getTareas: '/get_tareas',
      createTarea: '/create_tarea',
      updateTarea: '/update_tarea',
      deleteTarea: '/delete_tarea',
    },
    personas: {
      base: 'http://localhost:8000/persona',
      getAllPersonas: '/get-all-personas',
    },
    tareaProgramada: {
      base: 'http://localhost:8000/tareaProgramada',
      createTareaProgramada: '/create_tarea_programada',
    },
  };