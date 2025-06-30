import { Component, input } from '@angular/core';

@Component({
  selector: 'app-figure',
  standalone: true,
  imports: [],
  templateUrl: './figure.html',
  styleUrl: './figure.css'
})
export class Figure {
  
  public mistakesCount = input.required<number>();

}