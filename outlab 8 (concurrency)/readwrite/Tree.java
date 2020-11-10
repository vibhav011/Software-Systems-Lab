package readwrite;

import java.util.Scanner;
import java.io.File;

public class Tree
{
    private boolean done = false;
    private int root;
    private Tree left = null, right = null;
    public void write(int x)
    {
        if(done)
        {
            if(root == x)
                return ;
            if(root > x)
            {
                if(left == null)
                    left = new Tree();
                left.write(x);
            }
            else
            {
                if(right == null)
                    right = new Tree();
                right.write(x);
            }
        }
        else
        {
            root = x;
            done = true;
        }
    }

    public int read(int x)
    {
        if(root > x && left != null)
            return left.read(x);
        if(root < x && right != null)
            return right.read(x);
        return root;
    }

    // public static void main(String[] args) 
    // {
    //     Tree t = new Tree();
    //     File file1 = new File(args[0]);
    //     File file2 = new File(args[1]);
    //     Scanner sc = null;
    //     try
    //     {
    //         sc = new Scanner(file1);
    //         while(sc.hasNextLine())
    //         {
    //             int a = sc.nextInt();
    //             t.write(a);
    //         }
    //         sc = new Scanner(file2);
    //         while(sc.hasNextLine())
    //         {
    //             int a = sc.nextInt();
    //             System.out.println(t.read(a));
    //         }
    //     }
    //     catch (Exception e)
    //     {
    //         System.out.println("a");
    //     }
    // }
}