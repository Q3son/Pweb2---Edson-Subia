import { Component, inject } from '@angular/core';
import { Hangman } from '../../services/hangman';
import { Figure } from '../figure/figure';
import { Keyboard } from '../keyboard/keyboard';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-game',
  standalone: true,
  imports: [
    Figure,
    Keyboard,
    MatCardModule,
    MatButtonModule
  ],
  templateUrl: './game.html',
  styleUrl: './game.css'
})
export class Game {
  // Inyectamos el servicio de la app para que tengamos acceso a toda la lógica y estado de los componentes totales.
  public hangman = inject(Hangman);
}
