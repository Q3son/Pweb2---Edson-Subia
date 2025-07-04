import { Component, OnInit } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';
import { CommonModule } from '@angular/common'; 
import { HelloWorld } from './hello-world/hello-world';
import { User } from './user/user';
import { FormsModule } from '@angular/forms';
import { Data } from './data'; 
import { Post } from './Post';  
import { Router } from 'express';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule, 
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    HelloWorld,
    User,
    FormsModule,
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  title = 'my-dream-app';
  name : string;
  age : number;
  email; // : string :
  webpage: string;
  hobbies: string[];
  showHobbies: boolean;
  posts: Post[] = [];
  users = ['Edson','Jose','Jonathan','Valeria'];
  activated = false;

  constructor(private dataService: Data){
    console.log("Constructor working...");
    this.name = "Edson Fabricio Subia Huaicane";
    this.age = 20;
    this.email = "esubiahu@unsa.edu.pe";
    this.webpage = "https://www.unsa.edu.pe";
    this.hobbies = ["Basquet","Games Developing","HBO-MAX"];
    this.showHobbies = false;
  }
  ngOnInit() {
    this.dataService.getData().subscribe(data => {
      //console.log(data);
      this.posts = data;
    });
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