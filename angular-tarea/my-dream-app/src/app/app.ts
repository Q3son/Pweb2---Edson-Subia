import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common'; 
import { HelloWorld } from './hello-world/hello-world';
import { User } from './user/user';  
@Component({
  selector: 'app-root',
  imports: [
    CommonModule, 
    RouterOutlet,
    HelloWorld,
    User
  ],
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
  users = ['Edson','Jose','Jonathan','Valeria'];
  activated = false;
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
  newHobby(hobby: { value: string; }){
    //console.log(hobby.value);
    this.hobbies.push(hobby.value);
    hobby.value = "";
    return false;
  }
  
  sayHello(){
    alert("Hola desde App");
  }
  addUser(newUser: { value: string; focus: () => void; }){
    //console.log(newUser.value);
    this.users.push(newUser.value);
    newUser.value = '';
    newUser.focus();
    return false;
  }
  
  deleteUser(user: string){
    for(let i=0; i<this.users.length; i++){
      if (user==this.users[i]){
        this.users.splice(i,1);
      }
    }
  }

}