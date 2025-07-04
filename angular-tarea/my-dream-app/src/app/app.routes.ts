import { Routes } from '@angular/router';
import { About } from './about/about';
import { HelloWorld } from './hello-world/hello-world';
export const routes: Routes = [
    { path: '', redirectTo: '/about', pathMatch: 'full' },
    // La ruta para '/about' mostrará el AboutComponent
    { path: 'about', component: About },

    // La ruta para '/hello' mostrará el HelloWorldComponent
    { path: 'hello', component: HelloWorld },
    { path: '**', redirectTo: '/about' }
];
