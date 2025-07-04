import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  title = 'my-dream-app';
  name = "Edson Fabricio Subia Huaicane";
  email = "esubiahu@unsa.edu.pe";
  webpage = "https://www.unsa.edu.pe";
}