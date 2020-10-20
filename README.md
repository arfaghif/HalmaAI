# Halma Game Application With Minimax (Alpha-Beta Pruning) & Local Search+Minimax
Aplikasi Permainan Halma ini merupakan permainan halma yang dapat dimainkan untuk melawan sesama manusia atau bot
yang bot tersebut dapat dipilih apakah dengan menggunakan algoritma minimax alpha-beta pruning atau algoritma local search minimax.

## Developed By
1. **Daniel Riyanto		  /  13518075**
2. **Arthur Edgar Yunanto /	13518090**
3. **Naufal Arfananda	/	13518096**
4. **Yan Arie Motinggo	/	13518129**
<br> <br/>

## Requirements
Aplikasi Permainan Halma ini dikembangkan dengan menggunakan bahasa pemrograman Python3 dengan bantuan library tkinter
sebagai pembuatan GUInya.<br> <br/>

## How To Run
> Sistem Operasi yang kami gunakan adalah Windows 10.

1. Unduh sebagai ZIP *repository* ini. Untuk menjalankan permainan, kita hanya memerlukan file yang ada pada *branch* master.
2. Lalu *extract* file ZIP tersebut. Pada tempat folder tersebut, bukalah terminal di sana. Dengan menekan dua kali *location bar* yang ada pada di sana, lalu ketik **cmd**.
3. Setelah itu, masukan dengan format penulisan seperti di bawah ini.
    ```
    Python main.py <board size> <t_limit> <type player 1> <type player 2>
    ```
    
    **board size** dapat diisi dengan : 8, 10, 16 <br/>
    **t_limit** dapat diisi dengan waktu berapapun (dalam detik). <br/>
    **Tipe player** dapat diisi dengan 1, 2, atau 3 di mana 1 adalah manusia, 2 adalah bot minimax alpha-beta pruning, dan 3 adalah bot local search minimax.<br/>
    Contohnya adalah sebagai berikut untuk bermain dengan ukuran papan 10, batas waktu maksimal 10, pemainnya adalah manusia melawan bot minimax alpha-beta pruning:
    ```
    Python main.py 10 10 1 2
    ```
