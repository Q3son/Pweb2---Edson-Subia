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
  showHobbies: boolean;
  
  constructor(){
    console.log("Constructor working...");
    this.name = "Edson Fabricio Subia Huaicane";
    this.email = "esubiahu@unsa.edu.pe";
    this.webpage = "https://www.unsa.edu.pe";
    this.hobbies = ["Basquet","Games Developing","HBO-MAX"];
    this.showHobbies = false;
  }

  toggleHobbies(){
    this.showHobbies = !this.showHobbies;
  }
  newHobby(hobby){
    //console.log(hobby.value);
    this.hobbies.push(hobby.value);
    hobby.value = "";
    return false;
  }
}