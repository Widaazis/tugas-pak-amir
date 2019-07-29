import java.util.Scanner;
 
 
public class Adttanggal {
 
    
     
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int hari = 0;
        int tanggal,bulan,tahun,kabisat;
        String bln = null ;
         
        String nama_bulan [] = {"Januari","Februari","Maret","April","Mei","Juni","Juli",
              "Agustus","September","Oktober","November","Desember"};
         
        System.out.print("Masukkan Tanggal : ");
        tanggal = input.nextInt();
        System.out.print("Masukkan Bulan : ");
        bulan = input.nextInt();
        System.out.print("Masukkan Tahun : ");
        tahun = input.nextInt();
        kabisat = tahun % 4;
         
        if (bulan % 2 == 0){
            hari = 30;
            bln = nama_bulan[bulan-1];
             
            //tahun kabisat 
            if (kabisat==0){
                hari =29;
                bln = nama_bulan[bulan-1];
                 
            }
                else {
                        hari = 28;
                        bln = nama_bulan[bulan-1];
                         
                        }
            }
        else if (bulan %2 == 1){
            hari = 31;
            bln = nama_bulan[bulan-1];
        }
         
        boolean x, y, z;
         
        x = tanggal &gt; 0 &amp;&amp; tanggal <= hari;
        y = bulan &gt; 0 &amp;&amp; bulan <= 12;
        z = x &amp;&amp; y;
         
        if (z){
            System.out.println(+tanggal+" "+bln+" "+tahun+" adalah tanggal yang Valid");
        }
        else {
            System.out.println(+tanggal+" "+bln+" "+tahun+" adalah tanggal yang tidak Valid");
        }
         
    } 
               
  }
