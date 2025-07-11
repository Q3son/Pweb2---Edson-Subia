import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Api } from './api';


@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css',
  providers: [Api]
})
export class App {
  protected readonly title = signal('crud');
  movies = [{id:1,title:'peli1',year:2021},{id:2,title:'peli2',year:2022}];
  constructor(private api:Api) {
    this.getMovies();
  }
  getMovies = () => {
    this.api.getAllMovies().subscribe (
      (data: any) => {
        console.log('Datos recibidos:', data);
        this.movies = data;  
        data.results;
      },
      (error: any) => {
        console.error('Error al obtener datos:', error);
      } 
    ) 
  } 
}