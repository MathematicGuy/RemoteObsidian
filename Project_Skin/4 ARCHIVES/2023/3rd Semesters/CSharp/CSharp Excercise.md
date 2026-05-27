*Exercise 1:*
> **a.** Viết lệnh trong hàm main() khai báo biến n,  kiểu số nguyên/
Viết hàm nhập từ bàn phím giá trị số nguyên dương. Nếu nhập sai thì nhập lại, có chặn exception khi nhập.  
Gọi hàm trong hàm main() để nhận được số nguyên dương n. Hiển thị n.  
**b.** Viết hàm nhập 1 mảng số thực dương 4byte với số phần tử là n. Gọi hàm trong hàm main() để nhận được mảng a.
**c.** Viết hàm hiển thị 1 mảng số thực. Gọi hàm trong hàm main() để hiển thị mảng a.
**d.** Viết 1 hàm trả về 2 giá trị: giá trị nhỏ nhất, giá trị lớn nhất của các phần tử của 1 mảng số thực 1 chiều.
**Gọi hàm trong hàm main() để hiển thị giá trị phần tử nhỏ nhất, phần tử lớn nhất của mảng a.**


```cs
using System.Runtime.InteropServices;

namespace Var1
{
    internal class Program
    {
        static int nhapsonguyen()
        {
            int n;
			
            while (true)
            {
                try
                {
                    n = Convert.ToInt32(Console.ReadLine());
                    break;
                }
                catch
                {
                    Console.WriteLine("Nhập lại! Số vừa rồi sai định dạng ");
                }
            }
            return n;
        }
			
        static double nhapsothuc()
        {
            double x;
			
            while (true)
            {
                try
                {
					// chuyển về dạng float 8-bytes
                    x = Convert.ToDouble(Console.ReadLine()); 
                    if (x > 100)
                    {
                        Console.Beep();
                    }
                    break;
                }
                catch
                {
                    Console.WriteLine("Nhập lại! Số vừa rồi sai định dạng ");
                }
            }
            return x;
        }
			
        static ushort nhapsonguyen2byteskhongdau()
        {
            ushort n = 0;
            while (true)
            {
                try
                {
                    string sz;
                    sz = Console.ReadLine();
                    n = ushort.Parse(sz);
                    break;
                }
                catch
                {
                    Console.Beep();
                }
            }
            return n;
        }
			
        static ushort[] nhapmang1chieusonguyen2byteskhongdau(int phantu)
        {
            ushort[] a; // innitiate array
            a = new ushort[phantu]; // assign elements to array
			
            if (a == null) return null;
			
            for (int i = 0; i < phantu; i++)
            {
                Console.Write("array[" + i.ToString()+"]=");
                a[i] = nhapsonguyen2byteskhongdau();
            }
			
            return a;
        }
			
        static void hienthimang1chieu(ushort[] array)
        {
            int sophantu = array.Length;
            decimal min = Decimal.MaxValue;
            decimal max = Decimal.MinValue;
			
            for (int i = 0; i < sophantu; i++)
            {
                Console.WriteLine("array[" + i.ToString() + "]= "
                    + array[i].ToString());
                if (array[i] < min)
                    min = array[i];
                if (array[i] > max)
                    max = array[i];    
            }
			
            Console.WriteLine();
            for (int i = (sophantu - 1); i >= 0; i--)
            {
                Console.WriteLine("array[" + i.ToString() + "]= "
                    + array[i].ToString());
            }
			
            Console.WriteLine();
            Console.WriteLine("Min value: " + min.ToString());
            Console.WriteLine("Max value: " + max.ToString());
            Console.WriteLine("Trug bình cộng: " + (min + max)/2);
        }
			
        static void Main(string[] args) // không cần trả về -> void
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
			
            ushort[] array;
            Console.WriteLine("Nhập số nguyên không dấu 2 bytes: ");
            int num = Convert.ToInt16(Console.ReadLine());
            array = nhapmang1chieusonguyen2byteskhongdau(num);
            if (array != null)
            {
                Console.WriteLine();
            }
			
            Console.WriteLine();
            Console.WriteLine("Nhập vào 1 số nguyên: ");
            int n = nhapsonguyen();
			
            Console.Clear();
            Console.WriteLine("Nhập vào 1 số thực: ");
            double x = nhapsothuc();
			
            hienthimang1chieu(array);
            Console.WriteLine();
            Console.WriteLine("Giá trị của n là: " + n.ToString());
            Console.WriteLine("Giá trị của x là: " + x.ToString());
        }
    }
}
```