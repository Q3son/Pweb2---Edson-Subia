import { Component, OnInit } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';
import { CollapseModule } from 'ngx-bootstrap/collapse'; // Para el menú hamburguesa
import { BsDropdownModule } from 'ngx-bootstrap/dropdown'; // Para menús desplegables

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    CollapseModule,
    BsDropdownModule
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  title = 'my-dream-app';
  isCollapsed = true;
}