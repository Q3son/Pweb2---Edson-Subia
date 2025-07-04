import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-user',
  imports: [],
  templateUrl: './user.html',
  styleUrl: './user.css'
})
export class User implements OnInit{
  @Input() nameUser: any;
  ngOnInit(): void { }
}
