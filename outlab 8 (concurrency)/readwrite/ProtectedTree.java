package readwrite;

import java.util.Scanner;
import java.io.File;
import java.util.concurrent.locks.*;

public class ProtectedTree {
	private Tree tree;
	private int writes = 0;
	private int reads = 0;

	final Lock lock = new ReentrantLock();
	final Condition moreWrites  = lock.newCondition(); 

	public void ProtectedTree(Tree t) {
		this.tree = t;
	}

	public void write(int value) {
		lock.lock();

		System.out.println("WE");
		this.tree.write(value);
		System.out.println("WX");

		writes++;
		if (writes > reads) moreWrites.signal();

		lock.unlock();
	}

	public int read(int value) {
		lock.lock();
		int answer = 0;
		try {
			while (writes <= reads)
				moreWrites.await();

			answer = this.tree.read(value);
			if (answer == value) {
				System.out.println("RS");
				reads++;
			}
			else 
				System.out.println("RF");

		} catch (InterruptedException e) {
		} finally {
			lock.unlock();
		}
		return answer;
	}
}