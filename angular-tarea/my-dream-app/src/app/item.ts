export interface Item {
  id: number;
  name: string;
  price: number;
  quantity: number;
  completed: boolean; // Para saber si el usuario lo quiere pagar o no
}