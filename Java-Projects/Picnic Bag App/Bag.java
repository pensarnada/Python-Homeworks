package picnicbagapp;

import java.lang.reflect.Array;

public class Bag<T> implements IBag<T> {

	public boolean add(T newItem) {
		return true;
	}
	
	public boolean isEmpty() {
		return true;
	}
	
	public boolean isFull() {
		return true;
	}
	
	public T removeByIndex(int index) {
		return null;
		
	}
	
	public T remove() {
		return null;
	}
	
	public T remove(T item) {
		return item;
	}
	
	public int getItemCount() {
		return 0;
	}
	
	public int getIndexOf(T item) {
		return 0;
	}
	
	public boolean contains(T item) {
		return true;
	}
	
	public void displayItems() {
		
	}
	
	public void dump() {
		// removes all the items from the bag
	}
	
	public boolean transferTo(Bag<T> targetBag, T item) {
		return true;
	}
	
public class FileIO {
	public IBag<Item> readInventory() {
		return null;
	}
}

public class Item {
	public String toString() {
		return null;
	}
	public boolean equals(Object obj) {
		return true;
	}
}
/*
public class PicnicBag implements IBag{
	public boolean consume(T item) {
		return true;
	}
}
	
public class InventoryBag implements IBag{
	
}
public class OrganicTrashBag implements IBag{
	
}
public class PaperTrashBag implements IBag{
	
}
public class PlasticTrashBag implements IBag{
	
}*/

	
}
