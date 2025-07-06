import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Item } from '../item'; // Asegúrate de que la ruta a tu interfaz Item sea correcta

@Component({
  selector: 'app-shopping-cart',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './shopping-cart.html',
  styleUrls: ['./shopping-cart.css']
})
export class ShoppingCart implements OnInit {
  
  items: Item[] = [];
  total: number = 0;

  constructor() { }

  ngOnInit(): void {
    // Usamos los datos de prueba
    this.items = [
      { id: 1, name: 'ZAPATILLAS', price: 250.00, quantity: 3, completed: false },
      { id: 2, name: 'PANTALONES', price: 150.00, quantity: 4, completed: false },
      { id: 3, name: 'MANZANA', price: 10.50, quantity: 2, completed: true },
      { id: 4, name: 'PAN', price: 3.50, quantity: 8, completed: true },
      { id: 5, name: 'CASACA', price: 300.00, quantity: 2, completed: false },
    ];
    // ¡Calculamos el total inicial al cargar el componente!
    this.getTotal();
  }

  // --- AÑADE ESTOS TRES MÉTODOS ---

  /**
   * Calcula el precio total sumando los subtotales de los ítems
   * que NO están marcados como 'completed'.
   */
  getTotal(): void {
    this.total = this.items
      .filter(item => !item.completed) // 1. Filtra solo los que no están completados
      .map(item => item.quantity * item.price) // 2. Calcula el subtotal de cada uno
      .reduce((acc, subtotal) => acc + subtotal, 0); // 3. Suma todos los subtotales
  }

  /**
   * Elimina un ítem de la lista.
   * @param itemToDelete El ítem que se va a eliminar.
   */
  deleteItem(itemToDelete: Item): void {
    this.items = this.items.filter(item => item.id !== itemToDelete.id);
    this.getTotal(); // Siempre recalcula el total después de una modificación
  }

  /**
   * Cambia el estado 'completed' de un ítem (de true a false y viceversa).
   * @param itemToToggle El ítem cuyo estado se va a cambiar.
   */
  toggleItem(itemToToggle: Item): void {
    itemToToggle.completed = !itemToToggle.completed;
    this.getTotal(); // Recalcula el total para reflejar el cambio
  }
}