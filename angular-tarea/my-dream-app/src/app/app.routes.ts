import { Routes } from '@angular/router';
import { About } from './about/about';
import { HelloWorld } from './hello-world/hello-world';
import { Home } from './home/home';
import { ShoppingCart } from './shopping-cart/shopping-cart';
export const routes: Routes = [
    { path: '', component: Home},
    // La ruta para '/about' mostrará el AboutComponent
    { path: 'about', component: About },

    // La ruta para '/hello' mostrará el HelloWorldComponent
    { path: 'hello', component: HelloWorld },
    { path: 'cart', component: ShoppingCart },
    { path: '**', redirectTo: '' }
];
