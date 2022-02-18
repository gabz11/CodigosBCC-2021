package Testes;

import java.util.ArrayList;

public class ListaItem {

    ArrayList<ItemConsumivel> consumiveis = new ArrayList<>();
    ArrayList<ItemArma> slot_arma = new ArrayList<>(); // Simula equipar
    ArrayList<ItemArmadura> slot_armadura = new ArrayList<>();

    public ArrayList<ItemConsumivel> getConsumiveis() {
        return consumiveis;
    }

    public void setConsumiveis(ArrayList<ItemConsumivel> consumiveis) {
        this.consumiveis = consumiveis;
    }

    public ArrayList<ItemArma> getSlot_arma() {
        return slot_arma;
    }

    public void setSlot_arma(ArrayList<ItemArma> slot_arma) {
        this.slot_arma = slot_arma;
    }

    public ArrayList<ItemArmadura> getSlot_armadura() {
        return slot_armadura;
    }

    public void setSlot_armadura(ArrayList<ItemArmadura> slot_armadura) {
        this.slot_armadura = slot_armadura;
    }

    public ListaItem()
    {
        this.consumiveis = new ArrayList<>();
        this.slot_arma = new ArrayList<>();
        this.slot_armadura = new ArrayList<>();
    }
}
