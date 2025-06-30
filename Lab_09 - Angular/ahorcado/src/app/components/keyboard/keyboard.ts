import { Component, EventEmitter, Output, input } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-keyboard',
  standalone: true,
  imports: [MatButtonModule],
  templateUrl: './keyboard.html',
  styleUrl: './keyboard.css'
})
export class Keyboard {
  // Lista de letras ya intentadas para deshabilitar los botones (lo recibe)
  public triedLetters = input.required<string[]>();
  
  // Avisa al componente padre (Game -> mi juego) que una letra fue presionada
  @Output() letterPressed = new EventEmitter<string>();

  public alphabet: string[] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

  onLetterClick(letter: string) {
    this.letterPressed.emit(letter);
  }
}