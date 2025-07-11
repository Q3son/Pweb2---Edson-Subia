import { Component, signal } from '@angular/core';
import { Api } from './api';
import { Movie } from './api';


@Component({
  selector: 'app-root',
  imports: [ ],
  templateUrl: './app.html',
  styleUrl: './app.css',
})

export class App {
  protected readonly title = signal('crud');
  movies: Movie[] = [];
  constructor(private api:Api) {
    this.getMovies();
  }
  getMovies = () => {
      this.api.getAllMovies().subscribe({
        next: (data: any) => { 
          console.log('Datos recibidos:', data);
          this.movies = data;
        },
        error: (error: any) => { 
          console.error('Error al obtener datos:', error);
        },
        complete: () => {
          console.log('La subscripción ha finalizado.');
        }
      }
    )
  }
}