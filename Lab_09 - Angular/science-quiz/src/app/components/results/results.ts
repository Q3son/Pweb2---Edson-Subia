import { Component, inject } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { QuizService } from '../../services/quiz.service';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { CommonModule } from '@angular/common'; // Necesario para ngClass

@Component({
  selector: 'app-results',
  standalone: true,
  imports: [CommonModule, RouterLink, MatCardModule, MatButtonModule, MatListModule, MatIconModule],
  templateUrl: './results.html',
  styleUrl: './results.css'
})
export class Results {
  quizService = inject(QuizService);
  router = inject(Router);

  restartQuiz() {
    this.router.navigate(['/']);
  }
}