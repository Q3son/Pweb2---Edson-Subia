import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { Question } from './components/question/question';
import { Results } from './components/results/results';

export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'question', component: Question }, // No necesitamos ID, el estado lo maneja el servicio
    { path: 'results', component: Results },
    { path: '**', redirectTo: '' } // Redirige cualquier otra ruta al inicio
];
