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
  name : string;
  email; // : string :
  webpage: string;
  hobbies: string[];
  constructor(){
    console.log("Constructor working...");
    this.name = "Edson Fabricio Subia Huaicane";
    this.email = "esubiahu@unsa.edu.pe";
    this.webpage = "https://www.unsa.edu.pe";
    this.hobbies = ["Basquet","Games Developing","HBO-MAX"];
  }
  showhobbies() {
    return true;
  }
}