import { Component, OnInit, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './user.html',
  styleUrl: './user.css'
})
export class User implements OnInit{
  @Input() nameUser: string = '';
  ngOnInit(): void { }
  
  sayhello(nameUser: string){
    alert("Hola "+nameUser);
  }
}
