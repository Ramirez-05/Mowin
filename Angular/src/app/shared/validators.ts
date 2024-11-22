import { AbstractControl } from "@angular/forms";

export function fechaPasadaValidator(control: AbstractControl) {
    if (!control.value) return null;
    
    const fecha = new Date(control.value);
    const hoy = new Date();
    
    fecha.setHours(0, 0, 0, 0);
    hoy.setHours(0, 0, 0, 0);
    
    const fechaTimestamp = fecha.getTime();
    const hoyTimestamp = hoy.getTime();
    
    return fechaTimestamp >= hoyTimestamp ? null : { fechaPasada: true };
  }
  